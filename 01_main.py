# importing numpy for generating randon numbers
import numpy as np
# import matplotlib library
import matplotlib.pyplot as plt
from matplotlib import style

# %matplotlib inline

# let's generate 10 random numbers
randomNumber = np.random.rand(10)

# to view the generated numbers
print(randomNumber)

# select the style of the plot
style.use('ggplot')
# plot the random number
plt.plot(randomNumber, 'g', label='line one', linewidth=2)
# x~axis is number of random numbers (index)
plt.xlabel('Range')
# y~axis is actual random number
plt.ylabel('Numbers')
# Title of the plot
plt.title('First Plot')

# To display the visualized data
plt.legend()
plt.show()
