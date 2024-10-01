import random
# start

list_num: list[int] = [i for i in range(95, 105 + 1 , + 1)]
print(list_num)

list_num2: list[int] = [i  for i in range(10, 20 + 1 , + 2)]
print(list_num2)

list_true_false: list[int] = [random.choice([True, False]) for i in range(5)]
print(list_true_false)

list_ran_num: list[int] = [random.randint(1, 100) for i in range(10)]
print(list_ran_num)

list_ran_num_bigger_50: list[int] = [num for num in list_ran_num if num > 50]
print(list_ran_num_bigger_50)

list_mixed: list[int] = [num for num in [random.randint(1, 100) for _ in range(10)] if num > 50]
print(list_mixed)

sentence: str = (input('Enter a sentence: '))
list_word: list[str] = [letter for letter in sentence if letter != ' ' and letter != 't']
print(list_word)

list_random_num: list[int] = [random.randint(10, 99) for _ in range(10)]
print(list_random_num)
unit_digits: list[int] = [num // 10 for num in list_random_num]
print(unit_digits, end=" ")

# end
