# CodeAlpha Python Programming Internship 🚀

Welcome to my repository for the **CodeAlpha Python Programming Internship** (June 1st, 2026 – June 30th, 2026). This repository serves as a centralized portfolio containing all the tasks and automation tools I developed during the program.

---

## 📁 Repository Structure

Each task is self-contained within its own directory, featuring independent logic and clean data handling:

```text
Aky29-CodeAlpha_Python_Programming/
│
├── Task_1_Hangman_Game/
│   └── hangman.py
│
├── Task_2_Email_Extractor/
│   └── email_extractor.py
│
└── Task_3_Stock_Tracker/
    ├── stock_tracker.py
    └── Investment.csv
```

🛠️ Project Summaries
🎮 Task 1: Word Guessing Game (Hangman Style)
Description: An interactive terminal game where a user attempts to guess a secret word within 5 attempts.

Key Concepts Used: while loops, conditional logic (if-elif-else), indexing, string manipulation, and dynamic terminal output.

How It Works: The program prompts for a secret word, loops through user guesses, and compares characters element-by-element to provide partial feedback (using underscores for unmatched letters) while preventing index overflows.

📧 Task 2: Automated Email Extractor
Description: A text-parsing utility that scans raw inputs to find and extract all valid email addresses instantly.

Key Concepts Used: Regular Expressions (re module), data collection, and string parsing.

How It Works: Uses a rigorous regex pattern ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}) to isolate valid emails from text blocks and outputs them in a clean, user-friendly listed layout.

📈 Task 3: Stock Investment Tracker
Description: A data tracking system that maps user stock inputs against a database dictionary of prices, calculates total investments, and exports the metrics to a spreadsheet.

Key Concepts Used: Dictionary mapping, persistent file manipulation, CSV Reading/Writing (csv.DictWriter, csv.DictReader).

How It Works: Prompts users for stock tickers and volumes, computes cost calculations on the fly, aggregates records into a structured list, and flushes them safely into an Investment.csv file upon completion.

🚀 How to Run the Code Locally
Clone the Repository:

Bash
git clone [https://github.com/Aky29/Aky29-CodeAlpha_Python_Programming.git](https://github.com/Aky29/Aky29-CodeAlpha_Python_Programming.git)
Navigate to the Repository Folder:

Bash
cd Aky29-CodeAlpha_Python_Programming
Execute Any Task:
Navigate into the specific task folder and run the python file. For example, to run the Stock Tracker:

Bash
cd Task_3_Stock_Tracker
python stock_tracker.py

👤 Intern Details

Name: Anish Kumar Yadav

Student ID: CA/DF1/108396

Domain: Python Programming

Duration: June 2026
