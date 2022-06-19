def hex2rgb(hex:str, ignore_alpha=True):
    if hex.startswith('#'):
        hex = hex[1:]
    rgb=[]
    for i in range(0, 6, 2):
        rgb.append(int(hex[i:i+2], 16) / 255.0)
    if not ignore_alpha and len(hex) == 8:
        rgb.append(int(hex[6:8], 16) / 255.0)
    return rgb

print(hex2rgb('090300'))