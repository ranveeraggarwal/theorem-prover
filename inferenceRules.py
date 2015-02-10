from parsingFunctions import checkWhole, getLhs
import time


def getSymbols(Expression):
    symbols = []
    for char in Expression:
        if ord(char) >= ord('a') and ord(char) <= ord('z') and char != 'f':
            symbols.append(char)
    return symbols

def getAxiom():
    axiom = raw_input("Enter axiom number: ")
    if axiom == "end":
        return False, None
    elif int(axiom) > 5:
        print "Wrong axiom, try again"
        return getAxiom()
    else:
        with open('axioms.ini', 'r') as f:
            x = f.readlines();
        if int(axiom) <= 4:
            temp = x[int(axiom)-1].strip()
        else:
            temp = raw_input("Enter pre-proved Theorem with apostrophes: ")

        syms = getSymbols(temp)
        for sym in syms:
            sym_map = raw_input("Expression for %s': " % sym)
            temp = temp.replace("%s'" % sym, sym_map)
        print "Substituded axiom:", temp
        return True, temp
        
        '''
        if int(axiom) == 1 or int(axiom) == 4:
            p_map = raw_input("Expression for p':")
            q_map = raw_input("Expression for q':")
            temp = temp.replace('p\'',  p_map)
            temp = temp.replace('q\'', q_map)
        elif int(axiom) == 2:
            p_map = raw_input("Expression for p':")
            q_map = raw_input("Expression for q':")
            r_map = raw_input("Expression for r':")
            temp = temp.replace('p\'',  p_map)
            temp = temp.replace('q\'',  q_map)
            temp = temp.replace('r\'',  r_map)
        elif int(axiom) == 3:
            p_map = raw_input("Expression for p':")
            temp = temp.replace('p\'', p_map)
        else:
            syms = getSymbols(temp)
            for sym in syms:
                sym_map = raw_input("Expression for %s': " % sym)
                temp = temp.replace("%s'" % sym, sym_map)
        print "Substituded axiom:", temp
        return True, temp
        '''

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
        print hypothesesInit
        return True
    else:
        status, axiom = getAxiom()
        if status:
            yes = False
            for term in hypotheses:
                if term == axiom:
                    yes = True
                    break
            if not yes:
                hypotheses.append(axiom)
            print hypotheses
            return modusPonens(hypotheses)
        else:
            print "STOP"
            return False