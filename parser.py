#(p->q)->((~p->q)->q)
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
					print theExpression
					break
				else:
					if theExpression[i] == "(":
						brackstackCount += 1
					elif theExpression[i] == ")":
						brackstackCount -= 1
					else:
						pass
			print delimIndex
			return tokenize(theExpression[delimIndex+2:]).append(theExpression[0:delimIndex])


#(p->q)->((~p->q)->q)
expr = "((p->q)->((~p->q)->q))"

print tokenize(expr)


'''
rhs = expr
lhs = []
brackstack = []
aTerm = ""
i = 0

while True:
	if rhs == "":
		break
	elif checkWhole(rhs):
		rhs = rhs[1:-1]
	else:
		if brackstack == [] and aTerm != "":
			lhs.append(aTerm)
			aTerm = ""
			rhs = rhs[2:]
			i = i + 2
		else:
			if rhs[0] == "(":
				brackstack.append(i)
				rhs = rhs[1:]
				i = i + 1
			elif rhs[0] == ")":
				current = brackstack[-1]
				brackstack = brackstack[:-1]
				if brackstack == []:
					aTerm = expr[current:i]
					print aTerm
				rhs = rhs[1:]
				i = i + 1
			else:
				rhs = rhs[1:]
				i = i+1
'''