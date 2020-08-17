
COUNT  = 10 # How many photos to generate

import PIL
from PIL import Image
from random import randint
import os
import zipfile
import random
circle=Image.open("imgs/circle.png")
circles=["circlegreen1","circlegreen2","circlegreen3","circlegreen4","circlegreen5"]

print("Generating random images")


background = Image.open("imgs/whitebackground.png")
#resize background so it doesn't ocuppies so much space
background = background.resize((256,256),resample=PIL.Image.LANCZOS)

aspect = circle.width/circle.height
circle_count = []

z = zipfile.ZipFile("files.zip", "w", zipfile.ZIP_DEFLATED)
for c in range(COUNT):
    print(c)
    render_img = background.copy()
    cnt = randint(50,250)
    circle_count.append(cnt)
    for i in range(cnt):
        a = randint(0,360)
        circle_size = randint(40,190)
        w = int(circle_size*aspect)

        whatcircle_txt=random.choices(circles,k=1)
        whatcircle_txt=whatcircle_txt.pop()
        whatcircle_img=Image.open("palette/"+whatcircle_txt+".png")
        circlef = whatcircle_img.resize((w,circle_size),resample=PIL.Image.LANCZOS)


        x = randint(-int(circlef.width/2),background.width - int(circlef.width/2))
        y = randint(-int(circlef.height/2),background.height - int(circlef.height/2))

        circlef = PIL.Image.Image.rotate(circlef,a,resample=PIL.Image.BICUBIC,expand=True)
        
        render_img.paste(circlef,(x,y),circlef)
        
    render_img.save(str(c)+".png")
    z.write(str(c)+".png")
    os.remove(str(c)+".png")

z.close()    
print("done")
print(circle_count)
