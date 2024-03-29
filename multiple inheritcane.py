class A:
    def displayA(self):
        print("Prem is learning Python,A")
class B:
    def displayB(self):
        print("he was confused but God is helping him now, B")
class C(A,B):
    def displayC(self):
        print("he will be succesfull for sure,C")
obj=C()
obj.displayC()
obj.displayA()
obj.displayB()