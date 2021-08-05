#!/usr/bin/env python
# coding: utf-8

# PP1 Write a program to create and store information in a text file.
# PP2 Write a program to read an entire text file, first n lines and last n lines.
# PP3 Write a program to read a file line by line store it into a variable as well as into list.
# PP4 Write a program to count the frequency of all words in a file.
# PP5 Write a program to copy the contents of a file to another file
# PP6 Write a program to remove newline characters from a file.


#PP1
a=open("Newfile.txt","a+")
a.write(input("What do you want to write: "))
a.close()


#PP2
c=open("Newfile.txt","r")
n=int(input("Enter a number: "))
d=c.readlines()[0:n]
print(d)


#PP3
e=open("Newfile.txt","r")
f=e.readlines()
print(f)
g=""
for x in f:
   g+=x
print(g)
e.close()

#PP4
h=open("Newfile.txt","r")
i=h.read()
i=list(i)
j=""
normalchars=list("1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm \n")
for x in i:
    if x not in normalchars:
        i.remove(x)
for x in i:
   j+=x
j=j.split()
l=list(set(j))
for x in l:
    print("Number of occurences of",x,"=",j.count(x))
h.close()


#PP5
j=input("Name of the file")
k=open("Newfile.txt","r")
l=k.read()
k.close()
m=open(j,"w")
m.write(l)
m.close()


#PP6
n=open("Newfile.txt","r+")
o=""
p=n.read().split("\n")
for x in p:
    o+=x
n.write(o)
n.close()


