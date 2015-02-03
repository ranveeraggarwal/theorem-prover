from parsingFunctions import getLhs
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(project_dir, 'expressions.ini'))
f = f.read()

listOfExpressions = f.split("\n")

for expr in listOfExpressions:
	print "Expression: ", expr
	print "LHS: ", getLhs(expr)