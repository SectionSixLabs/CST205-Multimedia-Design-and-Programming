#Sergiy Zarubin
#Danny Tran
#Specific to each student based opn the environment 
DIR =r"D:\\Users\\live\Source\\Repos\\CST205-Multimedia-Design-and-Programming\\CST205Labs\\CST205Labs\\"
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
  printNow (sourceSampleRate)
  printNow (len(getSamples(source)))
  numberSamples = end-start+1
  printNow (numberSamples)
  newClip = makeEmptySound (numberSamples,sourceSampleRate)
  for sampleIndex in range(start,end-2):
    sourceVolume = getSampleValueAt(source, sampleIndex) 
    setSampleValueAt(newClip,sampleIndex-start,sourceVolume)
  return maxVolume(newClip)

def SampleDown(source,coeficient):

    sourceSamples =getSamples(source)
    newSampleRate = int(getSamplingRate(source))//coeficient
    numSourceSamples = len(sourceSamples)
    
    index=0
    newClip = makeEmptySound (numSourceSamples//coeficient,newSampleRate)
    
    for sampleIndex in range(0,numSourceSamples,coeficient):
      sourceVolume = getSampleValueAt(source, sampleIndex) 
      setSampleValueAt(newClip,index,sourceVolume)
      index=index+1
    return newClip

def copy(source, target, start):
    sourceSamples =getSamples(source)
    targetSamples = getSamples(target)
    
    sourceRate = int(getSamplingRate(source))
    targetRate = int(getSamplingRate(source))
    if sourceRate==targetRate:

      newSampleRate = targetRate
      coeficient = 1
      numSourceSamples = len(sourceSamples)
      numTargetSamples = len(targetSamples)
      
    elif sourceRate>targetRate:
    
      newSampleRate = targetRate
      coeficient =  targetRate//sourceRate
      source = SampleDown(source,coeficient)
      numSourceSamples = len(sourceSamples)
      numTargetSamples = len(targetSamples)
      sourceSamples =getSamples(source)
      
    elif sourceRate<targetRate:
    
      newSampleRate = sourceRate
      coeficient =  sourceRate//targetRate
      source = SampleDown(source,coeficient)
      numSourceSamples = len(sourceSamples)
      numTargetSamples = len(targetSamples)
      targetSamples = getSamples(target)
      
    newClip = makeEmptySound (numSourceSamples+numTargetSamples,newSampleRate)
    numNewClipSamples = len(getSamples(newClip))
    
    sourceIndex = 0
    targetIndex = start+1
    
    for sampleIndex in range (0,numNewClipSamples-1):
      if sampleIndex<start:
        targetVolume = getSampleValueAt(target, sampleIndex) 
        setSampleValueAt(newClip,sampleIndex,targetVolume)
      elif sourceIndex<numSourceSamples:
        sourceVolume = getSampleValueAt(source, sourceIndex) 
        setSampleValueAt(newClip,sampleIndex,sourceVolume)
        sourceIndex=sourceIndex+1
      elif sourceIndex>=numSourceSamples  and sampleIndex>numNewClipSamples:
        targetVolume = getSampleValueAt(target, targetIndex) 
        setSampleValueAt(newClip,sampleIndex,targetVolume)
        targetIndex=targetIndex+1
    return newClip  
def makeaSound(): 
  filePath1 =r"LAB9\\tdnpss02.wav"
  filePath2 =r"LAB9\\tmapss02.wav"
  filePath3 =r"LAB9\\tmapss05.wav"
  filePath4 =r"LAB9\\tphpss01.wav"
  filePath5 =r"LAB9\\tvkwht02.wav"
  #Set input and output path
  fileIn1 =DIR+r"Original\\"+filePath1
  fileIn2 =DIR+r"Original\\"+filePath2
  fileIn3 =DIR+r"Original\\"+filePath3
  fileIn4 =DIR+r"Original\\"+filePath4
  fileIn5 =DIR+r"Original\\"+filePath5
  #print fileIn
  #Initialise the sound 
  sound1 = makeSound(fileIn1)
  #explore(sound1)
  sound2 = makeSound(fileIn2)
  #explore(sound2)
  sound3 = makeSound(fileIn3)
  #explore(sound3)
  sound4 = makeSound(fileIn4)
  #explore(sound4)
  sound5 = makeSound(fileIn5)
  #explore(sound5)
  newClip= copy(sound2,sound3,14219)
  newClip= copy(sound4,newClip,48927)
  newClip= copy(clip(sound1,31408,53976),newClip,81968)
  newClip= copy(clip(sound5,4964,40442),newClip,105501)
  newClip =clip(newClip,0,145501)
  return newClip

def reverse(source):
   sourceSamples =getSamples(source)
   numSourceSamples = len(sourceSamples)
   newSampleRate = int(getSamplingRate(source))
   newClip = makeEmptySound (numSourceSamples,newSampleRate)
   index=0
   endIndex = numSourceSamples-1
   for sample in sourceSamples:
     sourceVolume = getSampleValueAt(source, index) 
     setSampleValueAt(newClip,endIndex-index,sourceVolume)
     index=index+1
   return maxVolume(newClip)
  
def Run():

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
  #Set input and output path
  #fileIn =DIR+r"Original\\"+filePath
  #fileOut =DIR+r"Result\\"+filePath
  #print fileIn
  #Initialise the sound 
  #sound = makeSound(fileIn)
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
#LAB9
  filePath =r"LAB9\\cards.wav"
  fileIn =DIR+r"Original\\"+filePath
  sound = makeSound(fileIn)
  #newClip=reverse(sound)
  #explore(newClip)
  newClip=reverse(sound)
  #explore(newClip)
  #Sound 1 (0 - 11232) But I think
  #32760-53976 Too Familiar
  #Sound 2 0-24272 Oh My God
  #25912 - 49692 he's wet
  #Sound 3 0-14219 You wana pee 48927 81968
  #explore(newSound)
  #fileOut =DIR+r"Result\\LAB9\\ReversedCards.wav"
  fileOut =DIR+r"Result\\LAB9\\NewSounds.wav"
  #writeSoundTo(newClip, fileOut)
  writeSoundTo(makeaSound(), fileOut)
  
    