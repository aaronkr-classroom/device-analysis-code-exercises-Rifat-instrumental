#data-tupes.py
a = 10
b = 3.14
c = "hello"
d = True

print (f"{a} is a {type(a)}")
print (f"{b} is a {type(b)}")
print (f"{c} is a {type(c)}")
print (f"{d} is a {type(d)}")

# str
e = 'Sinha'
f = 'Rabindra'
name = e + " " + f

g = name + "said, \"It's a beautiful day!"
h = ' " How \'ya doin\' today?"\n\t"Good!"'
print(g, "\n", h)

# Bool - only False or 0 or "" is False
i = True
j = False
k = bool(-1)
l = bool(a)
m = bool("")
n = bool(0)
o = bool(g)

print(i,j,k,l,m,n,o)