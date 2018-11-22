import math
import sympy

"""[evalResult(string_rep)] is the string result of the mathematical evaluation of [string_rep].
Returns None on an invalid or malformed [string_rep]. """
def evalResult(string_rep): 
    try: 
        return eval(string_rep)
    except: 
        return None

"""[buildLatex(string_rep)] is the latex code output for the expression [string_rep]. 
Returns None on an invalid or malformed [string_rep]. """
def buildLatex(string_rep): 
    expr_result = evalResult(string_rep)
    if not expr_result: 
        return None
    latex_rep = sympy.latex(string_rep + "=" + str(expr_result))

"""[postProcess(string_rep)] prints result and latex code output for the expression [string_rep].
Returns true on a successful evaluation and translation. 
Returns false on an invalid or malformed [string_rep] during evaluation or latex translation.
"""
def postProcess(string_rep): 
    try: 
        expr_result = str(eval(string_rep))
        latex_rep = sympy.latex(string_rep + "=" + str(expr_result))
        printf("Result: %s\nLatex Representation: %s\n", expr_result, latex_rep)
        return True
    except: 
        return False
    
   
    
