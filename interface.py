import re
import os
import preprocessor
import classifier
import postprocessor
import sys

"""
VERSION 1: Static Image Analysis
- Single image path and analysis
"""
if __name__ == "__main__":
    exit_regex = re.compile(r"exit{1}|quit{1}|(no{1})|n{1}|done{1}", re.IGNORECASE)
    print("Handwriting Recognition and Translation.\n")
    while(1):
        print("Enter the path to the writing sample:")
        path = str(sys.stdin.readline()[:-1])
        if exit_regex.match(path): 
            print("Exiting...")
            exit(0)
        if os.path.isfile(path): 
            img = preprocessor.process_image(path)
            str_rep = classifier.classify(img)
            expr_result, latex_rep = postprocessor.postProcess(str_rep)
            print("Result: %s\nLatex Representation: %s\n" % (expr_result, latex_rep))
        else:
            print("Invalid path.")
        
