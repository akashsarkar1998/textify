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
    text = request.POST.get('Your_Input', 'default')
    analyzed_text = text
    removepunc = request.POST.get('remove_punctuation', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    small = request.POST.get('small', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    sentencecount = request.POST.get('sentencecount', 'off')
    paragraphcount = request.POST.get('paragraphcount', 'off')
    keywordextraction = request.POST.get('keywordextraction', 'off')
    ner = request.POST.get('ner', 'off')
    palindrome = request.POST.get('palindrome', 'off')
    spellchecker = request.POST.get('spellchecker', 'off')
    spell = SpellChecker()
 
    if removepunc == 'on':
        punctuations = ''' , . ! ? : ; ' " ( ) [ ] { } - — _ / \ * + = < > % $ # @ & '''
        analyzed_text = ''.join(char for char in analyzed_text if char not in punctuations)
            
    elif capitalize == 'on':
        analyzed_text = analyzed_text.upper()
    
    elif small == 'on':
        analyzed_text = analyzed_text.lower()
    
    elif newlineremover == 'on':
        analyzed_text = ''
        for char in text:
            if char != '\n' and char != '\r':
                analyzed_text += char    
                
    elif extraspaceremover == 'on':
        analyzed_text = ' '.join(analyzed_text.split())
    
    elif charcount == 'on':
        charnumber = len(analyzed_text.replace(" ", ''))
        analyzed_text += f'\nTotal Character Count: {charnumber}'
    
    # Check sentence count before modifying the text
    elif sentencecount == 'on':
        sentencecount = analyzed_text.count('.') + analyzed_text.count('!') + analyzed_text.count('?')
        analyzed_text += f'\nSentence Count: {sentencecount}'
    
    elif paragraphcount == 'on':
        paragraphs = analyzed_text.split('\n\n')
        paragraphcount = len(paragraphs)
        analyzed_text += f'\nParagraph Count: {paragraphcount}'
    
    elif keywordextraction == 'on':
        keywords = extract_keywords(analyzed_text)
        analyzed_text += f'\nKeywords: {keywords}'
    
    elif ner == 'on':
        doc = nlp(analyzed_text)
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        analyzed_text += '\nNamed Entities:\n'
        analyzed_text += "\n".join([f"{entity[0]}: {entity[1]}" for entity in entities])
    
    # Check palindrome before modifying the text
    elif palindrome == 'on':
        if analyzed_text.lower().replace(" ", '') == analyzed_text.lower().replace(" ", '')[::-1]:
            analyzed_text += '\nYour text is Palindrome'
        else:
            analyzed_text += '\nYour text is not a Palindrome'
    
    elif spellchecker == 'on':
        misspelled = spell.unknown(analyzed_text.split())
        for word in misspelled:
            analyzed_text = analyzed_text.replace(word, spell.correction(word))
            
    elif removepunc != 'on' and capitalize != 'on' and newlineremover != 'on' and small != 'on' and extraspaceremover != 'on' and charcount != 'on' and sentencecount != 'on' and paragraphcount != 'on' and keywordextraction != 'on' and ner != 'on' and palindrome != 'on' and spellchecker != 'on':
        return HttpResponse('<h1>Error:</h1> <p> You have to select an operation. Please try again.</p> <p>Go back to <a href="/">HOME</a></p>')
    
    params = {'purpose': 'Text Analysis', 'analyzed_text': analyzed_text}
    return render(request, 'analyze2.html', params)
    
def aboutme(request):
    return render(request, 'aboutme.html')

def contact(request):
    return render(request, 'contact.html')
