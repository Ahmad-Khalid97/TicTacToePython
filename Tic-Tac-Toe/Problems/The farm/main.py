money = int(input())
chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

if money >= sheep:
    print(str(int(money / sheep)) + " sheep")
elif cow <= money <= sheep:
    print(str(int(money / cow)) + " cow")
elif pig <= money <= cow and int(money / pig) == 1:
    print(str(int(money / pig)) + " pig")
elif pig <= money <= cow and int(money / pig) > 1:
    print(str(int(money / pig)) + " pigs")
elif goat <= money <= pig:
    print(str(int(money / goat)) + " goat")
elif chicken <= money <= goat and int(money / chicken) == 1:
    print(str(int(money / chicken)) + " chicken")
elif chicken <= money <= goat and int(money / chicken) > 1:
    print(str(int(money / chicken)) + " chickens")
else:
    print("None")
