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
    addTextWithStyle(pic, 20, 20, txt, txtStyle, txtColor)
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
def beforeAndAfter(picOne,picTwo):
  pic1W,pic1H = getDimantions(picOne)
  pic2W,pic2H = getDimantions(picTwo)
  newPicW = pic1W+pic2W+1
  if pic1H>pic2H: 
    newPicH = pic1H
  else: 
    newPicH = pic2H
  print newPicW,newPicH
  myPic = makeNewPic (newPicW, newPicH)
  myPic= pyCopy(picOne,myPic,0,0)
  myPic= pyCopy(picTwo,myPic,pic1W+1,0)
  txtColor = makeColor(255, 255, 255)
  txtStyle = makeStyle(sansSerif, bold, 30)
  addTextWithStyle(myPic, (pic1W//2)-150, pic1H-31, "BEFORE", txtStyle, txtColor)
  addTextWithStyle(myPic, pic1W+(pic2W//2)-150, pic1H-31, "AFTER",txtStyle, txtColor)
  return myPic
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def makeNewPic(width,hight):
  mypic = makeEmptyPicture(width, hight)
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y),black )
  return mypic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#LAB 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def halfRed(pic):
  pixels = getPixels(pic)
  for pixel in pixels:
    pixelRed = getRed(pixel)
    setRed(pixel, pixelRed*0.5)
  return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#removes all of the blue from an image
def noBlue(pic): 
   pixels = getPixels(pic)
   for pixel in pixels:
     setBlue(pixel, 0)
   return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#removes all of the green from an image
def noGreen(pic): 
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
    setRed(pixel, pixelRed-pixelRed * percent/100)
  return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 2: function takes a multiple parameter to increase red, DT

def moreRed(pic, percent):
  pixels = getPixels(pic)
  for pixel in pixels:
    pixelRed = getRed(pixel)
    newRed = pixelRed + (pixelRed*percent)/100
    if newRed>255: 
       newRed = 255
    setRed(pixel,newRed)
  return pic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 3: make an image look pink SZ
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def roseColoredGlasses( pic):
   baseColor = makeColor(255, 0, 128)
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
# Problem 4: write a function makeLighter that lightens the photo SZ

def lightenUp(pic):
   pixels = getPixels(pic)
   for pixel in pixels:
    pixelColor = getColor(pixel)
    newColor= makeLighter(pixelColor)
    setColor(pixel,newColor)
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
def mirrorVertical(pic):
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
def mirrorHorisontalTB(pic):
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
def mirrorHorisontalBT(pic):
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
def mirrorQuad(pic):
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
      pixelRed = getRed(pixel) 
      pixelRed = getGreen(pixel)
      pixelBlue = getBlue(pixel)
      newPixel  = getPixelAt(newPic,x,y)
      newPicColor = makeColor( pixelRed,pixelRed,pixelBlue)
      setColor(newPixel,newPicColor)
  return newPic 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def rotatePic(pic):
  widthPic, heightPic = getDimantions(pic)
  newPic = makeEmptyPicture(heightPic,widthPic)
  for x in range (0,widthPic ):
    for y in range (0,heightPic ):
      pixel = getPixelAt(pic,x,y)
      newPixel  = getPixelAt(newPic,y,widthPic-x-1)
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
def pyCopy (source, backGround, coordX, coordY): 
  sourceW,sourceH = getDimantions(source)
  bgW,bgH = getDimantions(backGround)
  if (sourceW+coordX)>bgW or (sourceH+coordY)>bgH :
    return errorMSG(source,"YELL NO "+str(sourceW)+"x"+str(sourceH)+" "+str(coordX)+":"+str(coordY)+" "+str(bgW)+"x"+str(bgH))
  for x in range (0, bgW):
   for y in range (0, bgH):
    if x>=coordX and x<sourceW+coordX and y>=coordY and y<sourceH+coordY:
     picPixel=getPixelAt(backGround,x,y)
     pixelX=x-coordX
     pixelY=y-coordY
     pixel = getPixelAt(source,pixelX,pixelY)
     pixelRed = getRed(pixel) 
     pixelGreen = getGreen(pixel)
     pixelBlue = getBlue(pixel)
     newPicColor = makeColor( pixelRed,pixelGreen,pixelBlue)
     setColor(picPixel,newPicColor)
  return backGround

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def makeCollage(): 
    collage = makeNewPic(2550,3300)
    dir =r"D:\\Users\\live\Source\\Repos\\CST205-Multimedia-Design-and-Programming\\CST205Labs\\CST205Labs\\"
    #First
    filePath =r"LAB5\\lightenUp.jpg"
    fileIn =dir+r"Original\\"+filePath
    pic = makePicture(fileIn)
    offset = 0
    picW,picH = getDimantions(pic)
    newPic = pyCopy (pic,collage,629,offset)
    offset= offset+picH
    #Second
    filePath =r"LAB5\\lessRed.jpg"
    fileIn =dir+r"Original\\"+filePath
    pic = makePicture(fileIn)
    newPic = pyCopy (pic,collage,629,offset)
    picW,picH = getDimantions(pic)
    offset= offset+picH
    #Third
    filePath =r"LAB5\\mirrorHorisontalTB.jpg"
    fileIn =dir+r"Original\\"+filePath
    pic = makePicture(fileIn)
    newPic = pyCopy (pic,collage,629,offset)
    picW,picH = getDimantions(pic)
    offset= offset+picH
    #Forth
    filePath =r"LAB5\\betterBnW.jpg"
    fileIn =dir+r"Original\\"+filePath
    pic = makePicture(fileIn)
    newPic = pyCopy (pic,collage,629,offset)
    picW,picH = getDimantions(pic)
    offset= offset+picH
    #Fifth
    filePath =r"LAB5\\halfRed.jpg"
    fileIn =dir+r"Original\\"+filePath
    pic = makePicture(fileIn)
    newPic = pyCopy (pic,collage,629,offset)
    picW,picH = getDimantions(pic)
    offset= offset+picH
    #Sixth
    filePath =r"LAB5\\mirrorVertical.jpg"
    fileIn =dir+r"Original\\"+filePath
    pic = makePicture(fileIn)
    newPic = pyCopy (pic,collage,629,offset)
    picW,picH = getDimantions(pic)
    offset= offset+picH
    #Seven
    filePath =r"LAB5\\moreRed.jpg"
    fileIn =dir+r"Original\\"+filePath
    pic = makePicture(fileIn)
    newPic = pyCopy (pic,collage,0,0)
    #Eight
    filePath =r"LAB5\\noBlue.jpg"
    fileIn =dir+r"Original\\"+filePath
    pic = makePicture(fileIn)
    newPic = pyCopy (pic,collage,-961,1296)
    #Nine
    filePath =r"LAB5\\roseColoredGlasses.jpg"
    fileIn =dir+r"Original\\"+filePath
    pic = makePicture(fileIn)
    newPic = pyCopy (pic,collage,-961,600)
    #Twn
    filePath =r"LAB5\\rotatePic.jpg"
    fileIn =dir+r"Original\\"+filePath
    pic = makePicture(fileIn)
    newPic = pyCopy (pic,collage,-961,2003)
    #OutPutFile
    filePath =r"LAB5\\collage.jpg"            
    fileOut = dir+r"Result\\"+filePath
    writePictureTo(newPic,fileOut)
    
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
  dir =r"D:\\Users\\live\Source\\Repos\\CST205-Multimedia-Design-and-Programming\\CST205Labs\\CST205Labs\\"
  filePath =r"LAB5\\pyCopy.jpg"
  fileIn =dir+r"Original\\"+filePath
  fileOut = dir+r"Result\\"+filePath
  pic = makePicture(fileIn)
  emptyPic = makeNewPic(960,960)
  newPic = pyCopy (pic,emptyPic,105,144)
  pic = makePicture(fileIn)
  newPic = beforeAndAfter(pic,newPic)
  writePictureTo(newPic,fileOut)
    