import numpy
from os import listdir
from os.path import isdir, isfile, join


# TODO Iterate through images in dir, converting them to 45x45 pixel arrays
def grab_imgs(dir):
    return []


# Iterate through dir indexing data relating to the desired labels
def from_dir(dir):
    complete_data = []
    labels = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
              "+": 10, "-": 11, "times": 12, "div": 13, "forward_slash": 13, "=": 14}
    if isdir(dir):
        chars_dir = [f for f in listdir(dir) if isdir(join(dir, f))]
        for dirs in chars_dir:
            if dirs in labels:
                complete_data[labels[dirs]] = grab_imgs(join(dir, dirs))

    testing_data = []
    distribution_data = []
    for arr in complete_data:
        separation_point = len(arr)/3
        testing_data.append(arr[:separation_point])
        distribution_data.append(arr[separation_point:])
        
    return labels,   numpy.ndarray(testing_data), numpy.ndarray(distribution_data)

if __name__ == "__main__":
    from_dir("./extracted_images")