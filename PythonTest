#### 1 ####
import re

def getDicValue(estr, edic):
    for x in edic:
        getNumOfIdx = [m.start() for m in re.finditer(x, estr)]
        for s in getNumOfIdx:
            if s+1 < len(estr):
                if estr[s+1].isdigit() :
                    edic[x] += int(estr[s+1])
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
        mParenthesis = re.match(".*\((.*)\).*", e)
        resultDic = getDicValue(mParenthesis.group(1),rDic)
        if e.index(mParenthesis.group(1))+len(mParenthesis.group(1))+1 < len(e):
            if e[e.index(mParenthesis.group(1))+len(mParenthesis.group(1))+1].isdigit():
                for x in resultDic:
                    resultDic[x] *= int(e[e.index(mParenthesis.group(1))+len(mParenthesis.group(1))+1])
    return resultDic
    
    # mParenthesis = re.match(".*\((.*)\).*", e)
    # print(mParenthesis.group(1))
    # if mParenthesis:
    # mSquarebrackets = re.match(".*\[(.*)\].*", x)
    # print(mSquarebrackets.group(1))
