Readme
Problem statement
add the student detail (roll number , name , marks of 5 subject)
calculate the percentage of student
based on percent assign grade
write the student detail on file

Logic
Program start with main function
create a empty dictionary s_detail
call the studentData() function that take the student data input
	1. roll number
	2. name
	3. marks(English, Biology, Chemistry, Physics, Hindi)
check the roll number exist in the file using check_roll_number_exists() function
call cal_percentage() function to calculate function
call the grade function to assign in grade based on percentage
all the detail now saves in file Student_result.txt using write_on_file() function
read and print the stored student result using read_on_file() function

file structure
day7/
|-resultAnalizer.py
|-student_Result.txt
|-README.md
