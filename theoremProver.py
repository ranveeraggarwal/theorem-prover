from parsingFunctions import getLhs
from inferenceRules import modusPonens

DEBUG = False

f = open('expressions.ini')
f = f.read()

listOfExpressions = f.split("\n")

if (DEBUG):
	expr = listOfExpressions[0] #(p->q)->((~p->q)->q)
	print expr
	hypotheses = getLhs(expr) #['(p->q)', '(~p->q)', '~q']
	print hypotheses
	print modusPonens(hypotheses)

else:
	for expr in listOfExpressions:
		print "Expression: ", expr
		hypotheses = getLhs(expr)
		print "LHS: ", hypotheses
		print "Running Theorem prover ...\n", modusPonens(hypotheses)
		print "\n"
