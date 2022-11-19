def generateData(musiciens : list):
    doc_complet=""
    retourLigne ="\n"
    if(len(musiciens)==12):
        ligneMusicien ="MUSICIEN = 	{Alex,			Billie,			Chris,		Dora,		Emile,			Franck,		Gisele,		Horst, 		Iris, 		Jean,		Karl,		Lisa};"
        ligneStyle = "STYLE = 		{Rock,			Metal,			Jazz, 		Pop, 		Classique,		Funk,		RnB,		Rap, 		Punk, 		Electro};"
        ligneInstrument = "INSTRUMENT = 	{Guitare,		Batterie,		Violon,		Piano, 		Basse};"
        ligneVille = "VILLE = 		{Angers,		Nantes};"
        ligneNbHeure = "NB_HEURE = 		2..5;"
        ligneNiveau = "NIVEAU = 			1..5;"
        ligneNbHeureMin = "NB_HEURE_MIN = 	1..3;"
        ligneNbHeureMax = "NB_HEURE_MAX = 	2..6;"
        ligneNiveauMin = "NIVEAU_MIN = 		1..5;"
        ligneNiveauMax = "NIVEAU_MAX = 		2..5;"
        ligneStyleMin = "NB_STYLE_MIN = 	1..3;"
        doc_complet+=ligneMusicien+retourLigne
        doc_complet+=ligneStyle+retourLigne
        doc_complet+=ligneInstrument+retourLigne
        doc_complet+=ligneVille+retourLigne
        doc_complet+=ligneNbHeure+retourLigne
        doc_complet+=ligneNiveau+retourLigne
        doc_complet+=ligneNbHeureMin+retourLigne
        doc_complet+=ligneNbHeureMax+retourLigne
        doc_complet+=ligneNiveauMin+retourLigne
        doc_complet+=ligneNiveauMax+retourLigne
        doc_complet+=ligneStyleMin+retourLigne

        #données récupérées
        ligneNbHeureValue = "nb_heure =["
        ligneNiveauValue = "niveau =["
        ligneNbHeureMinValue = "nb_heure_min =["
        ligneNbHeureMaxValue = "nb_heure_max =["
        ligneNiveauMinValue = "niveau_min["
        ligneNiveauMaxValue = "niveau_max =["
        ligneNbStyleMinValue = "nb_style_min =["
        
        for musicien in musiciens:
            ligneNbHeureValue += str(","+musicien.heureHebdo)
            ligneNiveauValue += str(","+musicien.niveau)
            ligneNbHeureMinValue += str(","+musicien.heureMin)
            ligneNbHeureMaxValue += str(","+musicien.heureMax)
            ligneNiveauMinValue += str(","+musicien.nivMin)
            ligneNiveauMaxValue += str(","+musicien.nivMax)
            ligneNbStyleMinValue += str(","+musicien.styleMin)
            
        ligneNbHeureValue += "];"
        ligneNiveauValue += "];"
        ligneNbHeureMinValue += "];"
        ligneNbHeureMaxValue += "];"
        ligneNiveauMinValue += "];"
        ligneNiveauMaxValue += "];"
        ligneNbStyleMinValue += "];"
        
        
        ligneNbHeureValue= ligneNbHeureValue.replace(',', '', 1)
        ligneNiveauValue= ligneNiveauValue.replace(',', '', 1)
        ligneNbHeureMinValue= ligneNbHeureMinValue.replace(',', '', 1)
        ligneNbHeureMaxValue= ligneNbHeureMaxValue.replace(',', '', 1)
        ligneNiveauMinValue= ligneNiveauMinValue.replace(',', '', 1)
        ligneNiveauMaxValue= ligneNiveauMaxValue.replace(',', '', 1)
        ligneNbStyleMinValue= ligneNbStyleMinValue.replace(',', '', 1)
        
        doc_complet+=ligneNbHeureValue+retourLigne
        doc_complet+=ligneNiveauValue+retourLigne
        doc_complet+=ligneNbHeureMinValue+retourLigne
        doc_complet+=ligneNbHeureMaxValue+retourLigne
        doc_complet+=ligneNiveauMinValue+retourLigne
        doc_complet+=ligneNiveauMaxValue+retourLigne
        doc_complet+=ligneNbStyleMinValue+retourLigne
    return doc_complet

import os

def genereFichier(dataOfDoc):
    if(dataOfDoc!=""):
        file_dir = os.path.dirname(__file__)
        file_name = os.path.join(file_dir, "tmpData.dzn")
        text_file = open(file_name, "w")
        n = text_file.write(dataOfDoc)
        text_file.close()
        return True
    return False