import json
from pprint import pprint
import matplotlib.pyplot as plt

with open('CK_application_to_r9.json') as data_file:
    data = json.load(data_file)

combinationKeyList = data.keys()
contents = ""

for combinationKey in combinationKeyList:

    attrKeyList = data[combinationKey]["attractors"].keys()
    eachActivity = []
    dic = {}

    for attrKey in attrKeyList:
        if data[combinationKey]["attractors"][attrKey]["type"] == "point":
            pointRatio = data[combinationKey]["attractors"][attrKey]["ratio"]
            pointValue = data[combinationKey]["attractors"][attrKey]["value"]
            pointAttr = data[combinationKey]["state_key"][pointValue]

            for eachNode in pointAttr:
                nodeRatio = float(eachNode) * float(pointRatio)
                eachActivity.append(nodeRatio)
                dic[pointValue] = eachActivity
            else:
                eachActivity = []

        elif data[combinationKey]["attractors"][attrKey]["type"] == "cyclic":
            cyclicRatio = data[combinationKey]["attractors"][attrKey]["ratio"]
            cyclicValue = data[combinationKey]["attractors"][attrKey]["value"]
            cyclicLength = len(cyclicValue)

            for eachValue in cyclicValue:
                cyclicAttr = data[combinationKey]["state_key"][eachValue]
                for eachNode in cyclicAttr:
                    nodeRatio = float(eachNode) * float(cyclicRatio) * (1 / cyclicLength)
                    eachActivity.append(nodeRatio)
                    dic[eachValue] = eachActivity
                else:
                    eachActivity = []

    averageActivity = []
    for k in range(0, len(data[combinationKey]["labels"])):
        averageActivity.append(0)

    for eachValue in data[combinationKey]["state_key"]:
        z = 0
        for eachNode in dic[eachValue]:
            averageActivity[z] = float(averageActivity[z]) + float(eachNode)
            z = z + 1
        else:
            z = 0

    print(combinationKey, end="\n")
    for i in averageActivity:
        print(i, end=" ")
        contents += str(i)
        contents += " "
    else:
        print("")

    contents += str(combinationKey).replace(" ", "")
    contents += "\n"

all = open("CK_application_to_r9.txt", "w")
all.write(contents)
all.close()