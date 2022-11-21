def generateData(musiciens : list):
    doc_complet=""
    retourLigne ="\n"
    if(len(musiciens)==12):
        ligneMusicien ="MUSICIEN = 	{Alex,			Billie,			Chris,		Dora,		Emile,			Franck,		Gisele,		Horst, 		Iris, 		Jean,		Karl,		Lisa};"
        ligneStyle = "STYLE = 		{Rock,			Metal,			Jazz, 		Pop, 		Classique,		Funk,		RnB,		Rap, 		Punk, 		Electro};"
        ligneInstrument = "INSTRUMENT = 	{Guitare,		Batterie,		Violon,		Piano, 		Basse};"
        ligneVille = "VILLE = 		{Angers,		Nantes};"
        ligneNbHeure = "NB_HEURE = 		1..10;"
        ligneNiveau = "NIVEAU = 			1..10;"
        ligneNbHeureMin = "NB_HEURE_MIN = 	1..10;"
        ligneNbHeureMax = "NB_HEURE_MAX = 	1..10;"
        ligneNiveauMin = "NIVEAU_MIN = 		1..10;"
        ligneNiveauMax = "NIVEAU_MAX = 		1..10;"
        ligneStyleMin = "NB_STYLE_MIN = 	1..10;"
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
        ligneNiveauMinValue = "niveau_min=["
        ligneNiveauMaxValue = "niveau_max =["
        ligneNbStyleMinValue = "nb_style_min =["
        ligneVille = "ville = ["
        ligneInstrument = "instrument = ["
        ligneStyle = "style = [ "
        for musicien in musiciens:
            ligneNbHeureValue += ","+str(musicien.heureHebdo)
            ligneNiveauValue += ","+str(musicien.niveau)
            ligneNbHeureMinValue += ","+str(musicien.heureMin)
            ligneNbHeureMaxValue += ","+str(musicien.heureMax)
            ligneNiveauMinValue += ","+str(musicien.nivMin)
            ligneNiveauMaxValue += ","+str(musicien.nivMax)
            ligneNbStyleMinValue += ","+str(musicien.styleMin)
            ligneVille += ","+str(musicien.ville)
            ligneInstrument += ","+str(musicien.instru)
            ligneStyle += ",{"+str(musicien.style)+"}"
            
            
        ligneNbHeureValue += "];"
        ligneNiveauValue += "];"
        ligneNbHeureMinValue += "];"
        ligneNbHeureMaxValue += "];"
        ligneNiveauMinValue += "];"
        ligneNiveauMaxValue += "];"
        ligneNbStyleMinValue += "];"
        ligneVille += "];"
        ligneInstrument += "];"
        ligneStyle += "];"
        
        
        ligneNbHeureValue= ligneNbHeureValue.replace(',', '', 1)
        ligneNiveauValue= ligneNiveauValue.replace(',', '', 1)
        ligneNbHeureMinValue= ligneNbHeureMinValue.replace(',', '', 1)
        ligneNbHeureMaxValue= ligneNbHeureMaxValue.replace(',', '', 1)
        ligneNiveauMinValue= ligneNiveauMinValue.replace(',', '', 1)
        ligneNiveauMaxValue= ligneNiveauMaxValue.replace(',', '', 1)
        ligneNbStyleMinValue= ligneNbStyleMinValue.replace(',', '', 1)
        ligneVille= ligneVille.replace(',', '', 1)
        ligneInstrument= ligneInstrument.replace(',', '', 1)
        ligneStyle= ligneStyle.replace(',', '', 1)
        
        doc_complet+=ligneNbHeureValue+retourLigne
        doc_complet+=ligneNiveauValue+retourLigne
        doc_complet+=ligneNbHeureMinValue+retourLigne
        doc_complet+=ligneNbHeureMaxValue+retourLigne
        doc_complet+=ligneNiveauMinValue+retourLigne
        doc_complet+=ligneNiveauMaxValue+retourLigne
        doc_complet+=ligneNbStyleMinValue+retourLigne
        doc_complet+=ligneVille+retourLigne
        doc_complet+=ligneInstrument+retourLigne
        doc_complet+=ligneStyle+retourLigne
    return doc_complet

def generateTrio(contrainteHeure,contrainteNiveau):
    doc_complet =""
    ligneInlcude ="include \"globals.mzn\";\n\n\n"
    ligneEnum ="enum MUSICIEN;\nenum STYLE;\nenum INSTRUMENT;\nenum VILLE;"
    ligneEnsembles="set of int : NB_HEURE;\nset of int : NIVEAU;\nset of int : NB_HEURE_MIN;\nset of int : NB_HEURE_MAX;\nset of int : NIVEAU_MIN;\nset of int : NIVEAU_MAX;\nset of int : NB_STYLE_MIN;"
    ligneTableau = "array[MUSICIEN] of var MUSICIEN : trio1;\narray[MUSICIEN] of var MUSICIEN : trio2;\narray[MUSICIEN] of var NB_HEURE : nb_heure;\narray[MUSICIEN] of var NIVEAU : niveau;\narray[MUSICIEN] of var NB_HEURE_MIN : nb_heure_min ;\narray[MUSICIEN] of var NB_HEURE_MAX : nb_heure_max;\narray[MUSICIEN] of var NIVEAU_MIN : niveau_min;\narray[MUSICIEN] of var NIVEAU_MAX : niveau_max;\narray[MUSICIEN] of var NB_STYLE_MIN : nb_style_min;\narray[MUSICIEN] of var INSTRUMENT : instrument ;\narray[MUSICIEN] of var VILLE : ville ;\narray[MUSICIEN] of set of STYLE : style ;\n\n"
    ligneContraintedifferenceMembreTrio = "/*les trios doivent être differents*/\nconstraint forall(m in MUSICIEN) (m != trio1[m] /\ m != trio2[m] /\ trio1[m] != trio2[m]);\n"
    ligneContrainteVille = "/*Les trios habitent la même ville*/\nconstraint forall(m in MUSICIEN) (ville[m] == ville[trio1[m]] /\ ville[m] == ville[trio2[m]]);\n"
    if contrainteHeure:
        ligneContrainteHeure ="/*le nombre d’heures voulues doit être dans le créneau Min - Max souhaité par l’autre*/\nconstraint forall(m in MUSICIEN)(nb_heure[m] in nb_heure_min[trio1[m]]..nb_heure_max[trio1[m]] /\ nb_heure[m] in nb_heure_min[trio2[m]]..nb_heure_max[trio2[m]]);\nconstraint forall(m in MUSICIEN)(nb_heure[trio1[m]] in nb_heure_min[m]..nb_heure_max[m] /\ nb_heure[trio1[m]] in nb_heure_min[trio2[m]]..nb_heure_max[trio2[m]]);\nconstraint forall(m in MUSICIEN)(nb_heure[trio2[m]] in nb_heure_min[m]..nb_heure_max[m] /\ nb_heure[trio2[m]] in nb_heure_min[trio1[m]]..nb_heure_max[trio1[m]]);\n\n"
    lignestyleCommun ="/*le nombre de style commun doit respecter les exigences de chacun*/\nconstraint forall(m in MUSICIEN)(card(style[m] intersect style[trio1[m]]) >= 1);\nconstraint forall(m in MUSICIEN)(card(style[m] intersect style[trio2[m]]) >= 1);\nconstraint forall(m in MUSICIEN)(card(style[trio1[m]] intersect style[trio2[m]]) >= 1);\n\n"
    ligneInstrument = "/*deux musiciens jouant du même instrument ne peuvent former un trio*/\nconstraint forall(m in MUSICIEN)(instrument[m] != instrument[trio1[m]] /\ instrument[m] != instrument[trio2[m]] /\ instrument[trio1[m]] != instrument[trio2[m]]);\n\n";
    ligneConsistante = "/*le trio est consistant : il s’agit donc d’un matching parfait, c’est à dire que si m est associé à m’ alors m’ est associé aussi à m*/\nconstraint forall(m, n, o in MUSICIEN where (n == trio1[m] /\ o == trio2[m]) \/ (n == trio2[m] /\ o == trio1[m])) ((m == trio1[n] \/ m == trio2[n]) /\ (m == trio2[o] \/ m == trio1[o]));\n\n"
    ligneAlldiff ="/*Les musiciens doivent être différents de leur duos*/\nconstraint all_different(trio1);\nconstraint all_different(trio2);\n\n"
    ligneSolve ="solve satisfy;\n\n"
    ligneOutput="output[\n          \"{ \(p) | \(trio1[p])  | \(trio2[p]) }\\n \" | p in MUSICIEN];\n\n"

    doc_complet+=ligneInlcude
    doc_complet+=ligneEnum
    doc_complet+=ligneEnsembles
    doc_complet+=ligneTableau
    doc_complet+=ligneContraintedifferenceMembreTrio
    doc_complet+=ligneContrainteVille
    if contrainteHeure:
        doc_complet+=ligneContrainteHeure
    doc_complet+=lignestyleCommun
    doc_complet+=ligneInstrument
    doc_complet+=ligneConsistante
    doc_complet+=ligneAlldiff
    doc_complet+=ligneSolve
    doc_complet+=ligneOutput
    return doc_complet

    
import os

def genereFichier(dataOfDoc,fileName):
    if(dataOfDoc!=""):
        file_dir = os.path.dirname(__file__)
        file_name = os.path.join(file_dir, fileName)
        text_file = open(file_name, "w")
        n = text_file.write(dataOfDoc)
        text_file.close()
        return True
    return False