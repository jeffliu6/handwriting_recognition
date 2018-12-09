import math
import constants
import pprint
import __future__
import re
import wolframalpha
import ssl

"""[evalResult(string_rep)] is the string result of the mathematical evaluation of [string_rep].
Returns None on an invalid or malformed [string_rep]. """
def evalResult(string_rep): 
    def evaluate(e):
        return eval(compile(e, '<string>', 'eval', __future__.division.compiler_flag))

    client = wolframalpha.Client(constants.APP_ID)
    try:
        if "A" in string_rep:
            res = client.query(string_rep+" Solve for A")
        else:
            res = client.query(string_rep)
        return next(res.results).text
    except: 
        return "Bad Wolfram Query: "+string_rep

"""[toLatex(string_rep)] takes in [string_rep], a string representation of some arithmetic expression 
and returns the latex code represenation """ 
def toLatex(string_rep):
    tokens = []
    token = ""
    for (p,s) in constants.SUBSTITUION_PATTERS:
        re.sub(p,s,string_rep)
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
           latex_rep = "\div{"+latex_rep+"}{"+tokens[t+1]+"}"
           t += 2
        elif tokens[t] == "E":
           latex_rep = latex_rep+ "^{"+tokens[t+1]+"}"
           t += 2
        elif tokens[t] == "*":
            latex_rep += r"\times "
            t += 1
        else:
            latex_rep += tokens[t]
            t += 1
    return latex_rep
    
"""[buildLatex(string_rep)] is the latex code output for the expression [string_rep]. 
Returns None on an invalid or malformed [string_rep]. """
def buildLatex(string_rep, expr_result): 
    return  toLatex(string_rep)

"""[postProcess(string_rep)] prints result and latex code output for the expression [string_rep].
Returns true on a successful evaluation and translation. 
Returns false on an invalid or malformed [string_rep] during evaluation or latex translation.
"""
def postProcess(string_rep): 
    try: 
        expr_result = str(evalResult(string_rep))
        return expr_result,buildLatex(string_rep, expr_result)
    except Exception as e: 
        return e
    
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
