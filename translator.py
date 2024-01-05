#text translator
'''#api_id="45e68fa234msh1f0ecdefb82fac7p17d1b5jsn737e9607495a"'''
from deep_translator import GoogleTranslator
to_translate = input("Enter text to translate: ")
a=input("Enter language to translate to: ")
translated = GoogleTranslator(source='auto', target=a).translate(to_translate)
print(translated)