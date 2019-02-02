class Loop:
	def __init__(self, x=0):
		self.x = x
		
	def forloop(self):
		i = 0
		for i in range(0,10):
			print(self.x)
			self.x += 1
			i = i+1
if __name__ == "__main__":
	f = Loop()
	f.forloop()

