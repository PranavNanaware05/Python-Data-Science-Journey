class Mother:
    def __init__(self):
       super().__init__()
       print("mother is cooking")

class father:
    def __init__(self):
        super().__init__()
        print("Father is working")       


class Child(Mother,father):
    def __init__(self):
        super().__init__()
        
        print("Children is playing ")

c1=Child()
                