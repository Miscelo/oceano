
class Greatings:
    def __init__(self, saludo):
        self.saludo = saludo

    def tellIttotheWorld(self):
        return self.saludo

if __name__ == "__main__":
    misaludo = Greatings("Hello World!")
    print(misaludo.tellIttotheWorld())
