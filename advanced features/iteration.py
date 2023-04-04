def findMinAndMax(list):
    if list == []:
        return (None,None)
    else:
        return (min(list),max(list))

print(findMinAndMax([1,4,6,7,5,43]))
print(findMinAndMax([]))
print(findMinAndMax([7]))