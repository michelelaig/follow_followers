import argparse
import os
import sys
import time
from random import randint
#sys.path.append(os.path.join(sys[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")

args= parser.parse_args()

lista=os.listdir('cartella')
num=randint(0,len(lista)-1)
nome=lista[num]
foto='cartella/'+nome+'/'
lista=os.listdir('cartella/'+lista[num])

num=randint(0,len(lista)-1)
foto+=lista[num]


hashi =['#heart #ladiesnight #ladies #stunning #prilaga #instadaily #lady #womencrushwednesday #beach #girlsgeneration #sun #model #girlsday #face #tagsforlikes #life #bikini #pose #gorgeous #funny #adorable #portrait #followback #blonde #mouth',
'#awesome #lips #sweet #amazing #photooftheday #instagramers #like4like #instalike #nice #nofilter #beauty #pretty #makeup #prilaga #my #dress #photo #look #selfies #nomakeup #style #love #best #instafashion #bestoftheday #happy #eyes #selfie',
'#nofilters #cool #girl #picoftheday #beautiful #igers #girls #prilaga #me #instagood #girlswholikegirls #love #fashion #hair #smile #photooftheday #swag #girlsbestfriend #pretty #hot #follow #nofilter #girlsnight #followme #friends #cute #fun',
'#casapoundpesaro #casapoundlatina #casapoundtrento #sims4legacy #forzanuovapadova #prilaga #portraitlegacy #primagliitalianiindifficoltá #vaquejadalegal #forzanuovapuglia #primagliitaliani👍 #casapoundparma #forzanuovalombardia #primagliitalianiunca #casapoundtorino #forzanuovataranto #casapoundrieti #legalshield #primagliitalianiatestaingiù #primagliitaliani✌🏼 #legaliza #primagliitalianineicantieri #forzanuovabologna #forzanuovatorino #domingolegal',
'#legami #primagliitalianicheperononsianoidioti #forzanuovaorgoglionazionale #forzanuovavicenza #marihuanalegal #primagliitalianieranomeglio #primagliitaliani💙 #forzanuovacrotone #forzanuovabrescia #prilaga #forzanuovalaspezia #primagliitalianionesti #primagliitalianisempre #casapoundpescara #casapoundudine #primagliitaliani💚🇮🇹🍀 #forzanuovavecchiamerda #legalizabrasil #casapoundbergamo #subarulegacy #casapoundroma #leganes #casapoundmerda #casapoundmilano #lega',
'#sëduce #legalize #iostoconsalvini #governofederal #romantis #duces #legal #legado #matteosalvini #prilaga #governodegoiás #duce #governor #maiconsalvini #romania #roma #abortolegal #salvini #governodealagoas #salvinipremier #governo #introduce #legacy #governorsball #roman #educesalon #romantic #nessunotocchisalvini',
'#primagliitaliani #dalleparoleaifatti',
'#summer #beach #bikini #model #girl #booty #bodybuilding #glutes #ass #legs #sexy #body #fitness #fitnessmodel #fitnessgirl #gymlife #sun #beautiful #love',
'#summer #beach #sea #fitness #fitnessmodel #fitnessgirl #gym #sexy #hotgirl #muscle #booty #bodybuilding #glutes #ass #legs #abs #girlwholift #body #love #anticomunismo']
num=randint(0,len(hashi))
hashi=hashi[num]
args = parser.parse_args()

bot=Bot(filter_private_users=False,filter_users_without_profile_photo=False)
bot.login(username=args.u,password=args.p)
cap='seguite @'+nome+'! '+hashi



bot.upload_photo(foto, caption=cap)
print("Uploaddato ",foto)
foto=str(foto)
os.remove(foto)
os.remove(foto+'.CONVERTED.jpg.REMOVE_ME')
