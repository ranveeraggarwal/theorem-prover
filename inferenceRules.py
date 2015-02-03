from parsingFunctions import checkWhole

#['p', '(p->q)', '(q->f)']
def stripBrackets(term):
	if checkWhole(term):
		return term[1:-1]
	else:
		return term

def modusPonens(hypothesesInit):
	while True:
		hypotheses = hypothesesInit
		for term1 in hypotheses:
			for term2 in hypotheses:
				if (term1 == term2):
					pass
				else:
					term2 = stripBrackets(term2)
					if term2.startswith(term1, 0, len(term2)):
						delimIndex = len(term1)
						if term2[delimIndex] == "-":
							subterm2 = term2[delimIndex+2:]
							hypotheses.append(subterm2)
						else:
							pass
					else:
						pass
		if (hypothesesInit == hypotheses): 
			break
		else:
			hypothesesInit = hypotheses
	if "f" in hypothesesInit:
		return True
	else:
		return False