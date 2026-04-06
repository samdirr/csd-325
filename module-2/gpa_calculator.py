# Sam Dirr
# CSD325
# Module 2.2
# GPA Calculator Program

#mapping of letter grades to grade points to be used as a database call for later
GRADE_POINTS = {
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0
}

#create class of Student to capture first and last name along with course credits and grades
class Student:
    def __init__(self, first_name, last_name):
        """initialize the students first and last name for database"""

        #first, last, credits start 0, grade points start 0
        self.first_name = first_name
        self.last_name = last_name
        self.total_credits = 0
        self.total_grade_points = 0.0

    #add course and grade as input and translate it with if else to filter out incorrect values (this is for integrity and accuracy)
    #use self to add to student from database
    def add_course(self, credits, grade):
        """add the courses credits and grade to the record of the student"""
        grade = grade.upper()
        if grade in GRADE_POINTS: #call to database
            self.total_credits += credits
            #total grade += Grade Points x Credits
            self.total_grade_points += GRADE_POINTS[grade] * credits
        else: #Invalid please enter valid grade
            print(f"Invalid grade '{grade}' entered. Please enter a valid grade (A, B+, B, C+, C, D, F).")

    #calculate gpa and return valid output to student
    def calculate_gpa(self):
        """calculate and return students cumulative GPA"""
        if self.total_credits == 0:
            return 0.0
        #GPA is total grade points divided by total credits
        return self.total_grade_points / self.total_credits

    #display the cumulative gpa that we just calculated
    #GPA add to profile
    #print an output of first name, last name, culumative gpa
    def display_gpa(self):
        """display the students cumulative GPA"""
        gpa = self.calculate_gpa()
        print(f"\n{self.first_name} {self.last_name}'s cumulative GPA is: {gpa:.2f}")

#print and ask for first name
#print and ask for last name
#take those two inputs and create first name and last name inputs for profile to use for "self"
def get_student_name():
    """time to ask user for students first and last name"""
    first_name = input("Enter the student's first name: ").strip()
    last_name = input("Enter the student's last name: ").strip()
    return first_name, last_name

#get course grade and credits
def get_course_data():
    """ask user for course credits and grades"""
    #start with credits input done when finished for multiple inputs/loop effect
    while True: #while true ask for credits until done
        credits_input = input("\nEnter course credits (or type 'done' to finish): ").strip()
        if credits_input.lower() == 'done': #break loop
            return None, None
        try: #test if input not done is valid
            credits = float(credits_input)
            if credits <= 0:
                print("Credits must be a positive number.") #ask for valid input due to being invali
                continue
        except ValueError: #ask for valid input due to being invalid
            print("Invalid input for credits. Please enter a numeric value.")
            continue

        #all good values are listed as A, B+, B, C+, C, D, F
        grade = input("Enter the grade received (A, B+, B, C+, C, D, F): ").strip().upper()
        if grade not in GRADE_POINTS:
            print("Invalid grade entered. Please enter a valid grade (A, B+, B, C+, C, D, F).") ##ask for valid input due to being invali
            continue

        return credits, grade

#this is the 'simple' part
#set main to run the GPA calculator. We need first name, last name to get student name.
#then we set student profile
def main():
    """Main function to run the GPA calculator."""
    first_name, last_name = get_student_name()
    student = Student(first_name, last_name)

    #while in a student profile collect data for credits and grades
    while True:
        credits, grade = get_course_data()
        if credits is None:
            break
        student.add_course(credits, grade)
    #call the display_gpa for the student pofile
    student.display_gpa()

#Execute main
if __name__ == "__main__":
    main()
