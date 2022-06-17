import re
import console

colors = {
    '30': (0.1, 0.1, 0.1),
    '31': (1.0, 0.3, 0.3),
    '32': (0.0, 0.8, 0.0),
    '33': (1.0, 1.0, 0.3),
    '34': (0.3, 0.3, 1.0),
    '35': (1.0, 0.3, 1.0),
    '36': (0.3, 1.0, 1.0),
    '37': (0.9, 0.9, 0.9),
}

def colordprint(string, end='\n'):
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
                if m.groups()[0] in colors.keys():
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
