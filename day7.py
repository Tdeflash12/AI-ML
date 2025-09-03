
# '''
#   Syntax :
#   def function_name(parameter(s), default parameter can also be defined):
#       statements........
#       return varaible/value

      
#   ->function call
#   function_name(value(s) / variable)    
# '''



# # # #Task 1 to write a program  that greets the user function

# # # def greet(name):
# # #     print(f"Welcome {name}")
    
# # # name= input("Enter Your Name: ")
# # # greet (name)

# # #Task2  Temperature converter from degree to celsius

# # def celsius_to_farenheit(celsius):
# #     farenheit= (celsius*9 /5) + 32
# #     return(farenheit)

# # def main():
# #     celsius= float(input("Entet the temperature  in Celsius"))
# #     feren = celsius_to_farenheit(celsius)
# #     print(f"Temperature in farenheit = {feren:.2f} degree farenheit")
    
# # main()

# # Task3: Write a program to find  the maximum among three number

# def max_three_no(num1,num2,num3):
#     return max(num1,num2,num3)

# def main():
#     num1=int(input("Enter the number:"))
#     num2=int(input("Enter the another number"))
#     num3=int(input("Enter the another number"))
#     greatest= max_three_no(num1,num2,num3)
#     print(f"The greatest number  among {num1}, {num2}, {num3} = {greatest}")

# main()

# # Task4: Write a program to find  the minimum among three number

# def max_three_no(num1,num2,num3):
#     return min(num1,num2,num3)

# def main():
#     num1=int(input("Enter the number:"))
#     num2=int(input("Enter the another number"))
#     num3=int(input("Enter the another number"))
#     smallest= max_three_no(num1,num2,num3)
#     print(f"The greatest number  among {num1}, {num2}, {num3} = {smallest}")

# main()

# '''
# Task5: Build a simple calculator that performs addition,Subtraction, Multiplication and Division
#        using the comncept of functional programming

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")