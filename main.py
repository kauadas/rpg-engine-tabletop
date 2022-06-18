from kivy.app import App

from kivy.uix.screenmanager import Screen,ScreenManager

from kivy.graphics import *

from kivy.uix.button import Button

from kivy.uix.popup import Popup

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput

from kivy.core.image import Image as coreImage

from kivy.uix.image import Image

from kivy.uix.scatter import Scatter

from kivy.uix.relativelayout import RelativeLayout

from kivy.core.window import Window

from kivy.uix.label import Label

from PIL import Image as pilImage

from io import BytesIO

import os

screens = []
class sm(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        for i in screens:
            self.add_widget(i)


def createScreen(name):
    index = len(screens)-1

    if index < 0:
        index = 0

    screen = Screen()
    screen.name = name
    screens.append(screen)

    return screens[index]



Initial = createScreen("Initial")


def actionBar():
    global ab
    
    ab = BoxLayout()

    ab.size_hint = (None,None)
    ab.width = 50
    ab.height = 720

    with ab.canvas:
        Color(0.5,0.5,0.5,1)
        Rectangle(pos = (0,0),size = (ab.width,ab.height))


actionBar()

ab.orientation = 'vertical'

Initial.add_widget(ab)

distance = Label()

distance.font_size = 10

ab.add_widget(distance)

grid1 = RelativeLayout()

background = Image()

import random

moving = None

oldChar = None
atualChar = None

def randomInitial():
    files = os.listdir('backgrounds/')
    img ='backgrounds/'+random.choice(files)
    return img

fileImg = randomInitial()

background.source = fileImg

grid1.add_widget(background)

Initial.add_widget(grid1)

mouseposition = Label()

mouseposition.color = (1,0.5,0,1)


ab.add_widget(mouseposition)

def addChar(*args):
    popup = Popup()
    menu = BoxLayout()
    menu.orientation = 'vertical'
    popup.add_widget(menu)
    chars = os.listdir('Chars/')

    i2 = 0
    selection = ""
    for i in chars:
        selection += f"{i2} - {i} "
        if i2 % 2 == 0:
            selection += "\n"
        i2 += 1


    selection = Label(text = selection)
    menu.add_widget(selection)

    
    menu.title = 'create character'
    menu.size_hint = (None,None)

    menu.size = (600,600)

    Sprite = TextInput(multiline = False,text = "0")
    Sprite.size_hint_y = None
    Sprite.height = 30


    menu.add_widget(Sprite)

    pos = BoxLayout()
    pos.size_hint_y = None
    pos.height = 30

    x = TextInput(multiline = False)
    x.text = "660"
    pos.size_hint_y = None
    pos.height = 30

    y = TextInput(multiline = False)
    y.text = "333"
    pos.size_hint_y = None
    pos.height = 30

    pos.add_widget(x)
    pos.add_widget(y)

    hint = Label(text = 'pos')
    hint.size_hint_y = None
    hint.height = 30
    menu.add_widget(hint)

    menu.add_widget(pos)

    pronto = Button(text = "pronto")
    pronto.size_hint_y = None
    pronto.height = 30


    

    def prontoDef(*a):
        char = Button()
        char.size_hint = (None,None)

        img = pilImage.open('Chars/'+chars[int(Sprite.text)])

        char.size_hint = (None,None)
        char.size = img.size
        char.pos = (int(x.text)-char.size[0]/2,int(y.text)-char.size[1]/2)
        char.background_normal = ''
        char.background_color = (1,1,1,0)

        sprite = Image()
        sprite.size_hint = (None,None)
        sprite.size = char.size
        sprite.pos = char.pos

        sprite.source = 'Chars/'+chars[int(Sprite.text)]

        char.sprite = sprite
        sprite.angle = 0

        

        char.angle = 0
        def move_to_mouse(*ab):
            global moving, atualChar, oldChar

            if oldChar != atualChar:
                oldChar = atualChar

            atualChar = char

            if moving != char:
                moving = [char,sprite]

            else:
                moving = None


        char.on_press = move_to_mouse
        char.add_widget(sprite)


        grid1.add_widget(char)
        popup.dismiss()

    pronto.on_press = prontoDef


    menu.add_widget(pronto)

    popup.open()


addChar_ = Button(text='add Char',on_press = addChar)

addChar_.font_size = 10

def setBg(*args):
    popup = Popup()
    menu = BoxLayout()

    menu.title = 'set BG'
    
    menu.size_hint = (None,None)

    menu.size = (600,600)

    menu.orientation = 'vertical'

    popup.add_widget(menu)

    backgrounds = os.listdir('backgrounds/')

    i2 = 0
    selection = ""
    for i in backgrounds:
        selection += f"{i2} - {i} "
        if i2 % 2 == 0:
            selection += "\n"
        i2 += 1

     

    selection = Label(text = selection)
    selection.font_size = 10
    menu.add_widget(selection)

   

    bg = TextInput(multiline = False,text = "0")
    bg.size_hint_y = None
    bg.height = 30

    menu.add_widget(bg)

    def prontoDef(*a):
        background.source = "backgrounds/"+backgrounds[int(bg.text)]
        popup.dismiss()

    pronto = Button(text = "pronto")
    pronto.size_hint_y = None
    pronto.height = 30
    pronto.on_press = prontoDef

    menu.add_widget(pronto)
    popup.open()



def rotate(obj,angle):
    
        with obj.canvas.before:
                PushMatrix()
                
                Rot = Rotate()
                Rot.angle = angle
                
                obj.angle += angle
                Rot.origin = obj.center

        with obj.canvas.after:
                PopMatrix()

setBg_ = Button(text='set Bg',on_press = setBg)

setBg_.font_size = 10

ab.add_widget(setBg_)
ab.add_widget(addChar_)




actionBar()


def setMp(window,p):
    global mp
    mp = p

    if atualChar and oldChar:
        r = (atualChar.center_x - oldChar.center_x)**2 + (atualChar.center_y - oldChar.center_y)**2
        distance.text = "r: "+str(int(r/10000))

        if atualChar == oldChar:
            oldChar = None
            
    else:
        distance.text = "r: 0"
    
    
    if moving:
        rotate(moving[1],-moving[1].angle)

        for i in moving:
            i.pos = (p[0]-i.size[0]/2,p[1]-i.size[1]/2)
            
            
        

    mouseposition.text = f"x: {p[0]}\ny: {p[1]}"

    mouseposition.font_size = 10


def key(window,key,*args):
    global atualChar,angle
    
    
    if key == 127:
        if atualChar:
            grid1.remove_widget(atualChar)
            atualChar = None

    if key == 114:
        if atualChar:
            rotate(atualChar.sprite,90)
            


def stopMouseMotion(*args):
    global moving
    if moving != None:
        moving = None



class app(App):
    def build(self):
        Window.bind(mouse_pos = setMp)
        grid1.on_touch_up = stopMouseMotion
        Window.bind(on_key_down = key)
        return sm()

app().run()

