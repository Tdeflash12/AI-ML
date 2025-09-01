# # # # # # # # '''
# # # # # # # # lists
# # # # # # # # sets
# # # # # # # # tuples
# # # # # # # # dictionaries
# # # # # # # # '''
# # # # # # # # #list -> mutable data strucuture
# # # # # # # # #tuple -> immutable
# # # # # # # # #sets-> unique value unordered
# # # # # # # # #dictionaries -> key value pairs
# # # # # # # # #"name": "Shyam"
# # # # # # # # #"ph_no" :"9820364211"



# # # # # # # # #lists
# # # # # # # # #lists=[1,2,3,4, "Abhesh","true",9.1]
# # # # # # # # #empty _list=[]
# # # # # # # # l1=[1,2,3,"samip","firoj",4.2]
# # # # # # # # print(l1)
# # # # # # # # print(type(l1))
# # # # # # # # el=[]
# # # # # # # # print(el)
# # # # # # # # print(type(el))

# # # # # # # # #Indexing
# # # # # # # # l2=["Abhesh","Ram","Shyam",32,True,False]
# # # # # # # # '''
# # # # # # # # [0,1,2,3,4, and soon]
# # # # # # # # if we have n elements in a list;
# # # # # # # # the range of index:0 to (n-1)
# # # # # # # # For example if we have  10 elements:
# # # # # # # # the range of index: 0 to (10-1)=9

# # # # # # # # '''
# # # # # # # # print(l2[0])
# # # # # # # # print(type(l2[0]))


# # # # # # # # #-1 index gives the last elements
# # # # # # # # print(l2[-2])
# # # # # # # # print(type(l2[-2]))


# # # # # # # l3=["Abhesh","Ram",32,True,False,3.2,4.1,"Ram","Shyam","Hari",4,2,"Tensorflow","Numy"]
# # # # # # # '''
# # # # # # # the last element
# # # # # # # the second last element 
# # # # # # # the fifth eleement
# # # # # # # '''
# # # # # # # #slicing list[starting_index :ending_index]index 1 to 8 
# # # # # # # print(l3[1:])
# # # # # # # #Result=['Ram', 32, True, False, 3.2, 4.1, 'Ram', 'Shyam', 'Hari', 4, 2, 'Tensorflow', 'Numy']
# # # # # # # print(l3[-4:])
# # # # # # # #Result: [4, 2, 'Tensorflow', 'Numy']
# # # # # # # print(l3[-4:-1])
# # # # # # # #Result: [4, 2, 'Tensorflow']

# # # # # # # # #list function
# # # # # # # # #append
# # # # # # # # l3.append("apple")
# # # # # # # # l3.append("cat")
# # # # # # # # print(l3)

# # # # # # # #insert (1,"Radha")-> (index,value)
# # # # # # # l3.insert(0,"Radha")
# # # # # # # print(l3)
# # # # # # # # now insert at 5 "dog"
# # # # # # # l3.insert(5,"dog")
# # # # # # # print(l3)

# # # # # # # # to sort  the list 

# # # # # # l3=['Radha', 'Abhesh', 'Ram', 32, True, 'dog', False, 3.2, 4.1, 'Ram', 'Shyam', 'Hari', 4, 2, 'Tensorflow', 'Numy']
# # # # # # # my_list=[33,5,66,5,443,545,64,34,2,4,64,54,545,3,525,35,3]
# # # # # # # print(my_list)
# # # # # # # my_list.sort(reverse=True)
# # # # # # # print(my_list)
# # # # # # '''
# # # # # # for i in range(lens):
# # # # # # my_list[i]= (int my _list[i])
# # # # # # '''
# # # # # # # print(l3.pop())
# # # # # # # print(l3)
# # # # # # # l3.pop()
# # # # # # # print(l3)
# # # # # # # print(l3.append("Elon"))
# # # # # # l3.insert(5,"Ram")
# # # # # # print(l3)
# # # # # # l3.remove("Ram")
# # # # # # print(l3)
# # # # # # l3.remove("Ram")
# # # # # # print(l3)
# # # # # # l3.clear()
# # # # # # print(l3)

# # # # # '''
# # # # # tuple -> immutable , indexing and slicing same as list
# # # # my_tuple= (2,1,5,True,"Ram",43.3,1,545,3,1,3,1,3)
# # # # # print(my_tuple)
# # # # # print(type(my_tuple)) 
# # # # # number=my_tuple.count(1) 
# # # # # print(number)

# # # # # index9 =my_tuple.index(43.3)
# # # # # print(index9)
# # # # commas,should be give to represent tupple
# # # my_tuple=1,2,3,4,
# # # print(type(my_tuple))

# # #set
# # my_sets ={1,2,1,3,4,4}
# # print(my_sets)
# # print(type(my_sets))
# # #result ={1, 2, 3, 4}
# # #<class 'set'>
# # my_sets.add(5)
# # print(my_sets)
# # my_sets.remove(2)
# # print(my_sets)

# # my_sets.add(-1)
# # print(my_sets)

# my_sets={0,4,2,3,-2,-1,-5}
# print(my_sets)

'''
my_dict={
"key": "value"
...............
...........
...............
..............
"key_n": "value_n"
 the key must be unique and immutable
}
'''

my_dict= {
    "Name": "Abhesh",
    "Cast" : "Mandal",
    "Age" : "17"
}
print(my_dict)
print(type(my_dict))
print(my_dict.keys())
print(my_dict.values())