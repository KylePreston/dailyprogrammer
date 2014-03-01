# Disemvoweling means removing the vowels from text
vowel = 'aeiou'
print "Press CTRL-Z to escape"
def disemvoweler(sentence):
	words = sentence.strip().split()
	vowels = list()

	for i in range(len(words)):
		for char in words[i]:
			if char in vowel:
				vowels.append(char)
				words[i] = words[i].replace(char, "")

	return "".join(vowels), "".join(words)

while True:
	sent = raw_input("Enter your sentence: ")

	print disemvoweler(sent)
