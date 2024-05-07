from django.http import HttpResponse
from django.shortcuts import render
from spellchecker import SpellChecker
import spacy
from spacy import displacy
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from rake_nltk import Rake

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    r = Rake()     # Uses stopwords for english from NLTK, and all puntuation characters.
    r.extract_keywords_from_text(text)     # Extraction given the text.
    keyword_dict_scores = r.get_word_degrees()    # Getting the dictionary with key words as keys and their scores as values
    sorted_keywords = sorted(keyword_dict_scores.items(), key=lambda x: x[1], reverse=True)[:5]     # Sort and get the top 5 keywords
    keywords = [keyword for keyword, score in sorted_keywords]     # Extracting keywords from the sorted list
    return keywords

def index(request):
    param = {'name':'Akash Sarkar', 'place': 'India'}
    return render(request, 'index2.html', param)

def analyze(request):
    text = request.GET.get('Your_Input', 'default')
    analyzed_text = text
    removepunc = request.GET.get('remove_punctuation', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    small = request.GET.get('small', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    sentencecount = request.GET.get('sentencecount', 'off')
    paragraphcount = request.GET.get('paragraphcount', 'off')
    keywordextraction = request.GET.get('keywordextraction', 'off')
    ner = request.GET.get('ner', 'off')
    palindrome = request.GET.get('palindrome', 'off')
    spellchecker = request.GET.get('spellchecker', 'off')
    spell = SpellChecker()
 
 
    if removepunc == 'on':
        punctuations = ''' , . ! ? : ; ' " ( ) [ ] { } - — _ / \ * + = < > % $ # @ & '''
        analyzed_text = ''.join(char for char in analyzed_text if char not in punctuations)
            
    if capitalize == 'on':
        analyzed_text = analyzed_text.upper()
    
    if small == 'on':
        analyzed_text = analyzed_text.lower()
    
    if newlineremover == 'on':
        analyzed_text = analyzed_text.replace('\n', '')
    
    if extraspaceremover == 'on':
        analyzed_text = ' '.join(analyzed_text.split())
    
    if charcount == 'on':
        charnumber = len(analyzed_text.replace(" ", ''))
        analyzed_text += f'\nTotal Character Count: {charnumber}'
    
    # Check sentence count before modifying the text
    if sentencecount == 'on':
        sentencecount = analyzed_text.count('.') + analyzed_text.count('!') + analyzed_text.count('?')
        analyzed_text += f'\nSentence Count: {sentencecount}'
    
    if paragraphcount == 'on':
        paragraphs = analyzed_text.split('\n\n')
        paragraphcount = len(paragraphs)
        analyzed_text += f'\nParagraph Count: {paragraphcount}'
    
    if keywordextraction == 'on':
        keywords = extract_keywords(analyzed_text)
        analyzed_text += f'\nKeywords: {keywords}'
    
    if ner == 'on':
        doc = nlp(analyzed_text)
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        analyzed_text += '\nNamed Entities:\n'
        analyzed_text += "\n".join([f"{entity[0]}: {entity[1]}" for entity in entities])
    
    # Check palindrome before modifying the text
    if palindrome == 'on':
        if analyzed_text.lower().replace(" ", '') == analyzed_text.lower().replace(" ", '')[::-1]:
            analyzed_text += '\nYour text is Palindrome'
        else:
            analyzed_text += '\nYour text is not a Palindrome'
    
    if spellchecker == 'on':
        misspelled = spell.unknown(analyzed_text.split())
        for word in misspelled:
            analyzed_text = analyzed_text.replace(word, spell.correction(word))
    
    params = {'purpose': 'Text Analysis', 'analyzed_text': analyzed_text}
    return render(request, 'analyze2.html', params)

def aboutme(request):
    return render(request, 'aboutme.html')

def contact(request):
    return render(request, 'contact.html')
