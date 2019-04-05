def encode(message):
# Function that encodes your string

	morse_code = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	"0": "-----",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",
	" ": "(space)"
	}
# Dictonary with all caracters/numbers to morse code

	message = message.upper()
	codedmsg = ""
# Makes you massage in all CAPS, and creates an empy string

	for x in message:
		codedmsg = codedmsg + morse_code[x] + " "
# Takes your message imput and turns it into morse code

	return codedmsg
# Returns the morse code

def decode(secret):
# function that decodes your string

	pass



if __name__ == "__main__":
# execute program if started from original file

	secret = encode("Hello World")
# Defines secret as the string with the morse code

	print(secret)
# Prints the morse code