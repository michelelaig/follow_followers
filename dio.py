from instabot import Bot

def  inizializzazione(file):
    f=open(file,'r',encoding='utf-8')
    profili={}
    bot=Bot()
    bot.max_following_to_followers_ratio = 80
    #bot.filter_users= False
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

def seguire(prof,user,passs):
    numero=input('how many?')
    nome=input('whom?')
    bot = Bot()
    bot.login(username=user,password=passs)
    if nome not in prof:
        nome_id=bot.get_user_id_from_username(nome)
        seguitori = bot.get_user_followers(nome_id)
        prof[nome]=[nome_id, seguitori]
    else:
        nome_id= prof[nome][0]
        seguitori=prof[nome][1]
    
    ind=0
    l=[]
    if numero<len(seguitori) and numero !=0:
        while ind<=numero:
            l.append(seguitori[ind])
            ind+=1
        print('numero<len')
    else:
        l=seguitori
        print('tocca seguire:',len(l),'persone')

        
    '''for u in l:
        print('still',ind,'now',u)
        bot.follow(u)
        ind-=1'''
    bot.follow_users(l)

def seguirelike(user,passs):
    link=input('link')
    bot=Bot()
    bot.login(username=user,password=passs)
    ii=bot.get_media_id_from_link(link)
    l=bot.get_media_likers(ii)
    bot.follow_users(l)

def chiusura(prof):
    f=open('profili.txt','w',encoding='utf-8')
    #print('closing',prof)
    for i in prof:
        ids=''
        for el in prof[i][1]:
            ids+=" '"+el+"'"+','
        s=i+',,,'+prof[i][0]+',,,'+"'"+ids+'\n'
        f.write(s)
    f.close()





































start=input('che famo\n 1:seguireseguitori, 2:seguirelikatori')
user=input('user\n')
passs=input('password\n')

if start=='1':
    prof = inizializzazione('profili.txt')   
    seguire(prof,user,passs)
elif start=='2':
    seguirelike(user,passs)
chiusura(prof)
