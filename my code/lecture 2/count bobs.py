counter = 0

s = str(input("Please type a string of characters: "))

a=0

for index,character in enumerate(s):
    z = s[a:a+3]
    a+=1
    if z == ('bob'):
       counter +=1
print ('Number of times bob occurs is:', counter)
