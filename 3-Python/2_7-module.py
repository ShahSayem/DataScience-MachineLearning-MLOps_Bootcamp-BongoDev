from datetime import datetime, timedelta
import my_math_module as mmm

today = datetime.now()
print(today)

print(datetime.hour)

yesterday = today - timedelta(days=1)
print(yesterday)


res_1 = mmm.add(5, 3)
res_2 = mmm.subtract(5, 3)
res_3 = mmm.multiply(5, 3)
res_4 = mmm.divide(5, 3)

print(res_1)
print(res_2)
print(res_3)
print(res_4)