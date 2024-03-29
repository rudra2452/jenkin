class A:
    def displayA(self):
        print("Prem is learning Python,A")
class B(A):
    def displayB(self):
        print("he was confused but God is helping him now, B")

Obj=B()
Obj.displayA()
Obj.displayB()

#o/p=Prem is learning Python,A
#he was confused but God is helping him now, B