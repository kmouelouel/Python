#function definition is here 
def printme(str):
    print(str);
    
#now you can call printme function
printme("I am first call to user defined function");
printme("Again second call to the same function");

def changeme (mylist):
   # mylist.append([1,2,3,4]);
    mylist=[1,2,3,4];
    print(" values Inside the function: ",mylist);

#now you can call changeme function
mylist=[10,20,30];
changeme(mylist);
print("Values outside the function: ",mylist);

#function definition is here
def printinfo(name,age):
    print("Name :",name);
    print("Age :",age);
#now you call printinfo function
printinfo(name="kahina", age="32")

#default arguments
def printprofil(Name,Major="computer science"):
    print("Name :",Name);
    print("Major :",Major);

printprofil(Name="kahina Mouelouel")

#variable-length argument

def printinfo(arg, *vartuple):
    print("Output is:")
    print(arg);
    for var in vartuple:
       print(var)

printinfo(10);
printinfo(70,60,50)

#The anonymous function
sum = lambda arg1,arg2:arg1+arg2;

# now you can call sun as a function
print("Value of total :  ",sum(10,20));
print("Value of total :  ",sum(20,40));
#the return statement
#function definition is here
def sum(arg1,arg2):
    total=arg1+arg2
    print("inside the function :",total);
    return total;

#now you call sun function
total=sum(50,20);
print("outside the function:",total);
#scope of variables
#global vs local variables
total=0;# this is global variable
def sum(arg1,arg2):
    #both the parameters and return them.
    total=arg1+arg2;#here total is local variable.
    print("inside the function local total :",total);
    return total;
#now you can call sum function
sum(30,30)
print("outside the function global total :",total);
    



    
