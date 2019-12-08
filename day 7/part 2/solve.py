import threading
import time

with open("C:\\Users\\gabirat\\Desktop\\Python\\adventofcode\\day 7\\part 2\\input.txt", "r") as file:
    data = [int(val) for val in file.read().split(",")]

class IntPC:
    def __init__(self, program):
        self.mem = program.copy()
        self.registers = [None, None, None]
        self.pc = 0
        self.halted = False
        self.jump_table = {
            1: ("add", 3),
            2: ("mul", 3),
            3: ("inp", 1),
            4: ("out", 1),
            5: ("jnz", 2),
            6: ("jz", 2),
            7: ("lt", 3),
            8: ("eq", 3),
            99: ("halt", 0)
        }
        self.parameter_modes = [] # 0 - arg1, 1 - arg2, 2 - arg3

    def add(self):
        self.mem[self.registers[2]] = self.mem[self.registers[0]] + self.mem[self.registers[1]]
        self.pc += 4

    def mul(self):
        self.mem[self.registers[2]] = self.mem[self.registers[0]] * self.mem[self.registers[1]]
        self.pc += 4

    def inp_wrapper(self):
        return int(input())

    def inp(self):
        self.mem[self.registers[0]] = self.inp_wrapper()
        self.pc += 2

    def out_wrapper(self, val):
        print(val)

    def out(self):
        self.out_wrapper(self.mem[self.registers[0]])
        self.pc += 2
    
    def jnz(self):
        self.pc = self.mem[self.registers[1]] if self.mem[self.registers[0]] != 0 else (self.pc + 3)

    def jz(self):
        self.pc = self.mem[self.registers[1]] if self.mem[self.registers[0]] == 0 else (self.pc + 3)

    def lt(self):
        self.mem[self.registers[2]] = 1 if self.mem[self.registers[0]] < self.mem[self.registers[1]] else 0
        self.pc +=4

    def eq(self):
        self.mem[self.registers[2]] = 1 if self.mem[self.registers[0]] == self.mem[self.registers[1]] else 0
        self.pc +=4

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
            op_name, op_argc = self.jump_table[self.get_op()]
            for i in range(op_argc):
                self.registers[i] = self.mem[self.pc + (i + 1)] if self.parameter_modes[i] == 0 else (self.pc + (i + 1))
            #print(self.parameter_modes)
            #print(self.get_op())
            op = getattr(self, op_name, lambda: "INVALID OPERATION")
            if op == "INVALID OPERATION":
                print("INVALID OPERATION: %i AT memory %i\n" % (self.mem[self.pc], self.pc))
                print("MEMDUMP: %s" % str(self.mem))
                exit()

            op()
        #return self.mem

class Amplifier(IntPC, threading.Thread):
    def __init__(self, program, phase, dev_out, name):
        IntPC.__init__(self, program)
        threading.Thread.__init__(self)
        self.in_val = None
        self.out_val = None
        self.phase = phase
        #self.dev_in = dev_in
        self.dev_out = dev_out
        self.config_mode = True
        self.name = name

    def inp_wrapper(self):
        if self.config_mode == True:
            self.config_mode = False
            return self.phase
        while self.in_val is None:
            time.sleep(0.0001)
        return self.in_val

    def out_wrapper(self, val):
        #print(self.name, ": ", val)
        self.in_val = None
        self.out_val = val
        if not self.dev_out.halted:
            self.dev_out.feed(val)
        

    def feed(self, val):
        self.in_val = val

max_thrust = 0
possibilitises = [5,6,7,8,9]

for i in possibilitises:
    a = possibilitises.copy()
    a.remove(i)
    for j in a:
        b = a.copy()
        b.remove(j)
        for k in b:
            c = b.copy()
            c.remove(k)
            for l in c:
                d = c.copy()
                d.remove(l)
                for m in d:
                    bruteforcer = [i,j,k,l,m]
                    #print(bruteforcer)
                    amps =  [Amplifier(data, bruteforcer[n], None, "Amp id#%i" % n) for n in range(5)]
                    amps[0].in_val = 0
                    for na in range(5):
                        amps[na].dev_out = amps[(na + 1) % 5]
                    for na in range(5):
                        amps[na].start()
                    amps[-1].join()
                    max_thrust = amps[-1].out_val if amps[-1].out_val > max_thrust else max_thrust

print(max_thrust)