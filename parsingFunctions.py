def checkWhole(theExpression):
	'''
	checkWhole(theExpression)->bool
	
	Checks whether the whole expression is within brackets.

	checkWhole((p->q))
	> True
	checkWhole(p->(q->r))
	> False
	'''
	expClone = theExpression
	if theExpression[0] != "(" or theExpression[-1] != ")":
		return False
	else:
		brackstack = []
		for i in xrange(0, len(theExpression)):
			if brackstack == [0] and i == len(theExpression)-1:
				return True
			else:
				if theExpression[i] == "(":
					brackstack.append(i)
				elif theExpression[i] == ")":
					brackstack = brackstack[:-1]
		return False

def tokenize(theExpression):
	'''
	tokenize(theExpression)->[string, string, ...]
	
	Tokenises an expressions in a way the Deduction theorem would (not exactly; this is an intermediate function) bring variables from right to left.

	tokenize("(p->q)")
	> ['q', 'p']
	tokenize("(p->q)->r")
	> ['r', '(p->q)']
	'''
	if len(theExpression) == 1 or len(theExpression) == 2:
		return [theExpression]
	elif len(theExpression) == 0:
		return []
	else:
		if checkWhole(theExpression):
			return(tokenize(theExpression[1:-1]))
		else:
			tokens = []
			brackstackCount = 0
			delimIndex = 0
			for i in xrange(0,len(theExpression)):
				if theExpression[i] == "-" and brackstackCount == 0:
					delimIndex = i
					break
				else:
					if theExpression[i] == "(":
						brackstackCount += 1
					elif theExpression[i] == ")":
						brackstackCount -= 1
					else:
						pass
			temp = tokenize(theExpression[delimIndex +2:])
			temp.append(theExpression[0:delimIndex])
			return temp

def getLhs(theExpression):
	'''
	getLhs(theExpression)->[string, string, ...]
	
	Gets tokens on the LHS exactly as the deduction theorem would.

	getLhs("(p->q)")
	> ['p', '(q->f)']
	getLhs("(p->q)->r")
	> ['(p->q)', '(r->f)']
	'''
	temp = tokenize(theExpression)
	if (temp[0][0] == "~"):
		temp[0] = temp[0][1:]
	else:
		temp[0] = "~" + temp[0]
	for j in xrange(0, len(temp)):
		tempHypo = temp[j]
		while True:
			if "~" in tempHypo:
				for i in xrange(0, len(tempHypo)):
					if tempHypo[i] == "~":
						tempHypo = tempHypo[:i] + "(" + tempHypo[i+1] + "->f)" + tempHypo[i+2:]
						break
			else:
				temp[j] = tempHypo
				break
	return temp[::-1]