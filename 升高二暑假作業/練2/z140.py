print('Inside' if (lambda x, y: (x-5)**2+(y-6)**2 <=15**2)(*[int(input()) for i in range(2)]) else 'Outside')