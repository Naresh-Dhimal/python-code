class Operation:
    def add(self, a_num1, a_num2):
        return a_num1 + a_num2

    def diff(self, num1, num2):
        return num1 - num2
    
    def mul(self, m_num1, m_num2):
        return m_num1 + m_num2
    
    def div(self, d_num1, d_num2):
        return d_num1 / d_num2
    
    def expo(self, e_num1, e_num2):
        return e_num1 ** e_num2
    
    def floor(self,f_num1, f_num2):
        return f_num1 // f_num2
    

operation1 = Operation()
result = operation1.diff(num1=5, num2=6)
print(result)
    