from instabot import Bot

def  inizializzazione(file):
    f=open(file,'r',encoding='utf-8')
    profili={}
    bot=Bot()
    bot.max_following_to_followers_ratio = 80
    for r in f:
        ls=''
        r=r.strip().split(',,,')
        profili[r[0]]='ciao'
        nomeid=r[1]
        lista=r[2].strip().split()
        for el in lista:
            el=el[1:-2]
            ls+=el+' '
        ls=ls.split()
        profili[r[0]]=[nomeid,ls]
    print('in memory:')
    for i in profili:
        print(i) 
    return profili

def seguire(nome,numero,prof):
    
    bot = Bot()
    bot.login(username='',password='')
    if nome not in prof:
        nome_id=bot.get_user_id_from_username(nome)
        seguitori = bot.get_user_followers(nome_id)
        prof[nome]=[nome_id, seguitori]
    else:
        nome_id= prof[nome][0]
        seguitori=prof[nome][1]
    
    ind=0
    l=[]
    if numero<len(seguitori):
        while ind<=numero:
            l.append(seguitori[ind])
            ind+=1
        print('numero<len')
    else:
        l=seguitori
        
    for u in l:
        print('still',ind,'now',u)
        bot.follow(u)
        ind-=1



def chiusura(prof):
    f=open('profili.txt','w',encoding='utf-8')
    print('closing',prof)
    for i in prof:
        ids=''
        for el in prof[i][1]:
            ids+=" '"+el+"'"+','
        s=i+',,,'+prof[i][0]+',,,'+"'"+ids+'\n'
        f.write(s)
    f.close()







































numero=int(input('how many?\n'))
nome=input('whom?\n')
prof = inizializzazione('profili.txt')
seguire(nome,numero,prof)
chiusura(prof)
