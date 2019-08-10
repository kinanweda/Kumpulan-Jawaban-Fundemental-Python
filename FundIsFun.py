#soal no.1
# def Find_short(s):
#     kata = s
#     split = kata.split()
#     arr = []
#     for item in split:
#         arr.append(len(item))
#         arr.sort()
#     print(arr[0])

# Find_short("Many people get up early in the morning")
# Find_short("Every office would getting newest monitor")
# Find_short("Create new file after this morning")

#soal no.2
# def persistence(x):
#     angka = x
#     c = 0
#     while(angka>= 10):
#         string = str(angka)
#         jumlah = 1
#         for item in string:
#             jumlah *= int(item)
#         c += 1
#         angka = jumlah
#     print(c)

# persistence(39)
# persistence(999)
# persistence(4)

# soal no.3
# def multiplication_table(row,col):
#     lists = []
#     z = ''
#     for item2 in range(row):
#         lists.append(item2+1)
#     for item in range(len(lists)):
#         for item1 in range(col):
#             if item > item1:
#                 z+='{} '.format(lists[item1]*(item+1))
#             else:
#                 z+='{} '.format(lists[item]*(item1+1))
#         z+='\n'
#     print(z)
# multiplication_table(3,3)
# multiplication_table(5,3)
# multiplication_table(3,5)

# soal no.4
# import string
# def alphabet_position(text):
#     dicts = {
#         'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10, 'k':11,'l':12,'m':13,
#         'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,
#     }
#     for symbol in string.punctuation :
#         text = text.replace(symbol,' ')
#     splits = text.lower().split()
#     huruf = ''
#     lists = ''
#     for item in splits:
#         huruf += item
#     for item in huruf:
#         lists+= '{} '.format(dicts[item])
#     print(lists)

# alphabet_position("The sunset sets at twelve o' clock")
# alphabet_position("it's never too late to try")
# alphabet_position("Have you done your homework?")

def is_prime(num):
    if num <= 1 :
        print('False')
    elif num % 3 == 0:
        print('False')
    else:
        print('True')

is_prime(1)
is_prime(2)
is_prime(-1)
is_prime(5099)
