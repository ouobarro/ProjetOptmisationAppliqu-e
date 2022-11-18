

class Musicien :
    def __init__(self, name,heureHebdo,niveau,instru,ville,style,heureMin,heureMax,nivMin,nivMax,styleMin): 
        self.name = name 
        self.heureHebdo = heureHebdo
        self.niveau = niveau
        self.instru = instru
        self.ville = ville
        self.style = style
        self.heureMin = heureMin
        self.heureMax = heureMax
        self.nivMin = nivMin
        self.nivMax = nivMax
        self.styleMin = styleMin

    def get_name(self):
        return self._name

    def set_name(self, name):
        self.name=name
    
    def get_heureHebdo(self):
        return self._heureHebdo

    def set_heureHebdo(self, heureHebdo):
        self.heureHebdo=heureHebdo
    
    def get_niveau(self):
        return self._niveau

    def set_niveau(self, niveau):
        self.niveau=niveau
        
    def get_instru(self):
        return self._instru

    def set_instru(self, instru):
        self.instru=instru
    
    def get_ville(self):
        return self._ville

    def set_ville(self, ville):
        self.ville=ville
        
    def get_style(self):
        return self._style

    def set_style(self, style):
        self.style=style
    
    def get_heureMin(self):
        return self._heureMin

    def set_heureMin(self, heureMin):
        self.heureMin=heureMin
    
    def get_heureMax(self):
        return self._heureMax

    def set_heureMax(self, heureMax):
        self.heureMax=heureMax
    
    def get_nivMin(self):
        return self._nivMin

    def set_nivMin(self, nivMin):
        self.nivMin=nivMin
        
    def get_nivMax(self):
        return self._nivMax

    def set_nivMax(self, nivMax):
        self.nivMax=nivMax
    
    def get_styleMin(self):
        return self._styleMin

    def set_styleMin(self, styleMin):
        self.styleMin=styleMin
        
