dict={'Name':'Zara', 'Age':7, 'Class':'First'};
print("dict['Name']: ",dict['Name']);
print("dict['Age']: ",dict['Age']);
print("dict['Class']: ",dict['Class']);
dict['Age']=8;#update exixting entry
dict['School']="DPS School";# add new entry
print("dict['School']: ",dict['School']);
print("dict['Age']: ",dict['Age']);
del dict['Name']; #remove entry with key Name
dict.clear();     #remove all enties in dict 
del dict;       #delete entire dictionary

#time module
import time;

ticks=time.time();
print("Number of ticks since 12:00:", ticks)
localtime=time.localtime(time.time())
print("local current time : ",localtime)
import calendar
cal=calendar.month(2016,7)

print("Here is the calandar: ")
print (cal);
