from posTagger import pos
import speech_recognition as SR
class SpeechText_with_POS:
    def getText( self, lang='en-US' ):

        recognize = SR.Recognizer()
        with SR.Microphone() as source:# can be raised error like No input device from Microphone.May be solved by providing Device index 
            print("say something")
            speech = recognize.listen(source)   # start recording from microphone for the  first phrase
            print('listening finished')
        
        text=None

        try:
            text = recognize.recognize_google( speech, language=lang )#recognize speech using Google Speech Recognition
            print(text)
        except ValueError|LookupError as error:
            print("Couldn't uderstand the audio")
            print(error)
        
        return text
    
    def getTextWithPOS( self, text ):#text must be Bengali Language because used POS tagger is only for Bengali Language
        pos_tagger = pos()
        # sentence = 'কেমন আছেন'
        words = text.split()
        list_of_tagged_words=list()
        for word in words:
            # print(pos_tagger.posTagging(word))#print the POS for every words in the text
           list_of_tagged_words.append(pos_tagger.posTagging(word))
        
        return list_of_tagged_words

        

