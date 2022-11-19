from optiApp.modeles.musicien import Musicien 


def genMusiciens() :
    elements =[]
    elements.append( Musicien('Alex',3,2,'Guitare','Angers','Rock, Metal,Jazz',2,4,1,4,2))
    elements.append( Musicien('Billie',3,1,'Batterie','Nantes','Jazz,Pop,Classique,Rock, Funk',1,5,1,2,3))
    elements.append( Musicien('Chris',2,5,'Guitare','Angers','RnB, Rap,Classique',1,2,3,5,1))
    elements.append( Musicien('Dora',3,2,'Batterie','Nantes','Pop, Punk, Electro',1,4,1,5,1))
    elements.append( Musicien('Emilie',5,2,'Violon','Angers','Classique, Metal, Jazz',3,6,1,3,2))
    elements.append( Musicien('Franck',3,3,'Guitare','Angers','Punk, Rock, Classique,Jazz',1,5,1,3,2))
    elements.append( Musicien('Gisèle',3,5,'Piano','Nantes','Pop, Rock, Jazz,Classique',1,5,1,5,1))
    elements.append( Musicien('Horst',3,5,'Violon','Nantes','Classique',3,3,5,5,1))
    elements.append( Musicien('Iris',2,5,'Piano','Angers','Classique, Jazz',2,3,4,5,1))
    elements.append( Musicien('Jean',2,2,'Piano','Nantes','Jazz, Electro',1,5,1,3,1))
    elements.append( Musicien('Karl',3,2,'Basse','Nantes','Jazz, Rap, Funk, Rock',3,5,1,3,2))
    elements.append( Musicien('Lisa',3,4,'Basse','Angers','Metal, Pop, Electro, Jazz',3,6,2,5,1))
    return elements

def modifiyMusicienData(elements :list,post):
    if len(elements)>0:
        for element in elements:
            if (post.get(element.get_name()+"-heureHebdo") is not None):
               element.set_heureHebdo(post.get(element.get_name()+"-heureHebdo"))
               
            if (post.get(element.get_name()+"-niveau") is not None):
               element.set_niveau(post.get(element.get_name()+"-niveau"))
               
            if (post.get(element.get_name()+"-ville") is not None):
               element.set_ville(post.get(element.get_name()+"-ville"))
               
            if (post.get(element.get_name()+"-instru") is not None):
               element.set_instru(post.get(element.get_name()+"-instru"))
            
            if (post.get(element.get_name()+"-heureMin") is not None):
               element.set_heureMin(post.get(element.get_name()+"-heureMin"))
            
            if (post.get(element.get_name()+"-heureMax") is not None):
               element.set_heureMax(post.get(element.get_name()+"-heureMax"))
            
            if (post.get(element.get_name()+"-nivMin") is not None):
               element.set_nivMin(post.get(element.get_name()+"-nivMin"))
               
            if (post.get(element.get_name()+"-nivMax") is not None):
               element.set_nivMax(post.get(element.get_name()+"-nivMax"))
               
            if (post.get(element.get_name()+"-styleMin") is not None):
               element.set_styleMin(post.get(element.get_name()+"-styleMin"))
             
    return elements