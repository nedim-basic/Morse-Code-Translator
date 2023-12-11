# Define the Morse code dictionary
morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

def to_morse_code(text):
    # Convert the text to uppercase
    text = text.upper()
    
    # Initialize the result string
    result = ''
    
    # Iterate over each character in the text
    for char in text:
        # If the character is a space, add a space to the result string
        if char == ' ':
            result += '  '
        # If the character is not a space, get its Morse code equivalent from the dictionary and add it to the result string
        else:
            result += morse_dict[char] + ' '
    
    # Return the result string
    return result

def to_latin(morse_code):
    # Define the reverse Morse code dictionary
    reverse_morse_dict = {value: key for key, value in morse_dict.items()}
    
    # Split the Morse code string into individual codes
    codes = morse_code.split()
    
    # Initialize the result string
    result = ''
    
    # Iterate over each code in the list
    for code in codes:
        # If the code is a space, add a space to the result string
        if code == ' ':
            result += ''
        # If the code is not a space, get its English equivalent from the reverse Morse code dictionary and add it to the result string
        else:
            result += reverse_morse_dict[code]
    
    # Return the result string
    return result

# Define the menu function
while True :
    print('1. Morse to Latin')
    print('2. Latin to Morse')
    print('3. Quit')
    choice = input('Enter your choice: ')
    if choice == '1':
        print("Use space between each letter ")
        morse_code = input('Enter the Morse code: ')
        print(to_latin(morse_code))
    elif choice == '2':
        text = input('Enter the text: ')
        print(to_morse_code(text))
    elif choice == '3':
        print('Thank you for using our software :)')
        break
    else:
        print('Invalid choice')






