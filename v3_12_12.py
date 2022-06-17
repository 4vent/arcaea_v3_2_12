import sys
sys.path.append('.')
from colordprint import colordprint
from corresponds import corres, spaces, num2char

class arc_cripted_text_braker():   
    def __init__(self, correspondence_table:dict, space_list:list):
        self.corres = correspondence_table
        self.spaces = space_list
    
    def decript(self, text, with_num=False):
        result = ''
        for c in text:
            if c in self.spaces:
                if with_num:
                    result += '\e[38m' + c + '\e[0m'
                else:
                    result += ' '
            elif c in self.corres.keys():
                result += '\e[99m' + self.corres[c] + '\e[0m'
            else:
                result += c
        return result
    
    def get_space_letters(self, text):
        space_letters = ''
        for c in text:
            if c in self.spaces:
                space_letters += c
            else:
                space_letters += ' '
        return space_letters

cripted_texts = [
    "bO3ueWuP,3b4fEK4GVeO4vVe3VOD.",
    "bO4ueWuP,3b4fEK7GVeO7vVe3_VWOuhDKK4VuPDeK.",
    "",
    "dV,3b3eDvWKD",
    "b7eDvWKD4uV7hDu4Ehh4vEjD4EfEq...",
    "",
    "BPiK7XVi_D4b'XD7WKDj4uV4_Ehh7WrVO4KV3nEOq3VuPDeK...",
    "...iK7iu4eDE_PiOU3qVW?",
    "",
    "bv4qVW3PDEe3nD...",
    "hiKuDO,4EOj7E_u..."
]
        
ACTB = arc_cripted_text_braker(corres, spaces)

for cripted_text in cripted_texts:
    space_pickup = ''
    colordprint(
        ACTB.decript(cripted_text, with_num=False),
        colorful_strength=0.08,
        customcolor=(1.0, 0.4, 0.55)
    )
    colordprint('\e[99m' + ACTB.get_space_letters(cripted_text) + '\e[0m', customcolor=(0.5, 0.5, 0.5))
