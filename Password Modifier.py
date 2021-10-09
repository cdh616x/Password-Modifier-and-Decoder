word = input() + "!\n"
password = ''

for char in word:
    word[-1] == "!"
    if char == "a":
        print("@", end='')#<------replacement of a is successful
    elif char == "i":
        print("1", end='')
    elif char == "m":
        print("M", end='')
    elif char == "B":
        print("8", end='')
    elif char == "s":
        print("$", end='')
    else:
        print(char, end='')
    password = word#<---------does not carry over to the password!