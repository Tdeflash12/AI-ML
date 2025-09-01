# '''
# lists
# sets
# tuples
# dictionaries
# '''
# #list -> mutable data strucuture
# #tuple -> immutable
# #sets-> unique value unordered
# #dictionaries -> key value pairs
# #"name": "Shyam"
# #"ph_no" :"9820364211"



# #lists
# #lists=[1,2,3,4, "Abhesh","true",9.1]
# #empty _list=[]
# l1=[1,2,3,"samip","firoj",4.2]
# print(l1)
# print(type(l1))
# el=[]
# print(el)
# print(type(el))

# #Indexing
# l2=["Abhesh","Ram","Shyam",32,True,False]
# '''
# [0,1,2,3,4, and soon]
# if we have n elements in a list;
# the range of index:0 to (n-1)
# For example if we have  10 elements:
# the range of index: 0 to (10-1)=9

# '''
# print(l2[0])
# print(type(l2[0]))


# #-1 index gives the last elements
# print(l2[-2])
# print(type(l2[-2]))


l3=["Abhesh","Ram",32,True,False,3.2,4.1,"Ram","Shyam","Hari",4,2,"Tensorflow","Numy"]
'''
the last element
the second last element 
the fifth eleement
'''
#slicing list[starting_index :ending_index]index 1 to 8 
print(l3[1:])
#Result=['Ram', 32, True, False, 3.2, 4.1, 'Ram', 'Shyam', 'Hari', 4, 2, 'Tensorflow', 'Numy']
print(l3[-4:])
#Result: [4, 2, 'Tensorflow', 'Numy']
print(l3[-4:-1])
#Result: [4, 2, 'Tensorflow']