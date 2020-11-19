ss = input()
if "_" in ss:
    print(ss.replace("_", " ").title().replace(" ", ""))
else:
    print(ss.capitalize())
