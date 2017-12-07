text = open('restaurant_inspections.txt').readlines()[1:]

numberofinspections = (len(text))
database = {}

for i in text:
    n = -1
    data = {}
    for _ in i.replace("\n", "").split("*"):
        n += 1
        if n == 0:
            id = _
            data.update({"ID": _})
        if n == 1:
            data.update({"Name": _})
        if n == 3:
            data.update({"Cuisine": _})
        if n == 4:
            data.update({"InspectionDate": _})
        if n == 5:
            data.update({"Violation": _})
        if n == 6:
            data.update({"Score": _})
        if n == 7:
            data.update({"Grade": _})
        if n == 8:
            data.update({"GradeDate": _})
        if n == 9:
            data.update({"Borough": _})

    database.update({"%s" % id: data})

while 1:
    search = raw_input("Search ~ ")
    results = []
    for id in database:
        for info in database[id]:
            if search == database[id][info]:
                results.append(id)
    if len(results) > 0:
        for _ in results:
            data = database[_]
            print("ID:", data["ID"])
            print("Name:", data["Name"])
            print("Cuisine:", data["Cuisine"])
            print("InspectionDate:", data["InspectionDate"])
            print("Violation:", data["Violation"])
            print("Score:", data["Score"])
            print("Grade:", data["Grade"])
            print("GradeDate:", data["GradeDate"])
            print