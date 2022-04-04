string=input("Nhap chuoi")
new_arr= []
for char in string:
    if (char.isalnum() == True):
        new_arr.append(char)

new_string = ''.join(new_arr)
print(new_string)
        
