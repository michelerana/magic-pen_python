class Pen(object):
    def __init__(self):
        self.color = "black"

class NormalPen(Pen):
    def __init__(self):
        Pen.__init__(self)

class MagicPen(Pen):
    magicOn = 1

    def __init__(self, magicText):
        self.magicText = magicText
        Pen.__init__(self)

    @staticmethod
    def toggleMagic():
        if MagicPen.magicOn == 1:
            MagicPen.magicOn = 0
        else:
            MagicPen.magicOn = 1

    @staticmethod 
    def isMagicOn():
        return MagicPen.magicOn

    def getText(self, text):
        if MagicPen.magicOn != 0: 
            return self.magicText
        else:
            return text

class Person(object):
    def __init__(self, name):
        self.name = name
    
    def write(self, pen, text):
        pen.text = text
	print pen.text

