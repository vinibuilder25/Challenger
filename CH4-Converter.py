money = float(input("Enter the cash: R$"))
def converter(value):
    value *= 100
    return value
print(f' You have R${converter(money)} cents')