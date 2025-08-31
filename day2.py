# # '''
# # name="Abhesh ** Mandal"
# # new_name= name.replace(" ** "," ")
# # print(new_name)
# # naame="Jenisha__"
# # # rstrip for right cut
# # new_naame= naame.rstrip("__") 
# # print(new_naame)
# # '''
# # abc= " ---My---System name is Tdeflash123__"
# # new_abc=abc.strip(" -123_")
# # print(new_abc)
# # # new_abc=My---System name is Tdeflash
# # new_abc_final=new_abc.replace("---"," ") 
# # print(new_abc_final)
# # ''
# #  split()
# #  capatalize()
# #title()
# #  '''
# name= "  ---abhesh @@ mandal 1 2 3 __"
# new_name=name.strip(" -123_")
# print(new_name)
# #reault=abhesh @@ mandal
# new_name_1=new_name.replace(" @@ "," ")
# print(new_name_1)
# #Result=abhesh mandal
# new_name_final=new_name_1.title()
# print(new_name_final)
# #result= Abhesh Mandal

# #First name =Abhesh and Last name = Mandal
# new_name_final.split()
# '''
# after breaking 
# first name =>> first part
# Second name =>> Second part
# '''
# first_name,last_name=new_name_final.split()
# print(first_name)
# #Result =Abhesh
# print (last_name)
# #Result=Mandal

name="Abhesh,Kumar,Mandal "
first,middle,last=name.split(",")
print(first)
print(middle)
print(last)