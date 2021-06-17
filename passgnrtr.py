
# password generator
import random

password_dict = {}

numbers = [0,1,2,3,4,5,6,7,8,9]
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['@','!','*','&','^','$','#','(',')']

website = input("for which site you want to generate Password? ")

nmr_letter = int(input("Enter the number of letters in your password: "))
nmr_alpha = int(input("Enter the number of alphabets in your password: "))
nmr_digits = int(input("Enter the number of letters in your password: "))
nmr_symbols = int(input("Enter the number of letters in your password: "))

total = nmr_alpha+nmr_digits+nmr_symbols
if nmr_letter <total :
    print(f"total exceeded to {total}")
elif nmr_letter > total:
    print(f"total reduced to {total}")
password =""

for i in range(nmr_alpha):
    element = random.choice(letters)
    password+= element

for i in range(nmr_symbols):
    element = random.choice(symbols)
    password+= element

for i in range(nmr_digits):
    element = random.choice(numbers)
    password+= str(element)

new = list(password)
random.shuffle(new)
new_pass = "".join(new)

password_dict[website] = new_pass
print(f"password for the site {website} is: {new_pass}")
