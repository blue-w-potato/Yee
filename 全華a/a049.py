# 之前用爆力解
# a=int(input())
# b='@--'*a
# if a==1:
#     print('@')
# for i in range(0,a):
#     print(f'{b}'[3-i%3:3-i%3+a])

a=int(input())
for i in range(a):
    for j in range(a):
        if i%3 == j%3:
            print('@',end='')
        else:
            print('-',end='')
    print()