from PIL import IMAGE

def binary_conv(phrase):
    return [format for(ord(i), '08b') for i in phrase]

def modify_pix(pix, phrase):

def encode_image():
    #encode an image uploaded by user
    img = input("Enter Image file (w/ Extension): ")
    image = IMAGE.open(img, 'r')
    text = input("Phrase to be encoded: ")

    newImg = image.copy()

def decode_image():
    #decode an image uploaded by user
