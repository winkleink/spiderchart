# Code to create spider diagrams 
# Wonky code created by @Winkleink (2016-2018)
# Licence: MIT

# 2018-06-04 Update to have multiple lines for different years to show progression

# It does one thing (hopefully every time) but there is guarantee that it will work for you

# It runs successfully on a Raspberry Pi 

# Make sure all all files are in the same folder

# This program takes 3 input files

# Student_Scores.csv 
# File with the list of students and their scores 
# This is created using Student Scores.ods and OpenOffice

# spider_data_points.csv
# Contains the co-ordinates for the didderent points on the spider diagram
# You only need to edit this file if you change the location of the points on the spider diagra,

# __spider.png
# Blank version of the spider diagram
# Do not edit this file

# On running the code the co-ordinates are read and then each students scores are read and plotted on the screen
# Don't worry if the image is too big for your monitor it is working correctly

# It then goes through each student plotting and connecting their points by lines
# Once completed a .jpeg file is created using the students name as the filename

# Once done you will have individual jpeg files for each of the students with their scores plotted

# If you want to create your own __spider.png you can use __spider.svg which was created using Inkscape
# As long as you don't move the spiders web you should be able to add your own embellishments  to customize the output to match your needs

# Images for the characters created by  Andrew Palfreyman

# import relevant libraries
from pygame import *
import time

# class to create sprites and render them
class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=image.load(filename)
        print(self.x)
        print(self.y)
        print(filename)
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))
  
# initialise pygame
init()

# sdet up some colours and a font for the text
black=[0,0,0]
white=[255,255,255]
red=[255,0,0]
blue=[0,0,255]
green = [0,255,0]
orange = [255,165,0]

#linecolor is the list of colours for the year lines 3,4,5,6

linecolor = [red,blue,orange,green]

# print "linecolor is : " + str(linecolor[1])

myfont=font.SysFont("DejaVu Sans", 90)

# size of the window based on the __spider.png file size so it fills the screen 
SCREEN_WIDTH = 3508
SCREEN_HEIGHT = 2481
size=[SCREEN_WIDTH,SCREEN_HEIGHT]

# some set up st
screen=display.set_mode(size)
screen.fill(white)
display.set_caption("Spider Chart Maker")

# set  __spider.png as background 
background=Sprite(0,0,"__spider.png")
background.render()

# You have to execute an update to get the screen to refresh
display.update()


# Variables to whole the 2 csv input files
studentfile="Student_Scores.csv"
coordinatefile="spider_data_points.csv"

# Co-ordinated list
clist = open(coordinatefile).read().split('\n')

# Loop to go through each student 
with open(studentfile,"r") as slist:
    next(slist) #removes header

# Get student name and scores (I suspect a list would be neater for this)
    for line in slist:
        student= line.strip("\r\n").split(",")
        for year in range (0,3):
#            print "NOw doing year : " + str(year)
#            print "linecolor is :" + str(linecolor[year])
            sname = student[0] #student name
#            print sname
            sclass = student[1]

            scode = student[(year*7)+2]
            if scode != '':
                scode = int(scode) + 1
            else:
                scode = 1
            
            snet = student[(year*7)+3]
            if snet != '':
                snet = int(snet) + 1
            else:
                snet = 1

            ssearch = student[(year*7)+4]
            if ssearch != '':
                ssearch = int(ssearch) + 1
            else:
                ssearch = 1

            slogic = student[(year*7)+5]
            if slogic != '':
                slogic = int(slogic) + 1
            else:
                slogic = 1

            stech = student[(year*7)+6]
            if stech != '':
                stech = int(stech) + 1
            else:
                stech = 1

            shardware = student[(year*7)+7]
            if shardware  != '':
                shardware = int(shardware) + 1
            else:
                shardware = 1

#            scode = int(student[(year*7)+2])+1
#            snet = int(student[(year*7)+3])+1
#            ssearch = int(student[(year*7)+4])+1
#            slogic = int(student[(year*7)+5])+1
#            stech = int(student[(year*7)+6])+1
#            shardware = int(student[(year*7)+7])+1
            
            print "sname before if is : " + str(sname)
            print "sclass before if is : " + str(sclass)
            print "scode before if is : " + str(scode)
            print "snet before if is : " + str(snet)
            print "ssearch before if is : " + str(ssearch)
            print "Slogic before if is : " + str(slogic)
            print "Stech before if is : " + str(stech)
            print "Shardware before if is : " + str(shardware)
            
            # Check if ALL values are zero so no entry 
            if (scode != 1 and snet != 1 and ssearch != 1 and slogic != 1 and stech != 1 and shardware != 1):
                
#                print ("Len clist and scode coordinates")
                print (len(clist))
#                print ("scode  " + str(scode))
#                print ("clist line: " + clist[scode])

                # Get co-ordinates for code         
                scoord = clist[scode].strip("\r\n").split(",")
                print ("scode scoord: " + str(scoord))
#                print("scoord is: ")
                scodex = int(scoord[1])
                scodey = int(scoord[2])

                # Get co-ordinates for net 
                scoord = clist[snet].strip("\r\n").split(",")
                print("snet scoord: " + str(scoord))
#                print (scoord)
                snetx = int(scoord[3])
                snety = int(scoord[4])

                # Get co-ordinates for search         
                scoord = clist[ssearch].strip("\r\n").split(",")
                print("ssearch scoord is: " + str(scoord))
#                print (scoord)
                ssearchx = int(scoord[5])
                ssearchy = int(scoord[6])

                scoord = clist[slogic].strip("\r\n").split(",")
                print("scoord is: ")
                print (scoord)
                slogicx = int(scoord[7])
                slogicy = int(scoord[8])

                # Get co-ordinates for tech 
                scoord = clist[stech].strip("\r\n").split(",")
                print("scoord is: ")
                print (scoord)
                stechx = int(scoord[9])
                stechy = int(scoord[10])

                # Get co-ordinates for hardware 
                scoord = clist[shardware].strip("\r\n").split(",")
                print("scoord is: ")
                print (scoord)
                shardwarex = int(scoord[11])
                shardwarey = int(scoord[12])

                # Print the student name and co-ordinates to the screen for checking if something goes wrong
                print ("student name:" + sname)
                print ("scode x,y: " + str(scodex) + " , " + str(scodey))
                print ("snet x,y: " + str(snetx) + " , " + str(snety))
                print ("sseach x,y: " + str(ssearchx) + " , " + str(ssearchy))
                print ("slogic x,y: " + str(slogicx) + " , " + str(slogicy))
                print ("stech x,y: " + str(stechx) + " , " + str(stechy))
                print ("shardware x,y: " + str(shardwarex) + " , " + str(shardwarey))

                # Draw red circles at the score points
                draw.circle(screen,linecolor[year],(scodex,scodey),40,0)
                draw.circle(screen,linecolor[year],(snetx,snety),40,0)
                draw.circle(screen,linecolor[year],(ssearchx,ssearchy),40,0)
                draw.circle(screen,linecolor[year],(slogicx,slogicy),40,0)
                draw.circle(screen,linecolor[year],(stechx,stechy),40,0)
                draw.circle(screen,linecolor[year],(shardwarex,shardwarey),40,0)

                # Draw the lines between the points
                draw.lines(screen,linecolor[year],False,[(scodex,scodey),(snetx,snety),(ssearchx,ssearchy),(slogicx,slogicy),(stechx,stechy),(shardwarex,shardwarey),(scodex,scodey)],20)

                # Draw student name top left
                # font = pygame.font.Font(None, 25)
                nametext = myfont.render(sname, True, black)
#                text_rect = nametext.get_rect(center=(SCREEN_WIDTH/2, 2144))
                text_rect = nametext.get_rect(center=(1000, 2200))
                yeartext = myfont.render("Year " + str(year+3), True, linecolor[year])
                year_rect = yeartext.get_rect(center=(3000, 1800+(year*100)))
                
                screen.blit(nametext, text_rect)
                screen.blit(yeartext, year_rect)


                # namewidth = sname.get_rect().width
                # screen.blit(myfont.render(sname,1,black),(1754-(namewidth/2),2144))

                # all drawing done. Update the screen
                display.update()

        # Save the screen with the students name    
        image.save(screen,sname+".jpeg")
                
# Wait a second to admire your work        
        time.sleep(0.001)   
        
# Clear the screen and draw the clean spider diagram before starting all over again
        
        screen.fill(white)
        background.render()
        display.update()
