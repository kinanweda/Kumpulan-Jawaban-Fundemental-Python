def ascending():
    lists=[40,100,1,5,25,10]
    for item in range(len(lists)) :
        for item1 in range(0, len(lists)-1):
            if lists[item1]>lists[item1+1]:
                a = lists[item1]
                lists[item1]=lists[item1+1]
                lists[item1+1]=a
            else:
                lists
    return lists

print(ascending())

def descending():
    lists=[40,100,1,5,25,10]
    for item in range(len(lists)) :
        for item1 in range(0, len(lists)-1):
            if lists[item1]<lists[item1+1]:
                a = lists[item1]
                lists[item1]=lists[item1+1]
                lists[item1+1]=a
            else:
                lists
    return lists

print(descending())
print('Nilai tertinggi',descending()[0])
print('Nilai terendah',descending()[5])
