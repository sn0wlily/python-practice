year = int(input('西暦で年を入力してください> '))
if year % 400 == 0:
  i = 1
elif year % 100 == 0:
  i = 0
elif year % 4 == 0:
  i = 1
else:
  i = 0

if i == 0:
  print(str(year) + '年はうるう年ではありません')
else:
  print(str(year) + '年はうるう年です')
