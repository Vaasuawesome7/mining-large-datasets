import sys
sys.path.append('../')

import constants

HashTable1 = [0] * constants.HASH_TABLE_SIZE_MH1
HashTable2 = [0] * constants.HASH_TABLE_SIZE_MH2

def first_pass(baskets: list[list]):
    global HashTable1, HashTable2
    
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
        
    for basket in baskets:
        for i in range(len(basket)):
            for j in range(i+1, len(basket)):
                mitems = [itemIndexTable[basket[i].lower()], itemIndexTable[basket[j].lower()]]
                HashTable1[constants.hash_function_mh1(mitems)] += 1
                HashTable2[constants.hash_function_mh2(mitems)] += 1

    for item in C1.items():
        if (item[1] >= constants.SUPPORT_THRESHOLD):
            L1[item[0]] = item[1]
    
    return (itemIndexTable, L1, C1)

def intermediate_pass_1_2():
    global HashTable1, HashTable2
    
    TempHashTable1 = []
    for count in HashTable1:
        if count >= constants.SUPPORT_THRESHOLD:
            TempHashTable1.append(True)
        else:
            TempHashTable1.append(False)
            
    HashTable1 = TempHashTable1
    
    TempHashTable2 = []
    for count in HashTable2:
        if count >= constants.SUPPORT_THRESHOLD:
            TempHashTable2.append(True)
        else:
            TempHashTable2.append(False)
            
    HashTable2 = TempHashTable2

def second_pass(baskets: list[list], itemIndexTable: dict, L1: dict):    
    items = list(L1.keys())
    
    C2 = {}
    L2 = {}
    
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            mitems = [items[i], items[j]]
            if HashTable1[constants.hash_function_mh1(mitems)] == True and HashTable2[constants.hash_function_mh2(mitems)] == True:
                doubleton = tuple(sorted((items[i], items[j])))
                if C2.get(doubleton) == None:
                    C2[doubleton] = 0

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