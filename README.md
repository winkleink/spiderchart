# spiderchart
Spider diagram for school Computing skills

Sway Grantham Tweeted : https://twitter.com/SwayGrantham/status/744486919707430912
So, I took up the challenge ot create spider diagrams using date from the csv file.

This is the result.
Using Python and Pygame the program reads a CSV file with student names and scores and creates a unique UK A4 jpeg for each student.

It has been developed and runs successfully on a Raspberry Pi 
I have not tested it on any other computers so your milage may be different

This program takes 3 input files

Student_Scores.csv 
File with the list of students and their scores 
This is created using Student Scores.ods and OpenOffice

spider_data_points.csv
Contains the co-ordinates for the didderent points on the spider diagram

_spider.png
The main background image with the spiders web, characters and any custom graphics text required

Included are
__spider.svg and __spider_blank.png so you can create your own background.

__spider.svg was created using Inkscape and is for those who use vector tools like Inkscape or Illustrator
__spider_blank.png is a bitmap and so more suitable to being used with Photoshop or GIMP

On running the code the co-ordinates are read and then each students scores are read and plotted on the screen
Don't worry if the image is too big for your monitor it still works

It then goes through each student plotting and connecting their points by lines
Once completed a .jpeg file is created using the students name as the filename

 Once done you will have individual jpeg files for each of the students with their scores plotted

#Attribution
Idea by Sway Grantham
Images for the characters created by  Andrew Palfreyman
