# importing standard libraries for AI stuffs (and other stuff prob too)
import seaborn as sns #stats analysis
import tensorflow as tf #generic version of tensorflow, CPU version only    #created/owned by google, idk what exactly its for
import numpy as np #fancy stuff? w/ numbers and python prob
import pandas as pd #dataframe
import matplotlib.pyplot as plt #plot graphs
import matplotlib.image as mpimg #output images
import random #not really required

print("Tensorflow: ", tf.__version__, "Seaborne: ", sns.__version__)

# making a dataframe using the mnist dataset
mnist = tf.keras.datasets.mnist 
(x_train, y_train), (x_test, y_test) = mnist.load_data() # training data, testing data
# x = images(28x28 pixels), y = labels(int, 0-9)

# shows how many of each number
sns.countplot(x = y_train) # x axis of graph = labels 
plt.show()

# check to make sure that there are NO values that aren't numbers (NaN = not a number)
print("Any NaN Training: ", np.isnan(x_train).any())
print("Any NaN Testing: ", np.isnan(x_test).any())

# tell the model what shape to expect
input_shape = (28, 28, 1) # 28x28 pixels(p0x), 1 color channel for grayscale (3 color channels for RGB)

# reshape the data to include all the images at once
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1) # (60_000, 28, 28, 1)
x_train = x_train/255.0 #normalize the data to be between 0 and 1 (relative% instead of 0-255)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
x_test = x_test/255.0

# convert labels to be one-hot, not sparse
y_train = tf.one_hot(y_train.astype(np.int32), depth=10) #forcing the y_train data to be an integer through numpy, depth bc the vector has 10 parts
y_test = tf.one_hot(y_test.astype(np.int32), depth=10)

# show an example image from MNIST
example = random.randint(0,59_999)
plt.imshow(x_train[example][:,:,0], cmap='gray') #colon means not to change the value, cmap='gray' turns it to grayscale
plt.show()

batch_size = 128 #how many images to look at at a time; more in-depth data needs smaller batches
num_classes = 10 #bc theres 10 numbers
epochs = 5 #number of times through the data

# build the model
model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Conv2D(32, (5,5), padding='same', activation='relu', input_shape=input_shape),
        #convolutional 2D neural network building the edge detection: 32 kernels(filters), 5x5 p0x each; padding-> input+output same size; relu is a common shape; input_shape stays the same
        tf.keras.layers.Conv2D(32, (3,3), padding='same', activation='relu', input_shape=input_shape), #same but finer comb through
        tf.keras.layers.MaxPool2D(), #flatten and reduce the size of things; converge data
        tf.keras.layers.Dropout(0.25), #turn off a random 25% of the nuerons(filters) to prevent overfitting (learning/infering instead of memorizing)
        tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu', input_shape=input_shape), #more filters than previous Conv2D
        tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu', input_shape=input_shape),
        tf.keras.layers.Dense(num_classes, activation='softmax') #softmax activation gives probabilities that goes back to one-hot to get an estimate answer
    ]
)

# categorical_crossentropy is for one-hot, to force the prediction into a category; the metric for its answer is decided by is accuracy
model.compile(optimizer=tf.keras.optimizers.RMSprop(epsilon=1e-08), loss='categorical_crossentropy', metrics=['acc'])