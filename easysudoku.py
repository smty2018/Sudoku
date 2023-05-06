a=["A", 3,  5,  2, 6, "B", 7, 8,"C" ]
b=[ 6, "D", 2,  5, "E", 1, 4, 9, "F"]
c=[ 1,  9, "G", 8, 3, "H", 5, 6, "I"]
d=["J", 2, 6, "K", 9, 5, "L", 4, 7]
e=[3, "M", 4, 6, "N", 2, 9, "O", 5]
f=[9, "P", 1, 7, "Q", 3, 6, 2,"R"]
g=[5, 1, "S", 3, 2, 6, "T", 7, "U"]
h=[ 2, "V", 8,  9, "W", 7, 1, 3,"X"]
i=["Y", 6, "Z", 4, "$", 8, 2, 5, 9 ]
l=[a,b,c,d,e,f,g,h,i]

print("EASY")
print("Arizona Daily Wildcat: Tuesday, Jan 17th 2006\n")
print("+-------------------------------+")
print("Skillset: {}".format(a))
print('Skillset: {}'.format(b))
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print("+--------------------------------+\n")


dash = '-' * 40

for i in range(len(l)):
    if i == 0:
      print(dash)
      print("|"+'{:<10s}{:>4s}{:>12s}{:>12s}'.format(l[i][0],l[i][1],l[i][2],l[i][3]))
      print(dash)
    else:
      print('{:<10s}{:>4d}{:^12s}{:>12.1f}'.format(l[i][0],l[i][1],l[i][2],l[i][3]))

print("which value you want to enter first?\n")
print("1. A")
print("2. B")
print("3 .C")
print("4 .D")
print("5 .E")
print("6 .F")
print("7 .G")
print("8 .H")
print("9 .I")
print("10 J")
print("11.K")
print("12.L")
print("13.M")
print("14.N")
print("15.O")
print("16.P")
print("17.Q")
print("18.R")
print("19.S")
print("20.T")
print("21.U")
print("22.V")
print("23.W")
print("24.X")
print("25.Y")
print("26.Z")
print("27.$")






  

