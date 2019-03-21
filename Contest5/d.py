import re

password = input()
strong = True

if re.search(r'anna', password.lower()) is not None:
    strong = False

if re.search(r'\d+', password) is None:
    strong = False

if password == password.lower() or password == password.upper():
    strong = False

if len(set(password)) < 4:
    strong = False

print('strong' if strong else 'weak')
