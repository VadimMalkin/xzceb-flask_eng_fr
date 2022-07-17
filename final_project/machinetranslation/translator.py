'''This is translator, for a project'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey='3wk8xytF2Y5pUvH-hOqk0n4EDlRobJApqrVpMdOlZvgN'
url='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/3c7bc7f0-28b5-4997-9461-c078b903158a'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-07-15',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    '''This function transalates english to french '''
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    '''This function transalates french to english'''
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
