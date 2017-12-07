import random

class Node:
	def __init__(self, value=None, next=None, previous=None):
		if value == None:
			#sets the value to a random number if not specified
			self.value = random.randint(1,100)
		else:
			self.value = value
		self.next  = next
		self.previous = previous

	def __str__(self):
		return str(self.value)

class DLList:
	def __init__(self):
		self.head = None
		self.tail = None
				
	def size(self):
		#if the head is blank its empty
		if self.head == None:
			return 0
		size = 1
		temp = self.head
		#adding to size while there are still attached ndoes...
		while temp.next is not None:
			size += 1
			temp = temp.next
		return size

	def contains(self, val):
		temp = self.head
		while temp is not None:
			#iterate through each value starting from the head
			if temp.value == val:
				return True
			temp = temp.next
		return False

	def rand_init(self, list_size):
		self.head = None
		self.tail = Node()
 
		temp = self.tail
		#add to the tail and you end up with the head as the last value
		for x in range(0,list_size):
			temp.previous = Node()
			temp.previous.next = temp
			temp = temp.previous
		self.head = temp

	def remove_all(self, val):
		if self.head is not None:
			temp = self.head
			while temp is not None:
				if temp.value == val:
					temp.value = None
				temp = temp.next
			#set all values of "dead" nodes to null to do a second sweep to remove empty nodes

			#re-establish a head node and a tail node
			temp = self.head
			while temp.value == None and temp.next is not None:
				self.head = temp.next
				self.head.previous = None
				temp = temp.next
				
			temp = self.tail
			while temp.value == None and temp.previous is not None:
				self.tail = temp.previous
				self.tail.next = None
				temp = temp.previous
			

			#loop through the rest...
			temp = self.head.next
			while temp is not None and temp.next is not None:
				if temp.value == None:
					#set the previous node to look at the NEXT node since this one is empty
					temp.previous.next = temp.next

					#set the NEXT node to look back at the PREVIOUS node since this one is empty
					temp.next.previous = temp.previous
				temp = temp.next
				

	def __str__(self):
		#set up the bracket and first value, so even if its empty it displays
		string = "[" + str(self.head)
		#then iterate through every node
		if self.head is not None:
			temp = self.head.next
			while temp is not None:
				string += " " + str(temp)
				temp = temp.next
		string += "]"
		return string

	def append(self, item):
		#add to the tail, then point the tail at the new node
		self.tail.next = item
		self.tail = item

	def slice(self, start, stop):
		#set up some placeholders
		holder = list()
		place = 0
		temp = self.head
		#then iterate through the list and pull any values between the start and stop and add them to the list
		while place < stop and temp is not None:
			if place >= start:
				holder.append(temp.value)
			temp = temp.next
			place += 1

		return holder

	def swap(self, start, stop):
		place = 0
		temp = self.head
		
		#set up a couple placeholders so that it can jump through the list
		swap1 = None
		swap2 = None
		while place <= stop and temp is not None:
			if place == start:
				swap1 = temp
			if place == stop:
				swap2 = temp
			temp = temp.next
			place += 1

		# if both of the swap nodes were created, then both positions were valid
		if swap1 is not None and swap2 is not None:
			#hold a temp value from the first node
			temp_swap = swap1.value
			#then swap the values
			swap1.value = swap2.value
			swap2.value = temp_swap

	def shuffle(self):
		size = self.size()
		#run swap on each position of the list with a random end swap
		for x in range(0, size):
			self.swap(x,random.randint(0,size))

	def is_palindrome(self):
		#single place arrays are palindromes...
		if self.size == 1:
			return True
		else:
			#starting from the head and tail...
			temp = self.head
			temp2 = self.tail
			while temp2 is not self.head and temp is not self.tail:
				#...check to see if each opposite value is a match
				#and stop the script if the markers have hit the opposite ends
				if temp.value is not temp2.value:
					return False
				temp = temp.next
				temp2 = temp2.previous
			return True
		
	def decrease(self, item): 
		self.item = None
		if self.item < current.item: 
			return false 
		
	def ithinkitdecreases(self, item):
		if(current.item > next.item): 
			return('dude its decreasing')
		
	def read(self):
		print(self)

		
	def add(self, item):
		#set it as the head if there isnt one
		if self.head is None or self.head.value is None:
			self.head = item
			self.tail = item
		else:
		#or make it the new head and change the old heads previous too
			temp = self.head
			self.head = item
			temp.previous = self.head
			self.head.next = temp

   
print("Making a generic doubly linked list...")
test = DLList()
print("Removing any 3's from the empty list.")
test.remove_all(3)
print("Adding a node with a value of 3 to the list.")
test.add(Node(3))
print("Printing the list and it's size(): ",test.read(), test.size())
print("Removing all 3's again..")
test.remove_all(3)
print(test.read())
print("New list size: ",test.size())
print("Adding a 4 to the list")
test.add(Node(4))
print(test.read())
print("Does the list contain a 4?",test.contains(4))
print("Current list size: ",test.size())
print("Removing 4's..")
test.remove_all(4)
print("Does the list contain any 4's? ",test.contains(4))
print(test.read(), "--should be [None]")
print("Adding two 4s and running palindrome check..")
test.add(Node(4))
test.add(Node(4))
print("Is ",test.read()," a palindrome? ",test.is_palindrome())

print("Making a random list of 10 numbers 1-100..")
test.rand_init(10)
print(test.read())
print("Is ",test.read()," a palindrome? ",test.is_palindrome())

print("Appending a 7..")
test.append(Node(7))
print(test.read())

print("Adding a 1 to the beginning..")
test.add(Node(1))
print(test.read())

print("From index 1 to 3: ",list(test.slice(1,3)))
print("Swapping 1 and 3...")
test.swap(1,3)
print(test.read())
test.shuffle()
print("Shuffled: ",test.read())
