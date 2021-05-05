print("Hello world")
import tensorflow as tf 
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as no


tf.config.experimental.list_physical_devices()
tf.test.is_built_with_cuda()

(x_train, y_train), (x_test,y_test) = tf.keras.datasets.cifar10.load_data()

x_train.shape