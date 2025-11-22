# vityarthi_project_password_detection
Password Strength Checker (Tkinter GUI)

Overview

This is a simple, standalone desktop application built using Python and Tkinter for checking the strength of a password in real-time. It provides a strength rating (Weak, Medium, Strong) and actionable feedback on how to improve the password's security.

Features

Real-time Strength Scoring: Calculates a score out of 5 based on security criteria.

Visual Feedback: Displays the strength level using color-coded text (Red, Orange, Green).

Improvement Suggestions: Provides specific feedback on missing criteria (e.g., add special characters, increase length).

Toggle Visibility: Includes a "Show Password" checkbox to hide or display the entered text.

Requirements

This application requires Python (3.x recommended) and the standard library Tkinter, which is typically included with most Python installations.

Strength Calculation Criteria

The password strength is scored out of 5, with one point awarded for each of the following conditions met:

Length: At least 8 characters long.

Uppercase: Contains at least one uppercase letter (A-Z).

Lowercase: Contains at least one lowercase letter (a-z).

Numbers: Contains at least one digit (0-9).

Special Characters: Contains at least one special character (e.g., !@#$%^&*).

Score

Strength Level

Color

5/5

STRONG

Green

3-4/5

MEDIUM

Orange

0-2/5

WEAK

Red

How to Run the Application

Save the Code: Save the provided Python script as password_checker.py.

Execute: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command:

python password_checker.py


The GUI window will appear, and you can begin checking passwords immediately.