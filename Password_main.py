import random
letters = [chr(x) for x in range(ord('a'),ord('z')+1)]
numbers = [x for x in range(0,10)]
symbols = ['#','&','!','+','-','*','%']
password = []
number_of_letters = int(input("Enter number of letters you want? "))
number_of_digits = int(input("Enter number of digits you want? "))
number_of_symbols = int(input("Enter number of symbols you want? "))
for i in range(number_of_letters):
    ch = random.choice(letters)
    password.append(ch)
    letters.remove(ch)
for i in range(number_of_symbols):
    ch = random.choice(symbols)
    password.append(ch)
    symbols.remove(ch)
for i in range(number_of_digits):
    ch = random.choice(numbers)
    password.append(ch)
    numbers.remove(ch)
random.shuffle(password)
result_password = ""
for ch in password:
    result_password += str(ch)
print(f"Your Password can be {result_password}")
