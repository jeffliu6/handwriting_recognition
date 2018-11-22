# import preprocessing 
# import classifier 
# import postprocesing
import re
import os
import postprocessor
"""
VERSION 1: Static Image Analysis
- Single image path and analysis
"""
if __name__ == "__main__":
    exit_regex = re.compile(r"exit{1}|quit{1}|(no{1})|n{1}|done{1}", "gixu")
    print("Handwriting Recognition and Translation.\n")
    while(1):
        path = input("Enter the path to the desired writing sample:\n")
        if exit_regex.match(path): 
            break 
        if os.path.isfile(path): 
            # TODO pass path to preprocessor
            # TODO feed processed image into classifier 
            # TODO feed into post processor 
        else:
            print("Invalid path.")
        