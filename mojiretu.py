x = int(input())
n = input() #ai
for k in range(x):
  s = input() #paiza
  for i in range(len(n)): #ai
    for j in range(len(s)): #paiza
      if s[j] != n[i+j]:
        break
    if j == len(s)-1:
      print(s)



