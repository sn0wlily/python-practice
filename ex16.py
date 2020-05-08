i = 0
sum = 0
while 1:
  x = int(input('データ入力（負の数で終了）>'))
  if x < 0:
    break
  sum += x
  i += 1
print('データ数:' + str(i) + ' 合計:' + str(sum) + ' 平均:' + str(sum/i))
