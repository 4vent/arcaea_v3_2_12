import sys
sys.path.append('.')
from corresponds import corres, spaces, num2char
import platform

class arc_cripted_text_braker():   
    def __init__(self, correspondence_table:dict, space_list:list):
        self.corres = correspondence_table
        self.spaces = space_list
    
    def decript(self, text, with_num=False):
        result = ''
        for c in text:
            if c in self.spaces:
                if with_num:
                    result += '\033[0m' + c + '\033[0m'
                else:
                    result += ' '
            elif c in self.corres.keys():
                result += '\033[31m' + self.corres[c] + '\033[0m'
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
    "hiKuDO,4EOj7E_u...",
    "",
    "BPD3rEKu4DliKuK,4uPDeDvVeD3vEuD4_EO3GD7VXDeuWeODj.",
    "IVW4DliKu3OVf4hVOU4EvuDe3vEuD7PEK4ueEOKrieDj.",
    # ''.join(num2char.values())
]
        
ACTB = arc_cripted_text_braker(corres, spaces)

for cripted_text in cripted_texts:
    plain_text = ACTB.decript(cripted_text, with_num=False)
    nums = '\033[0m' + ACTB.get_space_letters(cripted_text) + '\033[0m'

    if platform.system() == 'Darwin':
        from colordprint import colordprint
        colordprint(
            plain_text,
            colorful_strength=0.08,
            customcolor=(1.0, 0.4, 0.55)
        )
        colordprint(nums, customcolor=(0.5, 0.5, 0.5))
    else:
        print(plain_text)
        print(nums)