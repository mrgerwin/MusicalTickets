from guizero import *
from viperdb import *

def wafflePressed():
    pass
def purchasePressed():
    pass
    
app = App(title="Musical Tickets", width=600, height=400)

instructionText = Text(app, text="Click On Available Seats")
seatsWaffle = Waffle(app, width=20, height=8, command=wafflePressed)
purchaseButton = PushButton(app, text="Purchase", command=purchasePressed)

app.display()