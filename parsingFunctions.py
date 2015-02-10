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

def getMiniToken(theExpression, i):
    tempStack = []
    if theExpression[i+1] == "(":
        for j in xrange(i+1,len(theExpression)):
            if theExpression[j] == "(":
                tempStack.append(j)
            elif theExpression[j] == ")":
                if len(tempStack) == 1:
                    return theExpression[tempStack[0]: j+1]
                else:
                    tempStack = tempStack[:-1]
            else:
                pass
    else:
        return theExpression[i+1]

def getLeftMiniToken(theExpression, i):
    tempStackCount = 1
    jWanted = 0
    if theExpression[i-1] == ")":
        for j in xrange(i-2, -2, -1):
            if tempStackCount == 0:
                jWanted = j
                break
            else:
                if theExpression[j] == ")":
                    tempStackCount = tempStackCount + 1
                elif theExpression[j] == "(":
                    tempStackCount = tempStackCount - 1
                else:
                    pass
        return getMiniToken(theExpression, jWanted)
    else:
        return theExpression[i-1]

def convertOr(theExpression):
    while True:
        if "V" in theExpression:
            for i in xrange(0, len(theExpression)):
                if theExpression[i] == "V":
                    tokLeft = getLeftMiniToken(theExpression, i)
                    tokRight = getMiniToken(theExpression, i)
                    theExpression = theExpression[:i-len(tokLeft)] + "(" + tokLeft + "->f)->" + tokRight + theExpression[i+len(tokRight)+1:]
                    break
                else:
                    pass
        else:           
            return theExpression

def convertAnd(theExpression):
    while True:
        if "^" in theExpression:
            for i in xrange(0, len(theExpression)):
                if theExpression[i] == "^":
                    tokLeft = getLeftMiniToken(theExpression, i)
                    tokRight = getMiniToken(theExpression, i)
                    theExpression = theExpression[:i-len(tokLeft)] + "(" + tokLeft + "->(" + tokRight + "->f))->f" + theExpression[i+len(tokRight)+1:]
                    break
                else:
                    pass
        else:           
            return theExpression

def convertNot(theExpression):
    while True:
        if "~" in theExpression:
            for i in xrange(0, len(theExpression)):
                if theExpression[i] == "~":
                    tok = getMiniToken(theExpression, i)
                    lenTok = len(tok)
                    theExpression = theExpression[:i] + "(" + tok + "->f)" + theExpression[i+lenTok+1:]
                    break
                else:
                    pass
        else:
            return theExpression

def convertAndOrNot(theExpression):
    theExpression = convertNot(theExpression)
    theExpression = convertAnd(theExpression)
    theExpression = convertOr(theExpression)
    return theExpression

#print convertAndOrNot("~p^q")

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
    theExpression = convertAndOrNot(theExpression)
    temp = tokenize(theExpression)
    if (temp[0][0] == "~"):
        temp[0] = temp[0][1:]
    else:
        temp[0] = "~" + temp[0]
    return temp[::-1]