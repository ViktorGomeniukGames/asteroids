# ASTEROIDS
#----------------
""" Frame size 1000 x 610 pixels. Change WIDTH if need but advise not 
to change HEIGHT because instruction about key control can be outputted
not appropriately.
"""
#----------------
__author__ = 'vgomeniuk'

# Import modules
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

#----------------
# globals for interface
WIDTH = 1000
HEIGHT = 610
time = 0.5
# start global features
score = 0
lives = 3
level = 0
started = False
game_mode = "singleplayer"
#-----------------
# helper class for image features
class ImageInfo:
    """ Create new instance - object with information about features of 
    loaded image. Check if image is animated and number of frames.
    Implement helper class methods for returning center, size, radius, 
    lifespan of image etc.
    """
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False, frames = 0):
        """ Initialize ImageInfo object. """
        self.frames = frames
        self.center = center
        self.size = size
        self.radius = radius
        
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        """ Return center of image. """
        return self.center

    def get_size(self):
        """ Return size of image. """
        return self.size

    def get_radius(self):
        """ Return radius of image. """
        return self.radius

    def get_lifespan(self):
        """ Return lifespan. """
        return self.lifespan

    def get_animated(self):
        """ Return animation. """
        return self.animated
    
    def get_frames (self):
        """ Return number of frames if object animated. """
        return self.frames

# load images and create ImageInfo objects to store its features    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_blue.png")
debris_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
debris_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_blue.png")
debris_image4 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_blue.png")
debris_image5 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_brown.png")
debris_image6 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_brown.png")
debris_image7 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_brown.png")
debris_image8 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_brown.png")
    # create group of images for random choice
debris_image_group = [debris_image1, debris_image2, debris_image3, debris_image4, debris_image5, debris_image6, debris_image7, debris_image8]
debris_image = debris_image1

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_1_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2013.png")
nebula_2_image = simplegui.load_image ("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png")
    # create group of images for random choice
nebula_image_group = (nebula_1_image, nebula_2_image)
background = nebula_1_image

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship_1 image
ship_1_info = ImageInfo([45, 45], [90, 90], 35)
ship_1_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# ship_2 image
ship_2_info = ImageInfo ([64, 64], [128, 128], 35)
ship_2_image = simplegui.load_image("http://www.alcove-games.com/wp-content/uploads/2013/03/spaceship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_1_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
missile_2_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png")

# asteroid images - warspawn.png
asteroid_info = ImageInfo([64, 64], [128, 128], 30, animated = True, frames = 64)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid1.opengameart.warspawn.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True, frames = 24)
explosion_1_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
explosion_2_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")
explosion_3_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue.png")
explosion_4_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue2.png")
    # create group of images for random choice
explosion_image_group = (explosion_1_image, explosion_3_image, explosion_4_image)
explosion_image = explosion_1_image

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_1_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
ship_2_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

#------------------
# helper functions to handle transformations
def angle_to_vector(ang):
    """ Return vector based on angle. """
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    """ Return destination between two points. """
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def draw_sprite_group (collection, canvas):
    """ Draw each object in collection. """
    for item in collection.copy():
        item.draw (canvas)

def update_sprite_group (collection):
    """ Update each object in collection. """
    for item in collection:
        item.update ()
                
def collide (object_1, object_2):
    """ Return True if object_1 collides object_2 and False otherwise. """
    
    # calculate safe distance
    safe_dist = object_1.get_radius () + object_2.get_radius ()
    # calculate real distance between two objects
    real_dist = dist (object_1.get_position (), object_2.get_position ())
        
    return real_dist <= safe_dist

def group_collide (object_1, group_of_objects):
    """ Return True if object_1 collides object_2 in group_of_objects and
    False otherwise. Remove object_2 from group_of_objects if True. If collision
    create new instance of Sprite.
    """
    remove_obj = group_of_objects.copy ()
    # flag about collision
    answer = False
    
    for obj in remove_obj:
        if collide (object_1, obj):
            # delete object
            group_of_objects.discard (obj)
            # change flag
            answer = True
            # if collision create an explosion object
            explosion_group.add (Sprite (obj.get_position (), [0, 0], 0, 0, 
                                         explosion_image, explosion_info, sound = explosion_sound))
   
    return answer

def two_group_collide (group_of_objects_1, group_of_objects_2):
    """ Check if any object in group_of_objects_1 collides 
    some object in group_of_objects_2. Remove collided objects
    and increase score.
    """
    global score
    group_1 = group_of_objects_1.copy ()
    for item in group_1:
        # check collision
        if group_collide (item, group_of_objects_2):
            # increase score
            score += 1
            # remove object
            group_of_objects_1.discard (item)
            
def process_group (collection):
    """ Remove temporary object in collection when getting required age. """
    remove_set = list (collection.copy ())
    for missile in remove_set:
        if missile.age >= missile.lifespan:
            collection.discard (remove_set[0])

#------------------
# helper functions to start new game
def new_game ():
    """ Stop current game. Remove asteroids and missiles. Rewind playing sounds. """
    global started, rock_group, missile_1_group, missile_2_group
    
    # set flag
    started = False
    
    # remove asteroids
    rock_group = set ([])
    
    # remove missiles
    missile_1_group = set ([])
    missile_2_group = set ([])
    
    # stop soundtrack
    soundtrack.rewind ()
    ship_1_thrust_sound.rewind ()
    ship_2_thrust_sound.rewind ()       

#------------------
# Ship class
class Ship:
    """ Create new instance - object with features: pos, vel, angle etc.
    Implement helper methods for drawing ship_image and update it when 
    shooting or moving. 
    """
    def __init__(self, pos, vel, angle, image, info, ship_number = 1):
        """ Initialize Ship object. """
        # set object's attributes
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.ship_number = ship_number
        self.lives = 3
        
        # choose sound depending on ship_number
        if self.ship_number:
            self.ship_sound = ship_1_thrust_sound
        else:
            self.ship_sound = ship_2_thrust_sound
        
    def draw(self,canvas):
        """ Draw ship_image. """
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, [90, 90], self.angle)
    
    def shoot (self):
        """ Draw a_missile. """
        # count velocity and update position of missle
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        
        # choose color and create new missile depending on ship
        if self.ship_number:
            missile_1_group.add (Sprite(missile_pos, missile_vel, self.angle, 0, missile_1_image, missile_info, missile_sound))
        else:
            missile_2_group.add (Sprite(missile_pos, missile_vel, self.angle, 0, missile_2_image, missile_info, missile_sound))
                
    def update(self):
        """ Update features of ship. """
        # update angle
        self.angle += self.angle_vel
        
        # move forward
        if self.thrust:
            self.ship_sound.play ()
            self.vel [0] = self.vel [0] * 0.8 + angle_to_vector (self.angle) [0]
            self.vel [1] = self.vel [1] * 0.8 + angle_to_vector (self.angle) [1]
            
            # if animated draw second image
            if self.ship_number:
                self.image_center [0] = 130
                
        else:
            self.ship_sound.rewind ()
            self.vel [0] *= (1 - 0.01)
            self.vel [1] *= (1 - 0.01)
            
            # if animated draw first image
            if self.ship_number:
                self.image_center [0] = 45
            
        
        # update position
        self.pos [0] += self.vel [0]
        self.pos [1] += self.vel [1]
        self.pos [0] %= WIDTH
        self.pos [1] %= HEIGHT
    
    def get_radius(self):
        """ Return radius of class object """
        return self.radius
    
    def get_position (self):
        """ Return position of class object """
        return self.pos
    
# Sprite class
class Sprite:
    """ Create new instance for object on canvas. Implement helper methods
    for getting radius and position of object, drawing images and update their
    actual position. 
    """
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        """ Initialize class object. """
        # set object's attributes
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.frames = info.get_frames ()
        self.age = 0
        self.frame_time = 0
        
        # play appropriate sounds
        if sound:
            sound.rewind()
            sound.play()
            
   
    def draw(self, canvas):
        """ Draw object on canvas. """
        # global frame_time
        # if animated draw all each frames in particular time
        print(get())
        if self.animated:
            # calculate number of required image
            current_rock_index = (self.frame_time % self.frames) // 1
            # calculate center of required image
            current_rock_center = (self.image_center[0] +  current_rock_index * self.image_size[0], self.image_center[1])
            # draw required image
            canvas.draw_image(self.image, current_rock_center, self.image_size, self.pos, (self.image_size [0] / 2, self.image_size [1] / 2)) 
            # update frame_time
            self.frame_time += 0.2
                    
        # if not animated draw as a usual object
        else:            
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):
        """ Update features on class object. """
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos [0] += self.vel [0]
        self.pos [1] += self.vel [1]
        self.pos [0] %= WIDTH
        self.pos [1] %= HEIGHT

        # update age
        self.age += 1
        
    def get_radius(self):
        """ Return radius of class object """
        return self.radius
    
    def get_position (self):
        """ Return position of class object """
        return self.pos
    
#------------------
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    """ Display starting field if not started. If player click in required
    field start game, reset number of lives and score, play soundtrack. """
    global started, score
    print(pos)
    # define position and size of starting fieald
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    
    # check if clicked inside requierd field
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    
    # start game and resetlives and score, play soundtrack
    if (not started) and inwidth and inheight:
        # set flag
        started = True
        # reset position, velocity and angle of both ships
        if game_mode == "singleplayer":
            first_ship.pos = [WIDTH / 2, HEIGHT / 2]
        else:
            first_ship.pos = [WIDTH / 3, HEIGHT / 2]
        second_ship.pos = [WIDTH * 2 / 3, HEIGHT / 2]
        first_ship.vel = [0, 0]
        second_ship.vel = [0, 0]
        first_ship.angle = 4.715
        second_ship.angle = 4.715
        
        # reset total score
        score = 0
        
        # play soundtrack
        soundtrack.play ()
        first_ship.lives = lives
        second_ship.lives = lives
#------------------
# draw handler           
def draw(canvas):
    """ Draw all the objects on canvas. """
    global time, started, rock_group, missile_1_group
    global missile_2_group, level

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    
    # draw background and it's elements
    canvas.draw_image(background, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw first_ship if lives left
    if first_ship.lives > 0:
        first_ship.draw(canvas)
    else:
        # if not draw stop playing sound
        ship_1_thrust_sound.rewind ()
    
    # draw second_ship if lives left and appropriate game_mode choosen
    if second_ship.lives > 0 and game_mode != "singleplayer":	
        second_ship.draw (canvas)
    else:
        # if not draw stop playing sound
        ship_2_thrust_sound.rewind ()
        
    # draw asteroids, missiles and explosions
    draw_sprite_group (rock_group, canvas)
    draw_sprite_group (missile_1_group, canvas)
    draw_sprite_group (missile_2_group, canvas)
    draw_sprite_group (explosion_group, canvas)
    
    # update first_ship if lives left
    if first_ship.lives > 0:
        first_ship.update()
    
    # update second_ship if lives left and appropriate game_mode choosen
    if second_ship.lives > 0 and game_mode != "singleplayer":	
        second_ship.update ()
    
    # update asteroids, missiles and explosions
    update_sprite_group (rock_group)
    update_sprite_group (missile_1_group)
    update_sprite_group (missile_2_group)
    update_sprite_group (explosion_group)
    
    # finish drawing temporary objects
    process_group (missile_1_group)
    process_group (missile_2_group)
    process_group (explosion_group)
    
    # if first_ship collides asteroid decrease lives
    if first_ship.lives > 0:
        if group_collide (first_ship, rock_group):
            first_ship.lives -= 1
    # if second_ship collides asteroid decrease lives
    if second_ship.lives > 0 and game_mode != "singleplayer":
        if group_collide (second_ship, rock_group):
            second_ship.lives -= 1
    
    # Check if missile collide asteroid
    two_group_collide (missile_1_group, rock_group)
    two_group_collide (missile_2_group, rock_group)
    
    # if multiplayer_battle mode choosen
    if game_mode == "multiplayer_battle":
        # if one of ships runs out of lives
        if first_ship.lives == 0 or second_ship.lives == 0:
            # start new game
            new_game ()
        else:
            # if first_ship collides enemy missile decrease lives
            if group_collide (first_ship, missile_2_group):
                first_ship.lives -= 1
            # if second_ship collides enemy missile decrease lives
            elif group_collide (second_ship, missile_1_group):
                second_ship.lives -= 1
        
    # Calculate current difficulty level
    level = score / 10
    
    # if run out of lives finish game
    if first_ship.lives <= 0 and game_mode == "singleplayer":
        new_game ()
    elif game_mode == "multiplayer_arcade" and first_ship.lives <= 0 and second_ship.lives <= 0:
        new_game ()
    
    # if multiplayer mode set correct output of first_ship's lives
    if first_ship.lives > 0:
        lives_1 = first_ship.lives
    else:
        lives_1 = 0
    output_2 = "1nd player lives:   " + str (lives_1)
    
    # if multiplayer mode set correct output for second_ship's lives
    if game_mode != "singleplayer":
        if second_ship.lives > 0:
            output_1 = "2st player lives:   " + str (second_ship.lives)
        else:
            output_1 = "2st player lives:   0"
    else:
        # if singleplayer set correct output for ship
        output_1 = ""
        output_2 = "Player lives:    " + str (first_ship.lives)
           
    # draw correct output_1 and output_2
    canvas.draw_text (output_1, (WIDTH - 260, 50), 30, "White")
    canvas.draw_text (output_2, (20, 50), 30, "White")
    
    
    # if not multiplayer_battle mode draw total score
    if game_mode != "multiplayer_battle":
        canvas.draw_text ("Total Score:   " + str (score * 10), (20, HEIGHT - 50), 30, "White")
    
    # calculate and draw difficulty level based on number of destroyed asteroids
    canvas.draw_text (("Difficulty Level:   " + str (int(level) + 1)), (WIDTH - 260, HEIGHT - 50), 30, "White")
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
    
#-----------------    
# timer handler that spawns a rock    
def rock_spawner():
    """ Respawn a_rock with random features. """
    global rock_group
    
    # choose random position and velocity due to difficulty level
    pos = [random.choice (range (WIDTH)), random.choice (range (HEIGHT))]
    vel = [random.choice (range (-2, 3)) * (1.25 ** level), random.choice (range (-2, 3)) * (1.25 ** level)]
    
    # create new asteroid due to limit of asteroids (based on level of difficulty)
    if len (rock_group) < 4 * (level + 1) and started and game_mode != "multiplayer_battle":
        rock = Sprite (pos, vel, 0, 0, asteroid_image, asteroid_info)
        # check if new asteroid will not collide ship as soon as created
        if not collide (rock, first_ship) and not collide (rock, second_ship):
            rock_group.add (rock)

#-------------------
# button handlers
def singleplayer ():
    """ Change current game_mode. Choose randomly background image and explosion image.
    Set number of first_ship.lives. Start new game.
    """
    global game_mode, background, lives, debris_image, explosion_image
    game_mode = "singleplayer"
    background = random.choice (nebula_image_group)
    debris_image = random.choice (debris_image_group)
    explosion_image = random.choice (explosion_image_group)
    lives = 3
    new_game ()

def multiplayer_battle ():
    """ Change current game_mode. Choose randomly background image and explosion image.
    Set number of first_ship's lives and second_ship's lives. Start new game.
    """
    global game_mode, background, lives, debris_image, explosion_image
    game_mode = "multiplayer_battle"
    background = random.choice (nebula_image_group)
    debris_image = random.choice (debris_image_group)
    explosion_image = random.choice (explosion_image_group)
    lives = 10
    new_game ()

def multiplayer_arcade ():
    """ Change current game_mode. Choose randomly background image and explosion image.
    Set number of first_ship's lives and second_ship's lives. Start new game.
    """
    global game_mode, background, lives, debris_image, explosion_image
    game_mode = "multiplayer_arcade"
    background = random.choice (nebula_image_group)
    debris_image = random.choice (debris_image_group)
    explosion_image = random.choice (explosion_image_group)
    lives = 3
    new_game ()

#-------------------
# event handlers for keyboard manipulations    
def keydown (key):
    """ Call ship's methods and change attributes when press keys. """
    # turn first_ship counter-clockwise
    if key == simplegui.KEY_MAP ['left']:
        first_ship.angle_vel = - 0.1
    
    # turn first_ship clockwise
    elif key == simplegui.KEY_MAP ['right']:
        first_ship.angle_vel = 0.1
    
    # turn second_ship counter-clockwise
    if key == simplegui.KEY_MAP ['A']:
        second_ship.angle_vel = - 0.1
    
    # turn second_ship clockwise
    elif key == simplegui.KEY_MAP ['D']:
        second_ship.angle_vel = 0.1
    
    # move first_ship forward    
    if key == simplegui.KEY_MAP ['up']:
        first_ship.thrust = True
        
    # move second_ship forward    
    if key == simplegui.KEY_MAP ['W']:
        second_ship.thrust = True
    
    # call first_ship's method for shoot if singleplayer
    if key == simplegui.KEY_MAP ['space']:
        if game_mode == "singleplayer":
            if first_ship.lives > 0 and started:
                first_ship.shoot ()
        # or second_ship's method for shoor if multiplayer
        else:
            if second_ship.lives > 0 and started:
                second_ship.shoot ()
    
    # call first_ship's method for shoot if multiplayer  
    if game_mode != "singleplayer" and key == simplegui.KEY_MAP ['L']:
        if first_ship.lives > 0 and started:
            first_ship.shoot ()

def keyup (key):
    """ Call ship's methods and change attributes when keys up. """
    # stop turning first_ship
    if key == simplegui.KEY_MAP ['left'] or key == simplegui.KEY_MAP ['right']:
        first_ship.angle_vel = 0.0
    
    # stop turning second_ship
    if key == simplegui.KEY_MAP ['A'] or key == simplegui.KEY_MAP ['D']:
        second_ship.angle_vel = 0.0
    
    # stop moving first_ship
    if key == simplegui.KEY_MAP ['up']:
        first_ship.thrust = False
        
    # stop moving second_ship
    if key == simplegui.KEY_MAP ['W']:
        second_ship.thrust = False

#----------------        
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize two ships, asteroids, missiles and explosions
second_ship = Ship([WIDTH / 3, HEIGHT / 2], [0, 0], 4.715, ship_2_image, ship_2_info, ship_number = 0)
first_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 4.715, ship_1_image, ship_1_info, ship_number = 1)
rock_group = set ([])
missile_1_group = set ([])
missile_2_group = set ([])
explosion_group = set ([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler (keydown)
frame.set_keyup_handler (keyup)
frame.set_mouseclick_handler(click)
frame.add_label ("Adrcade mode for one player")
frame.add_button ("Singleplayer: Arcade", singleplayer, 200)
frame.add_label ("Player vs. Player mode")
frame.add_button ("Multiplayer: Battle", multiplayer_battle, 200)
frame.add_label ("Arcade mode for two players")
frame.add_button ("Multiplayer: Arcade", multiplayer_arcade, 200)
    # Output instructions for key control
frame.add_label ("---------------------------------")
frame.add_label ("Singleplayer mode:")
frame.add_label ("")
frame.add_label ("To accelerate use 'Up'")
frame.add_label ("To counter-clockwise use 'Left'")
frame.add_label ("To clockwise use 'Right'")
frame.add_label ("To shoot use 'Space'")
frame.add_label ("---------------------------------")
frame.add_label ("Multiplayer mode:")
frame.add_label ("")
frame.add_label ("First Player:")
frame.add_label ("To accelerate use 'Up'")
frame.add_label ("To counter-clockwise use 'Left'")
frame.add_label ("To clockwise use 'Right'")
frame.add_label ("To shoot use 'L'")
frame.add_label ("")
frame.add_label ("Second Player:")
frame.add_label ("To accelerate use 'W'")
frame.add_label ("To counter-clockwise use 'A'")
frame.add_label ("To clockwise use 'D'")
frame.add_label ("To shoot use 'Space'")

# register timer
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

# Viktor Gomeniuk
# Google Chrome