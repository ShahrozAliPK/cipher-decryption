# Import Libraries and Functions
from sys import argv, exit
from alpha import test_alpha

# Keep prompting for valid user input
while (True):

    # Ask for user input
    user_text = input("\nWhat you are looking for ? ")

    # Pass input string to function
    check = test_alpha(user_text)

    # If function returns True
    if check == True:
        break
    
    # If not correct input is supplied
    print("\nEnter Correct Text!\n")

# Keep prompting till valid input
while (True):

    # Ask for user input
    encrypt_text = input("\nEncrypted text: ")

    # Pass input string to function
    check = test_alpha(encrypt_text)

    # If function returns True, Exit the loop
    if check == True:
        break
    
    # If not correct input is supplied
    print("\nEnter Correct Text!\n")

# String to store decrypted text
decrypted = ""

# Apply key from 1 - 25 for decryption
for key in range(1, 26):

    # Print key no.
    print("\nKey: ", key)

    # Iterate character by character
    for i in range(len(encrypt_text)):

        # Get ASCII value of char
        ascii_val = ord(encrypt_text[i])

        # If Uppercase
        if ascii_val >= 65 and ascii_val <= 90:

            # Encrypt the char with user key, Store in the string
            char_decipher = ((((ascii_val - key) - 65) % 26) + 65)
            decrypted += chr(char_decipher)

        # If Lowercase
        if ascii_val >= 97 and ascii_val <= 122:

            # Encrypt the char with user key, Store in the string
            char_decipher = ((((ascii_val - key) - 97) % 26) + 97)
            decrypted += chr(char_decipher)

        # If ith char is space, Store in the string
        if encrypt_text[i] == " ":

            decrypted += encrypt_text[i]

    # If user input matches with decrypted text, Stop the program
    if decrypted == user_text:

        print(decrypted, "[ MATCHED ]", "\n")
        print("Developed By Syed Shehroz Ali\n")
        exit(0)

    # Else, Print decrypted text
    else:

        print(decrypted, "\n")

    # Make string empty again for new decrypted text
    decrypted = ""

print("No match found!\n")
print("Developed By Syed Shehroz Ali\n")
exit(1)
