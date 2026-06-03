def encode_audio():
    #encode audio uploaded by user
    aud = input("Enter Audio file (w/ Extension): ")
    audio = AUDIO.open(aud, 'r')
    text = input("Phrase to be encoded: ")

    newAud = audio.copy()

def decode_audio():
    #decode audio uploaded by user