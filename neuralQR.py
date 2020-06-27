#вся инфа с официального сайта
#https://github.com/tensorflow/docs-l10n/blob/master/site/ru/tutorials/keras/classification.ipynb
# TensorFlow и tf.keras
import tensorflow as tf
from tensorflow import keras

# Вспомогательные библиотеки
import numpy as np
import matplotlib.pyplot as plt

def main():
    mnist = keras.datasets.mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
    
    model.fit(train_images, train_labels, epochs=10)

    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
    print('\nТочность на проверочных данных:', test_acc)

    model.save('emnist_digits.h5')

if __name__ == '__main__':
    main()