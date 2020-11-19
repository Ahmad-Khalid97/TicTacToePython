text = input()
large_cafe = ""
large_cat_count = 0

while text != "MEOW":
    text = text.split()
    if int(text[1]) > large_cat_count:
        large_cafe = text[0]
        large_cat_count = int(text[1])
    text = input()
print(large_cafe)
