# importing standard libraries for AI stuffs (and other stuff prob too)
import seaborn as sns #stats analysis
import tensorflow as tf #created/owned by google, idk what exactly its for
import numpy as np #fancy stuff? w/ numbers and python prob
import pandas as pd #dataframe
import matplotlib.pyplot as plt #plot graphs
import matplotlib.image as mpimg #output images

print("Tensorflow: ", tf.__version__, "Seaborne: ", sns.__version__)

# making a dataframe using the mnist dataset
mnist = tf.keras.datasets.mnist 
(x_train, y_train), (x_test, y_test) = mnist.load_data() # training data, testing data
# x = images(28x28 pixels), y = labels(int, 0-9)

sns.countplot(x = y_train) # x axis of graph = labels 
plt.show()

# check to make sure that there are NO values that aren't numbers (NaN = not a number)
print("Any NaN Training: ", np.isnan(x_train).any())
print("Any NaN Testing: ", np.isnan(x_test).any())

# tell the model what shape to expect
input_shape = (28, 28, 1) # 28x28 pixels, 1 color channel for grayscale (3 color channels for RGB)

# reshape the data to include all the images at once
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1) # (60_000, 28, 28, 1)
x_train = x_train/255.0 #normalize the data to be between 0 and 1
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
x_test = x_test/255.0