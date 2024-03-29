from typing import Self


class A:
    def displayA(self):
        print("Prem is learning Python,A")
class B(A):
    def displayB(self):
        print("he was confused but God is helping him now, B")
class C(B):
    def displayC(self):
        print("he will be succesfull for sure,C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
#o/p : all A,B and C were shown in the output
