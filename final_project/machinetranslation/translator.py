'''
This program to translate one language to another language
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
#os.environ['APIKEY'] = '/home/project/xzceb-flask_eng_fr/final_project/machinetranslation'
#os.environ['URL'] = '/home/project/xzceb-flask_eng_fr/final_project/machinetranslation'
apikey = os.environ['APIKEY']
url = os.environ['URL']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(englishtext):
    """Translate english To French"""
    translation = language_translator.translate(
    text=englishtext, model_id='en-fr').get_result()
    frenchtext =translation['translations'][0]['translation']
    return frenchtext

def french_to_english(frenchtext):
    """Translate french To English"""
    translation = language_translator.translate(
    text=frenchtext, model_id='fr-en').get_result()
    englishtext=translation['translations'][0]['translation']
    return englishtext

print(english_to_french('hello'))