# def one_to_ten(n):
#     if n==1:
#         return 1
#     return one_to_ten(n-1)
# print(one_to_ten(5))
def one_to_ten(n):
    if n==1:
        print( 1)
    return one_to_ten(n-1)
print(one_to_ten(5))