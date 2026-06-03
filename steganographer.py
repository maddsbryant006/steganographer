from PIL import IMAGE
from PIL import AUDIO

def upload_file():

def main_options():
    print("Welcome to the Audio and Image Steganographer")
    print("1. Encode Image")
    print("2. Decode Image")
    print("3. Encode Audio")
    print("4. Decode Audio")
    print("5. Exit")

def encode_image():
    #encode an image uploaded by user

def decode_image():
    #decode an image uploaded by user

def encode_audio():
    #encode audio uploaded by user

def decode_audio():
    #decode audio uploaded by user

def main():
    #main function for user option to encode or decode an image or audio
    main_options()
    user_input = int(input())

    while user_input != 5:
        if user_input == 1:
            encode_image()
            main_options()
            user_input = int(input())
        elif user_input == 2:
            decode_image()    
            main_options()
            user_input = int(input())
        elif user_input == 3:
            encode_audio()
            main_options()
            user_input = int(input())
        elif user_input == 4:
            decode_audio()
            main_options()
            user_input = int(input())
        else:
            print("Please input a valid option")
            main_options()
            user_input = int(input())


if __name__ == "__main__":
    main()