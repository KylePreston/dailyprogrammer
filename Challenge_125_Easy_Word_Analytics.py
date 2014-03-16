# This is my python solution to the /r/dailyprogrammer
# Word Analytics challenge

"""You're a newly hired engineer for a brand-new company that's building a "killer Word-like application". You've been specifically assigned to implement a tool that gives the user some details on common word usage, letter usage, and some other analytics for a given document! More specifically, you must read a given text file (no special formatting, just a plain ASCII text file) and print off the following details:

    Number of words
    Number of letters
    Number of symbols (any non-letter and non-digit character, excluding white spaces)
    Top three most common words (you may count "small words", such as "it" or "the")
    Top three most common letters
"""

abc = 'abcdefghijklmnopqrstuvwxyz'

def openFile(txt_file):
	word_list = [word.lower() for line in open(txt_file, 'r') for word in line.split()]
	return word_list

def returnNumberOfWords(word_list):
	"""Return the number of words in zee file """

	return len(word_list)

def returnLetterSymbolNumberCount(word_list):
	"""Return the number of letters, symbols and numbers in zee file """

	number_of_characters, number_of_symbols, number_of_numbers = 0, 0, 0

	for word in word_list:
		for char in word:
			if char in abc:
				number_of_characters += 1
			elif type(char) != int:
				number_of_symbols += 1
			else:
				number_of_numbers += 1

	return number_of_characters, number_of_symbols, number_of_numbers

def returnThreeMostCommonWords(word_list):
	"""Return the three most common words found in the file """

	max_words = {}

	for word in word_list:
		if word_list.count(word) > 1:
			max_words[word_list.count(word)] = word

	max_word_list = sorted(max_words.items(), reverse = True)

	return [max_word_list[i][1] for i in range(3)]


