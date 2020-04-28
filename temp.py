class A:
    def __init__(self):
        self.name="hello"

def test(a):
    print(a.name)

test(A())