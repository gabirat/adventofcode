with open("input.txt", "r") as file:
	data = [int(val) for val in file.read().split(",")]


class IntPC:
	def __init__(self, program):
		self.mem = program.copy()
		self.pc = 0
		self.halted = False
		self.jump_table = {
			1: "add",
			2: "mul",
			99: "halt"
		}

	def add(self):
		in1 = self.mem[self.pc + 1]
		in2 = self.mem[self.pc + 2]
		out = self.mem[self.pc + 3]

		self.mem[out] = self.mem[in1] + self.mem[in2]
		self.pc += 4

	def mul(self):
		in1 = self.mem[self.pc + 1]
		in2 = self.mem[self.pc + 2]
		out = self.mem[self.pc + 3]

		self.mem[out] = self.mem[in1] * self.mem[in2]
		self.pc += 4

	def halt(self):
		# print("FINISHED:")
		# print(self.mem)
		self.halted = True

	def run(self):
		while not self.halted:
			op = getattr(self, self.jump_table[self.mem[self.pc]], lambda: "INVALID OPERATION")
			op()
			if op == "INVALID OPERATION":
				print("INVALID OPERATION: %i AT memory %i\n" % (self.mem[self.pc], self.pc))
				print("MEMDUMP: %s" % str(self.mem))
				exit()
		return self.mem[0]


for i in range(99):
	for j in range(99):
		new_data = data.copy()
		new_data[1] = i
		new_data[2] = j
		vm = IntPC(new_data)
		if vm.run() == 19690720:
			print("Inputs were: %i and %i" % (i,j))
			print("Answer is: %i" % (100* i + j))