A = input()
B = input()
H = input()

if int(A) <= int(H) <= int(B):
    print("Normal")
elif int(H) > int(B):
    print("Excess")
else:
    print("Deficiency")
