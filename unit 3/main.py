import csv
from pathlib import Path

# create CSV file if it doesn't exist
def init_csv():
    if not Path('teacher_reviews.csv').exists():
        with open('teacher_reviews.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['review', 'teacher', 'class'])  # header

#read existing reviews
def read_reviews():
    reviews = []
    try:
        with open('teacher_reviews.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            reviews = list(reader)
    except FileNotFoundError:
        init_csv()
    return reviews

# new review
def write_review(review):
    with open('teacher_reviews.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(review)

# basic data
all_teachers = [['mr b', 'com sci'], ['mr a', 'math'], ['mr c', 'english']]

def teacher1():
    teacher = input('who do you want to send this message to?')
    while teacher not in [t[0] for t in all_teachers]:
        print('teacher not found')
        teacher = input('who do you want to send this message to?')

    classt = input('what class is this for?')
    teacherindex = [t[0] for t in all_teachers].index(teacher)
    while classt != all_teachers[teacherindex][1]:
        print('class does not match up with teacher')
        classt = input('what class is this for?')
    return [teacher, classt]
def get_teachers():
    teachers = {}
    try:
        with open('teacher_data.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                teacher_name = row.get('Teacher', '').strip()
                course_name = row.get('Course Name', '').strip()
                if teacher_name and course_name:
                    if teacher_name not in teachers:
                        teachers[teacher_name] = set()
                    teachers[teacher_name].add(course_name)
        # sets to sorted lists
        for teacher in teachers:
            teachers[teacher] = sorted(teachers[teacher])
        return teachers
    except Exception as e:
        print(f"Error reading teacher data: {e}")
        return {}
print(get_teachers())
def main():
    # create CSV if needed
    init_csv()

    # show available teachers
    print('teachers:')
    for teacher in all_teachers:
        print(teacher[0])

    # new review
    message = input('what do you wanna say to a teacher?')
    teach = teacher1()
    teacher, classt = teach[0], teach[1]

    # save review
    review = [message, teacher, classt]
    write_review(review)



    print(f'added {message} to reviews')

    # all reviews
    print('all reviews:')
    for review in read_reviews():
        print(review)

if __name__ == '__main__':
    main()
