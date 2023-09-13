str1="Time is 10"
a=str1.split()[::-1]
l= []
for i in a:
    l.append(i)
print(" ".join(l))