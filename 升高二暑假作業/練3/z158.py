n = sum( [ 1/(i**0.5+(i+1)**0.5) for i in range(1,int(input())) ] )

print( f'{n*10000//1/10000 + (n*10000%1>=0.5)*0.0001:.4f}' )