for num in range(2, 101):
  # for each number in the range between 2 and 100
    if all(num%i!=0 for i in range(2, num)):
      # if everything within the parenthesis is True, print the number selected within that range of 2 to 100; within the parenthesis, the selected number modulo not equal to 0, meaning there is a remainder, i being a number in the range 2 through the originally selected number
       print (num)