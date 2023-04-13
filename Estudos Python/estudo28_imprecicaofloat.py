import decimal

float_1_d = decimal.Decimal('0.33')
float_2_d = decimal.Decimal('0.66')
float_total_d = float_1_d + float_2_d

float_1 = 0.75
float_2 = 0.25
float_total = float_1 + float_2

print(float_total)
print(round(float_total, 3))
print(float_total_d)