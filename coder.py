'''
Created on Oct 4, 2016

@author: mako
'''
from random import randint, shuffle

print 'F4 Terminal Coder - test 2'

WORD_LENGTH = 10
DISTRIBUTION_WORDS_LIST = [0,0,0,1,1,1,2,2,3,4]
gues_word = ''
gues_words = []
sample_w = []
must_number = 4

#sprawdza zgodnosc slow i zwraca ilosc takich samych znakow na pozycji
def get_integrity(a,b):
    #pozycja znaku w b
    i = 0
    #ilosc zgodnych znakow
    x = 0
    if (len(a)!=len(b)):
        return 0
    for c in a:
        if c==b[i]:
            x = x + 1
        i = i + 1
    return x

#zwraca liste slow ktore na pewno zawieraja slowo z literka, list - slowa wejsciowe, secret - slowo porownywane, acc - ilosc zgodnychz  secret 
def get_integrated_word(in_list,secret,acc):
    possible = []
    for word in in_list:
        #jezeli inna niz 0 podobienstwo
        if (get_integrity(secret, word) >= acc):
            possible.append(word)
    return possible

#usuwa z listy slowa ktore wogole nie pasuja - porownanie wyszlo 0 wczesniej
def rem_not_integr_words(in_list,not_int_word):
    #slowa do zwrotu - te co nie maja byc usuniete
    out_list = []
    #jesli slowo zawiera jakas literke tzn ze nie bedzie jej w possible
    for word in in_list:
        if (get_integrity(not_int_word, word)==0):
            out_list.append(word)
    return out_list  

#losuje slowa podobne do sekretnego wg podanego rozkladu i slowo sekretne z podanej listy, slowo sekretne jest zawsze pierwsze !!!!!
def get_integreted_random_list(distribution_list, words_list):
    #id slow wylosowanych
    idxlist = []

    #losowanie slowa - na podst. tego slowa beda losowane pozostale
    idxlist.append(randint(0,len(words_list)-1)) 

    #licznik petli zabezp infinite loop whilea
    i = 0
    for d in distribution_list:
        if d > WORD_LENGTH:
            break
        while True:
            rid = randint(0,len(words_list)-1)
            #zabezpieczenie przed nieskonczona petla, zmniejszam wymagania co do slowa
            i = i + 1
            if i > len(words_list)*5:
                d = d - 1
                i = 0
                if d < 0: # jesli jzu nie mzoe znalesc to raczej nei ma takiego slowa to koniec
                    break
                
            #print rid,get_integrity(words_list[idxlist[0]],words_list[rid])
            #jezeli slowa nie ma an liscie i wylosowane jest podobne w danym stopniu to dodaj go do listy
            if (rid not in idxlist and get_integrity(words_list[idxlist[0]],words_list[rid])==d):
                i = 0
                idxlist.append(rid)
                break
            
    out_list = []
    for i in idxlist:
        out_list.append(words_list[i])
    return out_list



fh = open('allwords.txt')
for l in fh:
    line = l.strip()
    if (len(line)==WORD_LENGTH and '\'' not in line and ',' not in line and '.' not in line ):
        sample_w.append(line.title()) # 1st ucase

#lista slow podobnych do wylosowanego wg listy dystrybucji
words = get_integreted_random_list(DISTRIBUTION_WORDS_LIST, sample_w)
#print len(words)
secretword = words[0]

shuffle(words)

iter = must_number
#wlasciwe dzialanie algorytmu
while (get_integrity(secretword, gues_word)!=len(secretword) and iter>0):
    #print 'secret ',secretword
    for gw in gues_words:
        print gw,': ',get_integrity(secretword, gw) 
    print 'zostalo prob:',iter
    #print 'wybierz slowo'
    
    for x in range(0,len(words)):
        print x+1,words[x]
    
    word_number = raw_input('wybierz slowo ')
    gues_word = words[int(word_number)-1]
    gues_words.append(gues_word)
    integrity = get_integrity(secretword, gues_word) 
    print gues_word,': ',integrity
    
    
    
    #A TUTAJ DZIALANIE POMOCY usuwam slowo wybrane
    words.pop(int(word_number)-1)
    #jesli slowo mialo 0 integralnosc to od razu usun slowa niepasujace
    if (integrity==0):
        words = rem_not_integr_words(words, gues_word)
    else:    
        #zmniejszam ilosc prawdopodobnych slow
        words = get_integrated_word(words, gues_word, integrity)
    
    
      
    
    if (integrity == len(secretword)):
        print '-----zgadles slowo-----'
        break
    iter = iter - 1
    
    if(iter == 0 ):
        print '-----nie udalo ci sie odgadnac slowa------'
    
    
    print

    
