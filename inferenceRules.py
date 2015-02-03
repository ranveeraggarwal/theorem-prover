from parsingFunctions import checkWhole

#['p', '(p->q)', '(q->f)']
def stripBrackets(term):
	if checkWhole(term):
		return term[1:-1]
	else:
		return term

def modusPonens():
	hypotheses = ['p', '(p->q)', '(q->f)']
	for term1 in hypotheses:
		for term2 in hypotheses:
			if (term1 == term2):
				pass
			else:
				#print "a "
				term2 = stripBrackets(term2)
				if term2.startswith(term1, 0, len(term2)):
					#print term1, " ", term2
					delimIndex = len(term1)
					if term2[delimIndex] == "-":
						subterm2 = term2[delimIndex+2:]
						hypotheses.append(subterm2)
					else:
						pass
				else:
					pass
	if "f" in hypotheses:
		return True
	else:
		return False