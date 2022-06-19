import re
import platform
from random import uniform
import numpy as np

def hex2rgb(hex:str, ignore_alpha=True):
    if hex.startswith('#'):
        hex = hex[1:]
    rgb=[]
    for i in range(0, 6, 2):
        rgb.append(int(hex[i:i+2], 16) / 255.0)
    if not ignore_alpha and len(hex) == 8:
        rgb.append(int(hex[6:8], 16) / 255.0)
    return rgb

colors = {
    '30': np.array(hex2rgb('090300')),
    '31': np.array(hex2rgb('DB2D20')),
    '32': np.array(hex2rgb('01A252')),
    '33': np.array(hex2rgb('FDED02')),
    '34': np.array(hex2rgb('01A0E4')),
    '35': np.array(hex2rgb('A16A94')),
    '36': np.array(hex2rgb('B5E4F4')),
    '37': np.array(hex2rgb('A5A2A2')),
    '90': np.array(hex2rgb('5C5855')),
    '91': np.array(hex2rgb('DB2D20')),
    '92': np.array(hex2rgb('01A252')),
    '93': np.array(hex2rgb('FDED02')),
    '94': np.array(hex2rgb('01A0E4')),
    '95': np.array(hex2rgb('A16A94')),
    '96': np.array(hex2rgb('B5E4F4')),
    '97': np.array(hex2rgb('F7F7F7')),
}

def colordprint_pythonista(string, end='\n', colorful_strength=0, customcolor=(1.0, 1.0, 1.0)):
    import console
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

def colordprint_win(string:str, end='\n'):
    string = string.replace('\033[99m', '\033[31m')
    print(string, end=end)

def colordprint(string, end='\n', colorful_strength=0, customcolor=(1.0, 1.0, 1.0)):
    if platform.system() == 'Darwin':
        colordprint_pythonista(string, end=end, colorful_strength=colorful_strength, customcolor=customcolor)
    else:
        colordprint_win(string, end)

if __name__ == '__main__':
    colordprint('\033[30mthis is a sample')
    colordprint('\033[31mthis is a sample')
    colordprint('\033[32mthis is a sample')
    colordprint('\033[33mthis is a sample')
    colordprint('\033[34mthis is a sample')
    colordprint('\033[35mthis is a sample')
    colordprint('\033[36mthis is a sample')
    colordprint('\033[37mthis is a sample\033[0m')
    for i in range(10):
        for j in range(10):
            num = i * 10 + j
            print(f'\033[{num}m{num:03d}\033[0m', end=' ')
        print('')
