PATH_TO_IMAGES = "./extracted_images/"
PATH_TO_SAVED = "./saved_data/"
PATH_TO_VDATA = "./img/validation_img/"
APP_ID = "LLA9WY-Q4734L5HH7"
TEST_SPLIT = 0.2
LABELS =  {0:"0",1: "1",2 :"2", 3:"3",4: "4",  5:"5", 6: "6",  7:"7",8 : "8", 9 :"9",
              10 : "+", 11:"-", 12: "times",  13:"div", 14:"=", 15:"A", 16:"e", 17:"pi",
              18:"k", 19:"(", 20:")"}
ENCODING =  {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
              "+":10,"-":11,"times":12,"div":13,"=":14,"A":15,"e":16,"pi":17,
              "k":18, "(":19, ")":20}
EXTRACT_LABELS = ['+', '-', '0','1','2','3','4','5','6','7','8','9','=','A','div','e','pi','times',"(",")"]
<<<<<<< HEAD
OPERATORS = ["+", "*", "=", "/","E"]
SUBSTITUION_PATTERS = [(r"[pi]",'\pi'), (r"k",'E'),(r"div", '/'),(r"times", "*")]
=======
OPERATORS = ["+", "*", "=", "|","^"]
SUBSTITUION_PATTERS = [(r"[pi]",u"\u03C0"), (r"exp",'^'),(r"div", '|'),(r"times", "*"),(r',','.')]
>>>>>>> 32f906db08e21ef18507ecc1edc94b58c8424b80
