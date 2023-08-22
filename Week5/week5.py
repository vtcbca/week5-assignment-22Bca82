import csv
with open ('E:\22bca82\python\student.csv','w') as f:
    data=csv.writer(f)
    field=["sid","sname","city","contact"]
    d=[[1,"heer","kadod",9737762728],[2,"pitu","bardoli",1234567890],[3,"swweta","vyara",9874561230],[4,"suhani","surat",9879461230],[5,"pihu","bardoli",3216549870]]
    data.writerow(field)
    data.writerows(d)

# writing csv file  using user input
import csv
with open ('E:\22bca82\python\student.csv','a') as f:
    data=csv.writer(f)
    l=[]		
    for i in range(5):
            name=int(input("Enter sid:"))
            sname=input("Enter sname:")
            city=input("Enter city:")
            contact=int(input("Enter contact no:"))
            d=(["sid","sname","city","contact"])
            l.append(d)
    data.writerows(l)	

# reading csv file
import csv
with open ('E:\22bca82\python\student.csv','r',newline='') as f:
    data=csv.reader(f)
    for i in data:
        print(i)
    
