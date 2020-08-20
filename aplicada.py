def godel(A, B):
    resultRel = []
    for indexA in A:
        row = []
        itemA = A.get(indexA)
        for indexB in B:
            itemB = B.get(indexB)
            if itemA <= itemB:
                row.append(1)
            else:
                row.append(itemB)
        resultRel.append(row)
    return resultRel

def lukasiewicz(A,B):
    resultRel = []
    for indexA in A:
        row = []
        itemA = A.get(indexA)
        for indexB in B:
            itemB = B.get(indexB)
            if 1 < (1 - itemA + itemB):
                row.append(1)
            else:
                row.append((1 - itemA + itemB))
        resultRel.append(row)
    return resultRel

def goguen(A, B):
    resultRel = []
    for indexA in A:
        row = []
        itemA = A.get(indexA)
        for indexB in B:
            itemB = B.get(indexB)
            if itemA <= itemB:
                row.append(1)
            else:
                row.append(itemB/itemA)
        resultRel.append(row)
    return resultRel

def main():
    #Conjuntos iniciales
    X = [1, 2, 3, 4, 5]
    A = {
        X[0]: 0.3,
        X[1]: 0.5,
        X[2]: 1,
        X[3]: 0.7,
        X[4]: 0.2
    }
    Y = ['a','b','c','d','e','f']
    B = {
        Y[0]: 0.3,
        Y[1]: 0.5,
        Y[2]: 0.8,
        Y[3]: 1,
        Y[4]: 1,
        Y[5]: 1,
    }
    relacion = goguen(A, B)
    for row in relacion:
        print( row)
    
main()