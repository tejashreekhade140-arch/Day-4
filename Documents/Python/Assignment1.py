students={
    101:{"Name":"Aditi","Scores":[20,20,25]},
    102:{"Name":"Rahul","Scores":[40,60,25]},
    103:{"Name":"Snehal","Scores":[0,60,25]},
    104:{"Name":"Karan","Scores":[30,20,95]},
    105:{"Name":"Priya","Scores":[20,50,25]}

}
#Calculate avg Score and Flag Pass and Fail:
for sid,details in students.items():
    avg=sum(details["Scores"])/len(details["Scores"])
    details["Average"]=avg
    details["passed"]=avg>=25

#print names of Student who Passed
print("Student Who Passed:")
for sid,details in students.items():
    if details["Passed"]:
        print(details["Name"])

