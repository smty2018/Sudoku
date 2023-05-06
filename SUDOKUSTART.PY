print("+--------------------------+")
print("|   WELCOME  TO  SUDOKU    | ")
print("+--------------------------+")
print("| Please select an option! |")
print("|                          |")
print("| 1.Instructions           |")
print("| 2.Quit                   |")
print("+--------------------------+\n")

choice=int(input("enter your selection :"))

if choice==2:
    print("Thank You :) ")


else:
    print("+-------------------------------------------------------------------------------------------------------------------------------------+")
    print("|     INSTRUCTIONS                                                                                                                    | ")
    print("+-------------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                                                                                                     |")
    print("| 1.A standard Sudoku puzzle consists of a grid of 9 blocks.                                                                          |")
    print("| 2.Each block contains 9 boxes arranged in 3 rows and 3 columns.                                                                     |")
    print("| 3.There is only one valid solution to each Sudoku puzzle.                                                                           |")
    print("| 4.Each block contains 9 boxes arranged in 3 rows and 3 columns.                                                                     |") 
    print("| 5.When you start a game of Sudoku, some blocks will be pre-filled for you.                                                          |")
    print("| 6.Each column must contain all of the numbers 1 through 9 and no two numbers in the same column of a Sudoku puzzle can be the same. |")
    print("| 7.Each row must contain all of the numbers 1 through 9 and no two numbers in the same row of a Sudoku puzzle can be the same.       |")
    print("| 8.Each block must contain all of the numbers 1 through 9 and no two numbers in the same block of a Sudoku puzzle can be the same.   |")
    print("| 9.The characters like A,$,etc represent the blank spaces which need to be filled                                                    |")
    print("| 10.The values must be filled in sequentially                                                                                        |")
    print("| 11.The user will get 5 tries to fill one cell                                                                                       |")
    print("| 12.when the 5 chances are exhausted, the correct value will be filled automatically.                                                |")
    print("|                                                                                                                                     |")
    print("+-------------------------------------------------------------------------------------------------------------------------------------+\n")
 
    a=["A", 3,  5,  2, 6, "B", 7, 8,"C" ]
    b=[ 6, "D", 2,  5, "E", 1, 4, 9, "F"]
    c=[ 1,  9, "G", 8, 3, "H", 5, 6, "I"]
    d=["J", 2, 6, "K", 9, 5, "L", 4, 7]
    e=[3, "M", 4, 6, "N", 2, 9, "O", 5]
    f=[9, "P", 1, 7, "Q", 3, 6, 2,"R"]
    g=[5, 1, "S", 3, 2, 6, "T", 7, "U"]
    h=[ 2, "V", 8,  9, "W", 7, 1, 3,"X"]
    j=["Y", 6, "Z", 4, "$", 8, 2, 5, 9 ]
    dash = '-' * 70

    print("EASY")
    print("Arizona Daily Wildcat: Tuesday, Jan 17th 2006\n")

    for i in range(len(a)):
       if i==0:
         print(dash)
         print(dash)
         print('| '+'{:<3s}{:<1d}{:>4d}{:>5d}{:>12d}{:>5s}{:>12d}{:>12d}{:<10s}'.format(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8])+'| ')
         print(dash)
    for i in range(len(b)):
        if i==0:
      
         print('| '+'{:<3d}{:<1s}{:>4d}{:>5d}{:>12s}{:>5d}{:>12d}{:>12d}{:<10s}'.format(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8])+'| ')
         print(dash)      
    for i in range(len(c)):
        if i==0:
      
         print('| '+'{:<3d}{:<1d}{:>4s}{:>5d}{:>12d}{:>5s}{:>12d}{:>12d}{:<10s}'.format(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8])+'| ')
         print(dash) 
for i in range(len(d)):
    if i==0:
      
      print('| '+'{:<3s}{:<1d}{:>4d}{:>5s}{:>12d}{:>5d}{:>12s}{:>12d}{:<10d}'.format(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8])+'|')
      print(dash)
for i in range(len(e)):
    if i==0:
      
      print('| '+'{:<3d}{:<1s}{:>4d}{:>5d}{:>12s}{:>5d}{:>12d}{:>12s}{:<10d}'.format(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8])+'|')
      print(dash)      
for i in range(len(f)):
    if i==0:
      
      print('| '+'{:<3d}{:<1s}{:>4d}{:>5d}{:>12s}{:>5d}{:>12d}{:>12d}{:<10s}'.format(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8])+'|')
      print(dash)      
for i in range(len(g)):
    if i==0:
      
      print('| '+'{:<3d}{:<1d}{:>4s}{:>5d}{:>12d}{:>5d}{:>12s}{:>12d}{:<10s}'.format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8])+'|')
      print(dash)
for i in range(len(h)):
    if i==0:
      
      print('| '+'{:<3d}{:<1s}{:>4d}{:>5d}{:>12s}{:>5d}{:>12d}{:>12d}{:<10s}'.format(h[0],h[1],h[2],h[3],h[4],h[5],h[6],h[7],h[8])+'|')
      print(dash)      
for i in range(len(j)):
    if i==0:
      
      print('| '+'{:<3s}{:<1d}{:>4s}{:>5d}{:>12s}{:>5d}{:>12d}{:>12d}{:<10d}'.format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8])+'|')
      print(dash)
print(dash)      

c1=0
while c1<5:
        guess=int(input("enter the value for A "))
        if guess==4:
            a[0]=4
            print("correct")
            break
        else:
         c1=c1+1
if not c1<5:
          print("your chances are over :( . the correct answer For A is 4")
          a[0]=4            
         
c2=0
while c2<5:
        guess=int(input("enter the value for B "))
        if guess==9:
             a[5]=9
             print("correct")
             break
        else:
             c2=c2+1
if not c2<5:
       print("your chances are over :( . the correct answer For B is 9")
       a[5]=9      


c3=0
while c3<5:
        guess=int(input("enter the value for C "))
        if guess==9:
             a[5]=9
             print("correct")
             break
        else:
             c3=c3+1
if not c3<5:
       print("your chances are over :( . the correct answer For C is 9")
       a[5]=9


c4=0
while c4<5:
        guess=int(input("enter the value for D "))
        if guess==9:
             a[5]=9
             print("correct")
             break
        else:
             c4=c4+1
if not c4<5:
       print("your chances are over :( . the correct answer For D is 9")
       a[5]=9


c5=0
while c5<5:
        guess=int(input("enter the value for E "))
        if guess==9:
             a[5]=9
             print("correct")
             break
        else:
             c5=c5+1
if not c5<5:
       print("your chances are over :( . the correct answer For E is 9")
       a[5]=9


c6=0
while c6<5:
        guess=int(input("enter the value for F "))
        if guess==9:
             a[5]=9
             print("correct")
             break
        else:
             c6=c6+1
if not c6<5:
       print("your chances are over :( . the correct answer For F is 9")
       a[5]=9


c7=0
while c7<5:
        guess=int(input("enter the value for G "))
        if guess==9:
             a[5]=9
             print("correct")
             break
        else:
             c7=c7+1
if not c7<5:
       print("your chances are over :( . the correct answer For G is 9")
       a[5]=9


c8=0
while c8<5:
        guess=int(input("enter the value for H "))
        if guess==9:
             a[5]=9
             print("correct")
             break
        else:
             c8=c8+1
if not c8<5:
       print("your chances are over :( . the correct answer For H is 9")
       a[5]=9    
        
c9=0
while c9<5:
        guess=int(input("enter the value for I "))
        if guess==9:
             a[5]=9
             print("correct")
             break
        else:
             c9=c9+1
if not c9<5:
       print("your chances are over :( . the correct answer For I is 9")
       a[5]=9    
        
c10=0
while c10<5:
        guess=int(input("enter the value for J "))
        if guess==10:
             a[5]=10
             print("correct")
             break
        else:
             c10=c10+1
if not c10<5:
       print("your chances are over :( . the correct answer For J is 10")
       a[5]=10    


c11=0
while c11<5:
        guess=int(input("enter the value for K "))
        if guess==11:
             a[5]=11
             print("correct")
             break
        else:
             c11=c11+1
if not c11<5:
       print("your chances are over :( . the correct answer For K is 11")
       a[5]=11    

c12=0
while c12<5:
        guess=int(input("enter the value for L "))
        if guess==12:
             a[5]=12
             print("correct")
             break
        else:
             c12=c12+1
if not c12<5:
       print("your chances are over :( . the correct answer For L is 12")
       a[5]=12    
c13=0
while c13<5:
        guess=int(input("enter the value for M "))
        if guess==13:
             a[5]=13
             print("correct")
             break
        else:
             c13=c13+1
if not c13<5:
       print("your chances are over :( . the correct answer For M is 13")
       a[5]=13    

       
       





