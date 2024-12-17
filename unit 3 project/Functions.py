from pathlib import Path
import csv

#if it doesn't exist
def init_csv():
    if not Path("teacher_reviews.csv").exists():
        with open("teacher_reviews.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["review", "teacher", "class"])
            
def get_teachers():
    teachers = {}
    try:
        '''
        Goes through the teacher_data.csv file and gets all the unique teachers and what courses they teach
        '''
        with open("teacher_data_revised.csv", "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                teacher_name = row.get("Teacher", "").strip()
                course_name = row.get("Description", "").strip()
                if teacher_name and course_name: #is not empty
                    if teacher_name not in teachers:
                        teachers[teacher_name] = set()
                    teachers[teacher_name].add(course_name)
        # Convert sets to sorted lists because I'm awesome duh
        for teacher in teachers:
            teachers[teacher] = sorted(teachers[teacher])
        return teachers
    except Exception as e:
        print(f"Error reading teacher data: {e}")
        return {}
    
def read_reviews():
    reviews = []
    with open("teacher_reviews.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        reviews = list(reader)
    return reviews


def write_review(review):
    with open("teacher_reviews.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(review)

def show_reviews(teacher):
    reviews = read_reviews()
    return [review for review in reviews if review["teacher"] == teacher]