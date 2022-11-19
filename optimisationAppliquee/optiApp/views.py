
from optiApp.modeles.modele import resolutionContrainte 
from optiApp.modeles.musiceinsList import genMusiciens,modifiyMusicienData
from django.shortcuts import render
#from django.http import HttpResponse
from optiApp.modeles.musicien import * 
from optiApp.modeles.generateData import *
# Create your views here.
def index(request):
    musiciens = genMusiciens()
    context = {
        'musiciens': musiciens,
    }

    return render(request, 'index.html',context)
#return HttpResponse(result_str)


def afficheDuo(request):
    print(request.POST.get('Alex-heureHebdo'))
    musiciens = genMusiciens()
    #print("avant",musiciens[0].get_heureHebdo())
    musiciens = modifiyMusicienData(musiciens,request.POST)
    #print("après",musiciens[0].get_heureHebdo())
    result_str=""
    fichierPret =genereFichier(generateData(musiciens))
    if(fichierPret):
        result_str=resolutionContrainte("projetDuoMusicien.mzn","projetDuoMusicien.dzn")
    context = {
        'propositionDuo': result_str,
         'musiciens': musiciens,
    }
    return render(request, 'index.html',context)