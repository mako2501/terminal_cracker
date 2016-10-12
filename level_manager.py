'''
modol zawierajacy klase managera poziomu trudnosci - warunki gry - a scislej konkretnej rundy
by mako

1. ustawia zmienne gry w zaleznosci od poziomu trudnosci [PT]
2. listy dystrybucyjne rozne w zaleznosci od [PT]
3. dlugosc slow w zaleznosci od poziomu trudnosci
4. ilosc slow zalezna od [PT], scisly zwiazek z listami dystrybucyjnymi
5. listy dystrybucyjne powinny sie zmieniac takze od rundy - im dalej tym trudniej, ctz. trudniej?
6. ilosc prob zalezna od rundy
7. dobrze by bylo to jakos serializowac
8.

9. level - 1 - 4
dlugosc slow zalezna od poziomu 1 - 4, 2 - 6, 3 - 8, 4 - 10 - => 2 + lvl*2

lista dystrybucyjna - 
[1,1,1,1,1,1,1,1,dl-slowa - 2,dlslowa - 1]

'''




class Level_Manager:
    
    
    def __init__(self, actual_level):
        self.actual_level = actual_level
    
    def get_dist_list(self, rnd):
        x = self.actual_level * 2
        #lista startowa
        distrib_list =[x,x,x-self.actual_level,x-self.actual_level,x-self.actual_level,x-self.actual_level,x-self.actual_level,1,0]
        print distrib_list















