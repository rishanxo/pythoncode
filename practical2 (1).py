#Write a program which reads poem.txt given below and invoke functions:
#i. countlow() that counts lowercase in the file.
#ii. countw() that counts number of words in the file.
#iii. countupper() that counts uppercase in the file.
#iv. disp() that displays each word separated by ‘*’
'''def countlow():
    f=open("poem.txt","r")
    r=f.read()
    lowercount=0
    lowercase="abcdefghijklmnopqrstuvwxyz"
    for i in r:
        if i in lowercase:
            lowercount=lowercount+1
    print(lowercount)
    f.close()
    return

def countw():
    f=open("poem.txt","r")
    r=f.read()
    wordcount=0
    for i in r:
        if i==" " or i== "\n":
            wordcount=wordcount+1
    wordcount =wordcount+1
    print(wordcount)
    f.close()
    return

def countupper():
    f=open("poem.txt","r")
    r=f.read()
    uppercount=0
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in r:
        if i in uppercase:
            uppercount=uppercount+1
    print(uppercount)
    f.close()
    return

def disp():
    f=open("poem.txt","r")
    r=f.read()
    word=""
    for i in r:
        if i !=" ":
            word=word+i
        else:
            word=word+"*"
    print(word)
    f.close()
    return

    
while True:
    print("1. Count  lowercase \n 2. Count  no of words \n 3. Count of uppercase \n 4. Display  words separated by *\n 5. Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        countlow()
    elif choice==2:
        countw()
    elif choice==3:
        countupper()
    elif choice==4:
        disp()
    else:
        break'''

#**Write a menu drive program to perform following operations into stud.csv.
#1. Add record
#2. Update &amp; Display records
#3. Exit
#The structure of file content is: [sid, sname, sbatch]
'''import csv
def Addrecord():
            f=open("stud.csv","w")
            print("Add record")
            wo=csv.writer(f)
            ans="y"
            while ans=="y":
                sid=int(input("Enter the roll no:"))
                sname=input("Enter the name:")
                sbatch=input("Enter the batch:")
                list=([sid,sname,sbatch])
                wo.writerow(list)
                ans=input("Do you want to continue?")
            f.close()
            return
def updaterecord():
            f=open("stud.csv","r")
            print("Update record")
            sid=int(input("Enter the roll no:"))
            sbatch=input("enter the new batch name:")
            ro=csv.reader(f)
            list=[]
            for i in ro:
                print (i)
                if i[0]==chr(sid):
                    i[2]=sbatch
                    print(i)
                list.append(i)
            f.close()
            
            f=open("stud.csv","w")
            wo=csv.writer(f)
            wo.writerows(list)
            print("modified list")
            print(list)
            f.close()
            return
while True:
    print("1. Add record \n 2. Update & Display record \n 3. Exit")
    choice=int(input("Enter your choice:"))
    list=[]
    ans="y"
    if choice==1:
            Addrecord()
    elif choice==2:
            updaterecord()
    else:
        break'''

#Write a program to create an employee database and search for an employee number and display the record or print appropriate message. The structure of record is: [empid, empname, salary]
'''import mysql.connector
mycon=mysql.connector.connect(host="localhost",password="Adu_0687",user="root",database="employee")
mycursor=mycon.cursor()
ENo=int(input("Enter the employee id you wish to search:"))
query="select * from Employee where EmpNo={}".format(ENo)
mycursor.execute(query)
records=mycursor.fetchall()
for i in records:
    print("EmpNo:",i[0])
    print("Name:",i[1])
    print("Salary:",i[2])
mycon.close()'''
#Write a program to connect to a student database and update the record. The structure of the record is: [rlno, name, stream]
'''import mysql.connector
mycon=mysql.connector.connect(host="localhost",password="Adu_0687",user="root",database="SCHOOL")
mycursor=mycon.cursor()
Rno=int(input("Enter the roll no you want to modify:"))
mark=int(input("Enter the new mark you want to update:"))
strm=input("Enter the new stream you want to updatedata =(mark, strm, Rno)
query1="update student set Marks=%s,stream = %s where Rollno=%s"
mycursor.execute(query1, data)
mycon.commit()
mycursor.execute("select * from student")
records=mycursor.fetchall()
for i in records:
    print(i)
mycon.close()'''
#Write a program to create an employee database and insert two rows into it.
#The structure of file content is: [eid, name, salary]
'''import mysql.connector
mycon=mysql.connector.connect(host="localhost", password="Adu_0687", user="root", database="employee")
mycursor=mycon.cursor()
query1="insert into Employee values(5,'Rajesh',1500,'Engineer','Field','2021-05-04')"
query2="insert into Employee values(6,'Sheela',10000,'Accountant','Accounts','2022-03-05')"
mycursor.execute(query1)
mycursor.execute(query2)
mycon.commit()
mycursor.execute("select * from employee")
records=mycursor.fetchall()
for i in records:
    print(i)
mycon.close()
'''
#Write a function that takes two numbers and returns the number that has minimum
#value in one’s place. For eg: if numbers passed are 524 and 169, then the function will
#return 524 because it has got minimum value in one’s place(524’s 4 &lt; 169&#39;s 9
'''def onesplace():
    num1=int(input("Enter the no:"))
    num2=int(input("Enter the no:"))
    value1=num1%10
    value2=num2%10
    if value1>value2:
        print(num2)
    else:
        print(num1)
onesplace()'''
#Write a program to create emp.csv. The structure of file content is: [Eid, Ename, Sal].
#Display the records whose salary is iin the range of 5000 to 15000.
import csv

#**Write a menu drive program to perform following operations into stud.csv.
#1. Add record
#2. Update &amp; Display records
#3. Exit
#The structure of file content is: [sid, sname, sbatch]
'''import csv
def Addrecord():
            f=open("stud.csv","w")
            print("Add record")
            wo=csv.writer(f)
            ans="y"
            while ans=="y":
                sid=int(input("Enter the roll no:"))
                sname=input("Enter the name:")
                sbatch=input("Enter the batch:")
                list=([sid,sname,sbatch])
                wo.writerow(list)
                ans=input("Do you want to continue?")
            f.close()
            return
def updaterecord():
            f=open("stud.csv","r")
            print("Update record")
            sid=int(input("Enter the roll no:"))
            sbatch=input("enter the new batch name:")
            ro=csv.reader(f)
            list=[]
            for i in ro:
                print (i)
                if i[0]==chr(sid):
                    i[2]=sbatch
                    print(i)
                list.append(i)
                break
            '''
