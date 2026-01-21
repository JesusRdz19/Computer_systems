info_charly = {"name": "Chuy",
               "age": 20,
               "adress": "18 O.R.",
               "Salary": 1500,
               "Married": False}

print(info_charly["name"])
print(info_charly.keys())
print(info_charly.values())

for key, value in info_charly.items():
    print(key,value)
    