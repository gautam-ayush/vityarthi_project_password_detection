import tkinter as tk
import re

class PasswordStrengthChecker:
    def __init__(self, root):
        """
        Initialize the GUI application.
        """
        self.root = root
        self.root.title("Password Strength Checker")
        # Increased height slightly to fit the checkbox and feedback area
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # --- UI COMPONENTS ---

        # Title Label
        self.title_label = tk.Label(
            root, 
            text="Check Your Password Strength", 
            font=("Helvetica", 14, "bold"),
            pady=15
        )
        self.title_label.pack()

        # Password Entry Label
        self.pass_label = tk.Label(root, text="Enter Password:")
        self.pass_label.pack()

        # Entry Box 
        # show="*" is the default, but we can change this dynamically
        self.password_entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        # --- NEW FEATURE: SHOW PASSWORD CHECKBOX ---
        self.show_pass_var = tk.IntVar() # Variable to track checkbox state (0 or 1)
        self.show_pass_check = tk.Checkbutton(
            root, 
            text="Show Password", 
            variable=self.show_pass_var, 
            command=self.toggle_password # Calls function when clicked
        )
        self.show_pass_check.pack()
        # -------------------------------------------

        # Check Button
        self.check_button = tk.Button(
            root, 
            text="Check Strength", 
            command=self.check_strength, 
            bg="#007bff", 
            fg="white", 
            font=("Arial", 10, "bold")
        )
        self.check_button.pack(pady=15)

        # Result Label 
        self.result_label = tk.Label(
            root, 
            text="", 
            font=("Helvetica", 12, "bold")
        )
        self.result_label.pack()

        # Feedback Label
        self.feedback_label = tk.Label(
            root, 
            text="", 
            fg="gray", 
            font=("Arial", 9),
            justify=tk.LEFT # Align feedback text to the left
        )
        self.feedback_label.pack(pady=5)

    def toggle_password(self):
        """
        Toggles the visibility of the password characters by configuring the 'show' attribute.
        """
        if self.show_pass_var.get() == 1:
            # If checkbox is checked (value is 1), remove the masking character
            self.password_entry.config(show="")
        else:
            # If unchecked (value is 0), mask characters with asterisk
            self.password_entry.config(show="*")

    def check_strength(self):
        """
        Logic to determine password strength based on criteria (length,
        uppercase, lowercase, number, special character).
        """
        password = self.password_entry.get()
        score = 0
        feedback_messages = []

        # 1. Length Check
        if len(password) >= 8:
            score += 1
        else:
            feedback_messages.append("- Make it at least 8 characters long")

        # 2. Uppercase Check
        if re.search(r"[A-Z]", password):
            score += 1
        else:
            feedback_messages.append("- Add uppercase letters (A-Z)")

        # 3. Lowercase Check
        if re.search(r"[a-z]", password):
            score += 1
        else:
            feedback_messages.append("- Add lowercase letters (a-z)")

        # 4. Number Check
        if re.search(r"[0-9]", password):
            score += 1
        else:
            feedback_messages.append("- Add numbers (0-9)")

        # 5. Special Character Check
        # Regex covers common special characters
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            feedback_messages.append("- Add special characters (@, #, $, etc.)")

        self.update_ui(score, feedback_messages, len(password))

    def update_ui(self, score, feedback, length):
        """
        Updates the result labels based on the calculated score.
        """
        if length == 0:
            self.result_label.config(text="Please enter a password", fg="black")
            self.feedback_label.config(text="")
            return

        # Determine strength level based on score (max score is 5)
        if score == 5:
            self.result_label.config(text="STRONG PASSWORD", fg="green")
            self.feedback_label.config(text="Great job!")
        elif score >= 3:
            self.result_label.config(text="MEDIUM STRENGTH (Score: {}/5)".format(score), fg="orange")
            self.feedback_label.config(text="To improve, you need to:\n" + "\n".join(feedback))
        else:
            self.result_label.config(text="WEAK PASSWORD (Score: {}/5)".format(score), fg="red")
            self.feedback_label.config(text="To improve, you need to:\n" + "\n".join(feedback))

if __name__ == "__main__":
    root = tk.Tk()
    # Ensure the class is initialized with the correct constructor name
    app = PasswordStrengthChecker(root)
    root.mainloop()