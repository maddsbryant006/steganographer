import wave


def encrypt_phrase(audio, phrase):
    # embedded phrase into audio
    bytes = bytearray(list(audio.readframes(audio.readframes())))

    phrase += '[END]'
    bits = ''.join(format(ord(char), '08b') for char in phrase)

    if len(bits) > len(bytes):
        raise ValueError("Message is too long for current file")
    
    for i, bit in enumerate(bits):
        bytes[i] = (bytes[i] & 254) | int(bit)


def encode_audio():
    # encode audio uploaded by user
    aud = input("Enter Audio file (w/ Extension): ")
    audio = wave.open(aud, 'r')
    text = input("Phrase to be encoded: ")

    newAud = audio.copy() #bug here
    encrypt_phrase(newAud, text)
    newAudFile = input("Input encrypted files name: ")
    newAud.save(newAudFile, newAudFile.split(".")[-1].upper())


def decode_audio():
    # decode audio uploaded by user
    aud = input("Enter Audio file (w/ Extension): ")
    audio = wave.open(aud, 'r')
    text = iter(audio.getdata())
    phrase = ''

    bytes = bytearray(list(audio.readframes(audio.readframes())))

    bits = [str(bytes & 1) for bytes in bytes]
    bits = ''.join(bits)

    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        if len(byte) < 8: break
        phrase += chr(int(byte, 2))
        if phrase.endswith('[END]'):
            audio.close()

    return print(f'Decoded text: {phrase[:-5]}')