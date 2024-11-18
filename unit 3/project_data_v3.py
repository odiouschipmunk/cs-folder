basic_data=[['yeehaw!', 'mr b', 'com sci']]
#2d array in which it is [[review, teacher name],...]
#message=input('what do you wanna say to a teacher?')
all_teachers=[['mr b', 'com sci'], ['mr a', 'math'], ['mr c', 'english']]
print('teachers:')
for teacher in all_teachers:
    print(teacher[0])
#get data from user and add it
def teacher1():
    teacher=input('who do you want to send this message to?')
    while teacher not in [teacher[0] for teacher in all_teachers]:
        print('teacher not found')
        teacher=input('who do you want to send this message to?')
    classt=input('what class is this for?')
    #check if the class matches up with the teacher
    teacherindex=[teacher[0] for teacher in all_teachers].index(teacher)
    while classt!=all_teachers[teacherindex][1]:
        print('class does not match up with teacher')
        classt=input('what class is this for?')
    return [teacher, classt]
message=input('what do you wanna say to a teacher?')
teach=teacher1()
teacher=teach[0]
classt=teach[1]
basic_data.append([message, teacher, classt])

print(f'added {message} to the list of reviews')
print(f'all data: {basic_data}')
#export data as a csv file
import csv
with open('project_data.csv', 'a', newline='') as file:
    #in the form of message, teacher name, class
    writer=csv.writer(file)
    writer.writerows(basic_data)
    
print('data exported to project_data.csv')
csvdata=None
#read from csv file
with open('project_data.csv', 'r') as file:
    reader=csv.reader(file)
    csvdata=list(reader)
print(f'csv data: {csvdata}')

#todo; add timestamp, and topic of the message, and the class