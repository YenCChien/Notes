#### 1 ####
import re

def getDicValue(estr, edic):
    for x in edic:
        getNumOfIdx = [m.start() for m in re.finditer(x, estr)]
        # print(x,getNumOfIdx)
        for s in getNumOfIdx:
            if s+len(x) < len(estr):
                if estr[s+1].islower() and len(x) == 1:break
                if estr[s+len(x)].isdigit() :
                    edic[x] += int(estr[s+len(x)])
                else:
                    edic[x] += 1
            else:
                edic[x] += 1
    return edic

def parse_molecule(e):
    rDic = {}
    parseChemical = [s for s in filter(str.isalpha, e)]
    ## Get Element
    for x in parseChemical:
        if x.islower(): rDic.update({parseChemical[parseChemical.index(x)-1]+x:0})
    if rDic:
        newStr = e
        for i in rDic:
            newStr = newStr.replace(i,'')
        otherChemical = [s for s in filter(str.isalpha, newStr)] 
        for x in otherChemical:
            rDic.update({x:0})
    else:
        for x in parseChemical:
            rDic.update({x:0})
    ## Get Value
    if e.isalnum(): 
        resultDic = getDicValue(e,rDic)
    else:
        ## deal with parenthesis and multiplication
        mParenthesis = re.match(".*\((.*)\).*", e)
        resultDic = getDicValue(mParenthesis.group(1),rDic)
        rDic = {key : 0 for key in rDic}
        if e.index(mParenthesis.group(1))+len(mParenthesis.group(1))+1 < len(e):
            if e[e.index(mParenthesis.group(1))+len(mParenthesis.group(1))+1].isdigit():
                for x in resultDic:
                    resultDic[x] *= int(e[e.index(mParenthesis.group(1))+len(mParenthesis.group(1))+1])
                mParenthesisStr = '('+mParenthesis.group(1)+')'+ e[e.index(mParenthesis.group(1))+len(mParenthesis.group(1))+1]
            else:
                mParenthesisStr = '('+mParenthesis.group(1)+')'
        ## deal with Squarebrackets and Multiplication
        mSquarebrackets = re.match(".*\[(.*)\].*", e)
        if not mSquarebrackets: return "Wrong Input!!"
        mSquareStr = mSquarebrackets.group(1).replace(mParenthesisStr,'')
        SquareStrDic = getDicValue(mSquareStr,rDic)
        for x in SquareStrDic:
            resultDic[x]+=SquareStrDic[x]
        if e.index(mSquarebrackets.group(1))+len(mSquarebrackets.group(1))+1 < len(e):
            if e[e.index(mSquarebrackets.group(1))+len(mSquarebrackets.group(1))+1].isdigit():
                for x in resultDic:
                    resultDic[x] *= int(e[e.index(mSquarebrackets.group(1))+len(mSquarebrackets.group(1))+1])
                mSquarebracketsStr = '['+mSquarebrackets.group(1)+']'+ e[e.index(mSquarebrackets.group(1))+len(mSquarebrackets.group(1))+1]
            else:mSquarebracketsStr = '['+mSquarebrackets.group(1)+']'   
        else:mSquarebracketsStr = '['+mSquarebrackets.group(1)+']'
        mSquarefilterStr = e.replace(mSquarebracketsStr,'')
        rDic = {key : 0 for key in rDic}
        outsideSquare = getDicValue(mSquarefilterStr,rDic)
        # print(mSquarefilterStr)
        for x in outsideSquare:
            resultDic[x]+=outsideSquare[x]
    return resultDic
    
    # mParenthesis = re.match(".*\((.*)\).*", e)
    # print(mParenthesis.group(1))
    # if mParenthesis:
    # mSquarebrackets = re.match(".*\[(.*)\].*", x)
    # print(mSquarebrackets.group(1))

#### 2 ####
class Molecule():
    def parse(self,argv):
        return parse_molecule(argv)

class MoleculeNew(Molecule):
    def parse(self,argv):
        Dic = super().parse(argv)
        # print(Dic)
        total = 0
        for num in Dic.values():
            total+=int(num)
        percentDic = {}
        for e in Dic:
            # print(Dic[e])
            percentDic.update({e:'{0:.2f} %'.format(int(Dic[e])/total * 100)})
        return percentDic

#### 3 ####
'''
'[Co(H2NCH2CH2NH2)3]Cl3'
'K4[ON(SO3)2]2'
'Ka4[ON(SO3)2]2'
'K4[ON(SO3)'
'''
