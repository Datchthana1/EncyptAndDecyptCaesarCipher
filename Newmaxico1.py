import numpy as np
import Ohio as O
Loop = True
while Loop == True:
    output = ""
    ways = ""
    ways = str(input("Which do you want to fuction? \n1:encypt code by Caesar_Cipher 2:decypt by Caesar_Cipher 3:encypt by Rot13 4:decypt by Rot13 : "))
    word = str(input("Please type your code : "))
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if ways == "1":
        output = ""
        for a in word:
            for b in list:
                if a == b:
                    position = list.index(b)
                    position += 3
                    x =list[position]
                    for i in x:
                        output += i
    elif ways == "2":
        output = ""
        for a in word:
            for b in list:
                if a == b:
                    position = list.index(b)
                    position -= 3
                    x =list[position]
                    for i in x:
                        output += i
    elif ways == "3":
        output = ""
        for a in word:
            for b in list:
                if a == b:
                    position = list.index(b)
                    position = (position + 13)%26
                    x =list[position]
                    for i in x:
                        output += i
    elif ways == "4":
        output = ""
        for a in word:
            for b in list:
                if a == b:
                    position = list.index(b)
                    position = (position - 13)%26
                    x =list[position]
                    for i in x:
                        output += i  
    else:
        print("Cannot define your way")
    Loop = False
    print(output)
    stop = str(input("Do you want to repeat? \n1:Yes 2:No : "))
    if stop == "1":
        print("You repeat the function")
        Loop = True
    else:
        print("You don't repeat the function")
        Loop = False
O.Name.Input()