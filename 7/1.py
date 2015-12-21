import sys

class Circuit():

    def __init__(self):
        self.varD = {}
        self.ops = {'NOT': self.NOT,
                    'AND': self.AND,
                    'OR': self.OR,
                    'LSHIFT':self.LSHIFT,
                    'RSHIFT':self.RSHIFT}
        self.busWidth = 16
        self.false = [False]*self.busWidth

    def parse(self,line):
        line = line.split('->')
        sigStr = line[0]
        destStr = line[1].strip()
        sig = self.getSig(sigStr)
        return sig,destStr

    def assign(self,sig,destStr):
        self.varD[destStr] = sig

    def getSig(self,sigStr):
        sig = sigStr.split(' ')
        args = []; op = []
        while not sig == []:
            token = sig.pop(0)
            if token.isnumeric():
                args.append(self.int2arr(int(token)))
            elif token in self.ops:
                op = token
            else:
                if token in self.varD:
                    args.append(self.varD[token])
                else:
                    self.varD[token] = self.false
                    args.append(self.false)
        return self.computeSig(args,op)

    def computeSig(self,args,op):
        if op == []:
            return args[0]
        else:
            return self.ops[op](args)

    def NOT(self,args):
        string = args[0]
        return [not a for a in string]

    def AND(self,args):
        string1 = args[0]
        string2 = args[1]
        return [a and b for a,b in zip(string1,string2)]

    def OR(self,args):
        string1 = args[0]
        string2 = args[1]
        return [a or b for a,b in zip(string1,string2)]

    def LSHIFT(self,args):
        string = args[0]
        shift = self.arr2int(args[1])
        return string[shift:]+[False]*shift

    def RSHIFT(self,args):
        string = args[0]
        shift = self.arr2int(args[1])
        return [False]*shift+string[:-shift]

    def int2arr(self,num):
        binaryString = bin(num)[2:].zfill(self.busWidth)
        return [char == '1' for char in binaryString]

    def arr2int(self,arr):
        out = 0
        for ind,elem in enumerate(arr[::-1]):
            out += int(elem)*(2)**ind
        return out

circuit = Circuit()

with open(sys.argv[1]) as f:
    for line in f:
        signal, destination = circuit.parse(line)
        circuit.assign(signal,destination)

print(circuit.arr2int(circuit.varD[sys.argv[2]]))
