lists1 = []
lists2 = []

def input1():
inputs = int(input('Panjang Isi dictionary : '))
return inputs

def add():
  inputs = int(input('Panjang Isi dictionary : '))
  print('''
Jenis Value :
1.String
2.Number''')
  pilih = int(input('Pilih Jenis Value : '))
  if pilih == 1:
    for item in range (inputs):
      x= input('masukkan key : ')
      y= input('masukkan value : ')
      add = lists1.append(x)
      add2 = lists2.append(y)
  elif pilih == 2:
    for item in range (inputs):
      x= input('masukkan key : ')
      y= input('masukkan value : ')
      add = lists1.append(x)
      add2 = lists2.append(y)           
    
def look():
  print("""
 _____________________
|         |           |
|   key   |   value   |
|_________|___________|""")
  for item in range(0,len(lists1)) :
      
    print("""|   {}   |   {}   |
|___{}___|___{}___|""".format(lists1[item],lists2[item],lists1[item].replace(lists1[item],len(lists1[item])*'_'),lists2[item].replace(lists2[item],len(lists2[item])*'_')))


def menu():
    selection = 1
    while(selection <= 4):
        print('''
Pilih yang mana?  

1. Lihat Full Dictionary
2. Isi Dictionary
3. Search Dictionary
4. Keluar
''')
        selection = int(input('Pilih Nomor Menu : '))
        if selection == 1:
            look()
        elif selection == 2:
            add()
        elif selection == 3:
            kata = {lists1:lists2 for lists1,lists2 in zip(lists1,lists2)}
            inputkata = input('search :')
            search = list(filter(lambda x : inputkata in x.lower() or inputkata in x.upper() or inputkata in x.capitalize(),kata))
            if len(search) == 1:
              print("""
 _____________________
|         |           |
|   key   |   value   |
|_________|___________|""")
              print("""|   {}   |   {}   |
|___{}___|___{}___|""".format(search[item],kata[search[item]],search[item].replace(search[item],len(search[item])*'_'),kata[search[item]].replace(kata[search[item]],len(kata[search[item]])*'_')))

            elif len(search) > 1:
              for item in range(0,2):
                print("""
 _____________________
|         |           |
|   key   |   value   |
|_________|___________|""")
                print("""|   {}   |   {}   |
|___{}___|___{}___|""".format(search[item],kata[search[item]],search[item].replace(search[item],len(search[item])*'_'),kata[search[item]].replace(kata[search[item]],len(kata[search[item]])*'_')))      
        elif selection == 4:
            print('Terima Kasih!')
            break
menu()
