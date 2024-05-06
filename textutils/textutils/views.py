# from django.http import HttpResponse
# from django.shortcuts import render

# These are codes for Till Day 6 videos!!
# def index(request):
#     return HttpResponse("Hello, world. This is Akash Sarkar, You're at the polls index.")
# def about(request):
#     return HttpResponse('This is the ABOUT section')
# def display_text(request):
#     file = open('textutils/hello.txt', 'r')
#     return HttpResponse(file.read())
# def link_pages(request):
#     return HttpResponse('<h1>Click here to go to <a href="https://www.facebook.com/">facebook</a></h1> <br> <h2>Click here to go to <a href="https://www.google.com/">Google</a></h2>')



# Day 10 to 
from django.http import HttpResponse
from django.shortcuts import render
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
    text = request.GET.get('Your_Input', 'default')  # THis GET.get returns the text we put in the text area, if theres no value, then it will print default
    removepunc = request.GET.get('remove_punctuation', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    sentencecount = request.GET.get('sentencecount', 'off')
    paragraphcount = request.GET.get('paragraphcount', 'off')
    keywordextraction = request.GET.get('keywordextraction', 'off')
    ner = request.GET.get('ner', 'off')
    
    # Check box to check all punc s:
    if removepunc == 'on':
        punctuations = ''' , . ! ? : ; ' " ( ) [ ] { } - — _ / \ * + = < > % $ # @ & '''
        punctuations_in_text = ''
        analyzed_text = ''  # If I use empty list [], then result is ['d', 'j', 'd', 'd', 'p', 'k', 'a', 's', 'c', 'k', 'j', 'd', 'c', 'n']
        for char in text:
            if char not in punctuations:
                analyzed_text += char
            elif char in punctuations:
                punctuations_in_text += char
        params = {'purpose': 'Remove Punctuations from texts', 'analyzed_text': analyzed_text, 'punctuations_in_text' : punctuations_in_text,}
        return render(request, 'analyze2.html', params)
    
    #Check box to convert all text into upper case:
    elif capitalize == 'on' :
        analyzed_text = ''
        for char in text:
            analyzed_text += char
        params = {'purpose': 'Capitalize texts',  'analyzed_text': analyzed_text.upper()}
        return render(request, 'analyze2.html', params)
    
    #Checkbox to new line remover:
    elif newlineremover == 'on':
        analyzed_text = ''
        for char in text:
            if char !='\n':
                analyzed_text += char
        params = {'purpose': 'New Line remove',  'analyzed_text': analyzed_text}
        return render(request, 'analyze2.html', params)
    
    #Checkbox for extra space remover:
    elif extraspaceremover =='on':
        analyzed_text = ''
        for index, char in enumerate(text):
            # if text[index] == ' ' and text[index+1] == ' ':
            # if not(text[index] == ' ' and text[index+1] == ' '):
            if not (char == ' ' and text[index + 1] == ' '):
                # pass
                analyzed_text += char
            # else:
            #     analyzed_text += char
        params = {'purpose': 'New Line remove',  'analyzed_text': analyzed_text}
        return render(request, 'analyze2.html', params)
        
    #character count:
    elif charcount == 'on':
        charnumber = len(text.replace(" ", ''))
        # charnumber = 0  # ANother way
        # for char in text:
        #     if char != ' ': 
        #         charnumber += 1
        params = {'purpose': 'Total Character Count',  'analyzed_text': charnumber}
        return render(request, 'analyze2.html', params)
        
    #Sentence count:
    elif sentencecount == 'on':
        sentencecount = text.count('.') + text.count('!') + text.count('?')
        params = {'purpose': 'Sentence Count',  'analyzed_text': sentencecount}
        return render(request, 'analyze2.html', params)
    
    #Paragraph count:
    elif paragraphcount == 'on':
        paragraphs = text.split('\n\n')
        paragraphcount = len(paragraphs)
        params = {'purpose': 'Paragraph Count',  'analyzed_text': paragraphcount}
        return render(request, 'analyze2.html', params)

    # Extract Keywords:
    elif keywordextraction == 'on':
        keywords = extract_keywords(text)
        params = {'purpose': 'Keyword Extraction', 'analyzed_text': keywords}
        return render(request, 'analyze2.html', params)
    
    elif ner == 'on':
        analyzed_text = ''
        doc = nlp(text)
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        analyzed_text = "\n".join([f"{entity[0]}, '{entity[1]}" for entity in entities])
        params = {'purpose': 'Named Entity Recognition', 'analyzed_text': analyzed_text}
        return render(request, 'analyze2.html', params)
        
        
        
    else:
        return HttpResponse("You have to check any of these process <br> <p> Go back to <a href='/'>Home</a> </p>")
    
def aboutme(request):
    return render(request, 'aboutme.html')

def contact(request):
    return render(request, 'contact.html')