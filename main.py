from vpython import * #import vpython library

class Beaver:
    #constructor method for Beaver
    def __init__ (self):
        #sphere for face
        f = sphere()
        f.radius = 3 #sies of face
        #colors face
        self.furcolor = vector(188/255, 143/255, 108/255)
        self.face = f 
        #list of spheres for ears
        self.eyes = []
        #draw and position each eye 
        for i in range(2): #iterates twice
            eye = sphere() #draws eye sphere
            eye.radius = 0.5 #sies eye 
            #moves eye position up one from origin
            eye.pos.y += 1
            #if - else positions based on place in list 
            if i ==0:
                eye.pos.x = i-1
            else:
                eye.pos.x = i 
            eye.pos.z = 3
            #initialise eye as black on color
            eye.color = color.black
            self.eyes.append(eye) #add eye to list of eyes

        for i in range(2): #iterates twice
            ear = sphere() #draws eye sphere
            ear.radius = 0.5 #sies eye 
            #moves eye position up one from origin
            ear.pos.y += 2
            #if - else positions based on place in list 
            if i ==0:
                ear.pos.x = i-1
            else:
                ear.pos.x = i 
            
            #initialise eye as black on color
            ear.color = self.furcolor
            self.ear.append(ear) #add eye to list of eyes

 #stores a Beaver in variable b 

b = Beaver()
frames = 0



#Professor GREEN's method 
#blink eyes 
def blinkEyes (self,f): #check if 5 frames of elapsed since last blink 
    if f % 5 == 0:
        for eye in self.eyes:
            if eye.color == self.furcolor:
                eye.color = color.black
            else:
                eye.color = self.furcolor
                 



        
#create animation loop
while True:
    rate(9)
    b.blinkEyes(frames)
    frames += 2







   