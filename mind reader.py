valid_response = False
import time
# ***************************************************
# introduciton
# ***************************************************

print("""\n- Hello human, you are the luckiest person on earth now 🌍""")
time.sleep(1)
print("""- I'm an old spirit who has been living since dark ages 🦇⏳""")
time.sleep(1)
print("""- Don't panic i'm a good spirit 🧙‍♂️✨""")
time.sleep(1)
print("""- Whaaaat!!! you don't belive me 😏""")
time.sleep(1)
print("""- We can play a little game together to show you 🥱""")
time.sleep(1)
while not valid_response:
    time.sleep(1)
    ques = input("- Do you dare to play 😏? ")
    if ques.lower() == 'yes':
        valid_response = True
    else:
        print("""hhhh..., as i expected 😂 """)
        time.sleep(1)
        print("""- I'm gonna ask you again 🙄 """)

print("""- You are only allowed to answer with yes ✔ or no ✖ """)
time.sleep(1)
print("""- Think of a number from 1 to 10 🎲 """)

# ***************************************************
# Question one
# ***************************************************

while valid_response:
    time.sleep(1)
    ques_1 = input("Did you choose? ")
    if ques_1.lower() == 'yes':
        valid_response = False
    else:
        print("When you choose please write yes 😁 ")

# ***************************************************
# Question two
# ***************************************************

# main variables
the_range = range(1, 11)
answer = 0
out = []
out2 = []
out3 = []

while not valid_response:
    time.sleep(1)
    ques_2 = input("Is it even? ")
    if ques_2.lower() == 'yes' or ques_2.lower() == 'no':

        # if the numbers are even <----

        if ques_2.lower() == "yes":
            for num in the_range:
                if num % 2 == 0:
                    out.append(num)
            # ***************************************************
            # Question three
            # ***************************************************
            while not valid_response:
                time.sleep(1)
                ques_3 = input("Is the number greater than 5? ")
                if ques_3.lower() == 'yes' or ques_3.lower() == 'no':
                    if ques_3.lower() == "yes":
                        for num in range(len(out)):
                            if  out[num] > 5:
                                out2.append(out[num])
                        # ***************************************************
                        # Question four
                        # ***************************************************  
                        while not valid_response:
                            time.sleep(1)
                            ques_4 = input("Is the number greater than 7 🤔 ")
                            if ques_4.lower() == 'yes' or ques_4.lower() == 'no':
                                if ques_4.lower() == "yes":
                                    for num in range(len(out2)):
                                        if  out2[num] > 7:
                                            out3.append(out2[num])
                                    # ***************************************************
                                    # Question five
                                    # ***************************************************  
                                    while not valid_response:
                                        time.sleep(1)
                                        ques_5 = input("Is the number smaller than 9 🥱 ")
                                        if ques_5.lower() == 'yes' or ques_5.lower() == 'no':
                                            if ques_5.lower() == "yes":
                                                for num in range(len(out3)):
                                                    if  out3[num] < 9:
                                                        answer =  out3[num] 
                                                        valid_response = True  
                                            elif ques_5.lower() == "no": 
                                                for num in range(len(out3)):
                                                    if  out3[num] > 9:
                                                        answer =  out3[num] 
                                                        valid_response = True                                    
                                        else:
                                            print("Please enter yes or no only 😡 ")  
                                elif ques_4.lower() == "no": 
                                    for num in range(len(out2)):
                                        if  out2[num] < 7:
                                            answer =  out2[num] 
                                            valid_response = True                                
                            else:
                                print("Please enter yes or no only 😡 ")

                    elif ques_3.lower() == "no":  
                        for num in range(len(out)):
                            if  out[num] < 5:
                                out2.append(out[num])
                        # ***************************************************
                        # Question six
                        # ***************************************************  
                        while not valid_response:
                            time.sleep(1)
                            ques_6 = input("Is the number greater than 3? ")
                            if ques_6.lower() == 'yes' or ques_6.lower() == 'no':
                                if ques_6.lower() == "yes":
                                    for num in range(len(out2)):
                                        if  out2[num] > 3:
                                            answer =  out2[num] 
                                            valid_response = True 

                                elif ques_6.lower() == "no":
                                    for num in range(len(out2)):
                                        if  out2[num] < 3:
                                            answer =  out2[num] 
                                            valid_response = True     
                            else:
                                print("Please enter yes or no only 😡 ")
                else:
                    print("Please enter yes or no only 😡 ")

        # if the number are odd <----
            
        elif ques_2.lower() == "no":
            for num in the_range:
                if num % 2 != 0:
                    out.append(num)
            # ***************************************************
            # Question seven
            # ***************************************************
            while not valid_response:
                time.sleep(1)
                ques_7 = input("Is the number greater than 4? ")
                if ques_7.lower() == 'yes' or ques_7.lower() == 'no':
                    if ques_7.lower() == "yes":
                        for num in range(len(out)):
                            if  out[num] > 4:
                                out2.append(out[num])
                        # ***************************************************
                        # Question eight
                        # ***************************************************  
                        while not valid_response:
                            time.sleep(1)
                            ques_8 = input("Is the number greater than 6 🤔 ")
                            if ques_8.lower() == 'yes' or ques_8.lower() == 'no':
                                if ques_8.lower() == "yes":
                                    for num in range(len(out2)):
                                        if  out2[num] > 6:
                                            out3.append(out2[num])
                                    # ***************************************************
                                    # Question nine
                                    # ***************************************************  
                                    while not valid_response:
                                        time.sleep(1)
                                        ques_9 = input("Is the number smaller than 8 🥱 ")
                                        if ques_9.lower() == 'yes' or ques_9.lower() == 'no':
                                            if ques_9.lower() == "yes":
                                                for num in range(len(out3)):
                                                    if  out3[num] < 8:
                                                        answer =  out3[num] 
                                                        valid_response = True  
                                            elif ques_9.lower() == "no": 
                                                for num in range(len(out3)):
                                                    if  out3[num] > 8:
                                                        answer =  out3[num] 
                                                        valid_response = True                                    
                                        else:
                                            print("Please enter yes or no only 😡 ")  
                                elif ques_8.lower() == "no": 
                                    for num in range(len(out2)):
                                        if  out2[num] < 6:
                                            answer =  out2[num] 
                                            valid_response = True                                
                            else:
                                print("Please enter yes or no only 😡 ")

                    elif ques_7.lower() == "no":  
                        for num in range(len(out)):
                            if  out[num] < 4:
                                out2.append(out[num])
                        # ***************************************************
                        # Question ten
                        # ***************************************************  
                        while not valid_response:
                            time.sleep(1)
                            ques_10 = input("Is the number greater than 2 🥱 ")
                            if ques_10.lower() == 'yes' or ques_10.lower() == 'no':
                                if ques_10.lower() == "yes":
                                    for num in range(len(out2)):
                                        if  out2[num] > 2:
                                            answer =  out2[num] 
                                            valid_response = True 

                                elif ques_10.lower() == "no":
                                    for num in range(len(out2)):
                                        if  out2[num] < 2:
                                            answer =  out2[num] 
                                            valid_response = True     
                            else:
                                print("Please enter yes or no only 😡 ")
                else:
                    print("Please enter yes or no only 😡 ")
    else:
        print("Please enter yes or no only 😡 ")

# the end script 
    
time.sleep(1)
print(f"""Let me think """)
time.sleep(1)
print(f"""Wait, i just need to say my magic words """)
time.sleep(1.5)
print(f""""HABRA KADABRA..." 🧙‍♂️✨ """)
time.sleep(1)
print(f"""your number is... 👻 --> {answer} """)