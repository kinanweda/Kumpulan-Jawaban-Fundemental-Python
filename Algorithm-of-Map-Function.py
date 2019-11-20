def kali(num) :
    return num * 3

listNum = [1,2,3,4,5]

def map1(x,y):
    function = [x(item) for item in y]
    return function
  
kata = list(map1(kali,listNum))
print(kata)
