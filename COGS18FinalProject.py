import os
import sys

def Main():
    # intro 
    print("Is this world real?")
    print("""You have been pondering this question for a while. There's just.. the world is just seems.. out of place? Or is it 
          just you out of place? People stop moving when you are not around. They just froze there untill you are there. You 
          only have vage memory of everything. You know you are born here but you can't tell who is your childhood bestfriend 
          or the name of the neighbor live next to you""")
    print("""You come back home from school today. You see a piece of paper on your desk.It says 'You can find the truth in ... 
          .. .-. .. ..- ...'. The last part seems like using the Morse Code. You recently happen to brought a decode book 
          although you can't rememeber why you brought it.""")
    
    decode_or_not=input("You decide to: (decode/just ignore)") 
    # https://realpython.com/python-f-strings/
    print(f"Do you want decode it find out the truth(? or ignore it?" { decode_or_not})
        

# https://www.python-engineer.com/posts/ask-user-for-input/   the while loop for input documentation   still need 
    if "decode" in decode_or_not.lower():
        Rule.one()
        first_message = input("Based on the rule book, you think the Morse Code means --") 
        print(first_message)
        
        while True: 
            if MorseCode.check_player_input(first_message) == True: 
                print("Sirius?")
                print("""You wisphered. That place is your secreat place -- when you are overwhemled by the creepy thing in the 
                      world,you always go there becasue no one ever go there. You decide to go to find out the truth""")
                break 
        
            elif MorseCode.check_player_input(first_message) == False:
                if MorseCode.count<=3: 
                    print(MorseCode.hint(first_message))
                    chance_left = 3- MorseCode.count
                    print(f"You have {chance_left} chances left")
                    MorseCode.count+=1 
                
                elif MorseCode.count>3:
                    cantSolve()
                    break 

            
    elif "ignore" in decode_or_not.lower: 
        print("""This is so sketchy. Why would a random piece of paper show up on your desk?? Did someone break in? You decide 
              to call the police and they can't find any trace of that person. You never receive anything like that ever again
              in your life""") 
        choice1()
    
    
    print("""You went to Sirius and find a little box with a 4 digit combination padlock. It says enter any Narcissistic Number 
          that's 4 digit. """)
    
    Rule.two() 
    second_message = input("Based on the rule book,you come up with a 4 digit Narcissistic Number --")
    
    while True: 
        if NarcissisticNumber.check_player_input(second_message)== True:
            print("You enter the correct answer for the lock. It opens up and you find a Caesar Cipher Wheel inside the box") 
            break 
        elif NarcissisticNumber.check_player_input(second_message)== False: 
            if NarcissisticNumber.count<=3:
                print(NarcissisticNumber.hint(second_message))
                N_chance_left = 3- NarcissisticNumber.count
                print("You have {N_chance_left} chances left")
                NarcissisticNumber.count+=1
                
            elif NarcissisticNumber.count>3: 
                cantSolve()
                break
                
    print("In the Caesar Cipher, it says 'Txhb rm'")           
    Rule.three()
    third_message = input("You decoded it by shift 23 rotation, you enter --" )
          
    while True: 
        if CaesarCipher.check_player_input(third_message)== True:
            print(""" You feel extremely tired and feel your consciousness is fading. You try to stay awake but eyelid is too 
                  heavry. You collapased to the ground.""") 
            print("""Your consciousness slowly comes back and you try to open your eyes. The light was so bright and blinding   
                  you. You try to raise your arm but some hard and cold thing was on your wrist. You start panic and when you 
                  open you eyes, you see a person infront of you."Test Subject 18 is in good condition." The person who wears a 
                  white doctor coat starts writing something on the notebook while saying that.Then he smiled and say, " 
                  Welcome to real world, my dear." """)        
            break 
            
        elif CaesarCipher.check_player_input(third_message)== False: 
            if CaesarCipher.count<=3:
                print(CaesarCipher.hint(second_message))
                C_chance_left = 3- CaesarCipher.count
                print(f"You get {(C_chance_left)} chances")
                CaesarCipher.count+=1
                
            elif CaesarCipher.count>3: 
                cantSolve()
                break
       
    restart() 
               
             
    
class MorseCode():
    count = 0  
    morseCode = {
                "A": ".-",
                "B": "-...",
                "C": "-.-.",
                "D": "-..",
                "E": ".",
                "F": "..-.",
                "G": "--.",
                "H": "....",
                "I": "..",
                "J": ".---",
                "K": "-.-",
                "L": ".-..",
                "M": "--",
                "N": "-.",
                "O": "---",
                "P": ".--.",
                "Q": "--.-",
                "R": ".-.",
                "S": "...",
                "T": "-",
                "U": "..-",
                "V": "...-",
                "W": ".--",
                "X": "-..-",
                "Y": "-.--",
                "Z": "--..",
                " ": "  "
                                }
    def translater(self, MC): 
        MC_list = list(MC.upper())
        MC_Morse = ''
        for i in MC_list: 
            if i in self.morseCode: 
                MC_Morse += self.morseCode[i]
        return MC_Morse

    def check_player_input(self, MC):
        if "SIRIUS" in MC.upper():
            print(f"You put in {self.translater(MC) }. Hummmm... Is it correct...")
            return True
        else:
            return False 
        
    def hint(self, MC):
        MC_list = list(MC)
        Orginial_list = list("SIRIUS")
        if self.count == 1:
            i = 0
            while i < len(MC_list): 
                if MC_list[i] != Orginial_list[i]:
                    print(f"Humm {MC_list[i]} looks like this letter doesn't match.")
                    return 
                i += 1
        
        if self.count == 2: 
            i = 0
            while i < len(MC_list): 
                if MC_list[i] != Orginial_list[i]:
                    print("Humm " + MC_list[i] + " looks like this letter doesn't match. It might be this letter at that index? " + Orginial_list[i])
                    return
                i += 1
        
        if self.count == 3: 
            i = 0 
            while i < len(MC_list): 
                if MC_list[i] != Orginial_list[i]:
                    print("Hum. Maybe try looking at the rule.")
                    return 
                i += 1
        
             
class NarcissisticNumber():
    count=0
    def check_player_input(self, NN):
        NN_list=list(NN)
        length = len(NN_list)
        total = 0 
        for i in NN_list:
            total+= int(i)**length
            
        if length !=4: 
            return False 
        if total == int(NN):
            return True 
        if total !=int(NN): 
            return False
            
    def hint(self,NN):
        NN_list=list(NN)
        length=len(NN_list)
        total =0
        if length !=4: 
            print(" You didn't put in 4 digits.") 
            return 
      
        for i in NN_list:
            total+= int(i)**length
            
        if self.count ==1: 
            print(f"Humm the sum of these four digits seem to be {total}. It doesn't seem right.")
        
        # https://www.britannica.com/topic/number-game/Types-of-games-and-recreations#ref396105
        if self.count ==2: 
            print("According to the rule book, 'narcissistic numbers are numbers that can be represented by some kind of mathematical manipulation of their digits. A whole number, or integer, that is the sum of the nth powers of its digits (e.g., 153 = 13 + 53 + 33) is called a perfect digital invariant.'")
        
        if self.count ==3: 
            print("It's incorrect again. Last try..")
            
       
        
        
        
class CaesarCipher():
    cipher = {"A": "X", "B": "Y", "C": "Z", "D": "A", "E": "B",
              "F": "C", "G": "D", "H": "E", "I": "F", "J": "G",
              "K": "H", "L": "I", "M": "J", "N": "K", "O": "L",
              "P": "M", "Q": "N", "R": "O", "S": "P", "T": "Q",
              "U": "R", "V": "S", "W": "T", "X": "U", "Y": "V",
              "Z": "W"}
    count = 0 
    def translater(self, CC): 
        CC_list = list(CC.upper())
        CC_cipher = ''
        for i in CC_list: 
            if i in self.cipher: 
                CC_cipher += self.cipher[i]
        return CC_cipher

    def check_player_input(self, CC):
        if "WAKE UP" in CC.upper():
            return True 
        else:
            return False 
    def hint(self, CC): 
        if self.count ==1: 
            print("You put in " + CC + " and it means " + self.translater(CC) + "... doesn't seem right. ") 
        if self.count ==2: 
            print("You have to rotate the letter 23 times to the left.") 
        if self.count ==3: 
            print("what's it... feels like it is two words with a space in between...") 
                  
    
    
class Rule():
    #https://stackoverflow.com/questions/50193618/using-dictionary-and-printing-out-value-when-matched-key-and-vise-versa used the alphent dicictory 
    R_text ="Here is what the rule book say: "
    morseCode = {
                "A": ".-",
                "B": "-...",
                "C": "-.-.",
                "D": "-..",
                "E": ".",
                "F": "..-.",
                "G": "--.",
                "H": "....",
                "I": "..",
                "J": ".---",
                "K": "-.-",
                "L": ".-..",
                "M": "--",
                "N": "-.",
                "O": "---",
                "P": ".--.",
                "Q": "--.-",
                "R": ".-.",
                "S": "...",
                "T": "-",
                "U": "..-",
                "V": "...-",
                "W": ".--",
                "X": "-..-",
                "Y": "-.--",
                "Z": "--..",
                " ": "  "
                                }
    def one():
        print(R_text)
        for i in morseCode:
            print(i) 
    def two():
        print(R_text)
        print("Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of 
              "digits")
        
    #https://en.wikipedia.org/wiki/Caesar_cipher use the explaination 
    def three():
        print(R_text)
        print("The Caesar cipher is based on transposition and involves shifting each letter of the plaintext message by a 
              "certain number of letters,left rotation of 7 places, right rotation 19 places. Example: A --> X, B --> Y") 
        
def restart():
    answer = input("Do you want to replay? [yes/no] ")
    if answer.lower == "yes":
        os.execl(sys.executable, os.path.abspath(COGS18FinalProject.py), *sys.argv) 
    else:
        print("Thank you for playing. See you in next game :) ")
        sys.exit(0)
        
def choice1():
    restart()
    
def cantSolve():
        print("You just can't solve it, do better next time")
        restart()
 
    
   