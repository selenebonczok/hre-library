import os
from google.cloud import translate_v2 as translate
import pandas as pd
import six

# Set the path to the Google Cloud Credentials.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "[Insert here the location of your credentials]"

#The following versions of the same function serve different purposes.

def translate_text(source, text):
    """
    (GENERIC TRANSLATE_TEXT)
    Translates text from the source language to English.
    Source and text parameters are required.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    if pd.isnull(text):
        return text
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = #insert here the location of your credentials
    
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")
        
    try:

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
        result = translate_client.translate(text, source_language=source, target_language='en')
        return result["translatedText"]
    
    except:
        return text
    return result["translatedText"]

def translate_text(text):
    """
    Translates text from the source language to English.
    Source and text parameters are required.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    if pd.isnull(text):
        return text
    
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

      # Detect the source language
    detection = translate_client.detect_language(text)
    source_language = detection['language']
    
        # Check if the detected language is already English
    if source_language == 'en':
        return text

    try:
        result = translate_client.translate(text, source_language= source_language, target_language='en')
        return result["translatedText"]
    
    except:
        return text
    return result["translatedText"]

def translate_youtube_outputs(df, language_code):
    """
    Translates 'Title', 'Description', and 'Tags' columns from a YouTube dataframe using a specified language.
    """
    df['Title'] = df.apply(lambda row: translate_text(language_code, row['Title']), axis=1)
    df['Description'] = df.apply(lambda row: translate_text(language_code, row['Description']), axis=1)
    df['Tags'] = df.apply(lambda row: translate_text(language_code, row['Tags']), axis=1)

    return df

def translate_youtube_outputs(df):
    """
    Translates 'Title', 'Description', and 'Tags' columns from a YouTube dataframe by automatically detecting the source language.
    """
    df['Title'] = df['Title'].apply(translate_text)
    df['Description'] = df['Description'].apply(translate_text)
    df['Tags'] = df['Tags'].apply(translate_text)

    return df
    

