from django.http import HttpResponse
from django.shortcuts import render
import os
import json

def hello(request):
    return HttpResponse("Hello World!")

def upload(request):
    if request.method == 'POST':
        ret = {'status': False, 'data': None, 'error': None}
        try:
            user = request.POST.get('user')
            img = request.FILES.get('img')
            f = open(os.path.join('F:\\static\\', user), 'wb')
            for chunk in img.chunks(chunk_size=1024):
                f.write(chunk)
            ret['status'] = True
            ret['data'] = os.path.join('static', user)
        except Exception as e:
            ret['error'] = e
        finally:
            #f.close()
            return HttpResponse(json.dumps(ret))
    return render(request, 'upload.html')