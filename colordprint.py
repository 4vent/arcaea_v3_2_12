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
        if c == '\\':
            m = re.match(r'\\e\[([0-9][0-9])m', string[i:i+6])
            
            if string[i:i+5] == '\\e[0m':
                print(buffer, end='')
                buffer = ''
                console.set_color()
                i += 5
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
                i += 6
                continue
            else:
                buffer += '\\'
        else:
            buffer += c
        
        i += 1
    
    print(buffer, end='')
    print(end, end='')

if __name__ == '__main__':
    colordprint('\e[30mthis is a sample')
    colordprint('\e[31mthis is a sample')
    colordprint('\e[32mthis is a sample')
    colordprint('\e[33mthis is a sample')
    colordprint('\e[34mthis is a sample')
    colordprint('\e[35mthis is a sample')
    colordprint('\e[36mthis is a sample')
    colordprint('\e[37mthis is a sample\e[0m')
