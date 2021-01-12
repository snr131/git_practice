# this function (called function) will sum all integers from 0 to num
def function(num):
  # the variable result will hold a list, from 0 to num
  result = [*range(0,num)]
  # the variable sum will hold the sum of the result list
  sum = 0
  #print(result)
  # the for loop below will add each element of the result list to the sum variable
  for i in range(0, len(result)):
    sum = sum + result[i]
    # if the function input "num" is not an integer 0 will be returned along with a message
    if type(num) != int:
      return 0
      print('wrong input... BYE!')
  # if the function input "num" is an integer, the sum will be printed
  print(sum+num)


function(4)
  