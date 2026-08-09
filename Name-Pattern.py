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

temp = 0

for i in range(7):
    if choice[temp] == 'A':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'C':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'D':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'E':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'F':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'G':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'H':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'I':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'J':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'K':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'L':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'M':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'N':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'O':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'P':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'Q':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'R':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'S':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'T':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'U':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'V':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'W':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'X':
        print(a[i], end="    ")
        temp += 1
    elif choice[temp] == 'Y':
        print(a[i], end="    ")
        temp += 1
    else:
        print(a[i], end="    ")
        temp += 1
