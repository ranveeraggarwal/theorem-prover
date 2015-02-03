from parsingFunctions import getLhs
from inferenceRules import modusPonens

f = open('expressions.ini')
f = f.read()

listOfExpressions = f.split("\n")

expr = listOfExpressions[1] #(p->q)->((~p->q)->q)
hypotheses = getLhs(expr) #['(p->q)', '(~p->q)', '~q']
print modusPonens(hypotheses)

'''
We need to prove them false by modus ponens
'''
'''
for expr in listOfExpressions:
	print "Expression: ", expr
	print "LHS: ", getLhs(expr)

'''