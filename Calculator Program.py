print("Welcome To My First Calculator Program By Ppor")
again = True
while again:
      num1 = input('Enter Number :')
      op = input('Select +,-,*,/ :')
      num2 = input('Enter Number :')
                
      num1 = int(num1)
      num2 = int(num2)

      out = None
      
      if op == '+':
            out = num1 + num2
      elif op == '-':
            out = num1 - num2
      elif op == '*':
            out = num1 * num2
      elif op == '/':
            out = num1 / num2
      print("Answer :"+str(out))
      again = input('Again? Y/N :')
      if again == 'N':
            again = False
            print("Thank You!")
