#CST 205 Lab #6
#Section Six Labs
#Sergiy Zarubin


#Helper Functions
#We are assuming that we know the region affected by read eye issue
def getRegions(): 
  return [[358,526],[379,548],[592,526],[618,548]]
  
def getDimantions(pic):
  return getWidth(pic),getHeight(pic)

def errorMSG(pic,txt):
    w,h = getDimantions(pic)
    c = makeColor(255, 0, 0)
    s = makeStyle(sansSerif, bold, 30)
    addTextWithStyle(pic, w//2, h//2, txt, s, c)
    return pic

    
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
     
def betterBnW(pic):
  for pixel in getPixels(pic):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getGreen(pixel)
    better = r*0.299 + g*0.587 + b*0.114
    set = makeColor(better, better, better)
    setColor(pixel, set)
  return pic
 
  
def getDistanceFromBase(pixel, baseColor):
  col = getColor(pixel)
  return distance(baseColor, col)

##WARM UP##
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
   

#Problem #1 Sepia 
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


#Problem #2 Art-i-fy

def Artify(pic):
  for pixel in getPixels(pic):
    redP = getRed(pixel)
    blueP = getBlue(pixel)
    greenP = getGreen(pixel)
    newColour = makeColor(poseterize(redP), poseterize(greenP), poseterize(blueP))
    setColor(pixel, newColour)
  return (pic)

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
  
def Run():
  pic = makePicture('C:\\Users\\live\\OneDrive\\CSUMB\\CST205\\Week2\\Lab6\\Original\\maxresdefault.jpg')
  bg = makePicture('C:\\Users\\live\\OneDrive\\CSUMB\\CST205\\Week2\\Lab6\\Original\\swbg.jpg')
  newPic = chromakey (pic,bg,1000,1000)
  writePictureTo(newPic,'C:\\Users\\live\\OneDrive\\CSUMB\\CST205\\Week2\\Lab6\\Result\\GSError.jpg')
  #newPic=Sepia(makePicture(pickAFile()))
  #writePictureTo(newPic,'C:\\Users\\live\\OneDrive\\CSUMB\\CST205\\Week2\\Lab6\\Result\\Sepia.jpg')
  #newPic=Artify(makePicture(pickAFile()))
  #writePictureTo(newPic,'C:\\Users\\live\\OneDrive\\CSUMB\\CST205\\Week2\\Lab6\\Result\\Artify.jpg')
  #newPic=redEye(makePicture(pickAFile()))
  #writePictureTo(newPic,'C:\\Users\\live\\OneDrive\\CSUMB\\CST205\\Week2\\Lab6\\Result\\redEye.jpg')
  show(newPic)
    