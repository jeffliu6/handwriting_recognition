PATH_TO_IMAGES = "./extracted_images/"
PATH_TO_SAVED = "./saved_data/"
PATH_TO_VDATA = "./img/validation_img/"
APP_ID = "LLA9WY-Q4734L5HH7"
TEST_SPLIT = 0.2
LABELS =  {0:"0",1: "1",2 :"2", 3:"3",4: "4",  5:"5", 6: "6",  7:"7",8 : "8", 9 :"9",
              10 : "+", 11:"-", 12: "times",  13:"div", 14: "forward_slash", 15:"=", 16:",", 17:"A", 18:"e", 19:"pi", 20:"exp"}
EXTRACT_LABELS = ['+', '-', ',', '0','1','2','3','4','5','6','7','8','9','=','A','div','e','exp','forward_slash','pi','times']
OPERATORS = ["+", "*", "/", "=", "|","^"]
SUBSTITUION_PATTERS = [(r"[pi]",u"\u03C0"), (r"exp",'^'),(r"div", '|'),(r"times", "*"),(r',','.')]