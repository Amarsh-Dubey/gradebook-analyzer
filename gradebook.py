# GradeBook Analyzer by Amarsh Dubey
# Date: November 9, 2025

import csv
import sys

def show_welcome():
          print("="*50)
          print("    GRADEBOOK ANALYZER")
          print("="*50)
          print("Welcome!")

def show_menu():
          print("\n" + "="*50)
          print("MENU:")
          print("1. Enter marks manually")
          print("2. Load from CSV file")
          print("3. Exit")
          print("="*50)

def enter_marks():
          students = {}
          print("\nEnter student data (type 'done' to finish):")
          while True:
                        name = input("Student name (or 'done'): ")
                        if name == 'done':
                                          break
                                      try:
                                                        marks = float(input("Marks: "))
                                                        if marks >= 0 and marks <= 100:
                                                                              students[name] = marks
                                                                          else:
                print("Please enter marks between 0 and 100")
                                                    except:
            print("Invalid input")
                    return students

def load_csv():
          students = {}
    filename = input("Enter filename: ")
    try:
                  file = open(filename, 'r')
                  reader = csv.reader(file)
                  next(reader)
                  for row in reader:
                                    name = row[0]
                                    marks = float(row[1])
                                    students[name] = marks
                                file.close()
        print("Loaded", len(students), "students")
    except:
        print("File not found")
    return students

def get_average(students):
          total = 0
    for marks in students.values():
                  total = total + marks
    average = total / len(students)
    return average

def get_highest(students):
          highest = 0
    for marks in students.values():
                  if marks > highest:
                                    highest = marks
                            return highest

def get_lowest(students):
          lowest = 100
    for marks in students.values():
                  if marks < lowest:
                                    lowest = marks
                            return lowest

def get_grade(marks):
          if marks >= 90:
                        return 'A'
                    elif marks >= 80:
                                  return 'B'
                              elif marks >= 70:
                                            return 'C'
                                        elif marks >= 60:
                                                      return 'D'
                                                  else:
        return 'F'

def show_statistics(students):
          print("\n" + "="*50)
    print("STATISTICS")
    print("="*50)
    print("Total Students:", len(students))
    print("Average Marks:", round(get_average(students), 2))
    print("Highest Marks:", get_highest(students))
    print("Lowest Marks:", get_lowest(students))

def show_grades(students):
          grades = {}
    for name in students:
                  marks = students[name]
        grade = get_grade(marks)
        grades[name] = grade
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0
    for grade in grades.values():
                  if grade == 'A':
                                    a_count = a_count + 1
                                elif grade == 'B':
                                                  b_count = b_count + 1
                                              elif grade == 'C':
                                                                c_count = c_count + 1
                                                            elif grade == 'D':
                                                                              d_count = d_count + 1
                                                                          else:
            f_count = f_count + 1
    print("\n" + "="*50)
    print("GRADE DISTRIBUTION")
    print("="*50)
    print("Grade A:", a_count)
    print("Grade B:", b_count)
    print("Grade C:", c_count)
    print("Grade D:", d_count)
    print("Grade F:", f_count)
    return grades


def show_pass_fail(students):
          passed = 0
    failed = 0
    for name in students:
                  marks = students[name]
        if marks >= 40:
                          passed = passed + 1
                      else:
            failed = failed + 1
    print("~"*50)
    print("PASS/FAIL SUMMARY")
    print("~"*50)
    print("Passed:", passed)
    print("Failed:", failed)


def show_results(students, grades):
          print("~"*50)
    print("RESULTS TABLE")
    print("~"*50)
    names = []
    for name in students:
                  names.append(name)
    for i in range(len(names)):
                  for j in range(i+1, len(names)):
                                    if students[names[i]] < students[names[j]]:
                                                          temp = names[i]
                                                          names[i] = names[j]
                                                          names[j] = temp
                                              for name in names:
                                                            marks = students[name]
                                                            grade = grades[name]
                                                            print(name, marks, grade)


def main():
          show_welcome()
    while True:
                  show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
                          students = enter_marks()
        elif choice == "2":
            students = load_csv()
        elif choice == "3":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice")
            continue
        if len(students) == 0:
                          print("No students loaded")
            continue
        show_statistics(students)
        grades = show_grades(students)
        show_pass_fail(students)
        show_results(students, grades)
        again = input("Analyze again? (y/n): ")
        if again != "y":
                          print("Goodbye!")
            break


if __name__ == "__main__":
          main()
