# GradeBook Analyzer
# Author: Amarsh Dubey
# Date: November 9, 2025

import csv
import sys
from statistics import mean, median

def print_welcome():
      print("="*60)
      print(" "*15 + "GRADEBOOK ANALYZER")
      print("="*60)
      print("Welcome to the GradeBook Analyzer!")

def print_menu():
      print("\n" + "="*60)
      print("MENU OPTIONS:")
      print("="*60)
      print("1. Manual entry of student marks")
      print("2. Load marks from CSV file")
      print("3. Exit")
      print("="*60)

def manual_entry():
      marks_dict = {}
      print("\nEnter student names and marks (enter 'done' when finished)")
      while True:
                name = input("Enter student name (or 'done' to finish): ").strip()
                if name.lower() == 'done':
                              break
                          if not name:
                                        print("Name cannot be empty.")
                                        continue
                                    try:
                                                  mark = float(input(f"Enter marks for {name}: "))
                                                  if 0 <= mark <= 100:
                                                                    marks_dict[name] = mark
                                                                else:
                print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            return marks_dict

def load_from_csv():
      marks_dict = {}
    filename = input("Enter CSV filename: ").strip()
    try:
              with open(filename, 'r') as file:
                            csv_reader = csv.reader(file)
                            next(csv_reader)
                            for row in csv_reader:
                                              if len(row) >= 2:
                                                                    name = row[0].strip()
                                                                    try:
                                                                                              mark = float(row[1])
                                                                                              if 0 <= mark <= 100:
                                                                                                                            marks_dict[name] = mark
                                                                                                                    except ValueError:
                                                                                                                                              pass
                                                                                                                              print(f"Successfully loaded {len(marks_dict)} students")
                                                    except FileNotFoundError:
                        print("File not found.")
    return marks_dict

def calculate_average(marks_dict):
      if not marks_dict:
                return 0
    return mean(marks_dict.values())

def calculate_median(marks_dict):
      if not marks_dict:
                return 0
    return median(marks_dict.values())

def find_max_score(marks_dict):
      if not marks_dict:
                return 0
    return max(marks_dict.values())

def find_min_score(marks_dict):
      if not marks_dict:
                return 0
    return min(marks_dict.values())

def assign_grade(mark):
      if mark >= 90:
                return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'F'

def calculate_grades(marks_dict):
      grades_dict = {}
    for name, mark in marks_dict.items():
              grades_dict[name] = assign_grade(mark)
    return grades_dict

def grade_distribution(grades_dict):
      distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades_dict.values():
              distribution[grade] += 1
    return distribution

def filter_pass_fail(marks_dict):
      passed_students = [(name, mark) for name, mark in marks_dict.items() if mark >= 40]
    failed_students = [(name, mark) for name, mark in marks_dict.items() if mark < 40]
    return passed_students, failed_students

def print_statistics(marks_dict):
      print("\n" + "="*60)
    print("STATISTICAL ANALYSIS")
    print("="*60)
    print(f"Total Students: {len(marks_dict)}")
    print(f"Average Marks: {calculate_average(marks_dict):.2f}")
    print(f"Median Marks: {calculate_median(marks_dict):.2f}")
    print(f"Maximum Score: {find_max_score(marks_dict):.2f}")
    print(f"Minimum Score: {find_min_score(marks_dict):.2f}")

def print_grade_distribution(distribution):
      print("\n" + "="*60)
    print("GRADE DISTRIBUTION")
    print("="*60)
    for grade in ['A', 'B', 'C', 'D', 'F']:
              count = distribution[grade]
        print(f"Grade {grade}: {count} students")

def print_pass_fail_summary(passed, failed):
      print("\n" + "="*60)
    print("PASS/FAIL SUMMARY")
    print("="*60)
    print(f"Passed Students: {len(passed)}")
    print(f"Failed Students: {len(failed)}")

def print_results_table(marks_dict, grades_dict):
      print("\n" + "="*60)
    print("STUDENT RESULTS TABLE")
    print("="*60)
    print(f"{'Name':<25} {'Marks':<10} {'Grade':<10}")
    print("-"*60)
    sorted_students = sorted(marks_dict.items(), key=lambda x: x[1], reverse=True)
    for name, mark in sorted_students:
              grade = grades_dict[name]
        print(f"{name:<25} {mark:<10.2f} {grade:<10}")

def analyze_grades(marks_dict):
      if not marks_dict:
                print("No student data available.")
        return
    grades_dict = calculate_grades(marks_dict)
    print_statistics(marks_dict)
    distribution = grade_distribution(grades_dict)
    print_grade_distribution(distribution)
    passed, failed = filter_pass_fail(marks_dict)
    print_pass_fail_summary(passed, failed)
    print_results_table(marks_dict, grades_dict)

def main():
      print_welcome()
    marks_dict = {}
    while True:
              print_menu()
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == '1':
                      marks_dict = manual_entry()
            if marks_dict:
                              analyze_grades(marks_dict)
        elif choice == '2':
            marks_dict = load_from_csv()
            if marks_dict:
                              analyze_grades(marks_dict)
        elif choice == '3':
            print("Thank you for using GradeBook Analyzer!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        cont = input("\nAnalyze another dataset? (y/n): ").strip().lower()
        if cont != 'y':
                      print("Thank you for using GradeBook Analyzer!")
            break

if __name__ == "__main__":
      main()
