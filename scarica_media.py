import argparse
import os
import sys
import time
#sys.path.append(os.path.join(sys[0], '../'))
from instabot import Bot
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-a',type=str,help="account")

args = parser.parse_args()

bot=Bot(filter_private_users=False,filter_users_without_profile_photo=False)
bot.login(username=args.u,password=args.p)
bot.min_likes_to_like=0
account_id = bot.get_user_id_from_username(args.a)
lista = bot.get_user_medias(account_id, filtration = False)
corrente=os.getcwd()
current=corrente+'/cartella'
os.chdir(current)

bot.download_photos(lista, args.a)
os.chdir(corrente)
