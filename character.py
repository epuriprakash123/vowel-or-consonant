s=input()
V=['a','e','i','o','u']
if (s.isalpha()):
	if s in V:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
