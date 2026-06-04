from PIL import Image

def binary_conv(phrase):
    # convert phrase into list of 8-bit binary strings
    return [format(ord(i), '08b') for i in phrase]


def modify_pix(pix, phrase):
    # modify pixel values based on binary
    binList = binary_conv(phrase)
    length = len(binList)
    imgData = iter(pix)

    for i in range(length):
        pixels = [value for value in next(imgData)[:3] + next(imgData)[:3] + next(imgData)[:3]]

        # modify pixels based on binary data
        for j in range(8):
            if binList[i][j] == '0' and pixels[j] % 2 != 0:
                pixels[j] -= 1
            elif binList[i][j] == '1' and pixels[j] % 2 == 0:
                pixels[j] = pixels[j] -1 if pixels[j] != 0 else pixels[j] + 1

        # termination flag, even means continue, odd means stop
        if i == length - 1:
            pixels[-1] |= 1 # odd
        else:
            pixels[-1] &= ~1 # even

        yield tuple(pixels[:3])
        yield tuple(pixels[3:6])
        yield tuple(pixels[6:9])


def encrypt_phrase(image, phrase):
    # add modified pixel data to image 
    w = image.size[0]
    (x,y) =(0,0)

    for pixel in modify_pix(image.getdata(), phrase):
        image.putpixel((x,y), pixel)
        x = 0 if x == w - 1 else x + 1
        y += 1 if x == 0 else 0

def encode_image():
    # encode an image uploaded by user
    img = input("Enter Image file (w/ Extension): ")
    image = Image.open(img, 'r')
    text = input("Phrase to be encoded: ")

    newImg = image.copy()
    encrypt_phrase(newImg, text)
    newImgFile = input("Input encrypted files name: ")
    newImg.save(newImgFile, newImgFile.split(".")[-1].upper())


def decode_image():
    # decode an image uploaded by user
    img = input("Enter Image file (w/ Extension): ")
    image = Image.open(img, 'r')
    text = iter(image.getdata())
    phrase = ''

    while True:
        pixels = [value for value in next(text)[:3] + next(text)[:3] + next(text)[:3]]
        binStr = ''.join(['1' if i % 2 else '0' for i in pixels[:8]])
        phrase += chr(int(binStr, 2))

        if pixels[-1] % 2 != 0:
            break
    
    return print(f'Decoded text: {phrase}')
    