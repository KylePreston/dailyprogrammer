# /r/dailyprogrammer Tree Generation Challenge
# Kyle Preston

def tree(height):
	n = 1
	space = height
	for x in range (0, height):
		print (" " * space + "@" * n)
		n += 2; space -= 1

ht = int(raw_input('How high should your tree be? '))

tree(ht)
print (" " * (ht - 1) + "===")
