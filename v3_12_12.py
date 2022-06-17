import sys
sys.path.append('.')
from colordprint import colordprint
from corresponds import corres, spaces, num2char

class arc_cripted_text_braker():   
    def __init__(self, correspondence_table:dict, space_list:list):
        self.corres = correspondence_table
        self.spaces = space_list
    
    def decript(self, text):
        result = ''
        for c in text:
            if c in self.spaces:
                result += ' '
            elif c in self.corres.keys():
                result += '\e[31m' + self.corres[c] + '\e[0m'
            else:
                result += c
        return result
    
    def get_space_letters(self, text):
        space_letters = ''
        for c in text:
            if c in self.spaces:
                space_letters += c
        return space_letters

cripted_texts = [
    "bO3ueWuP,3b4fEK4GVeO4vVe3VOD.",
    "bO4ueWuP,3b4fEK7GVeO7vVe3_VWOuhDKK4VuPDeK.",
    "",
    "dV,3b3eDvWKD",
    "b7eDvWKD4uV7hDu4Ehh4vEjD4EfEq...",
    "",
    "BPiK7XVi_D4b'XD7WKDj4uV4_Ehh7WrVO4KV3nEOq3VuPDeK...",
    "...iK7iu4eDE_PiOU3qVW?"
]
        
ACTB = arc_cripted_text_braker(corres, spaces)

for cripted_text in cripted_texts:
    space_pickup = ''
    colordprint(ACTB.decript(cripted_text))
    print(ACTB.get_space_letters(cripted_text))
