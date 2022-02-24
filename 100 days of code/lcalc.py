# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1 + name2
combined_name = combined_name.lower()

i,j = 0,0

for cnt in "true":
    i += combined_name.count(cnt)
    

for cnt in "love":
    j += combined_name.count(cnt)


score = int(f"{i}{j}")
static_statement = f"Your score is {score}"
if(score < 10 or score > 90):
    print(static_statement + ", you go together like coke and mentos.")
elif(score > 40 and score < 50):
    print(static_statement + ", you are alright together.")
else:
    print(static_statement + ".")
