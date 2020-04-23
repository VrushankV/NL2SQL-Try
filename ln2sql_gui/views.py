from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import ln2sqlmodule as converter
import os
import speech_recognition as sr
from ln2sqlmodule.ParsingException import ParsingException

DATA_FILE_TYPES = ['sql', 'SQL',]
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.
def index(request):
    if request.method == 'POST':
        data = request.POST.get('record')

        # get audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # print("Speak:")
            audio = r.listen(source)

        try:
            output = " " + r.recognize_google(audio)
        except sr.UnknownValueError:
            output = "Could not understand audio"
        except sr.RequestError as e:
            output = "Could not request results; {0}".format(e)
        data = output
        _str = data
        
        return render(request, 'ln2sql_gui/index.html', {'data': data})
    return render(request,'ln2sql_gui/index.html',
           {
               'error_message':'',
               'success_message':''
           })

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        _str = request.POST['message']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        # file_type = filename.url.split('.')[-1]
        # file_type = file_type.lower()
        # if file_type not in DATA_FILE_TYPES:
        #     return render(request, 'ln2sql_gui/index.html', {
        #         'error_message': 'SQL dump file must be in .SQL format',
        #         'success_message': '',
        #         'result': ''
        #     })
        filename="/database/" + str(filename)
        try:
            result = converter.getSql(_str,filename)
            return render(request, 'ln2sql_gui/index.html', {
                'error_message': '',
                'success_message': 'Successfully processed',
                'result':result
            })
        except ParsingException:
            return render(request, 'ln2sql_gui/index.html', {
                'error_message': '',
                'success_message': 'uploaded',
                'result': 'Error : No keyword is found'
            })
    return render(request, 'ln2sql_gui/index.html',
                  {
                      'error_message': '',
                      'success_message': '',
                      'result': ''
                       })
