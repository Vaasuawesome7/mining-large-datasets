import sys
sys.path.append('../')

import constants

HashTable = [0] * constants.HASH_TABLE_SIZE_PCY

def first_pass(baskets: list[list]):    
    L1 = {}
    itemIndexTable = {}
    C1 = {}
    i = 0

    for basket in baskets:
        for item in basket:
            item = item.lower()
            if (itemIndexTable.get(item) != None):
                index = itemIndexTable[item]
                C1[index] = C1.get(index) + 1
            else:
                itemIndexTable[item] = i
                C1[i] = 1
                i = i+1

    for item in C1.items():
        if (item[1] >= constants.SUPPORT_THRESHOLD):
            L1[item[0]] = item[1]
            
    global HashTable
    
    for basket in baskets:
        for i in range(len(basket)):
            for j in range(i+1, len(basket)):
                mitems = [itemIndexTable[basket[i].lower()], itemIndexTable[basket[j].lower()]]
                HashTable[constants.hash_function_pcy(items=mitems)] += 1
    
    return (itemIndexTable, L1, C1)

def intermediate_pass_1_2():
    global HashTable
    
    TempHashTable = []
    for count in HashTable:
        if count >= constants.SUPPORT_THRESHOLD:
            TempHashTable.append(True)
        else:
            TempHashTable.append(False)
            
    HashTable = TempHashTable

def second_pass(baskets: list[list], itemIndexTable: dict, L1: dict):
    C2 = {}
    L2 = {}
    items = list(L1.keys())
    
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            mitems = [items[i], items[j]]
            if HashTable[constants.hash_function_pcy(items=mitems)]:
                C2[tuple(sorted((items[i], items[j])))] = 0
                
    for basket in baskets:
        for i in range(len(basket)):
            for j in range(i+1, len(basket)):
                item1 = itemIndexTable[basket[i].lower()]
                item2 = itemIndexTable[basket[j].lower()]
                doubleton = tuple(sorted((item1, item2)))
                if C2.get(doubleton) != None:
                    C2[doubleton] += 1
    print(C2)

    for item in C2.items():
        if item[1] >= constants.SUPPORT_THRESHOLD:
            L2[item[0]] = item[1]
            
    return L2

def third_pass(baskets: list[list], itemIndexTable: dict, L2: dict):
    keys = list(L2.keys())
    C3 = {}
    
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            doubleton1 = set(keys[i])
            doubleton2 = set(keys[j])
            res = doubleton1 & doubleton2
            if (len(res) == 1):
                doubleton3 = tuple(doubleton1.union(doubleton2) - res)
                if L2.get(doubleton3) != None:
                    candidateTriplet = tuple(doubleton1.union(doubleton2))
                    C3[candidateTriplet] = 0
                    
    for basket in baskets:
        for i in range(len(basket)):
            for j in range(i+1, len(basket)):
                for k in range(j+1, len(basket)):
                    item1 = itemIndexTable[basket[i].lower()]
                    item2 = itemIndexTable[basket[j].lower()]
                    item3 = itemIndexTable[basket[k].lower()]
                    
                    triplet = tuple(sorted((item1, item2, item3)))
                    
                    if C3.get(triplet) != None:
                        C3[triplet] += 1
    
    L3 = {}
    for item in C3.items():
        if item[1] >= constants.SUPPORT_THRESHOLD:
            L3[item[0]] = item[1]

    return L3

def find_quadrupletons(baskets: list[list], itemIndexTable: dict):
    C4 = {}
    for basket in baskets:
        for i in range(len(basket)):
            for j in range(i+1, len(basket)):
                for k in range(j+1, len(basket)):
                    for l in range(k+1, len(basket)):
                        item1 = itemIndexTable[basket[i].lower()]
                        item2 = itemIndexTable[basket[j].lower()]
                        item3 = itemIndexTable[basket[k].lower()]
                        item4 = itemIndexTable[basket[l].lower()]
                        
                        quadrupleton = tuple(sorted((item1, item2, item3, item4)))
                        if C4.get(quadrupleton) == None:
                            C4[quadrupleton] = 0

    return C4