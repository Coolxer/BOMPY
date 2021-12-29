class A:
    def __init__(self):
        self.create()

    def my(self):
        pass

    def create(self):
        self.my()


class B(A):
    def __init__(self):
        super().__init__()

    def my(self):
        print("Bas")


obj = B()
