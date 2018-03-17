#CST 205 
#Section Six Labs
#Sergiy Zarubin
#Danny Tran

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Helper Functions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#We are assuming that we know the region affected by read eye issue
def getRegions(): 
  return [[358,526],[379,548],[592,526],[618,548]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
def getDimantions(pic):
  return getWidth(pic),getHeight(pic)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def errorMSG(pic,txt):
    picWidth,picHight = getDimantions(pic)
    txtColor = makeColor(255, 0, 0)
    txtStyle = makeStyle(sansSerif, bold, 30)
    addTextWithStyle(pic, picWidth//2, picHight//2, txt, txtStyle, txtColor)
    return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def txtMSG(pic,txt_1,txt_2):
    picWidth,picHight = getDimantions(pic)
    txtColor = makeColor(0, 255, 0)
    txtStyle = makeStyle(sansSerif, bold, 30)
    addTextWithStyle(pic, (picWidth//2)-150, picHight//2, txt_1, txtStyle, txtColor)
    addTextWithStyle(pic, (picWidth//2)-100, (picHight//2)+30, txt_2,txtStyle, txtColor)
    return pic  

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Posterize collor  
def poseterize(color):
    if color < 64:
      return 31
    elif 63 < color < 128:
      return 95
    elif 127 < color < 192:
      return 159
    elif 191 < color < 256:
      return 223
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getDistanceFromBase(pixel, baseColor):
  pixelCol = getColor(pixel)
  return distance(baseColor, pixelCol)     

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def makeNegative (pic): 
   pixels = getPixels(pic)
   for pixel in pixels:
     pixelRed = getRed(pixel)
     pixelGreen = getGreen(pixel)
     pixelBlue = getBlue(pixel)
     newColor = makeColor(255-pixelRed,255-pixelGreen,255-pixelBlue )
     setColor(pixel,newColor)
   return pic 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def newPic(width,hight):
  mypic = makeEmptyPicture(width, hight)
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y),green )
  return mypic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#LAB 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def helfRed():
  pic = get_pic()
  pixels = getPixels(pic)
  for pixel in pixels:
    pixelRed = getRed(pixel)
    setRed(pixel, pixelRed*0.5)
  repaint(pic)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#removes all of the blue from an image
def noBlue(): 
   pic = get_pic()
   pixels = getPixels(pic)
   for pixel in pixels:
     setBlue(pixel, 0)
   return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#removes all of the green from an image
def noGreen(): 
   pic = get_pic()
   pixels = getPixels(pic)
   for pixel in pixels:
     setGreen(pixel, 0)
   return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 1: lessRed function adjusts red by percentage parameter DB

def lessRed(pic,percent):
  pixels = getPixels(pic)
  for pixel in pixels:
    pixelRed = getRed(pixel)
    setRed(pixel, pixelRed * percent/100)
  return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 2: function takes a multiple parameter to increase red, DT

def moreRed(pic, percent):
  pixels = getPixels(pic)
  for pixel in pixels:
    pixelRed = getRed(pixel)
    setRed(pixel, (pixelRed + pixelRed*(percent/100)))
  return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 3: make an image look pink SZ

def roseColoredGlasses():
   pic = get_pic()
   pixels = getPixels(pic)
   for pixel in pixels:
     pixelRed = getRed(pixel)
     pixelGreen = getGreen(pixel)
     pixelBlue = getBlue(pixel)
     setRGB(p,pixelRed*1.01,pixelGreen*0.51,pixelBlue*0.65)
   return pic 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
# Problem 4: write a function makeLighter that lightens the photo SZ

def lightenUp():
   pic = get_pic()
   pixels = getPixels(pic)
   for pixel in pixels:
    pixelColor = getColor(p)
    setColor(pixel,makeLighter(c))
   return pic 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 5 Logic/Psuedo LS
  #makePicture(pickAFile())
  #getRed(pix)
  #getGreen(pix)
  #getBlue(pix)
  #modify pixel: 255 - red, blue, green
  #make pixel
  #repaint image
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 6A: write a function BnW that turns a picture black and white LS
def BnW(pic):
  for pixel in getPixels(pic):
    pixelRed = getRed(pixel) 
    pixelGreen = getGreen(pixel)
    pixelBlue = getBlue(pixel)
    ave = (pixelRed+ pixelGreen+ pixelBlue) / 3
    set = makeColor(ave, ave, ave)
    setColor(pixel, set)
  return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#LAB 4  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def betterBnW(pic):
  for pixel in getPixels(pic):
    pixelRed = getRed(pixel)
    pixelGreen = getGreen(pixel)
    pixelBlue = getGreen(pixel)
    better = pixelRed*0.299 + pixelGreen*0.587 + pixelBlue*0.114
    newColor = makeColor(better, better, better)
    setColor(pixel, newColor)
  return pic
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def roseColoredGlasses( pic, baseColor):
   pixels = getPixels(pic)
   for pixel in pixels:
     dist = getDistanceFromBase(pixel, baseColor)
     if dist>60 :
         #get Existing Color
         pixelRed = getRed(pixel)
         pixelGreen = getGreen(pixel)
         pixelBlue = getBlue(pixel)
         #Set New color
         newRed = pixelRed*1.01
         #Check for overflow
         if newRed>255 :
             newRed = 255
         newGreen  = pixelGreen*0.51
         newBlue = pixelRed*0.65
         #Make new Color
         newColor = makeColor(newRed,newGreen,newBlue)
         setColor(pixel,newColor)
   return pic 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mirrorVertical():
   pic = get_pic()
   widthPic, heightPic = getDimantions(pic)
   for x in range( 0, widthPic/2):
     for y in range(0,heightPic):
       pixelL = getPixelAt(pic,x,y)
       newX = widthPic-1-x
       pixelR = getPixelAt(pic,newX,y)
       colot2Copy = getColor(pixelL)
       setColor(pixelR,colot2Copy)
      
   return pic



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mirrorHorisontalTB():
   pic = get_pic()
   widthPic, heightPic = getDimantions(pic)
   for x in range( 0, widthPic):
     for y in range(0,heightPic/2):
       pixelL = getPixelAt(pic,x,y)
       newY = heightPic-1-y
       pixelR = getPixelAt(pic,x,newY)
       colot2Copy = getColor(pixelL)
       setColor(pixelR,colot2Copy)
      
   return pic


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mirrorHorisontalBT():
   pic = get_pic()
   widthPic, heightPic = getDimantions(pic)
   for x in range( 0, widthPic):
     for y in range(heightPic/2,heightPic):
       pixelL = getPixelAt(pic,x,y)
       newY = heightPic-1-y
       pixelR = getPixelAt(pic,x,newY)
       colot2Copy = getColor(pixelL)
       setColor(pixelR,colot2Copy)
      
   return pic



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mirrorQuad():
   pic = get_pic()
   widthPic, heightPic = getDimantions(pic)
   for x in range( 0, widthPic/2):
     for y in range(0,heightPic/2):
       pixelL = getPixelAt(pic,x,y)
       newX = widthPic-1-x
       newY = heightPic-1-y
       pixelR = getPixelAt(pic,newX,y)
       pixelBL = getPixelAt(pic,x,newY) 
       pixelBR = getPixelAt(pic,newX,newY)
       colot2Copy = getColor(pixelL)
       setColor(pixelR,colot2Copy)
       setColor(pixelBL,colot2Copy)
       setColor(pixelBR,colot2Copy)
      
   return pic



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def simpleCopy(pic):
  widthPic, heightPic = getDimantions(pic)
  newPic = makeEmptyPicture(widthPic,heightPic)
  for x in range (0, widthPic):
    for y in range (0, heightPic):
      pixel = getPixelAt(pic,x,y)
      newPixel  = getPixelAt(newPic,x,y)
      color2Copy= getColor(pixel)
      setColor(newPixel,color2Copy)
  return pic 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def rotatePic(pic):
  widthPic, heightPic = getDimantions(pic)
  newPic = makeEmptyPicture(heightPic,widthPic)
  for x in range (widthPic,0 ):
    for y in range (heightPic,0 ):
      pixel = getPixelAt(pic,x,y)
      newPixel  = getPixelAt(newPic,y,x)
      color2Copy= getColor(pixel)
      setColor(newPixel,color2Copy)
  return newPic 
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def shrincPic(pic):
  widthPic, heightPic = getDimantions(pic)
  newPic = makeEmptyPicture(widthPic//2,heightPic//2)
  for x in range (0, widthPic,2):
    for y in range (0, heightPic,2):
      pixel = getPixelAt(pic,x,y)
      newPixel  = getPixelAt(newPic,x/2,y/2)
      color2Copy= getColor(pixel)
      setColor(newPixel,color2Copy)
  return newPic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def pyCopy(source, target, targetX, targetY,baseColor): 
#  print "Running"
  sourceW,sourceH = getDimantions(source)
  targetW,targetH = getDimantions(target)
  for x in range (0, targetW):
   for y in range (0, targetH):
     newPixel  = getPixelAt(target,x,y)
     targetDist = getDistanceFromBase(newPixel, green)
     if x-targetX<sourceW and y-targetY<sourceH and x>targetX and y>targetY:
        pixel = getPixelAt(source,x-targetX,y-targetY)
        dist = getDistanceFromBase(pixel, baseColor)
        if dist>80 and targetDist<60:
          color2Copy= getColor(pixel)
          setColor(newPixel,color2Copy)
  return target

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def makeCollage(): 
    collage = newPic(2550,3300)
    #Group Photo makeColor(19,177,110)
    pic =  makePicture('\\Original\\GroupPhoto.jpg')
    pic = makeNegative(pic)
    collage = pyCopy(pic,collage,764,173,makeColor(0,255,0))
    writePictureTo(collage,'\\Result\\Collage.jpg')
    #Group Photo makeColor(19,177,110)
    pic =  makePicture('\\Original\\CACW.jpg')
    pic = makeNegative(pic)
    collage = pyCopy(pic,collage,0,1066,makeColor(0,255,0))
    writePictureTo(collage,'\\Result\\Collage.jpg')
    #Group Photo
    pic =  makePicture('\\Original\\willV.jpg')
    collage = pyCopy(pic,collage,975,2450, makeColor(19,177,110))
    writePictureTo(collage,'\\Result\\Collage.jpg')
    #willQuad
    pic = makePicture('\\Original\\willQuad.jpg')
    pic=rotatePic(pic)
    writePictureTo(collage,'\\Result\\Collage.jpg')
    baseColor =makeColor(118,177,110)
    pic = roseColoredGlasses(pic, baseColor)
    pic = shrincPic(pic)
    collage = pyCopy(pic,collage,1083,2450,baseColor)
    writePictureTo(collage,'\\Result\\Collage.jpg')
    #will Speach
    pic =  makePicture('\\Original\\shia_labeouf_motivational_speech.jpg')
    pic = betterBnW(pic,makeColor(149,250,170))
    collage = pyCopy(pic,collage,1575,2911,makeColor(149,250,170))
    writePictureTo(collage,'\\Result\\Collage.jpg')
    #MF
    pic =  makePicture('\\Original\\maxresdefault.jpg')
    baseColor = makeColor(1,255,0)
    pic = betterBnW(pic, baseColor)
    collage = pyCopy(pic,collage,471,112,baseColor)
    writePictureTo(collage,'\\Result\\Collage.jpg')
    #Tie Bomber
    pic =  makePicture('\\Original\\swbg.jpg')
    baseColor = makeColor(1,255,0)
    pic = betterBnW(pic, baseColor)
    collage = pyCopy(pic,collage,0,0,baseColor)
    writePictureTo(collage,'\\Result\\Collage.jpg')
    #BG
    pic =  makePicture('\\Original\\forest.jpg')
    collage = pyCopy(pic,collage,0,1606,makeColor(0,255,0))
    writePictureTo(collage,'\\Result\\Collage.jpg')
    repaint(collage)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#LAB 6
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def redEye(pic):
   baseColor =  makeColor(218, 69, 96)
   regions = getRegions() 
   pixelsArray = []
   #It is posible to detect the read eye region by looking for the clusters or red spread certain distance appart PD-distance.
   # Than gradualy expend regione and lower color senaativity to fix all affected pixels. SZ
   for y in range (regions[0][1],regions[1][1]):
     for x in range (regions[0][0],regions[1][0]):
       p=getPixelAt(pic,x,y)
       cred = getDistanceFromBase(p,baseColor)
       if cred <80:
         pixelsArray.append(p)
     for x in range (regions[2][0],regions[3][0]):
         p=getPixelAt(pic,x,y)
         cred = getDistanceFromBase(p,baseColor)
         if cred <80:
           pixelsArray.append(p)
   #repaint(pic)
   for pixel in pixelsArray:
     newColor = makeColor(0, getGreen( pixel ), getBlue( pixel )) 
     setColor( pixel, newColor)
   return pic
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Sepia(pic):
  pic = betterBnW(pic)
  pixels = getPixels(pic) 
  for pixel in pixels:
    redP = getRed(pixel)
    blueP = getBlue(pixel)
    greenP = getGreen(pixel)  
    if redP < 63:
      redP = redP * 1.1
      blueP = blueP * 0.95
    elif 62 < redP < 192: 
      redP = redP * 1.15
      blueP = blueP * 0.85
    elif redP > 191:
      redP = redP * 1.08
      if redP > 255:
        redP = 255
      blueP = blueP * 0.93
      
    makeColour = makeColor(redP, greenP, blueP)
    setColor(pixel, makeColour)
  return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Problem #2 Art-i-fy
def Artify(pic):
  for pixel in getPixels(pic):
    redP = getRed(pixel)
    blueP = getBlue(pixel)
    greenP = getGreen(pixel)
    newColour = makeColor(poseterize(redP), poseterize(greenP), poseterize(blueP))
    setColor(pixel, newColour)
  return (pic)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Problem 3 GREEN SCREEN

#Two images to deal with
#1 Background image
#2 GreenScreen image
#Find the green pixels in Green Screen Image 
#Replace those pixels with pixels from Background Image
def chromakey (source, backGround, coordX, coordY): 
  sourceW,sourceH = getDimantions(source)
  bgW,bgH = getDimantions(backGround)
  if (sourceW+coordX)>=bgW or (sourceH+coordY)>bgH :
    return errorMSG(source,"YELL NO")
  for x in range (0, bgW):
   for y in range (0, bgH):
    if x>=coordX and x<sourceW and y>=coordY and y<sourceH:
     picPixel=getPixelAt(backGround,x,y)
     pixelX=x-coordX
     pixelY=y-coordY
     pixel = getPixelAt(source,pixelX,pixelY)
     pixelR = getRed(pixel)
     pixelG = getGreen(pixel)
     pixelB = getBlue(pixel)
     if (pixelR<80 and pixelG>120 and pixelB<75):
        x=getX(pixel)
        y=getY(pixel)
        #
        #setColor(picPixel,getColor(picPixel))
     elif (pixelR<120 and pixelG>30 and pixelB<120 and (abs(pixelR-pixelB)<51) and ((pixelR+pixelB/2)<(pixelG-20))):
       newGreen = float(pixelR+pixelG+pixelB)/3 #toned down green
       x=getX(pixel)
       y=getY(pixel)
       picPixel=getPixelAt(backGround,x,y)#Get background pixle color        
       picR = getRed(picPixel)
       picG = getGreen(picPixel)
       picB = getBlue(picPixel)
       proportion = float(pixelG)/220 - float(5)/9 #blending proportion
       pixelR = int(float(picR)*proportion + pixelR*(1-proportion))#blending colors
       pixelG = int(float(picG)*proportion + newGreen*(1-proportion))
       pixelB = int(float(picB)*proportion + pixelB*(1-proportion)) 
       colorPixel = makeColor(pixelR,pixelB,pixelG)
       setColor(picPixel,colorPixel)
     else:
       colorPixel = getColor(pixel)
       setColor(picPixel,colorPixel)
  return backGround
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#LAB 7  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def makeCard():
  pic = makePicture('\\Original\\Lab7\\johnny_walker_logo_bwv.jpg')
  bg = makePicture('\\Original\\Lab7\\JWG.jpg')
  bg = chromakey (pic,bg,298,19)
  pic = makePicture('\\Original\\Lab7\\SPD.jpg')
  Card = chromakey (pic,bg,500,320)
  Card=txtMSG(Card,"Make sure you keep walking","this St. Patrick`s Day")
  writePictureTo(Card,'\\Result\\Lab7\\spdCard.jpg')
  show(Card)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#RUN FUNCTION FOR TESTING 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Run():
  pic = makePicture('\\Original\\maxresdefault.jpg')
  bg = makePicture('\\Original\\swbg.jpg')
  newPic = chromakey (pic,bg,1000,1000)
  writePictureTo(newPic,'\\Result\\GSError.jpg')
  show(newPic)
    