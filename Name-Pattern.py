name = input("Enter Name: ").upper()

choice = []

for ii in name:
    choice.append(ii)

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
l = []
m = []
n = []
o = []
p = []
q = []
r = []
s = []
t = []
u = []
v = []
w = []
x = []
y = []
z = []

for ii in choice:
    match (ii):
        case 'A':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == 0 or ii == 3 or ij == 0 or ij == 6:
                        temp += "* "
                    else:
                        temp += "  "
                a.append(temp)

        case 'B':
            continue
        
        case 'C':
            continue
        
        case 'D':
            continue
        
        case 'E':
            continue
        
        case 'F':
            continue
        
        case 'G':
            continue
        
        case 'H':
            continue
        
        case 'I':
            continue
        
        case 'J':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == 6 or (ii > 3 and ij == 0) or ij == 6:
                        temp += "* "
                    else:
                        temp += "  "
                j.append(temp)
                
        case 'K':
            continue
        
        case 'L':
            continue
        
        case 'M':
            continue
        
        case 'N':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == ij or ij == 0 or ij == 6:
                        temp += "* "
                    else:
                        temp += "  "
                n.append(temp)
                
        case 'O':
            continue
        
        case 'P':
            continue
        
        case 'Q':
            continue
        
        case 'R':
            continue
        
        case 'S':
            continue
        
        case 'T':
            continue
        
        case 'U':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == 6 or ij == 0 or ij == 6:
                        temp += "* "
                    else:
                        temp += "  "
                u.append(temp)
                
        case 'V':
            continue
        
        case 'W':
            continue
        case 'X':
            continue
        case 'Y':
            continue
        case 'Z':
            continue

print()
print("Name: ",name)
print()
print(f"{"="*30} {name} {"="*30}")
print()

for ii in range(7):

    for temp in choice:

        if temp == 'A':
            print(a[ii], end="    ")

        if temp == 'B':
            print(b[ii], end="    ")

        if temp == 'C':
            print(c[ii], end="    ")

        if temp == 'D':
            print(d[ii], end="    ")

        if temp == 'E':
            print(e[ii], end="    ")

        if temp == 'F':
            print(f[ii], end="    ")

        if temp == 'G':
            print(g[ii], end="    ")

        if temp == 'H':
            print(h[ii], end="    ")

        if temp == 'I':
            print(i[ii], end="    ")

        if temp == 'J':
            print(j[ii], end="    ")

        if temp == 'K':
            print(k[ii], end="    ")

        if temp == 'L':
            print(l[ii], end="    ")

        if temp == 'M':
            print(m[ii], end="    ")

        if temp == 'N':
            print(n[ii], end="    ")

        if temp == 'O':
            print(o[ii], end="    ")

        if temp == 'P':
            print(p[ii], end="    ")

        if temp == 'Q':
            print(q[ii], end="    ")

        if temp == 'R':
            print(r[ii], end="    ")

        if temp == 'S':
            print(s[ii], end="    ")

        if temp == 'T':
            print(t[ii], end="    ")

        if temp == 'U':
            print(u[ii], end="    ")

        if temp == 'V':
            print(v[ii], end="    ")

        if temp == 'W':
            print(w[ii], end="    ")

        if temp == 'X':
            print(x[ii], end="    ")

        if temp == 'Y':
            print(y[ii], end="    ")

        if temp == 'Z':
            print(z[ii], end="    ")

    print()
