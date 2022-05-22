import util
import sys
sys.path.append('../')
import data

data.preprocess_dataset()

(itemIndexTable, L1, C1) = util.first_pass(data.baskets)
print("\n------ INDEX TABLE ------")
for item in itemIndexTable.items():
    print(item)

print("\n------ CANDIDATE SET ------\n")
for item in C1.items():
    print(item)

# this is to make the bitmap
util.intermediate_pass_1_2()

print("\n------ FIRST ITEMSET ------")
for item in L1.items():
    print(item)
    
print("\n------ SECOND ITEMSET ------")
L2 = util.second_pass(data.baskets, itemIndexTable, L1)
for item in L2.items():
    print(item)
    
print("\n------ THIRD ITEMSET ------")
L3 = util.third_pass(data.baskets, itemIndexTable, L2)
for item in L3.items():
    print(item)
    
print("\n------ CANDIDATE QUADRUPLETONS ------")
C4 = util.find_quadrupletons(data.baskets, itemIndexTable)

print("")