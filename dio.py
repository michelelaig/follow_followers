from instabot import Bot
from tqdm import tqdm
import argparse
import time
import os
import sys
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u',type=str,help='username')
parser.add_argument('-p',type=str, help='password')
args=parser.parse_args()


def seguirefoll(dichi):
    bot.follow_followers(dichi)

def seguirelike():
    link=input('link\n')
    ii=bot.get_media_id_from_link(link)
    l=bot.get_media_likers(ii)
    bot.follow_users(l)

def commanliek():
    users_list=[]
    ciao=input('profilo di cui prendere la gente: ')    
    medias_list = bot.get_user_medias(ciao)
    for media in medias_list:
        comments = bot.get_media_comments_all(media)
        for comment in comments:
            users_list.append(comment['user']['pk'])
    print(users_list)
    for username in tqdm(users_list):
        bot.like_user(username, amount=3, filtration=True)
        bot.follow(username)
        time.sleep(10 + 20 * random.random())


start=input('what to do\n 1:follow followers \n 2:follow likers of a post \n 3: like, follow commenters of a user\n')
user=args.u
passs=args.p
bot=Bot(filter_private_users=False,
                 filter_users_without_profile_photo=True,
                 filter_previously_followed=False,
                 filter_business_accounts=False,
                 filter_verified_accounts=True)
bot.login(username=args.u, password = args.p)
if start=='1':
    dichi=input('di chi:   ')
    seguirefoll(dichi)
elif start=='2':
    seguirelike()
elif start=='3':
    commanliek()
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





































start=input('what to do\t 1:follow followers \n 2:follow likers of a post \n')
user=input('user\n')
passs=input('password\n')

if start=='1':
    prof = inizializzazione('profili.txt')   
    seguire(prof,user,passs)
elif start=='2':
    seguirelike(user,passs)
chiusura(prof)
