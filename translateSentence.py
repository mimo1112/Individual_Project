from googletrans import Translator, constants
from pprint import pprint


class translateSentence:
    def trans_sentence(sentence_to_translate):
        translator = Translator()
        #googletrans.LANGUAGES LANGCODES
        translation = translator.translate(sentence_to_translate, dest="ko")
        return translation.text

