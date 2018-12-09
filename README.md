# cs4701
Handwriting digits to LaTeX

REQUIRES: requirements.txt


Running classifier interface: 
To run the classifier interface run the following command:
python3 interface.py 

When prompted, provide a path to the desired image. Be sure to not leave any trailing whitespace


Running system validator: 
To test system performance run the following command: 
python3 system_validation.py

The system validation script will test the classifier against a set of handwritten examples. It will 
produce the success rate, as well as print out each example that failed, complete with the expected 
results and the actual results.  
