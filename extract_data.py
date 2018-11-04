import numpy as np
from os import listdir
from os.path import isdir, isfile, join
from constants import *
import cv2


# Iterate through images in dir, converting them to 45x45 pixel arrays
# dir is the path to the folder, n is the #/character the folder represents
def grab_imgs(dir, n):
    size = len(listdir(dir))
    total_array = np.zeros((size, 45, 45))
    labels_vector = np.full((size, 1), n)

    ind = 0
    for f in listdir(dir):
        img = cv2.imread(join(dir, f), flags=cv2.IMREAD_GRAYSCALE)
        total_array[ind,:,:] = img
        ind += 1

    split_location = int(size * TEST_SPLIT)
    return total_array[:split_location,:,:], labels_vector[:split_location], total_array[split_location:,:,:], labels_vector[split_location:]


# Iterate through dir indexing data relating to the desired labels
def from_dir(dir):
    training_data = np.empty((0, 45, 45), int)
    training_labels = np.empty((0,1), int)
    test_data = np.empty((0, 45, 45), int)
    test_labels = np.empty((0,1), int)
    labels = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
              "+": 10, "-": 11, "times": 12, "div": 13, "forward_slash": 13, "=": 14}

    # iterate through each sub-directory
    if isdir(dir):
        chars_dir = [f for f in listdir(dir) if not f.startswith('.')]# if isdir(join(dir, f))]
        for dirs in chars_dir:
            if dirs in labels:
                new_train_matrix, new_train_labels, new_test_matrix, new_test_labels = grab_imgs(join(dir, dirs), dirs)
                training_data = np.append(training_data, new_train_matrix, axis=0)
                training_labels = np.append(training_labels, new_train_labels)
                test_data = np.append(test_data, new_test_matrix, axis=0)
                test_labels = np.append(test_labels, new_test_labels)

    # split data into test, validation, and training sets, based on parameters in constants file
    print(test_data.shape)
    print(test_labels.shape)

    # for ind in complete_data:
    #     arr = complete_data[ind]
    #     test_separation_point = int(len(arr) * TEST_SPLIT)
    #     val_separation_point = int(len(arr) * (TEST_SPLIT))
    #     test_data[ind] = arr[:test_separation_point]
    #     validation_data[ind] = arr[test_separation_point:val_separation_point]
    #     train_data[ind] = arr[val_separation_point:]
    #
    # return labels, test_data, validation_data, train_data
    # return labels, numpy.ndarray(test_data), numpy.ndarray(validation_data), numpy.ndarray(train_data)
    return None, None, None, None

if __name__ == "__main__":
    labels, test, val, train = from_dir(PATH_TO_IMAGES)
