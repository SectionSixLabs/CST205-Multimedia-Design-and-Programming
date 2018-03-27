#Sergiy Zarubin
#Danny Tran

#LAB8      
#Warm Up      
      
def retrieveSample(samples, index): 
  return getSampleValueAt(samples, index) 

def increaseVolume(sound):
   for sample in getSamples(sound):
     value = getSampleValue(sample)
     setSampleValue(sample, value * 2)
   
      
def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value/2)
  
    
def changeVolume(sound, amount):        
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    
    #issue with amount/100
    
    setSampleValue(sample, value + value * amount//100) #Floor (does not accept decimals)
  return sound
  
def maxSample(sound):
  soundArr = getSamples(sound)
  
  currentMax = getSampleValue(soundArr[0])
  
  for sample in soundArr:
    value = getSampleValue(sample)
    currentMax = max(value, currentMax)
    
  return currentMax    #127 from shirley, #32767 score.wav
  
  
def maxVolume(sound):
  largest = maxSample(sound)
  factor=32767.0/largest
  print factor
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    
    newVolume =  value*factor
    if newVolume>32767:
      newVolume = 32767
    
    setSampleValue(sample,newVolume) #Floor (does not accept decimals)
  return sound
    
    
def goToEleven(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    elif value < 0:
      setSampleValue(sample, -32767)
  
  return sound
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#LAB9
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def clip(source,start,end):
  sourceSampleRate =int( getSamplingRate(source))
  print sourceSampleRate
  numberSamples = end-start
  print numberSamples
  newClip = makeEmptySound (numberSamples,sourceSampleRate)
  for sampleIndex in range(start,end):
    sourceVolume = getSampleValueAt(source, sampleIndex) 
    setSampleValueAt(newClip,sampleIndex-start,sourceVolume)
  return maxVolume(newClip)

def copy(source, target, start):
    sourceSamples =getSamples(source)
    targetSamples = getSamples(target)
    numSourceSamples = len(sourceSamples)
    numTargetSamples = len(targetSamples)
    
def reverse(sound):
  return ""
  
def Run():
  #Specific to each student based opn the environment 
  dir =r"D:\\Users\\live\Source\\Repos\\CST205-Multimedia-Design-and-Programming\\CST205Labs\\CST205Labs\\"
#LAB8
  #Now you try it:
  #filePath =r"LAB8\\shirley.wav"
  #Increase the Volume:
  #filePath =r"LAB8\\increaseVolume.wav"
  #decreaseVolume 
  #filePath =r"LAB8\\decreaseVolume.wav"
  #changeVolume 
  #filePath =r"LAB8\\changeVolumePlus.wav"
  #changeVolume 
  #filePath =r"LAB8\\changeVolumeMinus.wav"
  #maxVolume
  #filePath =r"LAB8\\maxVolume.wav"
  #goToEleven
  #filePath =r"LAB8\\goToEleven.wav"
#LAB9
  filePath =r"LAB9\\cantdo.wav"
  #Set input and output path
  fileIn =dir+r"Original\\"+filePath
  fileOut =dir+r"Result\\"+filePath
  print fileIn
  #Initialise the sound 
  sound = makeSound(fileIn)
  explore(sound)
  newSound = clip(sound,0,16154)
  explore(newSound)
  #Now you try it:
  #print retrieveSample(sound, 10000)
  #increaseVolume(sound)
  #decreaseVolume(sound)
  #changeVolume(sound, 75)
  #changeVolume(sound, -75)
  #print maxSample(sound)
  #maxVolume(sound)
  #goToEleven(sound)
  #writeSoundTo(sound, fileOut)
  #explore(sound)
  
    