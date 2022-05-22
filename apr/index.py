import util
import data

data.preprocess_dataset()

(itemIndexTable, L1) = util.first_pass(data.baskets)
print("\n------ INDEX TABLE ------")
for item in itemIndexTable.items():
    print(item)

print("\n------ FIRST ITEMSET ------")
for item in L1.items():
    print(item)

print("\n------ SECOND ITEMSET ------")
L2 = util.second_pass(baskets=data.baskets, itemIndexTable=itemIndexTable, L1=L1)
for item in L2.items():
    print(item)

print("\n------ THIRD ITEMSET ------")
L3 = util.third_pass(baskets=data.baskets, itemIndexTable=itemIndexTable, L2=L2)
for item in L3.items():
    print(item)
    
print("\n------ CANDIDATE QUADRUPLETONS ------")
C4 = util.find_quadrupletons(data.baskets, itemIndexTable)

print("")
