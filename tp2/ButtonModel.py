class ButtonModel():
    def __init__(self, button):
        self.idle = True
        self.hover = False
        self.pressIn = False
        self.pressOut = False
        self.action = self.onClickEvent

    

    def onClickEvent(self):
        print("Button clicked")