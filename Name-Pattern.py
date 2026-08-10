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
                    if (ii == 0 and ij > 0 and ij < 6) or ii == 3 or (ij == 0 and ii > 0) or (ij == 6 and ii > 0):
                        temp += "* "
                    else:
                        temp += "  "
                a.append(temp)

        case 'B':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 0 and ij < 6) or ii == 3 or (ii == 6 and ij < 6) or ij == 0 or (ij == 6 and ii > 0 and ii < 6):
                        temp += "* "
                    else:
                        temp += "  "
                b.append(temp)
        
        case 'C':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 0 and ij > 0) or (ii == 6 and ij > 0) or (ij == 0 and ii > 0 and ii < 6):
                        temp += "* "
                    else:
                        temp += "  "
                c.append(temp)
        
        case 'D':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 0 and ij < 6) or (ii == 6 and ij < 6) or ij == 0 or (ij == 6 and ii > 0 and ii < 6):
                        temp += "* "
                    else:
                        temp += "  "
                d.append(temp)
        
        case 'E':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == 0 or ii == 6 or ii == 3 or ij == 0:
                        temp += "* "
                    else:
                        temp += "  "
                e.append(temp)
        
        case 'F':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == 0 or ii == 3 or ij == 0:
                        temp += "* "
                    else:
                        temp += "  "
                f.append(temp)
        
        case 'G':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 0 and ij > 0) or (ii == 3 and ij > 2 and ij < 6) or (ii == 6 and ij > 0 and ij < 6) or (ij == 0 and ii > 0 and ii < 6) or (ij == 6 and ii > 3 and ii < 6):
                        temp += "* "
                    else:
                        temp += "  "
                g.append(temp)
        
        case 'H':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == 3 or ij == 0 or ij == 6:
                        temp += "* "
                    else:
                        temp += "  "
                h.append(temp)
        
        case 'I':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == 0 or ii == 6 or ij == 3:
                        temp += "* "
                    else:
                        temp += "  "
                i.append(temp)
        
        case 'J':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 6 and ij > 0 and ij < 6) or (ii > 3 and ij == 0 and ii < 6) or (ij == 6 and ii < 6):
                        temp += "* "
                    else:
                        temp += "  "
                j.append(temp)
                
        case 'K':
            for ii in range(4,0,-1):
                temp = ""
                for ij in range(7):
                    if ij == ii or ij == 0:
                        temp += "* "
                    else:
                        temp += "  "
                k.append(temp)
            for ii in range(5):
                temp = ""
                if ii < 2:
                    continue
                for ij in range(7):
                    if ij == ii or ij == 0:
                        temp += "* "
                    else:
                        temp += "  "
                k.append(temp)
        
        case 'L':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 6 and ij < 6) or ij == 0:
                        temp += "* "
                    else:
                        temp += "  "
                l.append(temp)
        
        case 'M':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii < 4 and ii == ij and ij < 4) or (ii < 3 and 7 - ii - 1 == ij and ij > 3) or (ij == 0 and ii > 0) or (ij == 6 and ii > 0):
                        temp += "* "
                    else:
                        temp += "  "
                m.append(temp)
        
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
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 0 and ij > 0 and ij < 6) or (ii == 6 and ij > 0 and ij < 6) or (ij == 0 and ii > 0 and ii < 6) or (ij == 6 and ii > 0 and ii < 6):
                        temp += "* "
                    else:
                        temp += "  "
                o.append(temp)
        
        case 'P':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 0 and ij < 6) or (ii == 3 and ij < 6) or ij == 0 or (ij == 6 and ii < 3 and ii > 0):
                        temp += "* "
                    else:
                        temp += "  "
                p.append(temp)
        
        case 'Q':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 0 and ij > 0 and ij < 6) or (ii > 2 and ii == ij) or (ii == 6 and ij > 0 and ij < 5) or (ij == 0 and ii > 0 and ii < 6) or (ij == 6 and ii > 0 and ii < 5):
                        temp += "* "
                    else:
                        temp += "  "
                q.append(temp)
        
        case 'R':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 0 and ij < 6) or (ii > 3 and ii == ij) or (ii == 3 and ij < 6) or ij == 0 or (ij == 6 and ii > 0 and ii < 3):
                        temp += "* "
                    else:
                        temp += "  "
                r.append(temp)
        
        case 'S':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 0 and ij > 0 and ij < 6) or (ii == 3 and ij > 0 and ij < 6) or (ii == 6 and ij > 0 and ij < 6) or (ij == 0 and ii > 0 and ii < 3) or (ij == 6 and ii > 3 and ii < 6):
                        temp += "* "
                    else:
                        temp += "  "
                s.append(temp)
        
        case 'T':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == 0 or ij == 3:
                        temp += "* "
                    else:
                        temp += "  "
                t.append(temp)
        
        case 'U':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 6 and ij > 0 and ij < 6) or (ij == 0 and ii < 6) or (ij == 6 and ii < 6):
                        temp += "* "
                    else:
                        temp += "  "
                u.append(temp)
                
        case 'V':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == 0 and (ij == 0 or ij == 6)) or (ii == 2 and ii > 1 and (ij == 1 or ij == 5)) or (ii == 4 and ii > 3 and (ij == 2 or ij == 4)) or (ij == 3 and ii == 6):
                        temp += "* "
                    else:
                        temp += "  "
                v.append(temp)
        
        case 'W':
            for ii in range(7):
                temp = ""
                for ij in range(6,-1,-1):
                    if ij == 6 or ij == 0 or (ii == ij and ii > 2) or (ij == 6 - ii and ii > 3):
                        temp += "* "
                    else:
                        temp += "  "
                w.append(temp)
                
        case 'X':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == ij or (ij == 6 - ii):
                        temp += "* "
                    else:
                        temp += "  "
                x.append(temp)
                
        case 'Y':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if (ii == ij and ii < 3) or (ij == 6 - ii and ii < 4) or (ii > 3 and ij == 3):
                        temp += "* "
                    else:
                        temp += "  "
                y.append(temp)
                
        case 'Z':
            for ii in range(7):
                temp = ""
                for ij in range(7):
                    if ii == 0 or ii == 6 or (ij == 6 - ii):
                        temp += "* "
                    else:
                        temp += "  "
                z.append(temp)

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
