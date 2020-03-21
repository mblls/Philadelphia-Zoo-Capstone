import viz
import vizshape 
import vizconnect
import socket

CAVE_HEADNODE = "exx-PC"
CAVE_RENDERNODE = "render-PC"

def getHostName():
	#Conditional statement making runtime automated
	compterName = socket.gethostname()
	if compterName == socket.gethostname():
		CONFIG_FILE = "vizconnect_config_CaveFloor+ART_headnode.py"
		vizconnect.go(CONFIG_FILE)
	else:
		viz.go()

global_scene_index = 0
global_sphere = None
global_navigation_enabled = False
global_sound = None

class Node:
    def __init__(self):
        self.image = None
        self.info_image = None
        self.audio = None

        self.left = None
        self.right = None


#This will be called every time we want to swap through a scene
def load_scene(this_node, this_sphere, global_plane):
    global global_sound

	#Here we add our elephant photo to the current scene we're in
	this_texture = viz.addTexture(this_node.image)
	this_sphere.texture(this_texture)

	#Here we lock down the textbox to our scene, first we initilize
    if this_node.info_image is not None:
        print("Info Image:" + this_node.info_image)
        this_texture = viz.addTexture(this_node.info_image)
        global_plane.texture(this_texture)

    if global_sound is not None:
        global_sound.stop()

    global_sound = viz.addAudio(this_node.audio)
    global_sound.loop(viz.ON)

    if this_node.audio == "sounds/bushfield.mp3":
        global_sound.volume(.3)
    else:
        global_sound.volume(.5)

    global_sound.play()


# def globalAudio():
# 	#Creates global variable in order to constantly be looping the
# 	#audio between scenes
# 	sound = viz.addAudio('sounds/natureSounds.mp3')
# 	sound.loop(viz.ON)
# 	sound.volume(.5)
# 	sound.play()


def joystick_action():
    global current_node
    global global_sphere
    global global_navigation_enabled

    # BUTTON_TRIGGER = 'space'
    # BUTTON_1 = 'a'
    # BUTTON_2 = 'b'

    rawInput = vizconnect.getConfiguration().getRawDict("input")

    BUTTON_LEFT = 4
    BUTTON_RIGHT = 1
    BUTTON_TRIGGER = 0

    if rawInput['flystick'].isButtonDown(BUTTON_TRIGGER):
        global_navigation_enabled = False if global_navigation_enabled == True else True
        global_plane.visible(viz.TOGGLE)
        print("Navigation Enabled: " + str(global_navigation_enabled))
        print("Plane Enabled: " + str(global_plane.getVisible()) )

    if global_navigation_enabled:
        if rawInput['flystick'].isButtonDown(BUTTON_LEFT):
            print("left")
            if (current_node.left is not None):
                current_node = current_node.left
                load_scene(current_node, global_sphere, global_plane)
				# viz.playSound('sounds/click.wav',viz.SOUND_PRELOAD)

        elif rawInput['flystick'].isButtonDown(BUTTON_RIGHT):
            print("right")

            if (current_node.right is not None):
                current_node = current_node.right
                load_scene(current_node, global_sphere, global_plane)
				# viz.playSound('sounds/click.wav',viz.SOUND_PRELOAD)

            elif (current_node.left is not None):
                current_node = current_node.left
                load_scene(current_node, global_sphere, global_plane)
				# viz.playSound('sounds/click.wav',viz.SOUND_PRELOAD)

getHostName()
# globalAudio()


#===========================
#Enable full screnn anti-aliasing (FSAA) to smooth out edges
viz.setMultiSample(4)
viz.fov(60) #***How do we lock fov?

global_sphere = vizshape.addSphere(radius=128, slices=256)
global_sphere.setPosition([0,0,0])
global_sphere.setEuler(180,0,0) #rotating
#Setting hints for Vizard renderer
global_sphere.disable(viz.CULL_FACE) #Render interior, not exterior of sphere
global_sphere.disable(viz.LIGHTING) #Show full brightness of image, ignoring shading

global_plane = vizshape.addPlane(size=(5,5), axis=vizshape.AXIS_Z, cullFace = True)
global_plane.setEuler(-180,0,0)
global_plane.setPosition(5,0,10)
global_plane.disable(viz.LIGHTING)
global_plane.visible(viz.OFF)


#===========================

def define_scene_tree():

	#==================================================================
    #level1
    this_node = Node()
    this_node.image =  "elephantMerc/1start.jpg"
    this_node.info_image = "textboxes/1. welcome screen_1024x1024.png"
    this_node.audio = "sounds/bushfield.mp3"
    node01 = this_node

	#==================================================================
    #level2
    this_node = Node()
    this_node.image =  "elephantMerc/2wateringhole.jpg"
	this_node.info_image = "textboxes/2.wateringholetextbox_2048x2048.png"
    this_node.audio = "sounds/birdsfrogs.mp3"
    node01.left = this_node
    node02 = this_node

	#==================================================================
    #level 3
	#3a
    this_node = Node()
    this_node.image =  "elephantMerc/3afemalecalf.jpg"
	this_node.info_image = "textboxes/3a.femaleelephantandcalftextbox_2048x2048.png"
    this_node.audio = "sounds/bushfield.mp3"
    node02.left = this_node
	node3a = this_node

	#3b
    this_node = Node()
    this_node.image =  "elephantMerc/3bbull.jpg"
	this_node.info_image = "textboxes/3b.bullelephanttextbox.jpg"
    this_node.audio = "sounds/bull.mp3"
    node02.right = this_node
	node3b = this_node

	#==================================================================
	#level 4
	#4a
    this_node = Node()
    this_node.image =  "elephantMerc/4abathing.jpg"
	this_node.info_image = "textboxes/4a.bathingtextbox.jpg"
    this_node.audio = "sounds/rain.mp3"
    node3a.left = this_node
	node4a = this_node

	#4b
    this_node = Node()
    this_node.image =  "elephantMerc/4bplaying.jpg"
	this_node.info_image = "textboxes/4b.playingtextbox.jpg"
    this_node.audio = "sounds/bushfield.mp3"
    node3a.right = this_node
	node4b = this_node

	#4c
    this_node = Node()
    this_node.image =  "elephantMerc/4cexploring.jpg"
	this_node.info_image = "textboxes/4c.exploringtextbox.jpg"
    this_node.audio = "sounds/morning.mp3"
    node3b.left = this_node
	node4c = this_node

	#4d
    this_node = Node()
    this_node.image =  "elephantMerc/4d.jpg"
	this_node.info_image = "textboxes/4d.fightingbehaviortextbox.jpg"
    this_node.audio = "sounds/bull.mp3"
    node3b.right = this_node
	node4d = this_node

	#==================================================================
	#level 5
    this_node = Node()
	this_node.image =  "elephantMerc/5mating.jpg"
	this_node.info_image = "textboxes/5.matingtextbox.jpg"
    this_node.audio = "sounds/jungle.mp3"
    node4a.left = this_node
    node4b.left = this_node
    node4c.left = this_node
    node4d.left = this_node
	node5 = this_node

	#==================================================================
	#level 6
    this_node = Node()
	this_node.image =  "elephantMerc/6eating.jpg"
	this_node.info_image = "textboxes/6.eatingtextbox.jpg"
    this_node.audio = "sounds/bushfield.mp3"
    node5.left = this_node
	node6 = this_node

	#==================================================================
	#level 7
    this_node = Node()
	this_node.image =  "elephantMerc/7threats.jpg"
	this_node.info_image = "textboxes/7. threatstextbox.jpg"
    this_node.audio = "sounds/cricket.mp3"
    node6.left = this_node
	node7 = this_node

	#==================================================================
	#level 8
    this_node = Node()
	this_node.image =  "elephantMerc/8funfacts.jpg"
	this_node.info_image = "textboxes/8.funfactstextbox.jpg"
    this_node.audio = "sounds/rain.mp3"
    node7.left = this_node
	node8 = this_node

	#==================================================================`
	#level 9
    this_node = Node()
	this_node.image =  "elephantMerc/9sleeping.jpg"
	this_node.info_image = "textboxes/9.sleeptextbox.jpg"
    this_node.audio = "sounds/crickets.mp3"
    node8.left = this_node
	node9 = this_node

 #    # Should loop us back to the   addin node
	# if this_node == node9:
	# 	node9.left = this_node
	# 	node01 = this_node

    node9.left = node01

	# print("Finishing tree: " + node01)
    return node01


scene_head = define_scene_tree()


current_node = scene_head


load_scene(scene_head, global_sphere, global_plane)

vizact.ontimer(0.5, joystick_action)
# 23
