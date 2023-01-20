from microbit import *
R = Image("02579:"
                     "02579:"
                     "02579:"
                     "02579:"
                     "02579")


L =   Image("97520:"
                     "97520:"
                     "97520:"
                     "97520:"
                     "97520")



while True:
    LR = accelerometer.get_x()
    if LR > 20:
        display.show(R)
    elif LR < -20:
        display.show(L)
    else:
        display.show(Image.SQUARE)
        
    