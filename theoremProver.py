from parsingFunctions import getLhs
import os

f = open('expressions.ini')
f = f.read()

listOfExpressions = f.split("\n")

for expr in listOfExpressions:
	print "Expression: ", expr
	print "LHS: ", getLhs(expr)