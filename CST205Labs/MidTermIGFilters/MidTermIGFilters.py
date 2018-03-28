#Possible Filter Idea for the CSUMB-erize Instagram Filter
#What it does so far is just copy the CSUMB logo onto an chosen image
#Not sure what to do with the original image yet, Possibly make it monochrome
#Or possibly artified black / white...

def logoCopy (source, backGround, coordX, coordY,color2ignor): 
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
     if newPicColor!=color2ignor:
      setColor(picPixel,newPicColor)
  return backGround

def getDimantions(pic):
     widthPic= getWidth(pic)
     heightPic = getHeight(pic)
     return widthPic, heightPic

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def shrincPic(pic):
  widthPic, heightPic = getDimantions(pic)
  newPic = makeEmptyPicture((widthPic+1)//2,(heightPic+1)//2)
  for x in range (0, widthPic,2):
    for y in range (0, heightPic,2):
      pixel = getPixelAt(pic,x,y)
      newPixel  = getPixelAt(newPic,x//2,y//2)
      color2Copy= getColor(pixel)
      setColor(newPixel,color2Copy)
  return newPic

def blowUpPic(pic):
  widthPic, heightPic = getDimantions(pic)
  newW = widthPic*2
  newH = heightPic*2
  printNow(str(newW)+"X"+str(newH))
  newPic = makeEmptyPicture(newW,newH)
  for x in range (0, newW):
   for y in range (0, newH):
      pixel = getPixelAt(pic,x//2,y//2)
      newPixel  = getPixelAt(newPic,x,y)
      color2Copy= getColor(pixel)
      setColor(newPixel,color2Copy)
  return newPic 

def Artify(pic):
  for pixel in getPixels(pic):
    redP = getRed(pixel)
    blueP = getBlue(pixel)
    greenP = getGreen(pixel)
    newColour = makeColor(poseterize(redP), poseterize(greenP), poseterize(blueP))
    setColor(pixel, newColour)
  return (pic)

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

def filter8bit(pic):
  pic = Artify(pic)
  pic = shrincPic(pic) 
  pic = shrincPic(pic)
  pic = blowUpPic(pic)
  pic = blowUpPic(pic)
  return (pic)

def makeGameSplash(pic,gameName):
    dir =r"D:\\Users\\live\Source\\Repos\\CST205-Multimedia-Design-and-Programming\\CST205Labs\\\MidTermIGFilters\\"
    filePath =r"activision.jpg"
    fileIn =dir+r"Originals\\"+filePath
    logoBaseColor = makeColor(25,25,25)
    logo = makePicture(fileIn)
    logoW,logoH = getDimantions(logo)
    picW,picH = getDimantions(pic)
    pic= logoCopy(logo,pic,(picW-logoW-1)//2, picH-logoH-1,logoBaseColor)
    import java.awt.Font as Font
    myFont = makeStyle("Times New Roman", Font.BOLD, 84)
    addTextWithStyle(pic,200,200,gameName,myFont,red)
    pic = filter8bit(pic)
    return pic

def Run():
    dir =r"D:\\Users\\live\Source\\Repos\\CST205-Multimedia-Design-and-Programming\\CST205Labs\\\MidTermIGFilters\\"
    filePath =r"IMG_0097.jpg"
    fileIn =dir+r"Originals\\"+filePath
    fileOut =dir+r"Result\\"+filePath
    pic = makePicture(fileIn)
    pic = makeGameSplash(pic,"Wedding Crashers")
    writePictureTo(pic,fileOut)
