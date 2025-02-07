class Convertation():
    def _init_(self):
        self.sentance = ""
    def getString(self):
        self.sentance = input()
    def printStr(self):
        print(self.sentance.upper())

text = Convertation()
text.getString()
text.printStr()   