# PRACTICAL FILE QUESTIONS

# 1. Searching a word in a given string
"""
str1=input("enter a string: ")
str2=input("enter word to find: ")
temp2=0
for k in str2:
    temp2=temp2+1
str3=""
temp1=0
d1={}
for i in str1:
    if i==" ":
        d1[temp1]=str3
        str3=""
        temp1+=1
    else:
        temp1+=1
        str3=str3+i
for j in d1:
    if d1[j]==str2:
        print("The word ",str2," starts at position ",(j-temp2+1))
"""
# 2. Sum of even and odd elements in a tuple
"""
lst1=[]
n=int(input("enter number of elements in the tuple: "))
for temp in range(n):
    element=int(input("enter a number: "))
    lst1.append(element)
tup1=tuple(lst1)
print("Tuple is ",tup1)
even=0
odd=0
for i in tup1:
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print("Even sum = ",even)
print("Odd sum = ",odd)
"""
# 3. smallest and largest numbers in a list
"""
temp1=0
lst1=[]
n=int(input("enter number of elements in the list: "))
for temp in range(n):
    element=int(input("enter a number: "))
    lst1.append(element)
for i in lst1:
    if i>=temp1:
        temp1=i
temp2=temp1
for j in lst1:
    if j<=temp2:
        temp2=j
print("Highest number is ",temp1)
print("Lowest number is ",temp2)
"""
# 4. Barring lines with "@" at the start
"""
f1 = open ("source.txt" , "r")
f2 = open ("target.txt" , "w")
read=f1.readlines()
for i in read:
    if i[0] != "@" :
        f2.write(i)
f2.close()
"""
# 5. creating a file and displaying lines starting with "p" from the file
"""
lst1=[]
f= open ("Practical1.txt" , "w")
n=int(input("enter number of lines in the text: "))
for temp in range(n):
    element=input("enter a string: ")
    lst1.append(element+"\n")
f.writelines(lst1)
f.close()
f = open ("Practical1.txt" , "r",)
read=f.readlines()
for i in read:
    if i[0] in "pP" :
        print("\n"+i)
f.close()
"""
# 6. Count number of occurrences of me/my from TXT file
"""
lst1=[]
f= open ("Practical2.txt" , "w")
n=int(input("enter number of lines in the text: "))
for temp in range(n):
    element=input("enter a string: ")
    lst1.append(element+"\n")
f.writelines(lst1)
f.close()

count=0
f = open ("Practical2.txt" , "r",)
read=f.readlines()
print(read)
for i in read:
    if "my" in i :
        count=count+1
        print(i)
    elif "me" in i:
        count=count+1
        print(i)
print(count)
f.close()
"""
# 7. displaying "#" after each word
"""

lst1=[]
f= open ("Practical3.txt" , "w")
n=int(input("enter number of lines in the text: "))
for temp in range(n):
    element=input("enter a string: ")
    lst1.append(element+"\n")
f.writelines(lst1)
f.close()
count=0
f = open ("Practical3.txt", "r")
r = f.read()
lst2=[]
str1=""
for i in r:
    if i == " ":
        lst2.append(str1)
        str1=""
    elif i== "\n":
        lst2.append(str1)
        str1=""
    else:
        str1=str1+i
for j in lst2:
    print(j,"#",end="")
f.close()
"""
# 8. display number of uppercase,lowercase,digits,consonants and vowels
"""
lst1=[]
f= open ("Practical5.txt" , "w")
n=int(input("enter number of lines in the text: "))
for temp in range(n):
    element=input("enter a string: ")
    lst1.append(element+"\n")
f.writelines(lst1)
f.close()
up=0
low=0
digit=0
cons=0
vow=0
f1= open ("Practical5.txt" , "r")
r = f1.readlines()
lst2=[]
for i in r:
    for j in i:
        if j!="\n":
            lst2.append(j)
for var in lst2:
    if var in "1234567890":
        digit=digit+1
    if var in "abcdefghijklmnopqrstuvwxyz":
        low=low+1
    if var in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        up=up+1
    if var in "AaEeIiOoUu":
        vow=vow+1
    if var in "bBcCdDFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz":
        cons=cons+1
print("digit = ",digit)
print("vowel = ",vow)
print("consonant = ",cons)
print("lowercase = ",low)
print("uppercase = ",up)
"""
# 9. create new file without lines containing letter "a"
"""
lst1=[]
f= open ("Practical4-1.txt" , "w")
n=int(input("enter number of lines in the text: "))
for temp in range(n):
    element=input("enter a string: ")
    lst1.append(element+"\n")
f.writelines(lst1)
f.close()
f1= open ("Practical4-1.txt" , "r")
f2= open("Practical4-2.txt","w")
r = f1.readlines()
lst2=[]
for i in r:
    lst2.append(i)
f1.close()
for j in lst2:
    if "a" not in j:
        if "A" not in j:
            f2.write(j)
f2.close()
"""   
# 10. Create a Binary file and call the function for searching for a given roll no
"""
def searchrec():
    import pickle
    f=open("Student.dat","rb")
    list=pickle.load(f)
    ans="Y"
    while ans=="y" or ans=="Y":
        rollno=int(input("Enter a roll no to search:"))
        
        for i in list:#[[a,b],[c,f]]
            if i[0]==rollno:
                print("Rollno =",i[0])
                print("Name =",i[1])
                print("Class =",i[2])
                print("marks =",i[3])
                break
        ans=input("Do you want to search more?")
    f.close()
   

import pickle
f=open("student.dat","wb")
rec=[]
ans="Y"
while ans=="Y"or ans=="y":
    rollno=int(input("Enter the roll no:"))
    Name=input("Enter the name:")
    Class=input("Enter the class:")
    Marks=int(input("Enter the mark:"))
    data=[rollno,Name,Class,Marks]
    rec.append(data)
    ans=input("Do you want to continue?")
pickle.dump(rec,f)    
f.close()    
searchrec()
"""
# 11. Search and update in binary file
"""
import pickle

def create():
    with open("file.dat", "wb") as f:
        records = []  
        n = int(input("Enter the number of records: "))
        
        for i in range(n):  
            student = {}  
            student["Name"] = input("Enter the name of student: ")
            student["Roll number"] = int(input("Enter the roll number of the student: "))
            student["Percentage"] = float(input("Enter the overall percentage of the student: "))
            records.append(student)  
        
        pickle.dump(records, f) 
        
        print("File is created!")

create()

def update():
    try:
        with open("file.dat", "rb+") as f:
            roll_number = int(input("Enter the roll number of the student to be found: "))
            temp_var = False
            
            # Load all records into a list
            records = pickle.load(f)
            
            for a in records:
                if a["Roll number"] == roll_number:
                    print("The record is found!")
                    print("1: Name")
                    print("2: Roll Number")
                    print("3: Percentage")
                    
                    option = int(input("What do you want to update (1-3): "))

                    if option == 1:
                        new_name = input("Enter the new name: ")
                        a["Name"] = new_name
                    
                    elif option == 2:
                        new_roll_number = int(input("Enter the new roll number: "))
                        a["Roll number"] = new_roll_number
                        
                    elif option == 3:
                        new_percentage = float(input("Enter the new percentage: "))
                        a["Percentage"] = new_percentage
                    
                    temp_var = True
                    break
            
            if temp_var:
                pickle.dump(records, f)
                print("Record updated successfully!")
            else:
                print("The record is not found!")              
    except FileNotFoundError:
        print("The file does not exist")
    except Exception as e:
        print(e)
update()
"""
# 12. Search and delete from binary file
"""
import pickle

def create():
    with open("file.dat", "wb") as f:
        records = []  
        n = int(input("Enter the number of records: "))
        
        for i in range(n):  
            student = {}  
            student["Name"] = input("Enter the name of student: ")
            student["Roll number"] = int(input("Enter the roll number of the student: "))
            student["Percentage"] = float(input("Enter the overall percentage of the student: "))
            records.append(student)  
        
        pickle.dump(records, f) 
        
        print("File is created!")

create()

def delete(r):
    f = open("file.dat", 'rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    f = open("file.dat", "wb")
    for x in reclst:
        if x[1] == r:
            continue
        pickle.dump(x,f)
    f.close()

r = int(input("Enter the roll number: "))
delete(r)
"""
# 13. Create a CSV File, search a given name and display the relevant details.
"""
import csv 

def create():
        f = open("student.csv", 'a+')
        writer = csv.writer(f)
        l = []
        n = int(input("Enter the numbers of records to be inserted: "))
        for i in range(n):   
            name = input("Enter the name of the student: ")
            roll_number = int(input("Enter the roll number: "))
            percent = float(input("Enter the overall percentage: "))
            record = [name,roll_number,percent]
            l.append(record)
        writer.writerows(l)

create()

def search():
        f= open("student.csv","r")
        reader = csv.reader(f)
        name = input("Enter the name to search: ")
        found = False
        for i in reader:
            if i[0]!= ' ':
                if i[0] == name:
                    print("Name: ",i[0])
                    print("Roll number", i[1])
                    print("Percentage", i[2])
                    found = True
        if found == False:
            print("Record not found")

search()
"""
# 14. Create a menu driven program and create a function to write, read and display the data.
"""
import csv

def menu():
    print("1:Read and Display data")
    print("2:Add data in the file")
    print("3:exit")
    option = int(input("Enter the option: "))
    while True:
        if option == 1:
            read()
        elif option == 2:
            add_data()
        elif option == 3:
            print("Exiting...")
            break
        else:
            print("Enter a valid option")

def read():
    with open("Hhw.py/student.csv", 'r', newline='' ) as f:
        reader = csv.reader(f)
        for i in reader:
            print(i)
    menu()

def add_data():
    with open("Hhw.py/student.csv", 'a+', newline='' ) as f:
        writer = csv.writer(f)
        l = []
        n = int(input("Enter the numbers of records to be inserted: "))
        for i in range(n):   
            name = input("Enter the name of the student: ")
            roll_number = int(input("Enter the roll number: "))
            percent = float(input("Enter the overall percentage: "))
            print("Data successfully inserted!")
            record = [name,roll_number,percent]
            l.append(record)
        writer.writerows(l)
    menu()
    
menu()
"""
# 15. Create a CSV File with User and password and read and search the password.
"""
import csv

def create():
    with open("Hhw.py/student.csv", 'a+', newline='' ) as f:
        writer = csv.writer(f)
        l = []
        n = int(input("Enter the numbers of records to be inserted: "))
        for i in range(n):   
            User_id = input("Enter the user id: ")
            password = input("Enter the passwrod: ")
            record = [User_id , password]
            l.append(record)
        writer.writerows(l)

def search():
    with open("Hhw.py/student.csv", 'r', newline='' ) as f:
        reader = csv.reader(f)
        userid = input("Enter the name to search: ")
        found = False
        for i in reader:
            if i[0]!= ' ':
                if i[0] == userid:
                    print("User id: ",i[0])
                    print("Password", i[1])
                    found = True
        if found == False:
            print("Record not found")
"""
# 16. Create a CSV file and add multiple rows to it
"""
import csv 

def create():
    with open("Hhw.py/student.csv", 'a+', newline='' ) as f:
        writer = csv.writer(f)
        l = []
        n = int(input("Enter the numbers of records to be inserted: "))
        for i in range(n):   
            name = input("Enter the name of the student: ")
            roll_number = int(input("Enter the roll number: "))
            percent = float(input("Enter the overall percentage: "))
            record = [name,roll_number,percent]
            l.append(record)
        writer.writerows(l)

create()
"""
# 17. Connect an employee database and insert two rows
"""
import mysql.connector as mycon
con = mycon.connect(host = "localhost" , user = "root" , password = "prakalp1", database = "hhw")
cur = con.cursor()
for i in range(2):
    employee_id = int(input("Enter the employee id: "))
    Name = input("Enter the name of employee: ")
    salary = float(input("Enter the salary of the employee: "))
    query = "INSERT INTO employee (employee_id, name, salary) VALUES (%s, %s, %s)"
    
    cur.execute(query)
    con.commit()
print("Done")
"""
# 18. Connect an employee database and search and display the record
"""
import mysql.connector
mycon=mysql.connector.connect(host="localhost",password="prakalp1",user="root")
mycursor=mycon.cursor()
ENo=int(input("Enter the employee id you wish to search:"))
query="select * from Employee where EmpNo={}".format(ENo)
mycursor.execute(query)
records=mycursor.fetchall()
for i in records:
    print("EmpNo:",i[0])
    print("Name:",i[1])
    print("Designation:",i[3])
    print("Department:",i[4])
    print("Joining date:",i[5])
    print("Salary:",i[2])
mycon.close()
"""
# 19. Connect to a student database and update the record for a given roll number.
"""
import mysql.connector
mycon=mysql.connector.connect(host="localhost",password="prakalp1",user="root",database="SCHOOL")
mycursor=mycon.cursor()
Rno=int(input("Enter the roll no you want to modify:"))
mark=int(input("Enter the new mark you want to update:"))
query="update student set Marks={} where Rollno={}".format(mark,Rno)
mycursor.execute(query)
mycon.commit()
records=mycursor.fetchall()
"""
# 20. Connect to the product database and delete the record for the product ID
"""
import mysql.connector
mycon=mysql.connector.connect(host="localhost",password="prakalp1",user="root",database="productdata")
mycursor=mycon.cursor()
ProductID=int(input("Enter the id of the record you want to delete:"))
query="delete from PRODUCT where PID={}".format(ProductID)
mycursor.execute(query)
mycon.commit()
mycursor.execute("select * from product")
records=mycursor.fetchall()
print(records)
mycon.close()
"""