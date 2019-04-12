prompt = input("Give me a loooong number> ")

def Descending_Order(num):
  stringedNum = str(num)
  listedNum = list(stringedNum)
  sortedList = sorted(listedNum)
  stringedNum = ''.join(sortedList)
  num = int(stringedNum[:: -1])
  return num

print ('Ok, here you can have it back!',Descending_Order(prompt),)