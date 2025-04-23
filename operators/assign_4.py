
#assignment - 4
password = input("enter a password:")
special_characters = '@' in password or '#' in password or '$' in password or '%' in password or '&' in password and ' '  not in password
if special_characters:
    print("valid password: True")
else:
    print("valid password: False")

