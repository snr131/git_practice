def function(num):
  result = [*range(0,num)]
  sum = 0
  #print(result)
  for i in range(0, len(result)):
    sum = sum + result[i]
    if type(num) != int:
      return 0
      print('wrong input... BYE!')
  print(sum)
  