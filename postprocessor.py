import math
import constants
import pprint
import __future__
import wolframalpa
import re

"""[evalResult(string_rep)] is the string result of the mathematical evaluation of [string_rep].
Returns None on an invalid or malformed [string_rep]. """
def evalResult(string_rep): 
    def evaluate(e):
        return eval(compile(e, '<string>', 'eval', __future__.division.compiler_flag))
    client = wolframalpha.Client("LLA9WY-Q4734L5HH7")
    try: 
        string_rep = string_rep.replace("|","/")
        # if "=" in string_rep: 
        #     string_rep = string_rep.split("=")
        #     left = evaluate(string_rep[0])
        #     right = evaluate(string_rep[1])
        #     return left == right
        # return evaluate(string_rep)
        res = client.query(string_rep)
        return next(res.results).text
    except: 
        return None

"""[toLatex(string_rep)] takes in [string_rep], a string representation of some arithmetic expression 
and returns the latex code represenation """ 
def toLatex(string_rep):
    tokens = []
    token = ""
    for i in range(len(string_rep)):
        if string_rep[i] in constants.OPERATORS:
            tokens.append(token)
            tokens.append(string_rep[i])
            token = ""
        else: 
            token += string_rep[i]
    tokens.append(token)
    latex_rep = ""
    t = 0
    while t < len(tokens):
        if tokens[t] == "/":
            latex_rep = r"\frac{"+latex_rep+"}{"+tokens[t+1]+"}"
            t += 2
        elif tokens[t] == "|":
           latex_rep = "\div{"+latex_rep+"}{"+tokens[t+1]+"}"
           t += 2
        elif tokens[t] == "*":
            latex_rep += "\cdot"
            t += 1
        else:
            latex_rep += tokens[t]
            t += 1
    return latex_rep
    

"""[buildLatex(string_rep)] is the latex code output for the expression [string_rep]. 
Returns None on an invalid or malformed [string_rep]. """
def buildLatex(string_rep, expr_result): 
    if expr_result is None: 
        return None
    if expr_result is "True" or expr_result is "False":
        latex_rep = toLatex(string_rep.split("=")[0]) + "=" + toLatex(string_rep.split("=")[1])
    else:
        latex_rep = toLatex(string_rep)+"="+expr_result
    return latex_rep

"""[postProcess(string_rep)] prints result and latex code output for the expression [string_rep].
Returns true on a successful evaluation and translation. 
Returns false on an invalid or malformed [string_rep] during evaluation or latex translation.
"""
def postProcess(string_rep): 
    try: 
        expr_result = str(evalResult(string_rep))
        latex_rep = buildLatex(string_rep, expr_result)
        print("Result: %s\nLatex Representation: %s\n" % (expr_result, latex_rep))
        return True
    except Exception as e: 
        print("Exception in Postprocessing:")
        print(e)
        return False
    
if __name__ == "__main__":
    # print(toLatex("5+5"))
    # print(toLatex("5/5"))
    # print(toLatex("5*5"))
    # print(toLatex("5/5=5*5")+"\n")

    # print(buildLatex("5/5=5*5", "False"))
    # print(buildLatex("10=10", "True"))
    # print(buildLatex("5/5=1", "True")+"\n")
    # postProcess("5|5=5*5")
    # postProcess("5/5=5*5")
    # postProcess("10=10")
    # postProcess("5|5=1")
    # postProcess("5/5=1")
    # postProcess("1+2")
    postProcess("20/0")
    postProcess("2*2|8")
