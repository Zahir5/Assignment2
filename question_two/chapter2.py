# Function to separate numbers and letters from the string
def separate_numbers_and_letters(s):
    number_substring = ''.join(char for char in s if char.isdigit())
    letter_substring = ''.join(char for char in s if char.isalpha())
    return number_substring, letter_substring

# Function to convert even numbers to ASCII Code Decimal Values
def convert_even_numbers_to_ascii(number_substring):
    even_numbers = [int(num) for num in number_substring if int(num) % 2 == 0]
    ascii_values = [ord(chr(num)) for num in even_numbers]
    return even_numbers, ascii_values

# Function to convert uppercase letters to ASCII Code Decimal Values
def convert_uppercase_letters_to_ascii(letter_substring):
    uppercase_letters = [char for char in letter_substring if char.isupper()]
    ascii_values = [ord(char) for char in uppercase_letters]
    return uppercase_letters, ascii_values


def long_string_separator(example_string):
    s=example_string 

    # Separate numbers and letters
    number_substring, letter_substring = separate_numbers_and_letters(s)

    # Convert even numbers to ASCII Code Decimal Values
    even_numbers, even_ascii_values = convert_even_numbers_to_ascii(number_substring)

    # Convert uppercase letters to ASCII Code Decimal Values
    uppercase_letters, uppercase_ascii_values = convert_uppercase_letters_to_ascii(letter_substring)

    # Print the results
    print("Number Substring:", number_substring)
    print("Letter Substring:", letter_substring)
    print("Even Numbers:", even_numbers)
    print("ASCII Values of Even Numbers:", even_ascii_values)
    print("Uppercase Letters:", uppercase_letters)
    print("ASCII Values of Uppercase Letters:", uppercase_ascii_values)

# provide sample string during function calling 
# long_string_separator('56aAww1984skr235270amn145ss785fsq31D0')



# =============================== part2 of the quest ==================================


def decrypt_cryptogram(cryptogram, shift):
    decrypted_text = ""
    for char in cryptogram:
        if char.isalpha():
            # Shift the alphabetic characters
            shifted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A')) if char.isupper() else chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            decrypted_text += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            decrypted_text += char
    return decrypted_text

def find_shift_key(cryptogram):
    for shift in range(26):
        decrypted_text = decrypt_cryptogram(cryptogram, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Given cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"


# Find the shift key in our case the shift key is 13 and can be seen in the print statements
# find_shift_key(cryptogram)


