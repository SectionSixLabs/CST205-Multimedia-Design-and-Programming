#Midterm Project Picture Filters
#Sergiy Zarubin
#Danny Tang

DIR =r"D:\\Users\\live\Source\\Repos\\CST205-Multimedia-Design-and-Programming\\CST205Labs\\\MidTermIGFilters\\"

def pyCopy(source, target, targetX, targetY): #source need be a makePicture object parameter
  #pic = makePicture(source)  #input course should be file directory path
  #above is commented out so that source is now a makepicture parameter
  #that way use functions that pipe into pyCopy

  pic = source
  pwidth = getWidth(pic)
  pheight = getHeight(pic)

  for x in range(0, pwidth):
    for y in range(0, pheight):
      colorSource = getColor(getPixel(pic, x, y)) #get color pixel of source
      targetPixel = getPixel(target, x+targetX, y+targetY) #target pixel
      setColor(targetPixel, colorSource)

def logoCopy(target, targetX, targetY): #source need be a makePicture object parameter
  #pic = makePicture(source)  #input course should be file directory path
  #above is commented out so that source is now a makepicture parameter
  #that way use functions that pipe into pyCopy

  logo = makePicture('/home/wave/Downloads/gitWorkspace/FilterIdeas/logo.png')
  pwidth = getWidth(logo)
  pheight = getHeight(logo)

  wPixel = makeColor(255, 255, 255) #Pixel to ignore in logo (this is white)


  for x in range(0, pwidth):
    for y in range(0, pheight):
      colorSource = getColor(getPixel(logo, x, y)) #get color pixel of source
      targetPixel = getPixel(target, x+targetX, y+targetY) #target pixel
      if(colorSource != wPixel):
        setColor(targetPixel, colorSource)

def advance(source):
  
  pic = source
  #make pic into black and white image
  pixels = getPixels(pic)
  for p in pixels:
    redP = getRed(p)
    blueP = getBlue(p)
    greenP = getGreen(p)
    averageP = redP*0.299 + greenP*0.587 + blueP*0.114
    makeGrey = makeColor(averageP, averageP, averageP)
    setColor(p, makeGrey)


  width = getWidth(pic)
  height = getHeight(pic)
   
  for x in range(0, width-1):
    for y in range(0, height-1):
      currentPixel = getPixel(pic, x, y)
      belowPixel = getPixel(pic, x, y+1)
      rightPixel = getPixel(pic, x+1, y)
      
      #luminescence 
      currentPixelLum = (getRed(currentPixel) + getGreen(currentPixel) + getBlue(currentPixel))/3
      belowPixelLum = (getRed(belowPixel) + getGreen(belowPixel) + getBlue(belowPixel))/3
      rightPixelLum = (getRed(rightPixel) + getGreen(rightPixel) + getBlue(rightPixel))/3
  
      #from trying various differenceValues, increasing number resulted in less filled in black pixels and vice versa
      differenceValue = 7
      if( abs(currentPixelLum - belowPixelLum) > differenceValue and abs(currentPixelLum - rightPixelLum) > differenceValue):
        setColor(currentPixel, black)

      if( abs(currentPixelLum - belowPixelLum) <= differenceValue and abs(currentPixelLum - rightPixelLum) <= differenceValue):
        setColor(currentPixel, white) 
  
  return pic


def CSUMBerize():
    file = pickAFile()
    pic = makePicture(file)
    width = getWidth(pic)
    height = getHeight(pic)
    if(height < 250): #250 is logo height
      print("Image height too small")
      return None
    if(width < 685): #685 is logo width
      print("Image width is too small")
      return None

    canvas = makeEmptyPicture(width, height)
    pyCopy(pic, canvas, 0, 0)

    logoCopy(canvas, 0, height-250) #logo height 250
    advance(canvas)
    show(canvas)
    writePictureTo(canvas, '/home/wave/Downloads/gitWorkspace/FilterIdeas/CSUMBerize.jpg')
    return(canvas)

def logoCP (source, backGround, coordX, coordY,color2ignor): 
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
    newColor= makeColor(poseterize(redP), poseterize(greenP), poseterize(blueP))
    setColor(pixel, newColor)
  return (pic)

def Spectify(pic):
  for pixel in getPixels(pic):
    newColour = spectrumZX(pixel)
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
  pic = Spectify(pic)
  pic = shrincPic(pic) 
  pic = shrincPic(pic)
  pic = blowUpPic(pic)
  pic = blowUpPic(pic)
  return (pic)
  
def spectrumZX(pixel):
    redP = getRed(pixel)
    blueP = getBlue(pixel)
    greenP = getGreen(pixel)
    color = makeColor(redP,greenP,blueP)
    if redP<100 and blueP<100 and  greenP<100:
        return black
    elif redP<40 and blueP>170 and  greenP<40:
      return blue
    elif redP>170 and blueP<40 and  greenP<40:
      return red
    elif redP>150 and blueP>200 and  greenP==0:
     return magenta
    elif redP<40 and blueP<40 and  greenP>170:
      return green
    elif redP==0 and blueP>150 and  greenP>150:
      return cyan
    elif redP>150 and blueP==0 and  greenP>150:
      return yellow
    elif  redP>150 and blueP>150 and  greenP>150:
      return white
    else: 
      return color

def makeGameSplash(pic,gameName):
    filePath =r"activision.jpg"
    fileIn =DIR+r"Originals\\"+filePath
    logoBaseColor = makeColor(25,25,25)
    logo = makePicture(fileIn)
    logoW,logoH = getDimantions(logo)
    picW,picH = getDimantions(pic)
    pic= logoCP(logo,pic,(picW-logoW-1)//2, picH-logoH-1,logoBaseColor)
    import java.awt.Font as Font
    myFont = makeStyle("Times New Roman", Font.BOLD, 82)
    addTextWithStyle(pic,10,100,gameName,myFont,red)
    pic = filter8bit(pic)
    return pic

def Run():
    filePath =r"SeZa.jpg"
    fileIn =DIR+r"Originals\\"+filePath
    fileOut =DIR+r"Result\\"+filePath
    pic = makePicture(fileIn)
    pic = makeGameSplash(pic,"Office Simulator")
    writePictureTo(pic,fileOut)
