#Contoh soal 1

kata = ['Merdeka','Hello','Hellos','Sohib','Kari ayam']
inputkata = input('search :')
search = list(filter(lambda x : inputkata.lower() in x.lower(),kata))
print(search)

#------------------------------------------------------------------------------------------------------
#Contoh soal 2

kata = 'aku baru makan nasi terus aku mau makan mie nanti malam'
lists = kata.split(' ')
s = set(lists)
list1 = list(s)
for item in range(0,len(list1)):
  kata = list(filter(lambda lists: list1[item] in lists,lists))
  print('kata {} berjumlah {} '.format(list1[item],len(kata)))



#-----------------------------------------------------------------------------------------------------

def even(num) :
  return num % 2 == 0

listNum = [1,2,3,4,5]

def filter1(x,y):
  function = [item for item in y if x(item)]
  return function
  
kata = list(filter1(even,listNum))
print(kata)
