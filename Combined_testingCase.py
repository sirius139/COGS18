import unittest 
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

    
    def check_player_input(cls, MC):
        if "SIRIUS" in MC.upper():
            print(f"You put in {cls.translater(cls, MC)}. Hummmm... Is it correct...")
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
                    print(f"Humm looks like {MC_list[i]}  doesn't match.")
                    return 
                i += 1
        
        if self.count == 2: 
            i = 0
            while i < len(MC_list): 
                if MC_list[i] != Orginial_list[i]:
                    print(f"Humm {MC_list[i]} looks like this letter doesn't match. It might be this letter at that index? {Orginial_list[i]}")
                    return
                i += 1
        
        if self.count == 3: 
            i = 0 
            while i < len(MC_list): 
                if MC_list[i] != Orginial_list[i]:
                    print("Hum. Maybe try looking at the rule.")
                    return 
                    i += 1
                    
class MorseCode_testing(unittest.TestCase): 
    def constructor(self): 
        self.MC= MorseCode()
    def translater_test(self):
        self.assertEqual(self.MC.translater(("Hello World"), ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))
    def correct_answer(self): 
        self.assertTrue(self.MC.check_player_input("sirius"))
    def wrong_answer(self): 
        self.assertFalse(self.MC.check_player_input("fierfus"))
        
        
                      

class NarcissisticNumber():
    count = 0
    
    def check_player_input(cls, NN):
        try:
            NN_list = list(NN)
            length = len(NN_list)
            total = 0

            for i in NN_list:
                total += int(i) ** length

            if length != 4:
                return False
            if total == int(NN):
                return True
            if total != int(NN):
                return False

        except ValueError:
            print("Did you put in the correct type of answer?") 
            
    def hint(self, NN):
        NN_list = list(NN)
        length = len(NN_list)
        total = 0
        if length != 4: 
            print("You didn't put in 4 digits.") 
            return 
      
        for i in NN_list:
            total += int(i) ** length
        if self.count ==0: 
            print("It says incorrect...")
            
        if self.count == 1: 
            print(f"Humm, the sum of these four digits seems to be {total}. It doesn't seem right.")
        
        # https://www.britannica.com/topic/number-game/Types-of-games-and-recreations#ref396105
        if self.count == 2: 
            print("According to the rule book, 'narcissistic numbers are numbers that can be represented by some kind of mathematical manipulation of their digits. A whole number, or integer, that is the sum of the nth powers of its digits (e.g., 153 = 13 + 53 + 33) is called a perfect digital invariant.'")
        
        if self.count == 3: 
            print("It's incorrect again. Last try...")

class NarcissisticNumber_testing(unittest.TestCase):
    def constructor(self): 
        self.NN = NarcissisticNumber()
    def correct_answer(self):
        self.assertTrue(self.NN.check_player_input("1634"))
    def wrong_answer(self):
        self.assertFalse(self.NN.check_player_input("1234"))
    def wrong_data_type(self):
        self.assertFalse(self.NN.check_player_input("     4344"))
        
        
class CaesarCipher():
    cipher = {"A": "X", "B": "Y", "C": "Z", "D": "A", "E": "B",
              "F": "C", "G": "D", "H": "E", "I": "F", "J": "G",
              "K": "H", "L": "I", "M": "J", "N": "K", "O": "L",
              "P": "M", "Q": "N", "R": "O", "S": "P", "T": "Q",
              "U": "R", "V": "S", "W": "T", "X": "U", "Y": "V",
              "Z": "W"}
    count = 0 
    def translater(seld, CC): 
        CC_list = list(CC.upper())
        CC_cipher = ''
        for i in CC_list: 
            if i in self.cipher: 
                CC_cipher += self.cipher[i]
        return CC_cipher

    def check_player_input(cls, CC):
        if "WAKE UP" in CC.upper():
            return True 
        else:
            return False 
    def hint(cls, CC): 
        if self.count ==0: 
            print("It says incorrect...")
        if self.count ==1: 
            print("You put in " + CC + " and it means " + self.translater(CC) + "... doesn't seem right. ") 
        if self.count ==2: 
            print("You have to rotate the letter 23 times to the left.") 
        if self.count ==3: 
            print("what's it... feels like it is two words with a space in between...") 
       
    
    
class CaesarCipher_Testing(unittest.TestCase):
    def constructor(self): 
        self.CC = CaesarCipher()
    def correct_answer(self):
        self.assertTrue(self.CC.check_player_input("WAKE UP"))
    def wrong_answer(self): 
        self.assertFalse(self.CC.check_player_input("what's going on"))
    