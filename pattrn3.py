''''
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5

'''

# r = 6
# for i in range(1 , 6):
#     for j in range(1 , i+1):
#         print(j ,end=" ")
#     print()

'''-----------------------------------
1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''
# n = 6
# for i in range(n , 0 ,-1):
#     for j in range(1 , i+1):
#         print(j ,end=" ")
#     print()


'''-------------------------------------------------
5 5 5 5 5 
4 4 4 4 
3 3 3
2 2
1
'''
# n = 5
# for i in range(n , 0 , -1):
#     for j in range(1 , i+1 ):
#         print(i , end=" ")
#     print()

'''
5 4 3 2 1 
4 3 2 1 
3 2 1
2 1
1
'''
n = 5
for i in range(n , 0 , -1):
    for j in range(i , 0 , -1 ):
        print(j , end=" ")
    print()