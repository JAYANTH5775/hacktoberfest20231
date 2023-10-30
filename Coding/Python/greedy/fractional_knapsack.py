class item:

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def KP(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    usedCapacity = 0
    totalValue = 0

    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value

        else:
            unusedweight = capacity-usedCapacity
            value = i.ratio * unusedweight
            usedCapacity += unusedweight
            totalValue += value

        if usedCapacity == capacity:
            break
    print("Total capacity  is : "+str(totalValue))


item1 = item(20, 100)
item2 = item(30, 120)

item3 = item(10, 60)

cList = [item1, item2, item3]

KP(cList, 50)
