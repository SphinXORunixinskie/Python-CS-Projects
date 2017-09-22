'''
Nicole Gossett


Printer simulation program from Section 3.5 in the book.   

Simulation of printer queue in a computer lab with students 
submitting print tasks.  Objective: estimate task waiting time in queue
for different printer print rates. 

Assumptions: On average, there are 10 students in the lab.  A student
sends two print jobs on average, 1-20 pages long (equally likely). 
Printer can print in draft mode (10 ppm) or high quality (5 ppm).

Observations: With 10 students in the lab at any given time printing twice,
there are 20 print jobs per hour (or every 3600 seconds). So, we expect to 
see 1 job every 180 seconds (20 tasks / 3600 seconds).  

Simulation logic:
1. Create a queue of print tasks. Each task will be given a timestamp 
upon its arrival. The queue is empty to start.

2. For each second (current_second):
 - Does a new print task get created? If so, add it to the queue with 
   the current_second as the timestamp.
   - If the printer is not busy and if a task is waiting,
     Remove the next task from the print queue and assign it to the printer.
   - Subtract the timestamp from the current_second to compute the waiting 
     time for that task.
   - Append the waiting time for that task to a list for later processing.
   - Based on the number of pages in the print task, figure out how much 
     time will be required.
   - The printer now does one second of printing if necessary. It also subtracts 
     one second from the time required for that task.
   - If the task has been completed, in other words the time required has reached 
     zero, the printer is no longer busy.
   
3. After the simulation is complete, compute the average waiting time from 
   the list of waiting times generated.
'''

from Queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    #set it up to take a size input/min-max (optionally)
    def __init__(self,time,minPages,maxPages):
        self.timestamp = time
        ##between min and max...
        self.pages = random.randint(minPages,maxPages+1)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def loadConfig():

    try:
        file = open("sim_config.txt", "r")
    except IOError:
        print("Config file not found.")
        return False
    
    else:
        config = dict()

        #set each line, make sure it is in the right range, and check the next..
        config['duration'] = int(file.readline())
        if 3600<=config['duration']<=36000:
            config['numExperiments'] = int(file.readline())
            if 1<=config['numExperiments']<=100:
                config['minTask'] = int(file.readline())
                if 1<=config['minTask']<=100:
                    config['maxTask'] = int(file.readline())
                    if config['minTask']<=config['maxTask']<=100:
                        config['numPrint'] = int(file.readline())
                        if 0<config['numPrint']<=2:
                            config['rateOne'] = int(file.readline())
                            #dont get the second page rate if theres only one printer
                            if 1<=config['rateOne']<=50 and config['numPrint'] == 1:
                                return config
                            elif 1<=config['rateOne']<=50:
                                config['rateTwo'] = int(file.readline())
                                if 1<=config['rateTwo']<=50:
                                    return config
                                
    #if it hits here it failed...
    print("Formatting error. Configuration not loaded.")
    return False


    
def simulation(config):

    labprinter = Printer(config['rateOne'])
    printQueue = Queue()
    waitingtimes = []
    
    #if there are two printers...
    if config['numPrint'] == 2:
        labprinter2 = Printer(config['rateTwo'])
        for currentSecond in range(config['duration']):
            if newPrintTask():
                task = Task(currentSecond,config['minTask'],config['maxTask'])
                printQueue.enqueue(task)
            if (not printQueue.is_empty()):
                #if there is a job to print...

                #and the first printer is not busy, but the second one is:
                if (not labprinter.busy()) and (labprinter2.busy()):
                    nexttask = printQueue.dequeue()
                    waitingtimes.append(nexttask.waitTime(currentSecond))
                    labprinter.startNext(nexttask)

                #the second printer is not busy, but the first one is:
                if (not labprinter2.busy()) and (labprinter.busy()):
                    nexttask = printQueue.dequeue()
                    waitingtimes.append(nexttask.waitTime(currentSecond))
                    labprinter2.startNext(nexttask)

                #so at this point both are either busy or both are not busy...
                if (not labprinter.busy()) and (not labprinter2.busy()):
                    #if they aren't busy, print to the faster one...
                    if labprinter.pagerate >= labprinter2.pagerate:
                        nexttask = printQueue.dequeue()
                        waitingtimes.append(nexttask.waitTime(currentSecond))
                        labprinter.startNext(nexttask)
                    else: #two is faster... print to that one
                        nexttask = printQueue.dequeue()
                        waitingtimes.append(nexttask.waitTime(currentSecond))
                        labprinter2.startNext(nexttask)

            labprinter.tick()

        
    else:
        for currentSecond in range(config['duration']):
            if newPrintTask():
                task = Task(currentSecond,config['minTask'],config['maxTask'])
                printQueue.enqueue(task)

            if (not labprinter.busy()) and (not printQueue.is_empty()):
                nexttask = printQueue.dequeue()
                waitingtimes.append(nexttask.waitTime(currentSecond))
                labprinter.startNext(nexttask)

            labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    output = "Average Wait %6.2f secs %3d tasks remaining." \
          %(averageWait, printQueue.size())
    print(output)
    return output, averageWait
    #return the string and wait time so we can print it to the main file

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

def main():
    # run simulation X number of times, from config
    config = loadConfig()
    avgWait = 0

    #get the output file open... w for write new file so its blank
    try:
        out = open("sim_out.txt","w")
    except IOError:
        print("Output file could not be opened.")
        return
        
    if config is not False:
        for i in range(config['numExperiments']):
            #send the whole config in, and take the output string as a return value
            outString, wait = simulation(config)
            out.write(outString+"\n")
            avgWait = avgWait + wait

        #now make the actual avgwait and print it, then write it to the output file
        #and save it/close up...

        trueAvg = "Average wait time of all simulations: " + str(avgWait / config['numExperiments'])
        print(trueAvg)

        out.write(trueAvg)
        out.close()
            
        
if __name__ == "__main__":
    main()
