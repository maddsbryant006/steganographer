import audio_encoder_decoder 
import image_encoder_decoder
import qr_encoder_decoder
import uni_encoder_decoder
import pdf_encoder_decoder
import commit_encoder_decoder

#create payload capcity calculator for image
#after creating all encoders + decoders + gen excryption then change main to auto detect file type and call the correct encoder/decode

def main_options():
    print("------------------------------------------")
    print("Welcome to the Multi-Tool Steganographer")
    print("------------------------------------------")
    print("1. Image")
    print("2. Audio")
    print("3. QR Code")
    print("4. Unicode Text")
    print("5. PDF")
    print("6. Git Commits")
    print("7. Exit")
    print("------------------------------------------")

def options():
    print("1. Encode")
    print("2. Decode")
    print("------------------------------------------")
    
def gen_encrypt():
    # placeholder code
    img = input("Enter Image file (w/ Extension): ")
    image = Image.open(img, 'r')
    text = input("Phrase to be encoded: ")
    
def main():
    #main function for user option to encode or decode an image or audio
    main_options()
    user_input = int(input())

    while user_input != 7:
        if user_input == 1:
            options()
            user_choice = int(input())
            if user_choice == 1:
                image_encoder_decoder.encode_image()
            elif user_choice == 2:
                image_encoder_decoder.decode_image()
            else:
                print("Please enter a valid option")
                options()
                user_choice = int(input())
            main_options()
            user_input = int(input())
        elif user_input == 2:
            options()
            user_choice = int(input())
            if user_choice == 1:
                audio_encoder_decoder.encode_audio()
            elif user_choice == 2:
                audio_encoder_decoder.decode_audio()
            else:
                print("Please enter a valid option")
                options()
                user_choice = int(input())
            main_options()
            user_input = int(input())
        elif user_input == 3:
            options()
            user_choice = int(input())
            if user_choice == 1:
                qr_encoder_decoder.encode_qr()
            elif user_choice == 2:
                qr_encoder_decoder.decode_qr()
            else:
                print("Please enter a valid option")
                options()
                user_choice = int(input())
            main_options()
            user_input = int(input())
        elif user_input == 4:
            options()
            user_choice = int(input())
            if user_choice == 1:
                uni_encoder_decoder.encode_pdf()
            elif user_choice == 2:
                uni_encoder_decoder.decode_pdf()
            else:
                print("Please enter a valid option")
                options()
                user_choice = int(input())
        elif user_input == 5:
            options()
            user_choice = int(input())
            if user_choice == 1:
                pdf_encoder_decoder.encode_pdf()
            elif user_choice == 2:
                pdf_encoder_decoder.decode_pdf()
            else:
                print("Please enter a valid option")
                options()
                user_choice = int(input())
            main_options()
            user_input = int(input())
        elif user_input == 6:
            options()
            user_choice = int(input())
            if user_choice == 1:
                commit_encoder_decoder.encode_commit()
            elif user_choice == 2:
                commit_encoder_decoder.decode_commit()
            else:
                print("Please enter a valid option")
                options()
                user_choice = int(input())
            main_options()
            user_input = int(input())
        else:
            print("Please input a valid option")
            main_options()
            user_input = int(input())


if __name__ == "__main__":
    main()