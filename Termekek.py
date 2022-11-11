
class Termek():
    
    def __init__(self,azon, nev, ar, db, be):
        self.Id = azon;
        self.Nev = nev;
        self.Ar = ar;
        self.Db = db;
        self.Beszerzes = be
        
    def __str__(self):
        return "Id: "+ self.Id +"\nTermék: " + self.Nev + "\nÁra: " + str(self.Ar) + "\nDb: " + str(self.Db) +  "\nBeszerzes ideje: " + self.Beszerzes;
                

def Beolvasas()->[]:
    lista = [];
    with open("termek.csv", "r", encoding= "utf-8") as file:
        for sor in file:
            print(sor);
    
    return lista;
    

def Feladat():
    Beolvasas();

    
Feladat();