###################################
#####        Ship Class       #####
###################################

class Ship(object):
    def __init__(self):
        self.keyInputs = {
            # key: dx
            'left': -10,
            'right': 10
        }
        self.draw()

    def handleKeyInput(self, key):
        #### START OF BLOCK SHIP_KEY_INPUTS ####

        # Get the input from the key and attempt to move the ship using it.
        ### (HINT: Look at what we have defined in the .__init__() method!)
        ### Place Your Code Here ###
        self.attemptMove(self.keyInputs[key])
        pass

        #### END OF BLOCK ####


    def attemptMove(self, dx):
        #### START OF BLOCK SHIP_TRY_MOVE ####

        # Make sure moving the ship keeps it on the canvas. If it does,
        # move the ship and return True. Otherwise, return False.
        ### (HINT: we have defined a .move() method for you below.
        ### Place Your Code Here ###
    
        if 0 <= self.drawing.centerX + dx <= 400:
            self.move(dx)
            return True
        return False

        #### END OF BLOCK ####

    def move(self, dx):
        # This moves the ship.
        self.drawing.centerX += dx

    ##### Drawing Functions #####

    def draw(self):
        self.drawing = Rect(200, 340, 35, 70, align='center')

###################################
#####      Event Handers      #####
###################################

def onKeyHold(keys):
    for key in keys:
        if (key in ship.keyInputs):
            ship.handleKeyInput(key)

###################################
#####     Initialize Game     #####
###################################

# Instantiate game objects.
ship = Ship()

