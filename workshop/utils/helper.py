import os
import numpy as np
from os import path
from scipy import ndimage, misc

def crop(image, x, y, size):
    x_start, x_end = x, x+size
    y_start, y_end = y, y+size

    return image[x_start:x_end,y_start:y_end]

def load_document_images_cropped(size=64, x_start_at=50, y_start_at=50):
    X_train, y_train = [], []
    X_test, y_test = [], []

    path_files_root = path.join('..', 'datasets', 'document-images')
    path_files_train = path.join(path_files_root, 'train')
    path_files_train_cleaned = path.join(path_files_root, 'train_cleaned')
    path_files_test = path.join(path_files_root, 'test')

    for filename in os.listdir(path_files_train_cleaned):
        file = ndimage.imread(path.join(path_files_train_cleaned, filename), mode='L')
        file = crop(file, x_start_at, y_start_at, size)
        y_train.append(file)

        file = ndimage.imread(path.join(path_files_train, filename), mode='L')
        file = crop(file, x_start_at, y_start_at, size)
        X_train.append(file)

    for filename in os.listdir(path_files_test):
        file = ndimage.imread(path.join(path_files_test, filename), mode='L')
        file = crop(file, x_start_at, y_start_at, size)
        X_test.append(file)

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    X_test = np.array(X_test)
    y_test = np.array(y_test)

    return (X_train, y_train), (X_test, y_test)

def load_document_images():
    X_train, y_train = [], []
    X_test, y_test = [], []

    path_files_root = path.join('..', 'datasets', 'document-images')
    path_files_train = path.join(path_files_root, 'train')
    path_files_train_cleaned = path.join(path_files_root, 'train_cleaned')
    path_files_test = path.join(path_files_root, 'test')

    img_row, img_col = 420, 540

    for filename in os.listdir(path_files_train_cleaned):
        file = ndimage.imread(path.join(path_files_train_cleaned, filename), mode='L')
        file = misc.imresize(file, (img_row, img_col))
        y_train.append(file)

        file = ndimage.imread(path.join(path_files_train, filename), mode='L')
        file = misc.imresize(file, (img_row, img_col))
        X_train.append(file)

    for filename in os.listdir(path_files_test):
        file = ndimage.imread(path.join(path_files_test, filename), mode='L')
        file = misc.imresize(file, (img_row, img_col))
        X_test.append(file)

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    X_test = np.array(X_test)
    y_test = np.array(y_test)

    return (X_train, y_train), (X_test, y_test)
