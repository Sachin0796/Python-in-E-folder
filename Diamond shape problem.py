# Python handles Diamond shape problem very gracefully. Class name whichever is written first is taken into consideration while accessing any paticular variable or method

class A:
    def met(self):
        print("Method in A")

class B(A):
    def met(self):
        print("Method in B")

class C(A):
    def met(self):
        print("Method in C")

class D(B,C):
    pass
    # def met(self):
    #     print("Method in D")

a=A()
b=B()
c=C()
d=D()

d.met()