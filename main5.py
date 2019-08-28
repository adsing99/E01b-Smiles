#!/usr/bin/env python3

import utils, open_color, arcade #import everything needed for the program

utils.check_version((3,7))

SCREEN_WIDTH = 800 #set the width of the window to 800
SCREEN_HEIGHT = 600 #set the height of the window to 600
SCREEN_TITLE = "Smiley Face Example" #title that will show at the top of the window

class Faces(arcade.Window): #create a new class
    """ Our custom Window Class"""

    def __init__(self): #init function
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #super function

        # Show the mouse cursor
        self.set_mouse_visible(True) #make cursor visible

        self.x = SCREEN_WIDTH / 2 #start in center
        self.y = SCREEN_HEIGHT / 2 #start in center

        arcade.set_background_color(open_color.white) #set background to white

    def on_draw(self): #on draw function
        """ Draw the face """
        arcade.start_render() #begins the render, needed
        face_x,face_y = (self.x,self.y) #create 2 new variables to be used below
        smile_x,smile_y = (face_x + 0,face_y - 10) #set the coordinates of the smile relative to the face
        eye1_x,eye1_y = (face_x - 30,face_y + 20) #set the coordinates of the eye relative to the face
        eye2_x,eye2_y = (face_x + 30,face_y + 20) #set the coordinates of the eye relative to the face
        catch1_x,catch1_y = (face_x - 25,face_y + 25) #set the coordinates of the eye catch relative to the face
        catch2_x,catch2_y = (face_x + 35,face_y + 25) #set the coordinates of the eye catch relative to the face

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3) #draw in certain color
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4) #draw in certain color
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black) #draw in certain color
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black) #draw in certain color
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2) #draw in certain color
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2) #draw in certain color
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4) #draw in certain color


    def on_mouse_motion(self, x, y, dx, dy): #create new function
        """ Handle Mouse Motion """
        self.x = x #the x of the mouse is the x of the face
        self.y = y #the y of the mouse is the y of the face



window = Faces() #set the custom class to be the window
arcade.run() #run