import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import subprocess
import copy

direct = os.listdir('tweet/')
lmois = []
direct.sort() #trie solon date 

#lecture CSV*************************************
for d in direct : 

    with open('tweet/{}'.format(d), newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    lmois.append(data)

#recupere la date de debut de donnees
m =[]
for i in direct :
    v = i.split('_')
    m.append(v[4][4:6])

print("nombre de mois pris en compte : ", len(lmois), ", couvrant la periode du", direct[0].split('_')[4], "au", direct[-1].split('_')[4] )

#def liste utiles******************************
ldateTW = []

lTw = []

l_impr = []
l_engag = [] 
l_rt = []
l_eng_prct = []
l_like = []
l_clic_prof = []
chastag =[]
media=[]

impr_moy_mois = []
engag_moy_mois = []
l_eng_prct_mois = []
like_moy_mois = []
rt_moy_mois = []

total_tw = 0


#parcours tout les mois***************************
for mois in lmois :
    nbligne = len(mois)
    nbtw = nbligne - 1
    ldateTW.append(total_tw)
    total_tw += nbtw
    engag = []
    engag_prct = []
    impr = []
    like = []
    rt = []

    for tweet in reversed(mois[1:]) : 
        lTw.append(tweet[2])
        l_impr.append(float(tweet[4]))
        impr.append(float(tweet[4]))
        l_engag.append(float(tweet[5]))
        engag.append(float(tweet[5]))
        l_rt.append(float(tweet[7]))
        rt.append(float(tweet[7]))
        l_eng_prct.append(float(tweet[6]))
        engag_prct.append(float(tweet[6]))
        l_like.append(float(tweet[9]))
        like.append(float(tweet[9]))
        l_clic_prof.append(float(tweet[10]))

        chastag.append(float(tweet[12]))
        media.append(float(tweet[20])) #vue media

        

    impr_moy_mois.append(np.median(np.array(impr)))
    engag_moy_mois.append(np.median(np.array(engag)))
    l_eng_prct_mois.append(np.mean(np.array(engag_prct)*100))
    rt_moy_mois.append(np.median(np.array(rt)))
    like_moy_mois.append(np.median(np.array(like)))

print("total des tweet pris en compte : ", total_tw)
print()

#transformatieon en array pour utiliser np******************************

l_impr = np.array(l_impr)
l_engag= np.array(l_engag)
l_rt = np.array(l_rt)
l_eng_prct = np.array(l_eng_prct)*100
l_like = np.array(l_like)

clic_prof = np.array(l_clic_prof)
media = np.array(media)
chastag = np.array(chastag)

#print des indicateur*******************************
#print("vue total : ", np.sum(l_impr), " ; engagement total : ", np.sum(l_engag)," ; ratio : ",np.sum(l_engag)/np.sum(l_impr) )

impr_mean = np.mean(l_impr)
impr_med = np.median(l_impr)
print("Nombre d'impression : moyenne :", impr_mean, "; médiane :", impr_med)

engag_mean = np.mean(l_engag)
engag_med= np.median(l_engag)
print("Nombre d'engagment : moyenne :", engag_mean, " ; médiane :", engag_med)

engag_prct_mean = np.mean(l_eng_prct)
engag_prct_med = np.median(l_eng_prct)
print("taux d'engagment (prct) : moyenne :", engag_prct_mean, " ; médiane :", engag_prct_med)

rt_mean = np.mean(l_rt)
rt_med= np.median(l_rt)
print("Nombre de retweet : moyenne :", rt_mean, " ; médiane :", rt_med)

like_mean = np.mean(l_like)
like_med= np.median(l_like)
print("Nombre de like : moyenne :", like_mean, " ; médiane :", like_med)

print("Nombre de clic profil : moyenne :", np.mean(clic_prof), " ; médiane :", np.median(clic_prof))

print("\nsuppose que media vue au moins une fois", "\nvue media moyen : ", media[media!=0].mean())

print("\nsuppose que hastag cliqué au moins une fois", "\nclic hastag moyen : ", chastag[chastag!=0].mean())


#******************************************
x = np.arange(len(lTw)) # pr fct tweet

x2 = np.arange(len(impr_moy_mois)) #pr fct mois



#****************************************************
plt.figure(figsize=(15,15))
plt.subplot(121)
plt.plot(x,l_impr, label="impression")
plt.plot(x,l_engag, label="engagement")
plt.xticks(ldateTW, m)
plt.legend()
plt.title("impression / engagement en fonction du tweet")

plt.subplot(122)
plt.plot(x,l_like, label="like")
plt.plot(x,l_rt, label="RT")
plt.title("like / RT en fonction du tweet")
plt.legend()
plt.xticks(ldateTW, m)

plt.show()

#********************************************************
plt.figure(figsize=(15,15))
plt.subplot(121)
plt.plot(x2, impr_moy_mois, label = "impression median")
plt.plot(x2, engag_moy_mois, label = "engagement median")
#plt.title("impression / engagement median en fonction du mois")
plt.xlabel("mois")
plt.ylabel("vue")
plt.legend()
plt.xticks(x2, m)

plt.subplot(222)
plt.plot(x2, engag_moy_mois, label = "engagement median")
plt.plot(x2, like_moy_mois, label = "like median")
plt.plot(x2, rt_moy_mois, label = "rt median")
plt.xlabel("mois")
plt.ylabel("vue")
#plt.title("like / rt median en fonction du mois")
plt.legend()
plt.xticks(x2, m)

plt.subplot(224)
plt.plot(x2, l_eng_prct_mois, label = " taux engagement moyen")
plt.xticks(x2, m)
plt.xlabel("mois")
plt.ylabel("taux (%)")
plt.legend()
#plt.title("taux d'engagement en fonction du mois")

plt.show()

#*****************************************************************
plt.plot(l_impr, l_engag, 'd')
plt.title("engagement en fonction de l'impression")
plt.show()


#****************************
plt.figure(figsize=(15,15))
plt.subplot(121)
plt.hist(l_impr, bins = 15, density=False, log=True)
plt.title("impression")

plt.subplot(122)
plt.hist(l_engag, bins = 15, density=False, log=True)
plt.title("engagement")

plt.show()

#*************************
plt.plot(l_like, l_engag, 'd', label ='like')
plt.plot(l_rt, l_engag, "x",label = 'rt')
plt.legend()
plt.show()

#********************************************
# attention, modifie les liste. Ne plus leur faire confiance après
impr=list(clic_prof/l_impr)
print("\nlist des tweet avec le plus de clic profil : \n")

for i in range(5):
    tmax = impr.index(max(impr))
    print("tweet numéros {} avec {} clics par impression :".format(i+1,max(impr)),lTw[tmax],"", sep="\n")
    impr.pop(tmax)
    lTw.pop(tmax)