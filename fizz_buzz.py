from num2words import num2words

list_of_nums = []
for number in range(1, 1001):
    num = num2words(number).replace("-", "").replace(" ", "")
    list_of_nums.append(num)
print("\n".join(list_of_nums))
print(sum(len(i) for i in list_of_nums))