class Cellule:
    def __init__(self,v,s):
        self.valeur=v
        self.suivante=s

class Pile:
    def __init__(self):
        self._contenu=None

    def est_vide(self):
        return self._contenu is None
    
    def empiler(self, e):
        self._contenu=Cellule(e,self._contenu)

    def depiler(self):
        if self.est_vide():
            raise IndexError("depile une pile vide")
        v=self._contenu.valeur
        self._contenu=self._contenu.suivante
        return v
    
def cree_pile():
    return Pile()


def bien_parenthesee(a): #return booleen
    p=Pile()
    for chara in a:
        if chara =="("or chara =="[": 
            p.empiler(chara)
        elif chara == ")":
            f = p.depiler()
            if f!= "(":
                return False
        elif chara =="]":
            f=p.depiler()
            if f!="[":
              return False
    return True

        