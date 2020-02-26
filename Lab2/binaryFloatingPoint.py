from binaryAriphmetic import binaryMultiplication, binaryAddition, binarySubtraction, shiftLeft

if __name__ == "__main__":

    class BinaryFloat:
        def __init__(self, sign, exponent, mantissa):
            self.sign = sign
            self.exponent = exponent
            self.mantissa = mantissa
        
        @property
        def exponent(self):
            return self.__exponent

        @exponent.setter
        def exponent(self, exponent):
            if isinstance(exponent, list):
                if len(exponent) < 8:
                    self.__exponent = [0,] * (8 - len(exponent)) + exponent
                elif len(exponent) > 8:
                    separator = exponent.index(1)
                    exponent = exponent[separator:]
                    if len(exponent) > 8:
                        self.__exponent = [1,] * 8
                    self.__exponent = exponent
                else:
                    self.__exponent = exponent
            else:
                self.__exponent = [0,] * 8
        
        @property
        def mantissa(self):
            return self.__mantissa

        @mantissa.setter
        def mantissa(self, mantissa):
            if isinstance(mantissa, list):
                if len(mantissa) < 23:
                    self.__mantissa = mantissa + [0,] * (23 - len(mantissa))
                elif len(mantissa) > 23:
                    separator = mantissa.index(1)
                    mantissa = mantissa[separator:]
                    while (len(mantissa) > 23):
                        mantissa.pop()
                    self.__mantissa = mantissa
                else:
                    self.__mantissa = mantissa
            else:
                self.__mantissa = [0,] * 23

        def __str__(self):
            toString = str(self.sign) + " | "
            for bit in self.exponent:
                toString = toString + str(bit)

            toString = toString + " | "

            for bit in self.mantissa:
                toString = toString + str(bit)

            return toString

    def binaryFloatMultiplication(num1, num2):
        print("1) Check if one/both operands = 0 or infinity. Set the result to 0 or inf. i.e. exponents = all '0' or all '1'.")
        if len(list(filter(lambda x: x == 1, num1.exponent))) == 0 or len(list(filter(lambda x: x == 1, num2.exponent))) == 0:
            return "One or Both terms are '0'"
        else:
            result = BinaryFloat(0, [0,], [0,])
            print("2) S1, the signed bit of the multiplicand is XOR'd with the multiplier signed bit of S2. The result is put into the resultant sign bit.")
            result.sign = num1.sign ^ num2.sign
            print(f"\tX3 SIGN BIT: {result.sign}")
            print("3) The mantissa of the Multiplier (M1) and multiplicand (M2) are multiplied and the result is placed in the resultant field of the mantissa (truncate/round the result for 24 bits)")

            tempMantissa = binaryMultiplication([1,] + num1.mantissa, [1,] + num2.mantissa)

            print(f"\tMULTIPLY SIGNIFICANDS RESULT: {tempMantissa}")

            result.mantissa = tempMantissa
            result.mantissa.pop(0)
            result.mantissa = shiftLeft(result.mantissa)

            print("4) The exponents of the Multiplier (E1) and the multiplicand (E2) bits are added and the base value is subtracted from the added result.",
                  "\nThe subtracted result is put in the exponential field of the result block.")
            bias = binarySubtraction([0,1,1,1,1,1,1,1], [0,0,0,0,0,0,0,1])[0]
            print(bias)

            tempExponent = binaryAddition(num1.exponent, num2.exponent)
            tempExponent = binarySubtraction(tempExponent, bias)[0]
            result.exponent = tempExponent
            print(f"\tNORMALIZATION: \n\t\tBefore: {tempExponent}\n\t\tAfter: {result.exponent}")


            return result

    x1 = BinaryFloat(0, [1,0,0,0,0,1,0,1], [1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    x2 = BinaryFloat(0, [1,0,0,0,0,0,1,0], [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    print(f"x1: {x1}")
    print(f"x2: {x2}")

    x3 = binaryFloatMultiplication(x1, x2)

    print(f"x1: {x1}")
    print(f"x2: {x2}")
    
    print(f"X3: {x3}")

    