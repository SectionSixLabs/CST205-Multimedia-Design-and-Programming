def getDimantions(pic):
     widthPic= getWidth(pic)
     heightPic = getHeight(pic)
     return widthPic, heightPic

def shrincPic(pic):
  widthPic, heightPic = getDimantions(pic)
  newPic = makeEmptyPicture(widthPic//4,heightPic//4)
  for x in range (0, widthPic,4):
    for y in range (0, heightPic,4):
      pixel = getPixelAt(pic,x,y)
      newPixel  = getPixelAt(newPic,x//4,y//4)
      color2Copy= getColor(pixel)
      setColor(newPixel,color2Copy)
  return newPic 

def blowUpPic(pic)
  widthPic, heightPic = getDimantions(pic)
  newPic = makeEmptyPicture(widthPic*4,heightPic*4)
  for x in range (0, widthPic*4):
   for y in range (0, heightPic*4):
      pixel = getPixelAt(pic,x//4,y//4)
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


