height = float(input('身長をm単位で入力してください> '))
weight = float(input('体重をkg単位で入力してくだいさい> '))
BMI = weight/(height**2)
if BMI < 18.5:
  c = '痩せ型'
elif BMI < 25:
  c = '標準型'
elif BMI < 30:
  c = '肥満'
else:
  c = '高度肥満'
print('BMI=' + str(BMI) + '\nあなたは' + c)