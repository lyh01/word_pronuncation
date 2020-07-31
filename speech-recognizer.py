import sys
import speech_recognition as sr

_sampleRate = 16000

_recognizer = sr.Recognizer()

_microphone = sr.Microphone(sample_rate=_sampleRate, chunk_size=_sampleRate)

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

    Record each word and save as <word>.wav and <word>.txt

   """

   print("\nPlease pronounce: {} ".format(word))

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
for word in words:
   print(word)

needInstructions = True


if (needInstructions):
   msg1 = "\n\n\nTotal number of words: {}".format(len(words))
   msg2 = "\nPlease review the word list"
   msg3 = "\nThere will be five seconds for each word"
   msg4 = "\nPlease pronounce the word when presented"
   instruction(msg1 + msg2 + msg3 + msg4)
   needInstruction = False

# Check for presence of microphone(s), need at least one to begin
if (len(_microphone.list_microphone_names()) >=  1):
   print("\nMicrophone(s) detected on this computer: {}".format(_microphone.list_microphone_names()))
else:
   print("No microphone detected ... exiting")
   exit(12)

# Get started

input("\nPress enter when ready to start ...")


for word in words:
   record(word)

