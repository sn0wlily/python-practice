x = int(input('10進数> '))
z = 0
while x > 0:
  y = x % 2
  z = z * 10 + y
  x = x // 2#正数解は//
print(str(z))

