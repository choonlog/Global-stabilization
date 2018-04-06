import json
from pprint import pprint
import matplotlib.pyplot as plt

with open('6_5.json') as data_file:
    data = json.load(data_file)

combinationKeyList = data.keys()
contents = ""
singleton = ""

k = 1
for combinationKey in combinationKeyList:

    print("-------------------------------------------------------------------------")
    print("No." + str(k) + " " + combinationKey + " pertubation")
    print("-------------------------------------------------------------------------")

    contents += "-------------------------------------------------------------------------\n"
    contents += "No." + str(k) + " " + combinationKey + " pertubation\n"
    contents += "-------------------------------------------------------------------------\n"

    attrKeyList = data[combinationKey]["attractors"].keys()

    print("Nodes :", end=" ")

    contents += "Nodes : "
    contents += str(data[combinationKey]["labels"])

    for node in data[combinationKey]["labels"]:
        print(node, end=" ")
    else:
        print("\n")

    attrAllType = [0, 0, 0]
    sep = " "
    z = 1
    for attrKey in attrKeyList:
        attrType = data[combinationKey]["attractors"][attrKey]["type"]
        attrRatio = data[combinationKey]["attractors"][attrKey]["ratio"]
        print("Attractor " + str(z))
        print("Type : " + attrType)
        print("Ratio : " + str(attrRatio))

        contents += "Attractor " + str(z)
        contents += "\n"
        contents += "Type : " + attrType
        contents += "\n"
        contents += "Ratio : " + str(attrRatio)
        contents += "\n"

        if attrType == "point":
            attrAllType[0] = attrAllType[0] + 1
            attrValue = data[combinationKey]["attractors"][attrKey]["value"]
            pointAttr = data[combinationKey]["state_key"][attrValue]
            print(sep.join(pointAttr))

            contents += sep.join(pointAttr)
            contents += "\n"

        elif attrType == "cyclic":
            attrAllType[1] = attrAllType[1] + 1
            for attrValue in data[combinationKey]["attractors"][attrKey]["value"]:
                cyclicAttr = data[combinationKey]["state_key"][attrValue]
                print(sep.join(cyclicAttr))

                contents += sep.join(cyclicAttr)
                contents += "\n"

        else:
            attrAllType[2] = attrAllType[2] + 1
        z = z + 1
        print("", end="\n")

        contents += "\n"



    print("---------------------------------------------------")
    print("| The number of total attractors : " + str(attrAllType[0] + attrAllType[1]))
    print("| Point attractor : " + str(attrAllType[0]))
    print("| Cyclic attractor : " + str(attrAllType[1]))
    print("| Unknown attractor : " + str(attrAllType[2]))
    print("---------------------------------------------------", end="\n\n")

    if attrAllType[0] == 16 and attrAllType[1] == 0:
        singleton += "No." + str(k) + " " + combinationKey + " pertubation\n"


    contents += "---------------------------------------------------"
    contents += "\n"
    contents += "| The number of total attractors : " + str(attrAllType[0] + attrAllType[1])
    contents += "\n"
    contents += "| Point attractor : " + str(attrAllType[0])
    contents += "\n"
    contents += "| Cyclic attractor : " + str(attrAllType[1])
    contents += "\n"
    contents += "| Unknown attractor : " + str(attrAllType[2])
    contents += "\n"
    contents += "---------------------------------------------------\n\n\n"

    k = k + 1

all = open("6-5.txt", "w")
all.write(contents)
all.close()

single = open("6-5.txt", "w")
single.write(singleton)
single.close()


