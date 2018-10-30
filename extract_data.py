import numpy
from os import listdir
from os.path import isdir, isfile, join
from constants import *
import cv2


# Iterate through images in dir, converting them to 45x45 pixel arrays
# dir is the path to the folder, n is the #/character the folder represents
def grab_imgs(dir, n):
    total = []
    for f in listdir(dir):
        img = cv2.imread(join(dir, f), flags=cv2.IMREAD_GRAYSCALE)
        total.append(img)
    return total


# Iterate through dir indexing data relating to the desired labels
def from_dir(dir):
    complete_data = {}
    labels = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
              "+": 10, "-": 11, "times": 12, "div": 13, "forward_slash": 13, "=": 14}

    # iterate through each sub-directory
    if isdir(dir):
        chars_dir = [f for f in listdir(dir) if not f.startswith('.')]# if isdir(join(dir, f))]
        for dirs in chars_dir:
            if dirs in labels:
                complete_data[dirs] = grab_imgs(join(dir, dirs), dirs)

    # split data into test, validation, and training sets, based on parameters in constants file
    test_data = {}
    validation_data = {}
    train_data = {}
    for ind in complete_data:
        arr = complete_data[ind]
        test_separation_point = int(len(arr) * TEST_SPLIT)
        val_separation_point = int(len(arr) * (TEST_SPLIT + VALIDATION_SPLIT))
        test_data[ind] = arr[:test_separation_point]
        validation_data[ind] = arr[test_separation_point:val_separation_point]
        train_data[ind] = arr[val_separation_point:]

    return labels, test_data, validation_data, train_data
    # return labels, numpy.ndarray(test_data), numpy.ndarray(validation_data), numpy.ndarray(train_data)


if __name__ == "__main__":
    labels, test, val, train = from_dir(PATH_TO_IMAGES)
