from parsingFunctions import checkWhole

#['p', '(p->q)', '(q->f)']
def stripBrackets(term):
	if checkWhole(term):
		return term[1:-1]
	else:
		return term

def modusPonens(hypothesesInit):
	bo = False
	while not bo:
		bo = True
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
							hypothesesInit.append(subterm2)
							if (len(hypotheses) != len(hypothesesInit)):
								bo = False
						else:
							pass
					else:
						pass
		hypotheses = hypothesesInit
	if "f" in hypothesesInit:
		return True
	else:
		return False