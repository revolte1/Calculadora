class Calc:
    def sumar(self, num1, num2):
        if self.is_invalid(num1, num2):
            return "Invalid"
        return num1 + num2

    def restar(self, num1, num2):
        if self.is_invalid(num1, num2):   
            return "Invalid"               
        result = num1 - num2
        if result < 0:
            return "Invalid"   
        return result

    def multiplicar(self, num1, num2):
        if self.is_invalid(num1, num2):
            return "Invalid"
        return num1 * num2

    def dividir(self, num1, num2):
        if self.is_invalid(num1, num2):
            return "Invalid"
        return (num1 / num2) if num2 != 0 else "Invalid"

    def is_invalid(self,num1, num2):
        if num1 < 0 or num2 <0:
            return True
        return False

    def exponente(self, num1, num2):
        if self.is_invalid(num1, num2):
            return "Invalid"
        return num1 ** num2