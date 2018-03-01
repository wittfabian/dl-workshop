# Table of Contents

## [0-basics](0-basics.ipynb)
Introduction to building Autoencoders

## [autoencoder-example](autoencoder-example.ipynb)
Application to image denoising

We will train the autoencoder to map noisy digits images to clean digits images.

We use the well-known MNIST dataset of hand-written digits, where each row contains the 28^2=784 raw gray-scale pixel values from 0 to 255 of the digitized digits (0 to 9).

## [autoencoder-exercise-001](autoencoder-exercise-001.ipynb)
Application to image denoising

We will train the autoencoder to map noisy images to clean digits images.

You are provided two sets of images, train and test.
These images contain various styles of text, to which synthetic noise has been added to simulate real-world, messy artifacts.
The training set includes the test without the noise (train_cleaned).
You must create an algorithm to clean the images in the test set.