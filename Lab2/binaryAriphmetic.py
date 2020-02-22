if __name__ == "__main__":

    def binaryAddition(a, b):
        print("\n\t\tADDITION:\n")
        diff = len(a)-len(b)

        if (diff > 0):
            b = ([0,] * diff) + b   
        elif (diff < 0):
            a = ([0,] * (-diff)) + a 

        print(f"\t\tTerm 'a': {a}",
              f"\n\t\tTerm 'b': {b}\n")

        carry = 0
        sum = [0] * len(a)

        for i in reversed(range(len(a))):
                d = (a[i] + b[i] + carry) // 2
                sum[i] = (a[i] + b[i] + carry) - 2*d
                carry = d
                print(f"\t\t+Partial sum: {sum}     Carry: {carry}")
        
        if (carry == 1):
            sum = [carry] + sum

        print(f"\n\t\t+Final sum:   {sum}")
        return sum

    def shiftRight(reg):
        return [0,] + reg

    def binaryMultiplication(multiplicand, multiplier):
        print("MULTIPLICATION:\n")
        
        multiplicand = [0,] * (8 - len(multiplicand)) + multiplicand
        multiplier = [0,] * (8 - len(multiplier)) + multiplier
        print(f'\tMultiplicand: {multiplicand}',
              f'\n\tMultiplier:   {multiplier}\n')

        register = [0,] * 16
        print(f"\t*Register: {register}")
        print(f"\t+Add multiplier to register")
        register = binaryAddition(register, multiplier)

        iteration = 0

        while (iteration <= len(multiplicand)):
            currentBit = register.pop()
            print("\t*Shift register right")
            print(f"\tPop bit: {currentBit}")
            register = shiftRight(register)
            print(f"\t*Register: {register}")

            if (currentBit == 1):
                print("\t+Add multiplicand to first half of register")
                register = binaryAddition(register[:8], multiplicand) + register[8:]
                print(f"\t*Register: {register}")

            iteration += 1

        return register

    res = binaryMultiplication([1,1,1,1], [1,1,1,1])
    print(f"\n=RESULT: {res}\n")