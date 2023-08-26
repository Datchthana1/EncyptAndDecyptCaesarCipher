import numpy as np
import Ohio as O
Loop = True
count = 0
while Loop == True:
    output = ""
    ways = ""
    position = 0
    count = 0
    ways = str(input("Which do you want to fuction? \n1:encypt code by Caesar_Cipher \n2:decypt by Caesar_Cipher \n3:encypt by Rot13 \n4:decypt by Rot13 \n : "))
    code = str(input("Please type your code : "))
    word = code.lower()
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if ways == "1":
        for a in word:
            count += 1
            if count == 11:
                break
            else:
                for b in list:
                    if a == b:
                        position = list.index(b)
                        position += 3
                        x =list[position]
                        for i in x:
                            output += i
    elif ways == "2":
        for a in word:
            count += 1
            if count == 11:
                break 
            else:
                for b in list:
                    if a == b:
                        position = list.index(b)
                        position -= 3
                        x =list[position]
                        for i in x:
                            output += i
    elif ways == "3":
        for a in word:
            count += 1
            if count == 11:
                break
            else:
                for b in list:
                    if a == b:
                        position = list.index(b)
                        position = (position + 13)%26
                        x =list[position]
                        for i in x:
                            output += i
    elif ways == "4":
        for a in word:
            count += 1
            if count == 11:
                break
            else:
                for b in list:
                    if a == b:
                        position = list.index(b)
                        position = (position - 13)%26
                        x =list[position]
                        for i in x:
                            output += i  
    else:
        print("Cannot define your way")
    print(output)
    Loop = False
    stop = str(input("Do you want to repeat? \n1:Yes 2:No : "))
    if stop == "1":
        print("You repeat the function")
        Loop = True
    else:
        print("You don't repeat the function")
        Loop = False
O.Name.Input()
O.University.Input()