from PIL import IMAGE

def binary_conv(phrase):
    #convert phrase into binary
    return [format (ord(i), '08b') for i in phrase]

def modify_pix(pix, phrase):
    #modify pixels value based on binary
    binaryForm = binary_conv(phrase)
    length = len(binaryForm)
    imgdata = iter(pix)

def encrypt_phrase(image, phrase):
    #add modified pixel data to image

def encode_image():
    #encode an image uploaded by user
    img = input("Enter Image file (w/ Extension): ")
    image = IMAGE.open(img, 'r')
    text = input("Phrase to be encoded: ")

    newImg = image.copy()
    encrypt_phrase(newImg, text)
    newImgFile = input("Input encrypted files name: ")
    newImg.save(newImgFile, newImgFile.split(".")[-1].upper())


def decode_image():
    #decode an image uploaded by user
    