def RGB_to_CMYK(rgb):
    red = rgb['R'] / 255
    green = rgb['G'] / 255
    blue = rgb['B'] / 255
    kValue = 1 - max(red, green, blue)
    if kValue == 1:
        cyan = 0
        magenta = 0
        yellow = 0
        black = 100
    else: 
        cyan = int(((1 - red - kValue) / (1 - kValue)) * 100)
        magenta = int(((1 - green - kValue) / (1 - kValue)) * 100)
        yellow = int(((1 - blue - kValue) / (1 - kValue)) * 100)
        black = int(kValue * 100)
    cmyk = {
        'Cyan' : cyan, 
        'Magenta' : magenta, 
        'Yellow' : yellow,
        'Key (Black)' : black
    }
    return cmyk
print("RGB to CMYK Converter")

red = input('Enter the Red Color Value (or q to quit): ')
while red != "q" and red != "quit":
    try: 
        red = int(red)
        if red < 0 or red > 255:
            print('Error: Red value must be in between 0 and 255.')
            red = input('Enter the Red Color Value (or q to quit): ')
            continue
    except ValueError: 
        if red < 0 or red > 255:
            print('Error: RBG values must be in between 0 and 255.')
            red = input('Enter the Red Color Value (or q to quit): ')
            continue
    green = input("Enter the Green Color Value: ")
    if green == "q" or green == "quit":
        break
    try: 
        green = int(green)
        if green < 0 or green > 255:
            print('Error: Green value must be in between 0 and 255.')
            red = input('Enter the Red Color Value (or q to quit): ')
            continue
    except ValueError: 
        if green < 0 or green > 250: 
            print('Error: RBG values must be in between 0 and 255.')
            red = input('Enter the Red Color Value (or q to quit): ')
            continue
    blue = input("Enter the Blue Color Value: ")
    if blue == "q" or green == "quit":
        break
    try: 
        blue = int(blue)
        if blue < 0 or blue > 255:
            print('Error: Blue value must be in between 0 and 255.')
            red = input('Enter the Red Color Value (or q to quit): ')
            continue
    except ValueError: 
        if blue < 0 or blue > 250: 
            print('Error: RBG values must be in between 0 and 255.')
            red = input('Enter the Red Color Value (or q to quit): ')
            continue

    rgb = { 
        'R': int(red),
        'G': int(green),
        'B': int(blue)
    }
    
    cmyk = RGB_to_CMYK(rgb)
    print()
    print('CMYK Values')
    print('Cyan:', cmyk['Cyan'])
    print('Magenta:', cmyk['Magenta'])
    print('Yellow:', cmyk['Yellow'])
    print('Key (Black):', cmyk['Key (Black)'])
    print()
    red = input('Enter the Red value (or q to quit): ')
print('Bye Bye!')