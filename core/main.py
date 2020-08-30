import string

class Engine:

	def __init__(self, file):
		# Main variables
		self.file = file
		self.values = {}
		self.punc = string.punctuation
		# Workflow Start
		self.read_file()
		self.sort()
		# Workflow End

	def read_file(self):
		with open(self.file, "r+", encoding = "utf-8") as f:
			f = f.read().split()

			for word in f:
				word = word.lower() # Turning string into Lowercase
				word = word.translate(str.maketrans("","", self.punc)) # removing the punctuations from string
				if word not in self.values:
					self.values[word] = 1

				else:
					self.values[word] += 1

	def last(self, x):
		return x[-1]


	def sort(self):
		sorted_output = sorted(self.values.items(), key = self.last)

		for i in sorted_output: 
			print(i[0], ":", i[1])

if __name__ == "__main__":
	e = Engine("isimler.txt")
		
	