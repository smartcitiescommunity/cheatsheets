#!/usr/bin/env python
# -*- coding: utf-8 -*-
######################################
#        Jacek Zaleski               #
#            CAWG                    #
#     CHEATS WALPAPER GENERATOR      #
#            V0.2.2                  #
######################################
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import fileinput
import textwrap
import pygame
 
def pointstopixel(punkty):
    pixel=(punkty*(96/72))
    return pixel
def wieksza(a ,b):
    if a>=b:
        a=a
    else:
        a=b
    return a
    
outputfile="tapeta.png"
VROZMIAR=56
HROZMIAR=800
KOLUMNA=55
FONTSIZE=9
FONTSIZE2=14
pygame.init()
screen_info = pygame.display.Info() #Required to set a good resolution for the game screen
HROZMIAR,VROZMIAR = screen_info.current_w,screen_info.current_h
 
font1 = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf",FONTSIZE,encoding='unic')
font2 = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf",FONTSIZE2,encoding='unic')
 
 
img=Image.new("RGBA", (HROZMIAR,VROZMIAR),(0,0,0))
draw = ImageDraw.Draw(img)
#y_text=15
w=10
y_text = 45
width = 5
widthtt=0
maxw=0
height=0
f = open('dane.txt','r')
 
for text in iter(f):
    
    h=0
    lines = textwrap.wrap(text, KOLUMNA)
    if width < HROZMIAR:
        if pointstopixel(y_text+25)>VROZMIAR:
            width += pointstopixel(maxw)+10
            y_text=45
         
        if text[0]=='#': 
            font=font2
        else:
            font=font1
        semf=0
        for line in lines:
             
            if semf>0:
                line="           "+line
            widthtt, height = font.getsize(line)
            maxw=wieksza(maxw,widthtt)
            semf +=1     
            
             
        
            draw.text((width, y_text), line, font = font, fill = (255,255,255))
            y_text += height
      
    else:
        break
        print 'niediala'
             
  
f.close()
stopka="https://consolechars.wordpress.com"
width7, height7 = font.getsize(stopka)
draw.text((HROZMIAR-width7,VROZMIAR-height7),stopka , font = font1, fill = (255,255,255))
draw = ImageDraw.Draw(img)
pygame.display.set_mode
#print pygame.display.Info
img.save(outputfile)
img.show()
