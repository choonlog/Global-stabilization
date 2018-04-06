import json
from pprint import pprint
import matplotlib.pyplot as plt

with open('FVS.json') as data_file:
    data = json.load(data_file)

attrKeyList = data["attractors"].keys()

print("Nodes :", end=" ")

for node in data["labels"]:
    print(node, end=" ")
else:
    print("\n")

attrAllType = [0, 0, 0]
sep = " "
z = 1
for attrKey in attrKeyList:
    attrType = data["attractors"][attrKey]["type"]
    attrRatio = data["attractors"][attrKey]["ratio"]
    print("Attractor " + str(z))
    print("Type : " + attrType)
    print("Ratio : " + str(attrRatio))

    if attrType == "point":
        attrAllType[0] = attrAllType[0] + 1
        attrValue = data["attractors"][attrKey]["value"]
        pointAttr = data["state_key"][attrValue]
        print(sep.join(pointAttr))
    elif attrType == "cyclic":
        attrAllType[1] = attrAllType[1] + 1
        for attrValue in data["attractors"][attrKey]["value"]:
            cyclicAttr = data["state_key"][attrValue]
            print(sep.join(cyclicAttr))
    else:
        attrAllType[2] = attrAllType[2] + 1
    z = z + 1
    print("", end="\n")

print("---------------------------------------------------")
print("| The number of total attractors : " + str(attrAllType[0] + attrAllType[1]))
print("| Point attractor : " + str(attrAllType[0]))
print("| Cyclic attractor : " + str(attrAllType[1]))
print("| Unknown attractor : " + str(attrAllType[2]))
print("---------------------------------------------------", end="\n\n")