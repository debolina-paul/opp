class formulaire :
    def __init__(self, nom, prenom, naissance):
        self.nom = nom.upper()
        self.prenom = prenom.upper()
        na = str(naissance)
        if na.isnumeric():
            self.naissance = int(na)
        else:
            self.naissance = 1900
        def age(self):
            return 2020 - self.naissance
        def majeur(self):
            return self.age() >= 18
        def memefamille(self, formulaire):
            return self.nom == formulaire.nom

class data(formulaire):
     def __init__(self,nom,prenom,naissance):
         formulaire.__init__(self,nom, prenom, naissance)
     def buildID(self):        
         self.id = self.nom[:2]+self.prenom[:2]+str(self.age())
         return self.id

#version Rafik

class data(formulaire):
    def __init__(self, nom, prenom, naissance):
        formulaire.__init__(self, nom, prenom, naissance)
    def buildID(self):
        self.id = self.nom[:2]
        self.id += self.prenom[:2]
        self.id += str(self.age())
jd = data('Doe', 'Jhon', 1999)
ad = data('Doe', 'Alice', 1991)

jd.buildID()
ad.buildID()
print(jd.id)
print(ad.id)