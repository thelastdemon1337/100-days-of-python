import string, random

letters = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to Tarun's PyPassword Generator!")
letter_cnt = int(input("How many letters would you like in your password?\n"))

symbol_cnt = int(input("How many symbols would you like?\n"))

number_cnt = int(input("How many numbers would you like?\n"))

password = ""

for i in range(letter_cnt):
  password += letters[random.randint(0,len(letters)-1)]

for i in range(symbol_cnt):
  password += random.choice(symbols)

for i in range(number_cnt):
  password += random.choice(numbers)

password = list(password)
random.shuffle(password)
password = ''.join(password)
print(f"Here is your password: {password}")