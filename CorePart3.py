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
        self.isRotating = False

    def handleKeyInput(self, key):

        # Get the input from the key and attempt to move the ship using it.
        x = self.attemptMove(self.keyInputs[key])
        pass


        #### START OF BLOCK KEY_INPUT_ROTATE ####

        # If the attempted move fails, stop rotating the ship.
        ### Place Your Code Here ###
        if not x:
            self.isRotating = False
        else:
            self.isRotating = True
        
        pass

        #### END OF BLOCK ####

    def handleOnKeyRelease(self, key):
        # Straighten the boat.
        self.drawing.rotateAngle = 0

    def attemptMove(self, dx):

        # Make sure moving the ship keeps it on the canvas. If it does,
        # move the ship and return True. Otherwise, return False.
    
        if 0 <= self.drawing.centerX + dx <= 400:
            self.move(dx)
            return True
        return False


    def move(self, dx):
        # This moves the ship.
        self.drawing.centerX += dx

        #### START OF BLOCK ROTATE_MOVE ####

        # Rotate the ship to have a rotateAngle of 3/4ths the dx.
        ### Place Your Code Here ###
        if self.isRotating:
            self.drawing.rotateAngle = .75 * dx
        pass

        #### END OF BLOCK ####

    ##### Helper Functions #####

    def checkForCollision(self):
        #### START OF BLOCK COLLISION_CHECK ####

        # Check if the ship hits any of the obstacles. If so, pause the app and
        # make the ship red.
        ### (HINT: You need to check if the ship's drawing hits the obstacles group,
        #          not the ship itself.)
        ### Place Your Code Here ###
        pass

        #### END OF BLOCK ####

    ##### Drawing Functions #####

    def draw(self):
        self.drawing = Rect(200, 340, 35, 70, align='center')

###################################
#####      Event Handling     #####
###################################

def onKeyHold(keys):
    for key in keys:
        if (key in ship.keyInputs):
            ship.handleKeyInput(key)

def onKeyRelease(key):
    ship.handleOnKeyRelease(key)

def onStep():
    for obstacle in obstacles:
        obstacle.centerY += 3
        if (obstacle.top > 400):
            obstacles.remove(obstacle)

    # Create a new iceberg if it is time.
    app.step += 1
    if (app.step % 15 == 0):
        obstacles.add(
            Circle(randrange(0, 400), randrange(-100, 0), 10)
        )

    ship.checkForCollision()

###################################
#####     Initialize Game     #####
###################################

app.step = 0

# Instantiate game objects.
obstacles = Group()
ship = Ship()

