import sys
import speech_recognition as sr

_sampleRate = 16000

_recognizer = sr.Recognizer()

_microphone = sr.Microphone(sample_rate=_sampleRate, chunk_size=_sampleRate)

words = ["glycogen", "sugar", "Tesla"]

def getWordList():
   if sys.argv[1]:
      with open(sys.argv[1],"r") as input:
         _words = input.readlines()
      words = []
      for w in _words:
         words.append(w.strip("\n"))
   return words

def instruction(msg):
   print(msg)

def record(word):
   """

    Record each word save save as <word>.wav and <word>.txt

   """

   print("please pronounce: {} ".format(word))

   with _microphone as source:
      #_audioData = _recognizer.listen(source, phrase_time_limit=1)
      _audioData = _recognizer.record(source, duration=5)


   with open(word + ".wav", "wb") as _wavOut:
      _wavOut.write(_audioData.get_wav_data())
      _wavOut.close()

   with open(word + ".txt", "w") as _wordOut:
      _wordOut.write(word)
      _wordOut.close()


words = []
words = getWordList()

needInstructions = True

if needInstructions == True:
   msg1 = "\n\nThere will be five seconds for each word"
   msg2 = "\nThere will be {} words".format(len(words))
   msg3 = "\nHere they are:\n"
   instruction(msg1 + msg2 + msg3)
   print(words)
   instruction("\n\nPlease pronouce the word when presented")
   needInstruction = False


for word in words:
   record(word)

