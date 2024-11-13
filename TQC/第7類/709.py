a = {}
while True:
    k = input('Key: ')
    if k == 'end':break
    a[k] = input('Value: ')
    
for i in sorted(a.keys()):
    print(f'{i}: {a[i]}')