
from optiApp.modeles.modele import resolutionContrainte 
from optiApp.modeles.musiceinsList import genMusiciens,modifiyMusicienData
from django.shortcuts import render
#from django.http import HttpResponse
from optiApp.modeles.musicien import * 
from optiApp.modeles.generateData import *
# Create your views here.
def index(request):
    #musiciens = genMusiciens()
    #context = {
     #   'musiciens': musiciens,
    #}

    return render(request, 'index.html')
#return HttpResponse(result_str)

def resolve(request):
    musiciens = genMusiciens()
    context = {
        'musiciens': musiciens,
    }

    return render(request, 'resolve.html',context)

def afficheSolution(request):

    musiciens = genMusiciens()
    #print("avant",musiciens[0].get_heureHebdo())
    musiciens = modifiyMusicienData(musiciens,request.POST)
    #print("après",musiciens[0].get_heureHebdo())
    
    result_str=""
    context ={}
    niveauChecked=False
    heureChecked = False

    fichierPret =genereFichier(generateData(musiciens),"tmpData.dzn")
    if(fichierPret and request.POST.get('duo') is not None):
        result_str=resolutionContrainte("projetDuoMusicien.mzn","tmpData.dzn")
        context = {
            'propositionDuo': result_str,
            'musiciens': musiciens,
        }
    elif fichierPret and request.POST.get('trio') is not None:
        if(request.POST.get('contrainteHeure') is not None):
            heureChecked=True
        if(request.POST.get('contrainteNiveau') is not None):
            niveauChecked=True
            
        fichierPret =genereFichier(generateTrio(heureChecked,niveauChecked),"tmpContrainte.mzn")
        result_str=resolutionContrainte("tmpContrainte.mzn","tmpData.dzn")
        context = {
            'propositionTrio': result_str,
            'musiciens': musiciens,
        }
    return render(request, 'resolve.html',context)


def contact(request):
    return render(request, 'contact.html')