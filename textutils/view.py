#this filei have created
#print("vikas")
from django.http import HttpResponse
from django.shortcuts import render
# def about(request):
#     return HttpResponse("hello vikas chaurasia about page")
# def file1(request):
#     with open('vikas.txt') as f:
#         return HttpResponse(f.read())
# def file(request):
#     return HttpResponse('''<h1>this is home page</h1> <a href="https://www.w3schools.com/tags/tag_a.asp">anchor tag</a>''')
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print("removepunc")
    print(djtext)
    #analyzed=djtext
    if removepunc=="on":
        punct = '''!()-[]{};:'",<>./?@#$%^&*_-'''
        analyzed = ""
        for char in djtext:
            if char not in punct:
                analyzed = analyzed + char
        params = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        # return HttpResponse("rmove punc")
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Errror")