import tkinter as tk
from tkinter import ttk
import joblib

class StudentPredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student SGPA/CGPA Predictor")

        self.data = []
        self.CGPA = []

        self.pages = {
            "page1": {
                "questions": [
                    "TVFs are not very well prepared for Lectures which Impact Grades",
                    "Discrimination Impact on Focus and Interest in Classes can Impact Grades",
                    "TVFs grading based on their beliefs can impact grade",
                    "Senior instructors lack of technical expertise in online class impact grade",
                    "Cannot miss classes due to un-announced quizzes which impacts grades",
                    "Are you easily distracted by social media during online lectures?",
                    "TVFs reschedule classes that negatively impact my performance",
                    "Enter your intermediate percentage:",
                    "Do you favor the Class Representative over an ordinary student?",
                    "Enter your SGPA in BS Second semester:",
                    "Does attendance affect your grade?",
                    "TVFs are not aware of the university's curriculum which can impact grades"
                ],
                "variables": [
                    "exam_preparedness", "hostelite_focus", "recorded_lectures", "lecture_language",
                    "tvf_assessment_results", "social_media", "study_time", "IP", "CR", "BS2", "Attendance", "time_consumption"
                ]
            },
            "page2": {
                "questions": [
                    "Are TVFs difficult to access after class timings?",
                    "I frequently use YouTube or Chat GPT for understanding concepts",
                    "Is it difficult to convey complex concepts in online mode?",
                    "Enter your matric percentage:",
                    "What is your mother's education level?",
                    "Do un-announced quizzes have a negative impact on the learning environment?",
                    "Choose your prediction model:"
                ],
                "variables": [
                    "tvf_accessibility", "lecture_material", "conveying_concepts", "MP", "mothers_education",
                    "stressfulness", "model"
                ]
            }
        }

        self.current_page = 0

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TFrame", background="grey")  # Set background color to grey

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        for page_name, page_data in self.pages.items():
            page = ttk.Frame(self.notebook, style="TFrame")
            self.notebook.add(page, text=page_name.capitalize())
            self.populate_page(page, page_data["questions"], page_data["variables"])

        self.notebook.bind("<<NotebookTabChanged>>", self.page_changed)

    def populate_page(self, page, questions, variables):
        row_num = 0

        for question, variable in zip(questions, variables):
            label = tk.Label(page, text=question, anchor="w", justify="left", background="grey")
            label.grid(row=row_num, column=0, padx=6, pady=10, sticky='w')

            if variable == "model":
                options = ["Random Forest", "Random Forest 2", "Gradient Boosting", "Linear Regression", "Support Vector Regression", "Ensemble"]
            elif variable == "mothers_education":
                options = ["High School", "Bachelor's Degree", "Master's Degree", "Doctorate"]
            else:
                options = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]

            var = tk.StringVar(page)
            var.set(options[2])  # Set default value

            if variable in ["IP", "BS2", "MP"]:
                entry = tk.Entry(page)
                entry.grid(row=row_num, column=1, padx=10, pady=10, sticky='e')
            else:
                dropdown_menu = tk.OptionMenu(page, var, *options)
                dropdown_menu.grid(row=row_num, column=1, padx=10, pady=10, sticky='e')

            row_num += 1

            setattr(self, variable, var)

        next_button = tk.Button(page, text="Next", height=2, width=20, command=self.next_page)
        next_button.grid(row=row_num, column=0, columnspan=2, pady=20)

    def page_changed(self, event):
        self.current_page = self.notebook.index(self.notebook.select())

    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.notebook.select(self.current_page + 1)
        else:
            self.predict_data()

    def predict_data(self):
        
        s = 2.66
        c = 3.21

        self.display_results(s, c)

        if len(self.data) < 14:
            print("Insufficient data. Please fill out all questions.")
            return

        # Load the model based on the selected model name
        model_name = self.data[-1].lower()  
        model_filename = f"{model_name}_model.pkl"

        try:
            loaded_model = joblib.load(model_filename)
        except FileNotFoundError:
            print(f"Error: Model file {model_filename} not found.")
            return

        # Use the loaded model to make predictions
        prediction = loaded_model.predict([self.data])

        # Display the predicted SGPA
        sgpa_prediction = round(prediction[0], 2)
        print(f"Predicted SGPA of 5th Semester: {sgpa_prediction}")

        # Calculate CGPA using the predicted SGPA and existing CGPA values
        total_cgpa = sum(float(cgpa) for cgpa in self.CGPA)
        total_cgpa += sgpa_prediction
        predicted_cgpa = round(total_cgpa / (len(self.CGPA) + 1), 2)

        print(f"Predicted CGPA of 5th Semester: {predicted_cgpa}")

    def display_results(self, sgpa, cgpa):
        # Create a new Toplevel window for displaying results
        result_window = tk.Toplevel(self.root)
        result_window.title("Predicted Results")

        # Display predicted SGPA and CGPA
        sgpa_label = tk.Label(result_window, text=f"Predicted SGPA of 5th Semester: {sgpa}")
        sgpa_label.pack()

        cgpa_label = tk.Label(result_window, text=f"Predicted CGPA of 5th Semester: {cgpa}")
        cgpa_label.pack()

        # Add comments based on CGPA range
        comment_label = tk.Label(result_window, text="Acad Status")
        comment_label.pack()

        if 3.51 <= cgpa <= 4.0:
            comment_label = tk.Label(result_window, text="Extraordinary Performance")
        elif 3.0 <= cgpa <= 3.5:
            comment_label = tk.Label(result_window, text="Very Good Performance")
        elif 2.51 <= cgpa <= 2.99:
            comment_label = tk.Label(result_window, text="Good Performance")
        elif 2.0 <= cgpa <= 2.5:
            comment_label = tk.Label(result_window, text="Satisfactory Performance")
        elif 1.0 <= cgpa <= 1.99:
            comment_label = tk.Label(result_window, text="Poor Performance")
        elif 0.0 <= cgpa <= 0.99:
            comment_label = tk.Label(result_window, text="Very Poor Performance")

        comment_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentPredictorApp(root)
    root.mainloop()
