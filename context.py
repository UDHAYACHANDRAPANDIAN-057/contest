n=input("Enter the String : ")
s=int(input("Enter the key : "))
result=""
for i in range(len(n)):
    char=n[i]
    if(char.isupper()):
        result+=chr((ord(char)+s-64)%26+65)
    else:
        result+=chr((ord(char)+s-96)%26+97)
print("Cipher :",result)
