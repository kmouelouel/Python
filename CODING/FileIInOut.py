        #printing to the screen
print("pyhton is really a great language,", "is not it");
#Reading keyboard input
mydata = input('Prompt :');
print ("hello",mydata);
#opening and closing Files
#open file
#find out the file object attributes
fo=open("foo.txt","r+");
fo.write("Python is a great language.\nYeah its great!!\n");
print("Name if the file :",fo.name);
print("Closed or not :",fo.closed)
print("Opening mode :",fo.mode);
str=fo.readline((10);
print("read  the string :",str);
#close opened file
fo.close();


# this option doesnt work:
#print("Softspace flag: ",fo.softspace);

import os
#rename a file from test1.txt to text2.txt
                os.rename("foo.txt","foocc.txt")
