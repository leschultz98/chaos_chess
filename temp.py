class A:
    def __init__(self):
        self.name="hello"

def test(a):
    print(a.name)

test(A())

a=A()
b=A()
print(a==b)

