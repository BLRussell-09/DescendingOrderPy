num = 15
def Descending_Order(num):
  stringedNum = str(num)
  # reversedStr = stringedNum[::-1]
  listedNum = list(stringedNum)
  sortedList = sorted(listedNum)
  stringedNum = ''.join(sortedList)
  num = int(stringedNum[:: -1])
  return num

print (Descending_Order(num))