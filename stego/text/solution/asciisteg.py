originalFile = open('original-image.txt', "r")
challengeFile = open('../challenge/challenge.txt', "w")

outputString = ''
secretMsg = '  flag{psych0-t3xt}'
secretMsgCounter = 0
spacer = 50

for i, c in enumerate(originalFile.read()):
  if i % spacer == 0 and secretMsgCounter < len(secretMsg):
    outputString += secretMsg[secretMsgCounter]
    secretMsgCounter+=1
  else:
    outputString += c

challengeFile.write(outputString)
challengeFile.close()