# Assuming you have already imported the necessary libraries

# import the boston dataset from the sklearn library
from sklearn.datasets import load_diabetes
# import matplotlib
import matplotlib.pyplot as plt


# Load the diabetes dataset
diabetes_data = load_diabetes()

# Define x-axis for the data (features)
x_axis = diabetes_data.data

# Define y-axis for the target variable
y_axis = diabetes_data.target

# Plot scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x_axis[:, 2], y_axis, alpha=0.5, color='green', edgecolors='black')
plt.xlabel('BMI (Body Mass Index)')
plt.ylabel('Diabetes Progression')
plt.title('Scatter Plot of Diabetes Progression vs BMI')
plt.show()
