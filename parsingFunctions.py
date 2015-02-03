def checkWhole(theExpression):
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
	if len(theExpression) == 1:
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
	temp = tokenize(theExpression)
	temp[0] = "~" + temp[0]
	return temp[::-1]