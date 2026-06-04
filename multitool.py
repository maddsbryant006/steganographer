import audio_encoder_decoder 
import image_encoder_decoder
import qr_encoder_decoder
import pdf_encoder_decoder
import commit_encoder_decoder

def main_options():
    print("------------------------------------------")
    print("Welcome to the Multi-Tool Steganographer")
    print("------------------------------------------")
    print("1. Image")
    print("2. Audio")
    print("3. QR Code")
    print("4. PDF")
    print("5. Git Commits")
    print("6. Exit")
    print("------------------------------------------")

def options():
    print("1. Encode")
    print("2. Decode")
    print("------------------------------------------")

def main():
    #main function for user option to encode or decode an image or audio
    main_options()
    user_input = int(input())

    while user_input != 6:
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
                pdf_encoder_decoder.encode_pdf()
            elif user_choice == 2:
                pdf_encoder_decoder.decode_pdf()
            else:
                print("Please enter a valid option")
                options()
                user_choice = int(input())
            main_options()
            user_input = int(input())
        elif user_input == 5:
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