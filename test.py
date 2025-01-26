class A:
    def foo(self):
        print("helloA")

class B:
    def foo(self):
        print("helloB")

class C(A, B):  # C inherits from both A and B
    def foo(self):
        super().foo()  # Calling the foo() method from the next class in the MRO

# Create an instance of C
new = C()
new.foo()
