'''
def uniqueCharacters(str):       
    for i in range(len(str)): 
        for j in range(i + 1,len(str)):  
            if(str[i] == str[j]): 
                return False   
    return True     
# Driver Code 
str = "Protiijaayiiii"   
if(uniqueCharacters(str)): 
    print("The String ", str," has all unique characters") 
else: 
    print("The String ", str, " has duplicate characters")

def fix(string):
    s = set()
    list = []
    for ch in string:
        if ch not in s:
            s.add(ch)
            list.append(ch)

    return ''.join(list)        

string = "Protiijaayiiii"
print(fix(string))
'''
'''
def seg0s1s(A):
   n = ([i for i in A if i==0] + [i for i in A if i==1])
   print(n)

if __name__ == "__main__":
   A=list()
   n=int(input("Enter the size of the array ::"))
   print("Enter the number ::")
   for i in range(int(n)):
      k=int(input(""))
      A.append(int(k))
   print("The New ArrayList ::")    
   seg0s1s(A)
'''
'''
def seg0s1s(A):
      n=([i for i in A if i==0] +[i for i in A if i==1])
      print(n)
if __name__=="__main__":
     A=list()
     n=int(input("enter the size of array::"))
     print("Enter the number ::")
     for i in range(int(n)):
          k=int(input(""))
          A.append(int(k))
     print("the new array")
     seg0s1s(A)
'''
'''
s=input()

b=[]

for i in s:

    if i not in b:

        b.append(i)

for i in b:

    print(i,end="")

'''
'''
n=int(input())
c,a=0,[]
for i in range(0,n+1):
    b=[]
    for j in range(0,n+1):
        if j<=i:
            b.append(" ")
        else:    
            c+=1
            b.append(c)
    a.append(b)
for r in range(len(a)):
    for c in range(len(a)):
        print(a[c][r],end=" ")
    print()
'''
'''
n=int(input())
c,a=0,[]
for i in range(0,n+1):
     b=[]
     for j in range(0,n+1):
          if j<=i:
               b.append(" ")
          else:
               c+=1
               b.append(c)
     a.append(b)
for r in range(len(a)):
     for c in range(len(a)):
          print(a[c][r],end=' ')
     print()
'''
'''
s=input()
c,b=0,[]
for i in s:
       if i not in b:
              b.append(i)
       else:
              c=1
print()
if c==0:
       print("Unique characters")
else:
      print("Not Unique characters")
for i in b:
       print(i,end="")

'''
'''
s=input()
c,b=0,[]
for i in s:
     if i not in b:
          b.append(i)
     else:
          c=1
#print()
if c==0:
     print("Unique character")
else:
     print("Not Unique character")
for i in b:
     print(i,end='')
'''
'''
s=input()
c,b=0,[]
for i in s:
     if i not in b:
          b.append(i)
     else:
          c=1
if c==0:
     print("Unique character")
else:
     print("Not Unique character")
for i in b:
     print(i,end='')
'''
'''
n=int(input())
a=[]
for j in range(n):
    a.append(int(input()))
b,c=[],[]
for i in a:
    if i==0:
        b.append(i)
    else:
        c.append(i)

b=b+c
print(b)             
'''
'''
def seg0s1s(A):
      n=([i for i in A if i==0] +[i for i in A if i==1])
      print(n)
if __name__=="__main__":
     A=list()
     n=int(input("enter the size of array::"))
     print("Enter the number ::")
     for i in range(int(n)):
          k=int(input(""))
          A.append(int(k))
     print("the new array")
     seg0s1s(A)
'''
'''
n=int(input())
a=[]
for j in range(n):
     a.append(int(input()))
b,c=[],[]
for i in a:
     if i==0:
          b.append(i)
     else:
          c.append(i)
b=b+c
print(b)
'''
'''
#prod of subarray of aray
a=[10,3,7]
p=1
for i in range(len(a)):
     for j in range(i,len(a)):
          for k in range(i,j+1):
               p=p*a[j]
print(p)
'''
'''
b=input()
a=b.split( )
c=[]
for i in range(len(a)):
     s=1
     for j in range(i+1,len(a)):
          if a[i]==a[j]:
               s+=1
     if a[i] not in c:
          c.append(a[i])
          c.append(s)
               
print(c)
'''
'''
0000
0110
0110
0000
'''
'''
a=int(input())
for i in range(a):
     if i==0:
          print('0'*a)
          print()
     if i>=1 and i<=(a-2):
          print('0'*1,'1'*(a-2),'0'*1,sep='')
          print()
     if i==(a-1):
          print('0'*a)
          print()

'''
'''
a='1'
b='3'
c=a+b
print('3.6'+'5.8')
a=[1,2,3,4,6,7,8,9,0]
b=[5,6]
a.extend(b)
a.extend('3')
print(a[-1:4])   
'''
'''
a=set('pythob','lkj')
print(a)
'''
'''
a={1,2,3,4}
a.update([8,0])
print(a)
'''
'''
#ques2 fund course
a=int(input())
if a==1:
    print('Sunday')    
if a==2:
    print('Monday')
if a==3:
    print('Tuesday')
if a==4:
    print('Wednesday')
if a==5:
    print('Thursday')
if a==6:
    print('Friday')
if a==7:
    print('Saturday')
if a>7:
    print('Invalid')
'''
'''
#ques 2II
a=int(input())
if a%3 ==0 and a%5==0:
    print('Number is divisible by 3 and 5 both')
elif a%3 ==0:
    print('Number is divisible by 3 only')
elif a%5 ==0:
    print('Number is divisible by 5 only')
elif a%3!=0 and a%5!=0 :
    print('Number is not divisible by either 3 or 5')
'''
'''
#ques3 minmax
b=[]
for i in range(0,5):
    a=int(input())
    b.append(a)
print(b)
a=c=b[0]
for j in range(1,len(b)):    
    if a>b[j]:
        a=b[j]
    if c<b[j]:
        c=b[j]

print(a,c)

#ques3 linear search

b=[]
for i in range(0,5):
    a=int(input())
    b.append(a)
print(b)
key=int(input('key value'))
f=0
for i in range(len(b)):
    if key==b[i]:
        print(key)
        f=1
'''
'''
#ques3 binary search 
def binarySearch (arr,key,low,high): 

	# Check base case 
	if high >=low: 

		mid = low + (high - low) // 2

		# If element is present at the middle itself 
		if arr[mid] == key: 
			return mid 
		
		# If element is smaller than mid, then it 
		# can only be present in left subarray 
		elif arr[mid] > key: 
			return binarySearch(arr,key,low, mid-1) 

		# Else the element can only be present 
		# in right subarray 
		else: 
			return binarySearch(arr,key,mid + 1,high) 

	else: 
		# Element is not present in the array 
		return -1

# Driver Code 
arr = [2, 3, 43,2,1,4, 10,33,21,67, 40] 
key = 10

# Function call 
result = binarySearch(arr, key, 0,len(arr)-1) 

if result != -1: 
	print ("Element is present at index % d" % result) 
else: 
	print ("Element is not present in array") 
'''
'''
def my(couse='ll'):
    #couse='pp'
    print(couse)
my('oo')
'''

'''
Assignment Question 1.
 CARGO EXPRESS is a full-time courier and cargo dispatch agency for corporate companies around the world. It mainly deals with delivering and tracking the packages delivered. TRON EXPRESS has its annual budget session during the end of year. The company has more than 30,000 full-time employees, 5,00,000 customers per month, and an average of 3 million packages a day. The manner in which the company structures pay scales is different for permanent and temporary staff. Some of the criteria which the company uses to decide the pay are as follows: 
1. Number of packages being delivered: Permanent employees get $50 for every package they deliver, whereas temporary employees get $30 for every delivered package.
 2. The distance they travel: Permanent employees get a daily allowance of $75 for their travel. Similarly, temporary employees get a daily allowance of $65 for their travel.
3. Shifts: People who work for the night shift get an additional pay of 10% over and above their regular pay.
 Depending on all these factors, the basic pay structure is decided. 
Now, the company wants to reward the employees with bonuses based on their grade as follows: (Assume that grade is provided as input.) 
Grade A1: 5% of basic pay 
Grade A2: 10% of basic pay 
Grade A3: 15% of basic pay 

With all the information provided, use all possible type of statements and expressions and design a Python program to help the management to calculate the net pay (basic added to bonus) for employees. 
Hint: Make use of if-else, switch case, and arithmetic operators. Test the output by compiling the program and executing the same through Python IDLE/Jupyter.

Permanent= Basicsalary-5000
Temp = Basic_Sal - 3000
'''
a=input('Enter temperary or permanent')
n=0

if a=='temp':
        n=3000
        print('salary',n)
        
elif a=='perm':
        n=5000
        print('salary',n)




'''
#find factors of an entered Number
a=int(input())
if a==0:
        print('Factor of the number is 0')
else:
        for i in range(1,a+1):
                if a%i==0:                
                        print('Factor of the number is:',i)
                        
        
#input a number
#if input number ==0
#display/print factor of the number is 0
#for i In range from 1 to number+1
#start that loop with one and take it upto (input number +1)
#if reminder =0
#display that number

#program to check whether the entered number is PRIME or not
a=int(input())
flag=0
if a<=1:
        print('Number is not prime')
else:
        for i in range(2,a):
                if a%i==0:
                        flag+=1
                
        if flag==0:
                print('Number is not prime:',a)
        else:
                print('Number is prime:',a)
'''
'''
#sorting
a=[0,21,13,4,121,43,1111,12,3,1]
for i in range(0,len(a)):
        for j in range(i+1,len(a)):
                if a[i]>a[j]:
                        temp=a[i]
                        a[i]=a[j]
                        a[j]=temp
print(a)

'''
'''
#insertion sort
#a=[4,3,2,10,12,1,5,6]
a=[5,4,10,1,6,2]
for i in range(1,len(a)):
        #print('a[i]',a[i])
        flag=0
        temp=a[i]
        for j in range(i,-1,-1):
                #print('a[j]',a[j])
                
                #print('p',a[i])
                #print('temp',temp)
                if temp<a[j]:
                        #print('o',a[j])                       
                        a[j+1]=a[j]
                        print(a)
                        flag+=1
                        #print('flag',flag)
        else:
                if flag==0:
                        continue
                else:                   
                        a[i-flag]=temp
                        print(a)
'''
'''
#insertion sort
a=[5,4,10,11,77,21,1,6,2]
for i in range(1,len(a)):
    temp=a[i]
    j=i-1
    while(j>=0 and a[j]>temp):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp
print(a)
'''           
#Write the code in any programming language to display the largest element, smallest element and the difference between the position of these two elements.
#minmax
#sorted array
'''
a=[0,21,13,4,121,43,1111,12,3,1]
for i in range(0,len(a)):
        for j in range(i+1,len(a)):
                if a[i]>a[j]:
                        temp=a[i]
                        a[i]=a[j]
                        a[j]=temp
print(a)
min1=a[0]
max2=a[len(a)-1]
print(min1,max2)

'''
#unsorted array
b=[]
for i in range(0,5):
    a=int(input())
    b.append(a)
print(b)
a=c=b[0]
for j in range(1,len(b)):    
    if a>b[j]:
        a=b[j]
        ind=j
      
    if c<b[j]:
        c=b[j]
        ind1=j
        
print('index of minimum no:',ind,'minimum no',a)
print('index of maximum no:',ind1,'maximum no',c)
                
#Factorial value of entered number using Procedure call
a=int(input())
b=1
for i in range(a,0,-1):
    #print('i',i)
    b=b*i
    #print(b)
print(b)










                        






































