import cv2
import pandas as pd
import numpy
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import image
from image_tools.utility_crop import crop
from image_tools.utility_crop import scale
from PIL import Image

import random
import math

IMG_SIZE = (150, 150)
MODEL_WEIGHTS_FILE = "./model_weights.h5"


class Classificator:
    def __init__(self, image_size: tuple = IMG_SIZE, model_weights_file: str = "model_weights.h5"):
        self.image_size = image_size
        self.model = self.make_model(
            input_shape=self.image_size + (3,), num_classes=2)
        self.model.load_weights(model_weights_file)

    def make_model(self, input_shape, num_classes):
        """
            Определение модели для классификации
        """
        inputs = keras.Input(shape=input_shape)
        # Image augmentation block
        x = inputs

        # Entry block
        x = layers.Rescaling(1.0 / 255)(x)
        x = layers.Conv2D(32, 3, strides=2, padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Activation("relu")(x)

        x = layers.Conv2D(64, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Activation("relu")(x)

        previous_block_activation = x  # Set aside residual

        for size in [128, 256, 512, 728]:
            x = layers.Activation("relu")(x)
            x = layers.SeparableConv2D(size, 3, padding="same")(x)
            x = layers.BatchNormalization()(x)

            x = layers.Activation("relu")(x)
            x = layers.SeparableConv2D(size, 3, padding="same")(x)
            x = layers.BatchNormalization()(x)

            x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

            # Project residual
            residual = layers.Conv2D(size, 1, strides=2, padding="same")(
                previous_block_activation
            )
            x = layers.add([x, residual])  # Add back residual
            previous_block_activation = x  # Set aside next residual

        x = layers.SeparableConv2D(512, 3, padding="same")(x)
        x = layers.SeparableConv2D(512, 3, padding="same")(x)
        x = layers.SeparableConv2D(512, 3, padding="same")(x)

        x = layers.BatchNormalization()(x)
        x = layers.Activation("relu")(x)

        x = layers.GlobalAveragePooling2D()(x)
        if num_classes == 2:
            activation = "sigmoid"
            units = 1
        else:
            activation = "softmax"
            units = num_classes

        x = layers.Dropout(0.5)(x)
        outputs = layers.Dense(units, activation=activation)(x)
        return keras.Model(inputs, outputs)

    def make_prediction(self, image: numpy.ndarray) -> float:
        """
        Определяет, насколько занята парковка по картинке размера self.image_size
        :param image: numpy.ndarray
        :return: float - чем ближе к 0, тем вероятнее, что парковка занята.
        """
        if not self.model:
            raise Exception("Prediction model not loaded.")

        # img = keras.preprocessing.image.load_img(
        #     image, target_size=self.image_size
        # )
        # img_array = keras.preprocessing.image.img_to_array(img)
        image = tf.expand_dims(image, 0)

        predictions = self.model.predict(image)
        score = predictions[0]
        return score
