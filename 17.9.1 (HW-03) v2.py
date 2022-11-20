array = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
number = int(input('Введите любое число из последовательности чисел: '))

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)

while number:
    if number not in array:
        print('Вы ввели число не входящее в последовательность чисел!')
        number = int(input('Введите любое число из последовательности чисел: '))
    else:
        break

def binary_search(array, number, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == number:
        return middle
    elif number < array[middle]:
        return binary_search(array, number, left, middle - 1)
    else:
        return binary_search(array, number, middle + 1, right)

input_number = (binary_search(array, number, 0, len(array)-1))

print('Номер позиции введенного числа в списке: ', input_number)
print('Номер позиции элемента списка, который меньше введенного числа: ', input_number-1)
print('Номер позиции элемента списка, который больше введенного числа: ', input_number+1)