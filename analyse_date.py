import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import subprocess

direct = os.listdir('date/')
lmois = []
direct.sort() #trie solon date 

#lecture CSV*************************************
for d in direct : 

    with open('date/{}'.format(d), newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    lmois.append(data)

#recupere la date de debut de donnees
m =[]
for i in direct :
    v = i.split('_')
    m.append(v[5][4:6])

#def liste utiles******************************
ldateTW = [] #nombre tweet du jour
ldate = []
l_impr = []
l_engag = [] 
l_rt = []
l_eng_prct = []
l_eng_prct_mois = []
l_like = []
impr_moy_mois = []
engag_moy_mois = []
like_moy_mois = []
rt_moy_mois = []
total_tw = 0

#parcours tout les mois***************************
for mois in lmois :
    engag = []
    engag_prct = []
    impr = []
    like = []
    rt = []
    nbligne = len(mois)
    nbtw = nbligne - 1
    ldate.append(total_tw)
    total_tw += nbtw

    for tweet in mois[1:] : 
        ldateTW.append(tweet[1])
        l_impr.append(float(tweet[2]))
        impr.append(float(tweet[2]))
        l_engag.append(float(tweet[3]))
        engag.append(float(tweet[3]))
        l_rt.append(float(tweet[5]))
        rt.append(float(tweet[5]))
        l_eng_prct.append(float(tweet[4]))
        engag_prct.append(float(tweet[4]))
        l_like.append(float(tweet[7]))
        like.append(float(tweet[7]))
        

    impr_moy_mois.append(np.median(np.array(impr)))
    engag_moy_mois.append(np.median(np.array(engag)))
    l_eng_prct_mois.append(np.mean(np.array(engag_prct)*100))
    rt_moy_mois.append(np.median(np.array(rt)))
    like_moy_mois.append(np.median(np.array(like)))

x = np.arange(len(ldateTW))

plt.figure(figsize=(15,15))
plt.subplot(121)
plt.plot(x,l_impr, label="impression")
plt.plot(x,l_engag, label="engagement")
plt.xticks(ldate, m)
plt.legend()
plt.title("impression / engagement en fonction du jour")

plt.subplot(122)
plt.plot(x,l_like, label="like")
plt.plot(x,l_rt, label="RT")
plt.title("like / RT en fonction du jour")
plt.legend()
plt.xticks(ldate, m)

plt.show()