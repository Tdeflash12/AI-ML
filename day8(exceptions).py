# # # # # #Error
# # # # # #print("hello world") -> synatax error
 
# # # # # num1= int(input("Enter the number: "))
# # # # # num2= int(input("Ebter the another number "))

# # # # # sum = num1-num2 #This represents logical error
# # # # # print(f"sum ={sum}")

# # # # #Exceptions
# # # # # x = int(input("Enter the number:"))
# # # # #print(x) - > tp demonstrate Value Error
# # # # '''
# # # # try:


# # # # except:
# # # # .....
# # # # ........
# # # # .......
# # # # ........
# # # # else:
# # # # .....
# # # # .......
# # # # .........
# # # # finally

# # # # '''

# # # # try:
# # # #     x = int(input("enter the number: "))
# # # # except ValueError:
# # # #     print("Pleae enter an integer!!")
# # # # else:
# # # #  print(f"number = {x}")

# # # while True:
# # #     try:
# # #         x=int (input("Enter the number :"))
# # #     except ValueError:
# # #         #pass is used to not give any sugggestion that provide only enter a number not warning
# # #         print(f"Please enter an integer")
# # #     else:
# # #         break
# # # print(f"The enter number is : {x}")

# # #Division by error
# # #Task-> Program -> takes a number -> divides by the entered number.
# # while True:
# #    try:
# #     x = int(input("Enter the number : "))
# #     result = 10/x
# #    except ValueError:
# #     pass
# #    except ZeroDivisionError:
# #     print("The Divisior cannot be zero")
# #    else:
# #     break

# # print(f"Result is: {result}")
# def main():
#  x= get_int() 
#  print(f"number:{x}")
 
# def get_int():
#  while True:
#   try:
#    x=int(input("Enter a number:"))
  
#   except ValueError:
#     pass
  
#  else:
#   return x
 
#  main()

#  #program = take 3 number as input-> sum , product and operation(num1+num2)/num3
#            by using functional plrogramming
while True:
  try:
      num1= int(input("Enter the number:"))
      num2= int(input ("Enter the another number"))
      num3= int(input("Enter the another number"))
      operation = (num1+num2)/3
  except ValueError:
      pass
  except ZeroDivisionError:
      pass
  else:
      sum=num1+num2+num3
      product=num1*num2*num3
      print(f"sum= {sum}")
      print(f"product= {product}")
      print(f"operation = {operation}")
      
      break