#Features
#●	Input student data
#●	Calculate percentage
#●	Assign grades
#●	Save results to a file
import csv
import os
file_name = "Student_Result.csv"
def main():
    s_detail = {}
    create_file()
    studentData(s_detail)



def studentData(s_detail):
    roll_num=  int(input("Roll Number : ")) 

    if check_roll_number_exists(roll_num):
        print("------------Roll number already Exist----------------")
        return
        
    s_detail["roll_num"] = roll_num
    s_detail["name"] = input("Student Name : ")
    s_detail["English"] = int(input("marks of English : "))
    s_detail["Biology"] = int(input("marks of Biology : "))
    s_detail["Chemistry"] = int(input("marks of Chemistry : "))
    s_detail["Physics"] = int(input("marks of Physics : ")) 
    s_detail["Hindi"] = int(input("marks of Hindi : "))

    cal_pecentage(s_detail)
    grades(s_detail)
    write_on_file(s_detail)
    read_on_file(roll_num)
    

def check_roll_number_exists(roll_num):
    with open(file_name,"r")as file:
        reader = csv.DictReader(file)
        for read in reader:
            if int(read["roll number"]) == roll_num:
                 return True

    return False
    

def cal_pecentage(s_detail):
    obt_marks = s_detail["English"]+s_detail["Biology"]+s_detail["Chemistry"]+s_detail["Physics"]+s_detail["Hindi"]
    total_marks = 500
    percentage = (obt_marks/total_marks) * 100

    s_detail["Percent"] = percentage
    print(f"\n{s_detail["name"]} student percent is : {percentage:.2f}%\n")

def grades(s_detail):
    percent = s_detail["Percent"]
    if percent >=90:
        s_detail["Grade"] = "A"
    elif percent >=80:
         s_detail["Grade"] = "B"
    elif percent >=70:
         s_detail["Grade"] = "C"
    elif percent >=60:
         s_detail["Grade"] = "D"
    elif percent >=50:
         s_detail["Grade"] = "E"
    elif percent >=40:
         s_detail["Grade"] = "F"
    else:
         s_detail["Grade"] = "Fail"


def create_file():
     line = ["roll number","name","English","Biology","Chemistry","Physics","Hindi","percent","Grade"]
     if not os.path.exists(file_name):
        with open(file_name,"w",newline="" )as file:
            writer = csv.writer(file)
            writer.writerow(line)

def write_on_file(s_detail):
     line = [s_detail["roll_num"],s_detail["name"],s_detail["English"],s_detail["Biology"],s_detail["Chemistry"],s_detail["Physics"],s_detail["Hindi"],s_detail["Percent"],s_detail["Grade"]]
     with open(file_name,"a",newline="" )as file:
            writer = csv.writer(file)
            writer.writerow(line)
     
     

def read_on_file(roll_num):
     with open(file_name,"r")as file:
          reader = csv.DictReader(file)
          for read in reader:
               if int(read["roll number"]) == roll_num:
                    print(read)
                    return
     print("------------Student nor found--------------")
main()