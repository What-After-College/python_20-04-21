# 5! = 5*4*3*2*1 = 120

# n = int(input("Enter number "))
# val=1
# for x in range(2,n+1):
#     val*=x

# print(val)    

"""
1 * 1 = 1
1 * 2 = 2
2 * 3 = 6
6 * 4 = 24
24 * 5 = 120
"""

# def fact():
#     n = int(input())
#     var = 1
#     for x in range(2,n+1):
#         var*=x

#     return var    


# if __name__ == "__main__":
#     print(fact())

# 3628800

"""
nC2 ---> n!  
         2! = 2
         n-2! 

         n!/((n-r)!*r!)

"""         


# ls = [23,4,5,8]
# print(sum(ls))
# print(max(ls))
# print(min(ls))

# inp = input()
# l = inp.split()
# print(l)

ls = [1,4,57,6,3,0]
ls.sort()
print(ls)
# ls.sort(reverse=True)
# print(ls)
ls.reverse()
print(ls)