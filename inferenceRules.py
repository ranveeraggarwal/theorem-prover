from parsingFunctions import checkWhole, getLhs
import time

def getAxiom():
	axiom = raw_input("Enter axiom number: ")
	if axiom == "end":
		return None
	elif int(axiom) > 3:
		print "Wrong axiom, try again"
		return getAxiom()
	else:
		with open('axioms.ini', 'r') as f:
			x = f.readlines();
		temp = x[int(axiom)-1].strip()
		print temp
		return getLhs(temp);

def stripBrackets(term):
	if checkWhole(term):
		return term[1:-1]
	else:
		return term

def insertIntoList(lis, term):
	yes = False
	for item in lis:
		if item == term:
			yes = True
			break
	if not yes:
		lis.append(term)
		return lis[:]

def modusPonens(hypothesesInit):
	bo = False
	count = 1
	while not bo:
		bo = True
		hypotheses = hypothesesInit[:]

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
							yes = False
							for item in hypothesesInit:
								if item == subterm2:
									yes = True
									break
							if not yes:
								hypothesesInit.append(subterm2)
							if (len(hypotheses) != len(hypothesesInit)):
								bo = False
						else:
							pass
					else:
						pass
		hypotheses = hypothesesInit[:]

	if "f" in hypothesesInit:
		print "The Expression is Provable"
		return True
	else:
		axiom = getAxiom()
		hypotheses.extend(axiom)
		print hypotheses
		return modusPonens(hypotheses)
