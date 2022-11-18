
from optiApp.modeles.modele import resolutionContrainte 
from optiApp.modeles.musiceinsList import genMusiciens 
from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    elements = genMusiciens()
    context = {
        'elements': elements,
    }

    return render(request, 'index.html',context)
#return HttpResponse(result_str)


def afficheDuo(request):
    elements = genMusiciens()
    
    result_str=resolutionContrainte("projetDuoMusicien.mzn","projetDuoMusicien.dzn")
    context = {
        'propositionDuo': result_str,
         'elements': elements,
    }
    return render(request, 'index.html',context)