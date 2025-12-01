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
			3: "inp",
			4: "out",
			99: "halt"
		}
		self.parameter_modes = [] # 0 - arg1, 1 - arg2, 2 - arg3

	def add(self):
		in1 = self.mem[self.pc + 1] if self.parameter_modes[0] == 0 else (self.pc + 1)
		in2 = self.mem[self.pc + 2] if self.parameter_modes[1] == 0 else (self.pc + 2)
		out = self.mem[self.pc + 3] if self.parameter_modes[2] == 0 else (self.pc + 3)
		#print("OP", self.mem[self.pc])
		#print("Modes", self.parameter_modes)
		#print("Params", in1, in2, out)
		self.mem[out] = self.mem[in1] + self.mem[in2]
		self.pc += 4

	def mul(self):
		in1 = self.mem[self.pc + 1] if self.parameter_modes[0] == 0 else (self.pc + 1)
		in2 = self.mem[self.pc + 2] if self.parameter_modes[1] == 0 else (self.pc + 2)
		out = self.mem[self.pc + 3] if self.parameter_modes[2] == 0 else (self.pc + 3)

		self.mem[out] = self.mem[in1] * self.mem[in2]
		self.pc += 4

	def inp(self):
		arg = self.mem[self.pc + 1] if self.parameter_modes[0] == 0 else (self.pc + 1)
		self.mem[arg] = int(input())
		self.pc += 2

	def out(self):
		arg = self.mem[self.pc + 1] if self.parameter_modes[0] == 0 else (self.pc + 1)
		print(self.mem[arg])
		self.pc += 2

	def halt(self):
		# print("FINISHED:")
		# print(self.mem)
		self.halted = True

	def set_parameter_modes(self): #do it with integer division
		val = self.mem[self.pc]
		m3 = val // 10000
		m2 = (val % 10000) // 1000
		m1 = (val % 1000) // 100
		self.parameter_modes = [m1, m2, m3]

	def get_op(self):
		op_and_params = self.mem[self.pc]
		return op_and_params % 100

	def run(self):
		while not self.halted:
			self.set_parameter_modes()
			#print(self.parameter_modes)
			#print(self.get_op())
			op = getattr(self, self.jump_table[self.get_op()], lambda: "INVALID OPERATION")
			op()
			if op == "INVALID OPERATION":
				print("INVALID OPERATION: %i AT memory %i\n" % (self.mem[self.pc], self.pc))
				print("MEMDUMP: %s" % str(self.mem))
				exit()
		return self.mem

vm = IntPC(data)
m = vm.run()
print(m)