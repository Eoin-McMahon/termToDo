from termcolor import colored
import os
import pickle as pkl

class Utils():
    def __init__(self):
        return 

    def strike(self, text):
        result = ''
        for c in text:
            result = result + c + '\u0336'
        return colored(result, "red")
    
    def is_marked_done(self, text):
            if '\x1b[' in text:
                return True
            return False

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def showInputField(self):
        entry = input(">> ")
        return entry

    def load_items(self): 
        try:
            data = pkl.load(open("./items.pickle", "rb"))
        except (OSError, IOError) as e:
            data = ([], [])
        
        return data

    def store_items(self, items, done):
        try:
            pkl.dump((items, done), open("items.pickle", "wb"))
        except (OSError, IOError) as e:
            print("Could not save items:\n", e)
        
