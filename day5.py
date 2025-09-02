# # # # # # '''
# # # # # # if 
# # # # # # if else
# # # # # # if else.......else
# # # # # # nested
# # # # # # match case statement
# # # # # # '''
# # # # # # # a=6
# # # # # # # '''
# # # # # # # if condition:
# # # # # # #    statement(s)
# # # # # # # '''
# # # # # # # if a>0:
# # # # # # #     print("the number is positive")

# # # # # # num=12
# # # # # # if num > 0:
# # # # # #     print("the number is positvie")
# # # # # # else:
# # # # # #     print("THe number is negative")


# # # # # num = int (input("Enter a number:"))
# # # # # if num>0:
# # # # #     print("The number is postive ")
# # # # # else:
# # # # #     print("the number is negative")

# # # # # if -> else if (elif)......... -> else
# # # # '''
# # # # if conditon:
# # # #     statement(s)
# # # #     elif condition:
# # # #     ........
# # # #     ...........
# # # #     statement(s)
# # # #     ........
# # # #     else :
# # # #     stateent(S)
# # # # '''
# # # # num = int (input("Enter a number:"))
# # # # if num>0 :
# # # #     print ("the number is positive")
# # # # elif num< 0:
# # # #     print("The number is negative")
# # # # else:
# # # #     print("The number is zero")
# # # #  # Write a program to check whether the num is odd or even

# # # # num= int(input("Enter a number:"))
# # # # if num % 2 == 0:
# # # #     print ("The number is even")
# # # # elif num == 0:
# # # #     print("The number is zero")
# # # # else:
# # # #     print("The number is odd:")    

# # # num =2
# # # truth=num==3
# # # print(truth)    
# # '''
# #  if condition:
# #   if condition:
  

# #    else:
   
# # else:
# #   if conditon:


# #   else:   
# # '''  

# # num1 = int(input("Enter a number:"))
# # num2=int(input("Enter another number"))
# # num3= int (input("Enter the third number:"))
# # if num1 > num2:
# #     if num1> num3:
# #       print(f"The greatest number is {num1}")
# #     else:
# #       print(f"the greatest number is {num3}")    
# # else:
# #    if num2 > num3:
# #     print(f"the greatest number is {num2}")
# #    else:
# #      print(f"The greatest number is {num3}")

# num1 = int(input("Enter a number:"))
# num2=int(input("Enter another number"))
# num3= int (input("Enter the third number:"))
# if (num1>num2) and (num1>num3):
#     print("The Greatest number is {num1}")
# elif (num2>num3) and (num2>num1):
#     print("The Greatest numner is{num2}")
# else:
#     print("The Greatest numer is{num3}")

# truth = 5> 4
# print(truth)

num1 = int(input("Enter a number:")) 
num2=int(input("Enter another number"))
ch= int (input("Enter:\n1.for Addition\n2 for Subtraction\n3.product\n"))
match ch:
    case 1:
        add = num1+num2
        print(f"{num1}+ {num2}= {add}") 
    case 2:
        if num1>num2:
         sub = num1-num2
         print(f"{num1}- {num2}= {sub}") 
        else:
           sub=num2-num1 
           print(f"{num2}- {num1}= {sub}") 

    case 3:
     pro = num1*num2
     print(f"{num1}*{num2}={pro}")
    case _:
      print("Enter the valid number")
    
        


       
        
         
