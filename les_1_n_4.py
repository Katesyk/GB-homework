n = int(input('Введите целое положительное число:'))
greatest_dig = 0
while n > 0:
    digit = n % 10
    if digit > greatest_dig:
        greatest_dig = digit
        if greatest_dig == 9:
            break
    n = n // 10
print("Наибольшая цифра в числе = ", greatest_dig)
