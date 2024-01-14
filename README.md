# Project Title:
Semester 5 GPA Forecasting

# Description
The Semester 5 GPA Forecasting project aims to predict the SGPA and CGPA of students in their 5th semester using machine learning algorithms (Gradient Boosting Regressor, SVM Regressor, Random Forest, Linear Regressor and Voting Regressor). The project encompasses data preprocessing, exploratory data analysis (EDA), model development, data validation, deployment, and the development of a graphical user interface (GUI) for easy interaction.

# Guidelines for using the Project
Python 3.x 

Required Python libraries (NumPy, Pandas, Matplotlib, Seaborn, Joblib, Scikit-Learn, Tkinter for GUI)

# Project Structure
The project is organized as follows:

testing_data: Contains the dataset used for testing.

updated: Contains the dataset that is cleaned. 

useful_features: Contains the dataset used for training with removal of unnecessary features .

ensemble_model.pkl: Stores trained ensemble model.

gb_model.pkl: Stores trained gradient boosting regressor model.

lr_model.pkl: Stores trained linear regression model.

rf_model.pkl: Stores trained random forest model.

svr_model.pkl: Stores trained support vector regression model.

code_file: The source code for the project.

<blockquote>
  preprocessing: Code for data preprocessing.

  exploratory_analysis: Code for EDA.

  model_development: Code for predictive model development.

  data_validation: Code for validating the model with test data.

  deployment: Code for deployment and GUI development.
</blockquote>

# Running the Project
Open the project directory in VS Code.

Execute the code_file.ipynb to run the project.

# GUI Usage
After running the project, a GUI window will appear.

Enter the required input variables, as shortlisted after EDA, into the respective fields.

Select the desired machine learning algorithm for prediction.

Click the "Predict" button.

The predicted SGPA and CGPA will be displayed along with the performance classification based on the conditions provided.

# Additional Notes
Ensure that the necessary Python libraries are installed.

The project assumes that the required dataset is available in the folder.

# Credits
Mujtaba Zaidi https://www.linkedin.com/in/mujtaba-abbas-43406a206?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app - Project Lead

Syeda Farwa Rizvi - https://www.linkedin.com/in/syeda-farwa-rizvi-a9a97621a/ - Developer

Mohsin Raza - https://www.linkedin.com/in/mohsin-raza-0a4814224?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app - Data Scientist

Areej Dar - https://www.linkedin.com/in/areej-ijaz-511896241?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app - DevOps

# Conclusion
This project provides a comprehensive solution for predicting student performance in the 5th semester. Users can interact with the model through a user-friendly GUI, making it accessible and easy to use. Feel free to explore the code, adapt it to your specific needs, and contribute to the project's enhancement.
If you have any questions or encounter issues, please refer to the documentation or contact the project maintainers.
