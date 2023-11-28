# Creating Histograms (Similar to Bar chart)

# import the boston dataset from the sklearn library
from sklearn.datasets import load_diabetes
# import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

# load diabetes dataset
diabetes_read_state_data = load_diabetes()
print(diabetes_read_state_data.DESCR)

# define x-axis for the data
x_axis = diabetes_read_state_data.data
# define y-axis for the target
y_axis = diabetes_read_state_data.target
# plot histogram
style.use('ggplot')
plt.figure(figsize=(7, 7))
plt.hist(y_axis, bins=50)
plt.xlabel("Diabetes Progression")
plt.ylabel("Number of Patients")
plt.title("Distribution of Diabetes Progression in Diabetes DataSet")
plt.show()
