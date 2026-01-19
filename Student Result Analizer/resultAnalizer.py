#Features
#●	Input student data
#●	Calculate percentage
#●	Assign grades
#●	Save results to a file

def main():
    s_detail = {}
    studentData(s_detail)
    

def studentData(s_detail):
    roll_num=  int(input("Roll Number : ")) 
    s_detail["roll_num"] = roll_num

    if check_roll_number_exists(s_detail["roll_num"]):
        return print("------------Roll number already Exist----------------")
        

    s_detail["name"] = input("Student Name : ")
    s_detail["English"] = int(input("marks of English : "))
    s_detail["Biology"] = int(input("marks of Biology : "))
    s_detail["Chemistry"] = int(input("marks of Chemistry : "))
    s_detail["Physics"] = int(input("marks of Physics : ")) 
    s_detail["Hindi"] = int(input("marks of Hindi : "))

    cal_pecentage(s_detail)
    grades(s_detail)
    write_on_file(s_detail)
    read_on_file(s_detail,roll_num)

def check_roll_number_exists(roll_num):
    try:
        with open("Student_Result.txt","r")as file:
            line = file.readline()
            while line:
                s_detail = eval(line)
                if s_detail["roll_num"] == roll_num:
                    return True
                line = file.readline()
    except FileNotFoundError:
        return False
    return False

def cal_pecentage(s_detail):
    obt_marks = s_detail["English"]+s_detail["Biology"]+s_detail["Chemistry"]+s_detail["Physics"]+s_detail["Hindi"]
    total_marks = 500
    percentage = (obt_marks/total_marks) * 100

    s_detail["Percentage"] = percentage
    print(f"\n{s_detail["name"]} student percent is : {percentage:.2f}%\n")

def grades(s_detail):
    percent = s_detail["Percentage"]
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

def write_on_file(s_detail):
     line = str(s_detail)
     with open("Student_Result.txt","a")as file:
          file.writelines(line+"\n")

def read_on_file(s_detail,roll_num):
     with open("student_Result.txt","r")as file:
          line = file.readline()
          while line:
                s_detail = eval(line)
                if s_detail["roll_num"] == roll_num:
                    return print(line)
                line = file.readline()

main()