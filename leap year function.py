def f1(year):

   return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

print(f1(2100))