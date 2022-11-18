
from optiApp.modeles.modele import resolutionContrainte 
from optiApp.modeles.musiceinsList import genMusiciens 
from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    musiciens = genMusiciens()
    context = {
        'musiciens': musiciens,
    }

    return render(request, 'index.html',context)
#return HttpResponse(result_str)


def afficheDuo(request):
    musiciens = genMusiciens()
    
    result_str=resolutionContrainte("projetDuoMusicien.mzn","projetDuoMusicien.dzn")
    context = {
        'propositionDuo': result_str,
         'musiciens': musiciens,
    }
    return render(request, 'index.html',context)