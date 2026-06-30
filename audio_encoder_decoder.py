import wave
from pydub import AudioSegment

def flac_to_wav(file):
    load = AudioSegment.from_file(file, format="flac")
    new_file_name = input("Enter file name as '.wav': ")

    new_file = load.export(new_file_name, format="wav")
    return new_file

def encode_audio():
    # encode audio uploaded by user
    aud = input("Enter Audio file (w/ Extension): ")
    
    if ".flac" in aud :
        aud = flac_to_wav(aud)
        
        
    with wave.open(aud, 'r') as audio:
        audio_bytes = bytearray(list(audio.readframes(audio.getnframes()))) # TypeError: 'bytearray' object is not callable
    data = input("Phrase to be encoded: ")
    
    data += "###"
    
    data_bytes = "".join(format(ord(i), '08b') for i in data)
    
    for i, bit in enumerate(data_bytes):
        audio_bytes[i] = (audio_bytes[i] & 254) | int(bit)
        
    modified_data = bytes(audio_bytes)
    
    newAudFile = input("Input encrypted file name: ")
    
    with wave.open(newAudFile, 'w') as export:
        export.setparams(audio.getparams())
        export.writeframes(modified_data)


def decode_audio():
    phrase = ' '
    # decode audio uploaded by user
    aud = input("Enter Audio file (w/ Extension): ")
    with wave.open(aud, 'r') as audio:
        audio_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        
    extract_bytes = [str(audio_bytes[i] & 1) for i in range(len(audio_bytes))]
    extract_data = ''.join(extract_bytes)
    
    data_bytes = [extract_data[i:i+8] for i in range(0, len(extract_data), 8)]
    decode_data = ''.join(chr(int(b, 2)) for b in data_bytes)
    
    data = decode_data.split("###") [0]

    return print(f'Decoded data: {data}')