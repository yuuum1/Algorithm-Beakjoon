A = int(input())
B = int(input())

print(A * (B%10))
print(int(A * (((B%100)-(B%10))/10)))
print(int(A * ((B-(B%100))/100)))

print(A * B)