# # # # # # # #Looping or iterative statements

# # # # # # # # for loop
# # # # # # # fruits = ["apple","Banana","Kiwi","Mango","Watermelon"]
# # # # # # # for fruit in fruits:
# # # # # # #     print(fruit)

# # # # # # #my_list = range(starting value,ending value,step->1) 

# # # # # # my_list = list(range(1,11))
# # # # # # print(my_list)

# # # # # # i need to print the numbers from 1 to 10
# # # # # for i in range(1,21,2):
# # # # #     print(i,end=" ")

# # # # my_dic={
# # # #     "1": "Apple",
# # # #     "2":"Banana",
# # # #     "3":"mango"
# # # # }
# # # # for k in my_dic:
# # # #     print(f"{k}: {my_dic[k]}")

# # # fruits = ["Apple","Mango","Banana"]
# # # count = 0
# # # for fruit in fruits:
# # #     count = count+1
# # #     print(f"{count} : {fruit}")

# # #infinite loop

# # # count=0
# # # while count<=10:
# # #     print("My name is Abhesh ")
# # #     count+=1

# # #break -> when a particular condition occurs break the loop
 
# # for i in range(1,10):# [1,2,3,4,5,]
# #     if i == 6:
# #         break
# #     print(i)


# #continue -> when a particular condition occurs skip the iteration
# # Task my_list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
skipped=[]
for i in range(1,16):# [1,2,3,4,5,]
    if i  in[2,4,6]:
        skipped.append(i)
        continue  
    print(i,end=" ")
print()
print(f"Skipped values = {skipped}")

   
