'''
Identifier:
\d any number
\D anything but a number
\s space
\S anything but a space
\w any Character
\W anything but a character
. any character except for a new line
\b a white space around a character
\. a period

Modifier:
{1,3}  we are expexting 1-3
+ match one or more
? match 0 or one
* match 0 or more
$ match the end of a string
^ matching the begining of string
| either or
[] range or variance
{x} expecting x amount

white space character:
\n new line
\t tab
\s space
\e escape
\r return

Dont Forget:
. + * ? $ ^ () {} []
'''
import re
exampleString='''
Behnaz is 32,and Alireza is 36, and her sister Mahnaz is 39 yeas-old, her mom Fatemeh is 58
'''
ages=re.findall(r'\d{1,3}',exampleString)
print(ages)
names=re.findall(r'[A-Z][a-z]*',exampleString)
print(names)
dic={}
x=0
for eachName in names:
    dic[eachName]=ages[x]
    x=x+1
print(dic)