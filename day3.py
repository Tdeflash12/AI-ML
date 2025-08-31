# # name="abhesh mandal"
# # new_name=name.capitalize()
# # print(new_name)
# # '''
# name=" __-- firoj ##&& seikh 123 @@" 
# # first name =Firoj
# # Last_name =Karki

# new_name_1=name.strip(" _-123@")
# print(new_name_1)
# new_name_final=new_name_1.replace(" ##&& "," ").title()
# print(new_name_final)
# first,last=new_name_final.split()
# print(first)
# print(last)

# ph_no="(+977)9820364211"
# phone_no_2=ph_no.replace("(+977)","")
# print(phone_no_2)

Text =" $$ Shyam ** %(+977)9820364211"
'''
first name => Shyam
phone no =>9820364211
'''
clean_text=Text.strip(" $").replace(" ** %(+977)"," ")
print(clean_text)
first_name,phone_number=clean_text.split()
print(first_name)
print(phone_number)