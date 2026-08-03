'''
*
* *
* * *
* * * *
* * * * *
'''

# r = 5
# for i in range(1 , r+1):
#     for j in range(1 , i+1):
#         print("*", end=" ")
#     print()

n = 5
for i in range(n):  
    for j in range(i):
        print("*", end=" ")
    print()

    
'''
* * * * *
* * * *
* * *
* *
*
'''
n = 5
# for i in range(n , 0 , -1):
for i in range(n):  
    for j in range(i, n):
        print("*", end=" ")
    print()