from SpeechToText_POSTagger import SpeechText_with_POS

speech_to_text_and_POS = SpeechText_with_POS()

text = speech_to_text_and_POS.getText('bn-BD')

if text!=None:
    print( speech_to_text_and_POS.getTextWithPOS(text) )
else:
    print('failed to generate text')