'''
* 
* * 
* * * 
* * * * 
* * * * *
''' 

n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        
        print("*",end=" ")
    print()
    
'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

n=int(input("n:"))
for i in range(n):
   for j in range(i,n):
       print("*",end=" ")
   print()
   
'''
* * * * * 
    * * * * 
      * * * 
        * * 
          *
 '''

n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
    
'''    
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
'''

n=int(input("n:"))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
    
'''

          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
'''


n=int(input("n:"))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
    
'''

 * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
'''

n=int(input("n:"))
for i in range( n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

'''    
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
'''


n=int(input("n:"))
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range( n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
    
'''

        * * * * * 
      * * * * * 
    * * * * * 
  * * * * * 
* * * * * 
'''


n=int(input("n:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(n):
        print("*",end=" ")
    print()
    
'''

*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * *
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

'''

n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(2*(n-i-1)):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()    

for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for space in range(2*i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()    

