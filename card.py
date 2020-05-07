x = int(input())
for i in range(x):
  n = int(input())
  s = [0,0,0,0]
  s[0] = n // 1000
  n = n % 1000
  s[1] = n // 100
  n = n % 100
  s[2] = n // 10
  n = n % 10
  s[3] = n
  max = 0
  c = 0
  for j in range(1,10):
    x = s.count(j)
    if x == 2:
      c += 1 
    if x > max:
      max = x
  if max == 4:
    print('four card')
  elif max == 3:
    print('three card')
  elif max == 1:
    print('one card')
  else:
    if c == 1:
      print('two card')
    else:
      print('two pair')

