from enum import Enum

class State(Enum):
    IDLE = 0
    HOVER = 1
    PRESSIN = 2
    PRESSOUT = 3

class ButtonModel():
    def __init__(self, parent):
        self.parent = parent

        self.action = self.onClickEvent
        self.state = State.IDLE
    
    def onClickEvent(self):
        print("click")

    def enterHover(self):
        if self.state == State.IDLE:
            self.state = State.HOVER
        elif self.state == State.PRESSOUT:
            self.state = State.PRESSIN

    def leaveHover(self):
        if self.state == State.HOVER:
            self.state = State.IDLE
        elif self.state == State.PRESSIN:
            self.state = State.PRESSOUT

    def entrePress(self):
        if self.state == State.HOVER:
            self.state = State.PRESSIN

    def leavePress(self):
        if self.state == State.PRESSOUT:
            self.state = State.IDLE
        elif self.state == State.PRESSIN:
            self.action()
            self.state = State.HOVER

    