class arc_cripted_text_braker():   
    def __init__(self, correspondence_table:dict, space_list:list):
        self.corres = correspondence_table
        self.spaces = space_list
    
    def decript(self, text, with_num=False, kvswap=False):
        if kvswap:
            corres = {v: k for k, v in self.corres.items()}
        else:
            corres = self.corres
        
        result = ''
        for c in text:
            if c in self.spaces:
                if with_num:
                    result += '\033[0m' + c + '\033[0m'
                else:
                    result += ' '
            elif c in corres.keys():
                result += '\033[99m' + corres[c] + '\033[0m'
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

def combination_generator(chardict:dict):
    combinations = []
    for k in chardict.keys():
        if type(chardict[k]) is list:
            for c in chardict[k]:
                newdict = chardict.copy()
                newdict[k] = c
                combinations += combination_generator(newdict)
            return combinations
    return [''.join(chardict.values())]