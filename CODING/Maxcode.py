# this is my first program in python
# the program will find the max of three number that Inputed by user.
#var1=int(input("entre you first value : "))
#var2=int(input("entre you second value : "))
#var3=int(input("entre you third value : "))
#print("the max og three value is \n")
#print(max(var1,var2,var3))

# lesson 6:Strings
a='Hello, My name is: '
b="Kahina Mouelouel, "
c="""I am 32 years old"""
nbre=5
print (len(a))
 
print(a+b+c)
print(b+str(nbre))
#Lesson 7: lists
names=["Celia","Lynda","Safia","nassima","Mammy"]
print(names)
print(names[0])
names.append("Dad")
names.append("Said")
names.append("Belkacem")
Ages=[12,21,30,33,52,54,28,26]
print(names)
print(len(names))
print(Ages)
print(len(Ages)) 
print(names,Ages)
names.extend(Ages)
print(names)
names.remove("Said")
print(names)
print(Ages[2:7])
input("Please press entre to exit.")
