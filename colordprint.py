import re
import console
from random import uniform
import numpy as np

colors = {
    '30': np.array((0.15, 0.15, 0.15)),
    '31': np.array((1.0, 0.3, 0.3)),
    '32': np.array((0.0, 0.8, 0.0)),
    '33': np.array((0.9, 0.9, 0.1)),
    '34': np.array((0.4, 0.4, 1.0)),
    '35': np.array((1.0, 0.3, 1.0)),
    '36': np.array((0.2, 0.9, 0.9)),
    '37': np.array((0.95, 0.95, 0.95)),
    
    '38': np.array((0.4, 0.4, 0.4))
}

def colordprint(string, end='\n', colorful_strength=0, customcolor=(1.0, 1.0, 1.0)):
    st = colorful_strength
    buffer = ''
    i = 0
    while i < len(string):
        c = string[i]
        if c == '\033':
            m = re.match(r'\033\[([0-9][0-9])m', string[i:i+5])
            
            if string[i:i+4] == '\033[0m':
                print(buffer, end='')
                buffer = ''
                console.set_color()
                i += 4
                continue
            elif m:
                print(buffer, end='')
                buffer = ''
                if m.groups()[0] == '99':
                    console.set_color(
                        customcolor[0] + uniform(-st, st),
                        customcolor[1] + uniform(-st, st),
                        customcolor[2] + uniform(-st, st)
                    )
                elif m.groups()[0] in colors.keys():
                    console.set_color(*colors[m.groups()[0]])
                else:
                    console.set_color()
                i += 5
                continue
            else:
                buffer += '\033'
        else:
            buffer += c
        
        i += 1
    
    print(buffer, end='')
    print(end, end='')

if __name__ == '__main__':
    colordprint('\033[30mthis is a sample')
    colordprint('\033[31mthis is a sample')
    colordprint('\033[32mthis is a sample')
    colordprint('\033[33mthis is a sample')
    colordprint('\033[34mthis is a sample')
    colordprint('\033[35mthis is a sample')
    colordprint('\033[36mthis is a sample')
    colordprint('\033[37mthis is a sample\033[0m')
