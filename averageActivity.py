import json
from pprint import pprint
import matplotlib.pyplot as plt

with open('sm.json') as data_file:
    data = json.load(data_file)

attrKeyList = data["attractors"].keys()
eachActivity = []
dic = {}

for attrKey in attrKeyList:
    if data["attractors"][attrKey]["type"] == "point":
        pointRatio = data["attractors"][attrKey]["ratio"]
        pointValue = data["attractors"][attrKey]["value"]
        pointAttr = data["state_key"][pointValue]

        for eachNode in pointAttr:
            nodeRatio = float(eachNode) * float(pointRatio)
            eachActivity.append(nodeRatio)
            dic[pointValue] = eachActivity
        else:
            eachActivity = []

    elif data["attractors"][attrKey]["type"] == "cyclic":
        cyclicRatio = data["attractors"][attrKey]["ratio"]
        cyclicValue = data["attractors"][attrKey]["value"]
        cyclicLength = len(cyclicValue)

        for eachValue in cyclicValue:
            cyclicAttr = data["state_key"][eachValue]
            for eachNode in cyclicAttr:
                nodeRatio = float(eachNode) * float(cyclicRatio) * (1/cyclicLength)
                eachActivity.append(nodeRatio)
                dic[eachValue] = eachActivity
            else:
                eachActivity = []

averageActivity = []
for k in range(0, len(data["labels"])):
    averageActivity.append(0)

for eachValue in data["state_key"]:
    z = 0
    for eachNode in dic[eachValue]:
        averageActivity[z] = float(averageActivity[z]) + float(eachNode)
        z = z + 1
    else:
        z = 0

for i in averageActivity:
    print(i, end=" ")

