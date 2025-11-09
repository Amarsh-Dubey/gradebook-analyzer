# GradeBook Analyzer

**Author:** Amarsh Dubey
**Date:** November 9, 2025
**Assignment:** Mini Project - Analyzing and Reporting Student Grades

## Overview

GradeBook Analyzer is a Python-based CLI tool that helps lecturers and educators analyze student grades quickly and accurately. The system automates statistical analysis, grade assignment, and generates comprehensive summaries in a user-friendly format.

## Features

- ✅ **Multiple Input Methods**: Manual entry or CSV file import
- - ✅ **Statistical Analysis**: Calculate mean, median, min, and max scores
  - - ✅ **Automatic Grade Assignment**: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
    - - ✅ **Grade Distribution**: Visual representation of grade counts
      - - ✅ **Pass/Fail Analysis**: Automatic filtering with 40 as passing threshold
        - - ✅ **Formatted Output**: Clean, tabular results sorted by performance
          - - ✅ **Interactive CLI**: Menu-driven interface with repeat analysis option
           
            - ## Installation
           
            - 1. Clone the repository:
              2. ```bash
                 git clone https://github.com/Amarsh-Dubey/gradebook-analyzer.git
                 cd gradebook-analyzer
                 ```

                 2. Ensure you have Python 3.6+ installed:
                 3. ```bash
                    python --version
                    ```

                    3. No external dependencies required - uses only Python standard library!
                   
                    4. ## Usage
                   
                    5. ### Running the Program
                   
                    6. ```bash
                       python gradebook.py
                       ```

                       ### Option 1: Manual Entry

                       1. Select option `1` from the menu
                       2. 2. Enter student names and marks one by one
                          3. 3. Type `done` when finished
                             4. 4. View the comprehensive analysis
                               
                                5. ### Option 2: CSV File Import
                               
                                6. 1. Prepare a CSV file with format:
                                   2. ```csv
                                      Name,Marks
                                      Alice Johnson,92
                                      Bob Smith,78
                                      ```

                                      2. Select option `2` from the menu
                                      3. 3. Enter the filename (e.g., `students.csv`)
                                         4. 4. View the analysis results
                                           
                                            5. ### Sample CSV File
                                           
                                            6. A sample `students.csv` file with 10 test records is included in the repository for testing purposes.
                                           
                                            7. ## Output Examples
                                           
                                            8. The program generates:
                                           
                                            9. - Statistical Analysis Summary
                                               - - Grade Distribution Chart
                                                 - - Pass/Fail Breakdown
                                                   - - Sorted Results Table
                                                    
                                                     - ## Project Structure
                                                    
                                                     - ```
                                                       gradebook-analyzer/
                                                       ├── gradebook.py      # Main program file
                                                       ├── students.csv      # Sample data file
                                                       ├── README.md         # Documentation
                                                       └── .gitignore        # Python gitignore
                                                       ```

                                                       ## Assignment Tasks Completed

                                                       - [x] **Task 1**: Project setup with CLI menu and welcome message
                                                       - [ ] - [x] **Task 2**: Manual entry and CSV import functionality
                                                       - [ ] - [x] **Task 3**: Statistical functions (mean, median, min, max)
                                                       - [ ] - [x] **Task 4**: Grade assignment and distribution counting
                                                       - [ ] - [x] **Task 5**: Pass/Fail filter using list comprehensions
                                                       - [ ] - [x] **Task 6**: Formatted results table with repeat analysis loop
                                                      
                                                       - [ ] ## Technologies Used
                                                      
                                                       - [ ] - **Python 3.6+**
                                                       - [ ] - **Standard Library Modules:**
                                                       - [ ]   - `csv` - CSV file handling
                                                       - [ ]     - `statistics` - Mean and median calculations
                                                       - [ ]   - `sys` - Program exit functionality
                                                      
                                                       - [ ]   ## Key Programming Concepts
                                                      
                                                       - [ ]   - Dictionary data structures for student records
                                                       - [ ]   - List comprehensions for filtering pass/fail students
                                                       - [ ]   - Modular function design for maintainability
                                                       - [ ]   - File I/O operations with error handling
                                                       - [ ]   - Control flow with if-elif-else statements
                                                       - [ ]   - Loops for iterative processing
                                                       - [ ]   - String formatting with f-strings
                                                      
                                                       - [ ]   ## Author
                                                      
                                                       - [ ]   **Amarsh Dubey**
                                                       - [ ]   - GitHub: [@Amarsh-Dubey](https://github.com/Amarsh-Dubey)
                                                      
                                                       - [ ]   ## License
                                                      
                                                       - [ ]   This project is created for educational purposes as part of the "Programming for Problem Solving using Python" course assignment.
                                                      
                                                       - [ ]   ## Acknowledgments
                                                      
                                                       - [ ]   - Course: Programming for Problem Solving using Python
                                                       - [ ]   - Assignment Weightage: 15% of course grade
                                                       - [ ]   - Estimated Duration: 8-10 hours
