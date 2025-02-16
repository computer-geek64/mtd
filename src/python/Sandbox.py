#!/usr/bin/python3
# Sandbox.py
# Ashish D'Souza
# December 5th, 2018

import tensorflow as tf
import numpy as np


array = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6]
]
print(array[0])
print(array[0][0])
# print(array[0, 0])
print(np.array(array)[:, 0])
exit(0)


with tf.name_scope("input_layer"):
    x_training_data = tf.placeholder(dtype=tf.float32, shape=[None, 1], name="x_training_data")
y_training_data = tf.placeholder(dtype=tf.float32, shape=[None, 1], name="y_training_data")

with tf.name_scope("hidden_layer"):
    hidden_layer = tf.layers.dense(x_training_data, 1, activation=tf.nn.leaky_relu, name="hidden_layer")

with tf.name_scope("output_layer"):
    output = tf.layers.dense(hidden_layer, 1, name="output_layer")

with tf.name_scope("loss_function"):
    loss = tf.divide(tf.reduce_sum(tf.square(tf.subtract(y_training_data, output))), tf.constant(1, dtype=tf.float32), name="loss")
    print(tf.get_default_graph().get_tensor_by_name("loss_function/loss:0"))

loss_summary = tf.summary.scalar(name="loss_summary", tensor=loss)

with tf.name_scope("training"):
    optimizer = tf.train.ProximalAdagradOptimizer(learning_rate=0.1, name="optimizer")
    train = optimizer.minimize(loss, name="train")

summaries = tf.summary.merge_all()
writer = tf.summary.FileWriter("./graphs", tf.get_default_graph())

init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init)

print(tf.get_default_graph().get_tensor_by_name("hidden_layer:0"))
exit(0)
for i in range(10000):
    sess.run(train, feed_dict={x_training_data: [[0], [1], [2], [3], [4]], y_training_data: [[3], [4], [5], [6], [7]]})
    writer.add_summary(sess.run(summaries, feed_dict={x_training_data: [[0], [1], [2], [3], [4]], y_training_data: [[3], [4], [5], [6], [7]]}), i)

training_loss = sess.run(loss, feed_dict={x_training_data: [[0], [1], [2], [3], [4]], y_training_data: [[3], [4], [5], [6], [7]]})
prediction = sess.run(output, feed_dict={x_training_data: [[0], [1], [2], [3], [4]]})
print(prediction)
print(training_loss)
