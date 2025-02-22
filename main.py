def prints(n):
    if (n<=0):
     return n
    print("codingal")
    print("n/2")  #recursion
    print("n/2")  #recursion
#time complexity = O(nlogn)

#activity2

def su(n):
   return n*(n+1)/2
print(su(4))
#spce complexity = 1
#the space complexity will remain constant due to only 1 input

def arraysum(a):
       sum = 0
       for i in a:
           sum+=i
       return sum
a=[3,86,5,8]
print(arraysum(a))
#space  complexity= theta n
#oscillary space will increase due to array