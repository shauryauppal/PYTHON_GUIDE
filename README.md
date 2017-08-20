# PYTHON TUTORIAL
### Start
- Variable-Store value
- Data types-Numbers,string,boolean
- Comments-> by hash #
- Arthmetic operators-> * , + , - , / , % , **
- **NOTE - In python 2.7 print " " works while in python 3+ print ("") works**
**********************
### Explicit String Conversion->
+ print ("I have +str(2)+"apples")
+ str() converts a non-string to string
****************
###Escaping characters->
+ print 'I don\ 't know'
************
### Accessing by Index
+ c="cats"[2] ->c="t"
+ a="hello"[1] ->a="e"
****************
### String Methods->
1. len()
2. lower()
3. upper()
4. str()
+ a="hello"
+ print len(a)
+ print a.upper()
+ print a.lower()
+ print str(a) #If a is int type
*************************
### Take Input
+ name=input("Enter name->")
+ print (name)

+ x=input("Enter value->")
+ print int(x)+10

**NOTE-> input() gives always str type**
******************
### Python date & Time
+ #### date library
1. from datetime import datetime //import library
2. print datetime.now()
+ output-> 2017-08-18 11:02:44.5455
+ #### If you don't want full datetime
1. now = datetime.now
- print now.year
- print now.month
- print now.day
- print now.hour
- print now.minute
- print now.second
***********************
### IF-ELSE
```
if 8<9:
   print "Eight less"
 else:
   print "Greater"
   ```
   #### SYNTAX
   ```
   if condition:
     statement
   elif condition:
     statement
   else:
    statement
  ```
  *************************
### AND/OR/NOT
+ AND
+ ```  print 3>2 and 5==5 ```
+ OR
+ ``` print 3>2 or 5==5 ```
+ **NOTE-> && || doesnot work in python**
+ NOT
+ ```print not True```
*************************
### isalpha()
```
x=123
print x.isalpha() #gives false
```
**********************
### String Print
+ s="Charlie"
+ print s[0] # prints "C"

- print s[1:4]

prints "harl"
**This is called Slicing**
*****************
## Functions
**Syntax**
```
def function_name(parameter):
//code
return _____
```
*******************
### Use Maths
from maths import *
By this you can use sqrt
+ print sqrt(25)
******************
### Universal import
```from module import *```
************
+ ### max,min,abs
   + max(a,b)
   + min(a,b)
   + abs(-a)
+ ### type()
   + print type(42)
   + print type("wqw")
   + print type([1,2,3])
******************
# Sample program
```
def check_type(s):
   if(type(s)==int or type(s)==float):
      return abs(s)
   else:
      return "Nope"
  ```
  ******************
## Python List & Dictionary
+ list_name=[item1,item2]
+ List does not have a fixed length you can add items to end of a list any time you like->
```
> list_name=['a','b','c']
> list_name.append('d')
> print len(list_name)
> print list_name
```
### List Slicing
```
letter=['a','b','c','d','e']
slice = letter[1:3]
print slice
# ['b','c']
```
Syntax
```
list_name[start,end,stride]
```
### String Slicing
```
abc="shaurya"
abc[:2]      #Grabs the first two items
abc[3:]      #Grabs the fourth through last items
abc[4:7]     #print 'ury'
```
### Maintaing order
```
animals=["ant","dog","cat"]
print animals.index("dog")

animals.insert(1,"bat")
print animals            # ['ant','bat','dog','cat']
```
****************
### For loop
```for variable in list_name:```

```print variable```
*********************
### Sort()
+ animals=["cat","bat","apple"]
+ animals.sort()
+ print animals    #["apple","bat","cat"]
******************
### Dictionary
+ Dictionary Access data value by key not by index
+ key-> can be string or number
```
d={'key1':1,'key2':2,'key3':3}
print d['key1']
```
+ ##### Dictionary are not Fixed
    + We can add new key/value pairs to dictionaryafter it is created
    + dict_name[new_key]=value
+ #### Delete item in Dictionary
   + del dict_name[key_name]
+ #### Delte in List
   + letter=['a','b','c','d']
   1. BY value->letter.remove('b')
   2. BY index->n.pop(2)
   3. BY Del->del(n[1])
****************************
# Sample Program
```
my_dict={
  "fish":['a','b'],
  "hel":32,
  "pat":"men"
}

print my_dict["fist"][0]
```
***************************
## Iteration
## For
  ```
   a="hello"
   for x in range(0,len(a))
   print x
  ```
   ### Range
    + range function has 3 different versions
    1. range(stop)
    2. range(start,stop)
    3. range(start,stop,step)

  ### Iterate over a list
  1. Method1
     ```
     for item in list_name:
       print item

  2. Method2
     ```
     for i in range(0,len(list_name)):
       print list_name[i]
*****************************
#### Add two list
```
a=[1,20,3]
b=[14,1,9]
print a+b    #[1,20,3,14,1,9]
```
******************
