import sys
sys.path.append('.')
from colordprint import colordprint

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
corresponds = {
    # official tweet hint
    'V': 'o',
    'a': 'L',
    'N': 'W',
    'd': 'S',
    'v': 'f',
    'I': 'Y',
    'P': 'h',
    'X': 'V',
    'A': 'H',
    'r': 'p',
    
    # detective
    'b': 'I', # single char 'b' -> I
    'O': 'n', # I? -> In
    'D': 'e', # on? -> one
    'u': 't', # o?he?? -> others
    'e': 'r',
    'K': 's',
    'W': 'u', # tr?th -> truth
    'f': 'w', # I ??s (be verb?) -> I was
    'E': 'a',
    'h': 'l', # ?ess, ?et, a??(same char) -> l
    'G': 'b', # ?orn -> born
    'j': 'd', # fa?e -> fade
    'q': 'y', # awa? -> away
    '_': 'c',  # ?ountless -> countless
    # next
    'B': 'T',
    'i': 'i',
    'U': 'g',
    'n': 'm'
    }
spaces = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
num_2_car = {
    '0': 'J',
    '1': 'I', # l? L?
    '2': 'e',
    '3': '',
    '4': '',
    '5': 'j',
    '6': '',
    '7': 'h',
    '8': '4',
    '9': 'F', # key 6?
    '10': 'E',
    '11': 'U', # n? u?
}

for cripted_text in cripted_texts:
    result:str = ''
    space_numbers = ''
    for c in cripted_text:
        if c in spaces:
            result += ' '
            space_numbers += c
        elif c in corresponds.keys():
            result += '\e[31m' + corresponds[c] + '\e[0m'
        else:
            result += c
    print('')
    colordprint(result)
