from django.shortcuts import render
from django.http import HttpResponse
from prozer import code_of_scrapper
from prozer import ph_module

def home(request):

    return render(request,'base.html')

def search(request):
    try:
        if request.method =='POST':
            phcap = str(request.POST["phname"])
            ph = phcap.lower()
            ph_name = ph.replace(" ","")

        if("oppo" in ph_name):
            if("reno3pro" in ph_name):
                img = ph_module.opporeno3pro[0]
                re1 = code_of_scrapper.amazon(ph_module.opporeno3pro[1])
                re1_1 = ph_module.opporeno3pro[1]
                re2 = code_of_scrapper.flipkart(ph_module.opporeno3pro[2])
                re2_2 = ph_module.opporeno3pro[2]
                re3 = code_of_scrapper.reliance(ph_module.opporeno3pro[3])
                re3_3 = ph_module.opporeno3pro[3]

            if("reno5pro" in ph_name):
                img = ph_module.opporeno5pro[0]
                re1 = code_of_scrapper.amazon(ph_module.opporeno5pro[1])
                re1_1 = ph_module.opporeno5pro[1]
                re2 = code_of_scrapper.flipkart(ph_module.opporeno5pro[2])
                re2_2 = ph_module.opporeno5pro[2]
                re3 = code_of_scrapper.reliance(ph_module.opporeno5pro[3])
                re3_3 = ph_module.opporeno5pro[3]

            if("reno6pro" in ph_name):
                img = ph_module.opporeno6pro[0]
                re1 = code_of_scrapper.amazon(ph_module.opporeno6pro[1])
                re1_1 = ph_module.opporeno6pro[1]
                re2 = code_of_scrapper.flipkart(ph_module.opporeno6pro[2])
                re2_2 = ph_module.opporeno6pro[2]
                re3 = code_of_scrapper.reliance(ph_module.opporeno6pro[3])
                re3_3 = ph_module.opporeno6pro[3]

            if ("reno7pro" in ph_name):
                img = ph_module.opporeno7pro[0]
                re1 = code_of_scrapper.amazon(ph_module.opporeno7pro[1])
                re1_1 = ph_module.opporeno7pro[1]
                re2 = code_of_scrapper.flipkart(ph_module.opporeno7pro[2])
                re2_2 = ph_module.opporeno7pro[2]
                re3 = code_of_scrapper.reliance(ph_module.opporeno7pro[3])
                re3_3 = ph_module.opporeno7pro[3]

            if ("a15" in ph_name):
                img = ph_module.oppoa15[0]
                re1 = code_of_scrapper.amazon(ph_module.oppoa15[1])
                re1_1 = ph_module.oppoa15[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppoa15[2])
                re2_2 = ph_module.oppoa15[2]
                re3 = code_of_scrapper.reliance(ph_module.oppoa15[3])
                re3_3 = ph_module.oppoa15[3]

            if ("a16" in ph_name):
                img = ph_module.oppoa16[0]
                re1 = code_of_scrapper.amazon(ph_module.oppoa16[1])
                re1_1 = ph_module.oppoa16[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppoa16[2])
                re2_2 = ph_module.oppoa16[2]
                re3 = code_of_scrapper.reliance(ph_module.oppoa16[3])
                re3_3 = ph_module.oppoa16[3]

            if ("a53" in ph_name):
                img = ph_module.oppoa53[0]
                re1 = code_of_scrapper.amazon(ph_module.oppoa53[1])
                re1_1 = ph_module.oppoa53[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppoa53[2])
                re2_2 = ph_module.oppoa53[2]
                re3 = code_of_scrapper.reliance(ph_module.oppoa53[3])
                re3_3 = ph_module.oppoa53[3]   

            if ("a54" in ph_name):
                img = ph_module.oppoa54[0]
                re1 = code_of_scrapper.amazon(ph_module.oppoa54[1])
                re1_1 = ph_module.oppoa54[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppoa54[2])
                re2_2 = ph_module.oppoa54[2]
                re3 = code_of_scrapper.reliance(ph_module.oppoa54[3])
                re3_3 = ph_module.oppoa54[3] 

            if ("a55" in ph_name):
                img = ph_module.oppoa55[0]
                re1 = code_of_scrapper.amazon(ph_module.oppoa55[1])
                re1_1 = ph_module.oppoa55[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppoa55[2])
                re2_2 = ph_module.oppoa55[2]
                re3 = code_of_scrapper.reliance(ph_module.oppoa55[3])
                re3_3 = ph_module.oppoa55[3]  

            if ("a17" in ph_name):
                img = ph_module.oppoa17[0]
                re1 = code_of_scrapper.amazon(ph_module.oppoa17[1])
                re1_1 = ph_module.oppoa17[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppoa17[2])
                re2_2 = ph_module.oppoa17[2]
                re3 = code_of_scrapper.reliance(ph_module.oppoa17[3])
                re3_3 = ph_module.oppoa17[3]    

            if ("f19pro" in ph_name):
                img = ph_module.oppof19pro[0]
                re1 = code_of_scrapper.amazon(ph_module.oppof19pro[1])
                re1_1 = ph_module.oppof19pro[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppof19pro[2])
                re2_2 = ph_module.oppof19pro[2]
                re3 = code_of_scrapper.reliance(ph_module.oppof19pro[3])
                re3_3 = ph_module.oppof19pro[3] 

            elif ("f19s" in ph_name):
                img = ph_module.oppof19s[0]
                re1 = code_of_scrapper.amazon(ph_module.oppof19s[1])
                re1_1 = ph_module.oppof19s[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppof19s[2])
                re2_2 = ph_module.oppof19s[2]
                re3 = code_of_scrapper.reliance(ph_module.oppof19s[3])
                re3_3 = ph_module.oppof19s[3]  

            elif ("f19" in ph_name):
                img = ph_module.oppof19[0]
                re1 = code_of_scrapper.amazon(ph_module.oppof19[1])
                re1_1 = ph_module.oppof19[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppof19[2])
                re2_2 = ph_module.oppof19[2]
                re3 = code_of_scrapper.reliance(ph_module.oppof19[3])
                re3_3 = ph_module.oppof19[3] 

            if ("16k" in ph_name):
                img = ph_module.oppo16k[0]
                re1 = code_of_scrapper.amazon(ph_module.oppo16k[1])
                re1_1 = ph_module.oppo16k[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppo16k[2])
                re2_2 = ph_module.oppo16k[2]
                re3 = code_of_scrapper.reliance(ph_module.oppo16k[3])
                re3_3 = ph_module.oppo16k[3] 

            if ("a785g" in ph_name or "a78" in ph_name):
                img = ph_module.oppoa785g[0]
                re1 = code_of_scrapper.amazon(ph_module.oppoa785g[1])
                re1_1 = ph_module.oppoa785g[1]
                re2 = code_of_scrapper.flipkart(ph_module.oppoa785g[2])
                re2_2 = ph_module.oppoa785g[2]
                re3 = code_of_scrapper.reliance(ph_module.oppoa785g[3])
                re3_3 = ph_module.oppoa785g[3] 
            
            if ("reno8pro5g" in ph_name or "reno8pro" in ph_name):
                img = ph_module.opporeno8pro5g[0]
                re1 = code_of_scrapper.amazon(ph_module.opporeno8pro5g[1])
                re1_1 = ph_module.opporeno8pro5g[1]
                re2 = code_of_scrapper.flipkart(ph_module.opporeno8pro5g[2])
                re2_2 = ph_module.opporeno8pro5g[2]
                re3 = code_of_scrapper.reliance(ph_module.opporeno8pro5g[3])
                re3_3 = ph_module.opporeno8pro5g[3] 

        if("redmi" in ph_name):
            if ("note7pro" in ph_name):
                img = ph_module.redminote7pro[0]
                re1 = code_of_scrapper.amazon(ph_module.redminote7pro[1])
                re1_1 = ph_module.redminote7pro[1]
                re2 = code_of_scrapper.flipkart(ph_module.redminote7pro[2])
                re2_2 = ph_module.redminote7pro[2]
                re3 = code_of_scrapper.reliance(ph_module.redminote7pro[3])
                re3_3 = ph_module.redminote7pro[3]

            if ("note9promax" in ph_name):
                img = ph_module.redminote9promax[0]
                re1 = code_of_scrapper.amazon(ph_module.redminote9promax[1])
                re1_1 = ph_module.redminote9promax[1]
                re2= code_of_scrapper.flipkart(ph_module.redminote9promax[2])
                re2_2 = ph_module.redminote9promax[2]
                re3=code_of_scrapper.reliance(ph_module.redminote9promax[3])
                re3_3 = ph_module.redminote9promax[3]

            elif ("note9pro" in ph_name):
                img = ph_module.redminote9pro[0]
                re1 =code_of_scrapper.amazon(ph_module.redminote9pro[1])
                re1_1 = ph_module.redminote9pro[1]
                re2 = code_of_scrapper.flipkart(ph_module.redminote9pro[2])
                re2_2 = ph_module.redminote9pro[2]
                re3 = code_of_scrapper.reliance(ph_module.redminote9pro[3])
                re3_3 = ph_module.redminote9pro[3]

            elif ("note9" in ph_name):
                img = ph_module.redminote9[0]
                re1 = code_of_scrapper.amazon(ph_module.redminote9[1])
                re1_1 = ph_module.redminote9[1]
                re2 = code_of_scrapper.flipkart(ph_module.redminote9[2])
                re2_2 = ph_module.redminote9[2]
                re3 = code_of_scrapper.reliance(ph_module.redminote9[3])
                re3_3 = ph_module.redminote9[3]

            elif ("note10pro" in ph_name):
                img = ph_module.redminote10pro[0]
                re1 = code_of_scrapper.amazon(ph_module.redminote10pro[1])
                re1_1 = ph_module.redminote10pro[1]
                re2 = code_of_scrapper.flipkart(ph_module.redminote10pro[2])
                re2_2 = ph_module.redminote10pro[2]
                re3 = code_of_scrapper.reliance(ph_module.redminote10pro[3])
                re3_3 = ph_module.redminote10pro[3]

            elif("note10" in ph_name):
                img = ph_module.redminote10[0]
                re1 = code_of_scrapper.amazon(ph_module.redminote10[1])
                re1_1 = ph_module.redminote10[1]
                re2 = code_of_scrapper.flipkart(ph_module.redminote10[2])
                re2_2 = ph_module.redminote10[2]
                re3 = code_of_scrapper.reliance(ph_module.redminote10[3])
                re3_3 = ph_module.redminote10[3]

            if ("note11t" in ph_name):
                img = ph_module.redminote11t[0]
                re1 = code_of_scrapper.amazon(ph_module.redminote11t[1])
                re1_1 = ph_module.redminote11t[1]
                re2 = code_of_scrapper.flipkart(ph_module.redminote11t[2])
                re2_2 = ph_module.redminote11t[2]
                re3 = code_of_scrapper.reliance(ph_module.redminote11t[3])
                re3_3 = ph_module.redminote11t[3]

            elif ("note11s" in ph_name):
                img = ph_module.redminote11s[0]
                re1 = code_of_scrapper.amazon(ph_module.redminote11s[1])
                re1_1 = ph_module.redminote11s[1]
                re2 = code_of_scrapper.flipkart(ph_module.redminote11s[2])
                re2_2 = ph_module.redminote11s[2]
                re3 = code_of_scrapper.reliance(ph_module.redminote11s[3])
                re3_3 = ph_module.redminote11s[3]

            elif ("note11" in ph_name):
                img = ph_module.redminote11[0]
                re1 = code_of_scrapper.amazon(ph_module.redminote11[1])
                re1_1 = ph_module.redminote11[1]
                re2 = code_of_scrapper.flipkart(ph_module.redminote11[2])
                re2_2 = ph_module.redminote11[2]
                re3 = code_of_scrapper.reliance(ph_module.redminote11[3])
                re3_3 = ph_module.redminote11[3]

            elif ("11prime" in ph_name):
                img = ph_module.redmi11prime[0]
                re1 = code_of_scrapper.amazon(ph_module.redmi11prime[1])
                re1_1 = ph_module.redmi11prime[1]
                re2 = code_of_scrapper.flipkart(ph_module.redmi11prime[2])
                re2_2 = ph_module.redminote11[2]
                re3 = code_of_scrapper.reliance(ph_module.redmi11prime[3])
                re3_3 = ph_module.redmi11prime[3]

            elif ("note12pro5g" in ph_name):
                img = ph_module.redmiNote12pro5g[0]
                re1 = code_of_scrapper.amazon(ph_module.redmiNote12pro5g[1])
                re1_1 = ph_module.redmiNote12pro5g[1]
                re2 = code_of_scrapper.flipkart(ph_module.redmiNote12pro5g[2])
                re2_2 = ph_module.redmiNote12pro5g[2]
                re3 = code_of_scrapper.reliance(ph_module.redmiNote12pro5g[3])
                re3_3 = ph_module.redmiNote12pro5g[3]

        if('samsunggalaxy' in ph_name):
            if('f12' in ph_name):
                img = ph_module.samsunggalaxyf12[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxyf12[1])
                re1_1 = ph_module.samsunggalaxyf12[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxyf12[2])
                re2_2 = ph_module.samsunggalaxyf12[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxyf12[3])
                re3_3 = ph_module.samsunggalaxyf12[3]

            if('f23' in ph_name):
                img = ph_module.samsunggalaxyf23[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxyf23[1])
                re1_1 = ph_module.samsunggalaxyf23[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxyf23[2])
                re2_2 = ph_module.samsunggalaxyf23[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxyf23[3])
                re3_3 = ph_module.samsunggalaxyf23[3]

            if('f62' in ph_name):
                img = ph_module.samsunggalaxyf62[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxyf62[1])
                re1_1 = ph_module.samsunggalaxyf62[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxyf62[2])
                re2_2 = ph_module.samsunggalaxyf62[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxyf62[3])
                re3_3 = ph_module.samsunggalaxyf62[3]
                
            if('fold2' in ph_name):
                img = ph_module.samsunggalaxyfold2[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxyfold2[1])
                re1_1 = ph_module.samsunggalaxyfold2[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxyfold2[2])
                re2_2 = ph_module.samsunggalaxyfold2[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxyfold2[3])
                re3_3 = ph_module.samsunggalaxyfold2[3]

            if('fold3' in ph_name):
                img = ph_module.samsunggalaxyfold3[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxyfold3[1])
                re1_1 = ph_module.samsunggalaxyfold3[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxyfold3[2])
                re2_2 = ph_module.samsunggalaxyfold3[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxyfold3[3])
                re3_3 = ph_module.samsunggalaxyfold3[3]

            if('m12' in ph_name):
                img = ph_module.samsunggalaxym12[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxym12[1])
                re1_1 = ph_module.samsunggalaxym12[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxym12[2])
                re2_2 = ph_module.samsunggalaxym12[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxym12[3])
                re3_3 = ph_module.samsunggalaxym12[3]

            if('m21' in ph_name):
                img = ph_module.samsunggalaxym21[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxym21[1])
                re1_1 = ph_module.samsunggalaxym21[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxym21[2])
                re2_2 = ph_module.samsunggalaxym21[2]
                re3= code_of_scrapper.reliance(ph_module.samsunggalaxym21[3])
                re3_3 = ph_module.samsunggalaxym21[3]

            if('m02' in ph_name):
                img = ph_module.samsunggalaxym02[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxym02[1])
                re1_1 = ph_module.samsunggalaxym02[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxym02[2])
                re2_2 = ph_module.samsunggalaxym02[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxym02[3])
                re3_3 = ph_module.samsunggalaxym02[3]

            if('m32' in ph_name):
                img = ph_module.samsunggalaxym32[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxym32[1])
                re1_1 = ph_module.samsunggalaxym32[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxym32[2])
                re2_2 = ph_module.samsunggalaxym32[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxym32[3])
                re3_3 = ph_module.samsunggalaxym32[3]
        
            if('m33' in ph_name):
                img = ph_module.samsunggalaxym33[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxym33[1])
                re1_1 = ph_module.samsunggalaxym33[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxym33[2])
                re2_2 = ph_module.samsunggalaxym33[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxym33[3])
                re3_3 = ph_module.samsunggalaxym33[3]
            
            if('note10' in ph_name):
                img = ph_module.samsunggalaxynote10[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxynote10[1])
                re1_1 = ph_module.samsunggalaxynote10[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxynote10[2])
                re2_2 = ph_module.samsunggalaxynote10[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxynote10[3])
                re3_3 = ph_module.samsunggalaxynote10[3]

            if('note20' in ph_name):
                img = ph_module.samsunggalaxynote20[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxynote20[1])
                re1_1 = ph_module.samsunggalaxynote20[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxynote20[2])
                re2_2 = ph_module.samsunggalaxynote20[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxynote20[3])
                re3_3 = ph_module.samsunggalaxynote20[3]

            if('m135g' in ph_name or 'm13' in ph_name):
                img = ph_module.samsunggalaxym135G[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxym135G[1])
                re1_1 = ph_module.samsunggalaxym135G[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxym135G[2])
                re2_2 = ph_module.samsunggalaxym135G[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxym135G[3])
                re3_3 = ph_module.samsunggalaxym135G[3]

            if('a145g' in ph_name or "a14" in ph_name):
                img = ph_module.samsunggalaxya145g[0]
                re1 = code_of_scrapper.amazon(ph_module.samsunggalaxya145g[1])
                re1_1 = ph_module.samsunggalaxya145g[1]
                re2 = code_of_scrapper.flipkart(ph_module.samsunggalaxya145g[2])
                re2_2 = ph_module.samsunggalaxya145g[2]
                re3 = code_of_scrapper.reliance(ph_module.samsunggalaxya145g[3])
                re3_3 = ph_module.samsunggalaxya145g[3]

        if('appleiphone' in ph_name):
            if('12pro' in ph_name):
                img = ph_module.appleiphone12pro[0]
                re1 = code_of_scrapper.amazon(ph_module.appleiphone12pro[1])
                re1_1 = ph_module.appleiphone12pro[1]
                re2 = code_of_scrapper.flipkart(ph_module.appleiphone12pro[2])
                re2_2 = ph_module.appleiphone12pro[2]
                re3 = code_of_scrapper.reliance(ph_module.appleiphone12pro[3])
                re3_3 = ph_module.appleiphone12pro[3]

            elif('12' in ph_name):
                img = ph_module.appleiphone12[0]
                re1 = code_of_scrapper.amazon(ph_module.appleiphone12[1])
                re1_1 = ph_module.appleiphone12[1]
                re2 = code_of_scrapper.flipkart(ph_module.appleiphone12[2])
                re2_2 = ph_module.appleiphone12[2]
                re3 = code_of_scrapper.reliance(ph_module.appleiphone12[3])
                re3_3 = ph_module.appleiphone12[3] 

            if('11' in ph_name):
                img = ph_module.appleiphone11[0]
                re1 = code_of_scrapper.amazon(ph_module.appleiphone11[1])
                re1_1 = ph_module.appleiphone11[1]
                re2 = code_of_scrapper.flipkart(ph_module.appleiphone11[2])
                re2_2 = ph_module.appleiphone11[2]
                re3 = code_of_scrapper.reliance(ph_module.appleiphone11[3])
                re3_3 = ph_module.appleiphone11[3] 

            if('13' in ph_name):
                img = ph_module.appleiphone13[0]
                re1 = code_of_scrapper.amazon(ph_module.appleiphone13[1])
                re1_1 = ph_module.appleiphone13[1]
                re2 = code_of_scrapper.flipkart(ph_module.appleiphone13[2])
                re2_2 = ph_module.appleiphone13[2]
                re3 = code_of_scrapper.reliance(ph_module.appleiphone13[3])
                re3_3 = ph_module.appleiphone13[3]

            if('13pro' in ph_name):
                img = ph_module.appleiphone13pro[0]
                re1 = code_of_scrapper.amazon(ph_module.appleiphone13pro[1])
                re1_1 = ph_module.appleiphone13pro[1]
                re2 = code_of_scrapper.flipkart(ph_module.appleiphone13pro[2])
                re2_2 = ph_module.appleiphone13pro[2]
                re3 = code_of_scrapper.reliance(ph_module.appleiphone13pro[3])
                re3_3 = ph_module.appleiphone13pro[3]

            if('13promax' in ph_name):
                img = ph_module.appleiphone13promax[0]
                re1 = code_of_scrapper.amazon(ph_module.appleiphone13promax[1])
                re1_1 = ph_module.appleiphone13promax[1]
                re2 = code_of_scrapper.flipkart(ph_module.appleiphone13promax[2])
                re2_2 = ph_module.appleiphone13promax[2]
                re3 = code_of_scrapper.reliance(ph_module.appleiphone13promax[3])
                re3_3 = ph_module.appleiphone13promax[3]

            if('se' in ph_name):
                img = ph_module.appleiphonese[0]
                re1 = code_of_scrapper.amazon(ph_module.appleiphonese[1])
                re1_1 = ph_module.appleiphonese[1]
                re2 = code_of_scrapper.flipkart(ph_module.appleiphonese[2])
                re2_2 = ph_module.appleiphonese[2]
                re3 = code_of_scrapper.reliance(ph_module.appleiphonese[3])
                re3_3 = ph_module.appleiphonese[3]

            if('xr' in ph_name):
                img = ph_module.appleiphonexr[0]
                re1 = code_of_scrapper.amazon(ph_module.appleiphonexr[1])
                re1_1 = ph_module.appleiphonexr[1]
                re2 = code_of_scrapper.flipkart(ph_module.appleiphonexr[2])
                re2_2 = ph_module.appleiphonexr[2]
                re3 = code_of_scrapper.reliance(ph_module.appleiphonexr[3])
                re3_3 = ph_module.appleiphonexr[3]

            if('14promax' in ph_name):
                img = ph_module.appleiphone14promax[0]
                re1 = code_of_scrapper.amazon(ph_module.appleiphone14promax[1])
                re1_1 = ph_module.appleiphone14promax[1]
                re2 = code_of_scrapper.flipkart(ph_module.appleiphone14promax[2])
                re2_2 = ph_module.appleiphone14promax[2]
                re3 = code_of_scrapper.reliance(ph_module.appleiphone14promax[3])
                re3_3 = ph_module.appleiphone14promax[3]

        if('realme' in ph_name):
            if('narzo50a' in ph_name):
                img = ph_module.realmenarzo50a[0]
                re1 = code_of_scrapper.amazon(ph_module.realmenarzo50a[1])
                re1_1 = ph_module.realmenarzo50a[1]
                re2 = code_of_scrapper.flipkart(ph_module.realmenarzo50a[2])
                re2_2 = ph_module.realmenarzo50a[2]
                re3 = code_of_scrapper.reliance(ph_module.realmenarzo50a[3])
                re3_3 = ph_module.realmenarzo50a[3]
            
            if('8' in ph_name):
                img = ph_module.realme8[0]
                re1 = code_of_scrapper.amazon(ph_module.realme8[1])
                re1_1 = ph_module.realme8[1]
                re2 = code_of_scrapper.flipkart(ph_module.realme8[2])
                re2_2 = ph_module.realme8[2]
                re3 = code_of_scrapper.reliance(ph_module.realme8[3])
                re3_3 = ph_module.realme8[3]

            if('c11' in ph_name):
                img = ph_module.realmec11[0]
                re1 = code_of_scrapper.amazon(ph_module.realmec11[1])
                re1_1 = ph_module.realmec11[1]
                re2 = code_of_scrapper.flipkart(ph_module.realmec11[2])
                re2_2 = ph_module.realmec11[2]
                re3 = code_of_scrapper.reliance(ph_module.realmec11[3])
                re3_3 = ph_module.realmec11[3]

            if('gtmasteredition' in ph_name):
                img = ph_module.realmegtmasteredition[0]
                re1 = code_of_scrapper.amazon(ph_module.realmegtmasteredition[1])
                re1_1 = ph_module.realmegtmasteredition[1]
                re2 = code_of_scrapper.flipkart(ph_module.realmegtmasteredition[2])
                re2_2 = ph_module.realmegtmasteredition[2]
                re3 = code_of_scrapper.reliance(ph_module.realmegtmasteredition[3])
                re3_3 = ph_module.realmegtmasteredition[3]

            if('9i' in ph_name):
                img = ph_module.realme9i[0]
                re1=code_of_scrapper.amazon(ph_module.realme9i[1])
                re1_1=ph_module.realme9i[1]
                re2=code_of_scrapper.flipkart(ph_module.realme9i[2])
                re2_2=ph_module.realme9i[2]
                re3=code_of_scrapper.reliance(ph_module.realme9i[3])
                re3_3=ph_module.realme9i[3]

            if('narzo30' in ph_name):
                img = ph_module.realmenarzo30[0]
                re1=code_of_scrapper.amazon(ph_module.realmenarzo30[1])
                re1_1=ph_module.realmenarzo30[1]
                re2=code_of_scrapper.flipkart(ph_module.realmenarzo30[2])
                re2_2=ph_module.realmenarzo30[2]
                re3=code_of_scrapper.reliance(ph_module.realmenarzo30[3])
                re3_3=ph_module.realmenarzo30[3]

            if('c25y' in ph_name):
                img = ph_module.realmec25y[0]
                re1=code_of_scrapper.amazon(ph_module.realmec25y[1])
                re1_1=ph_module.realmec25y[1]
                re2=code_of_scrapper.flipkart(ph_module.realmec25y[2])
                re2_2=ph_module.realmec25y[2]
                re3=code_of_scrapper.reliance(ph_module.realmec25y[3])
                re3_3=ph_module.realmec25y[3]
    
            if('x7max' in ph_name):
                img = ph_module.realmex7max[0]
                re1=code_of_scrapper.amazon(ph_module.realmex7max[1])
                re1_1=ph_module.realmex7max[1]
                re2=code_of_scrapper.flipkart(ph_module.realmex7max[2])
                re2_2=ph_module.realmex7max[2]
                re3=code_of_scrapper.reliance(ph_module.realmex7max[3])
                re3_3=ph_module.realmex7max[3]

            if('7pro' in ph_name):
                img = ph_module.realme7pro[0]
                re1=code_of_scrapper.amazon(ph_module.realme7pro[1])
                re1_1=ph_module.realme7pro[1]
                re2=code_of_scrapper.flipkart(ph_module.realme7pro[2])
                re2_2=ph_module.realme7pro[2]
                re3=code_of_scrapper.reliance(ph_module.realme7pro[3])
                re3_3=ph_module.realme7pro[3]

            if('x50pro' in ph_name):
                img = ph_module.realmex50pro[0]
                re1=code_of_scrapper.amazon(ph_module.realmex50pro[1])
                re1_1=ph_module.realmex50pro[1]
                re2=code_of_scrapper.flipkart(ph_module.realmex50pro[2])
                re2_2=ph_module.realmex50pro[2]
                re3=code_of_scrapper.reliance(ph_module.realmex50pro[3])
                re3_3=ph_module.realmex50pro[3]

            if('c21y' in ph_name):
                img = ph_module.realmec21y[0]
                re1=code_of_scrapper.amazon(ph_module.realmec21y[1])
                re1_1=ph_module.realmec21y[1]
                re2=code_of_scrapper.flipkart(ph_module.realmec21y[2])
                re2_2=ph_module.realmec21y[2]
                re3=code_of_scrapper.reliance(ph_module.realmec21y[3])
                re3_3=ph_module.realmec21y[3]

            if('gtneo2' in ph_name):
                img = ph_module.realmegtneo2[0]
                re1=code_of_scrapper.amazon(ph_module.realmegtneo2[1])
                re1_1=ph_module.realmegtneo2[1]
                re2=code_of_scrapper.flipkart(ph_module.realmegtneo2[2])
                re2_2=ph_module.realmegtneo2[2]
                re3=code_of_scrapper.reliance(ph_module.realmegtneo2[3])
                re3_3=ph_module.realmegtneo2[3]

            if('x3' in ph_name):
                img = ph_module.realmex3[0]
                re1=code_of_scrapper.amazon(ph_module.realmex3[1])
                re1_1=ph_module.realmex3[1]
                re2=code_of_scrapper.flipkart(ph_module.realmex3[2])
                re2_2=ph_module.realmex3[2]
                re3=code_of_scrapper.reliance(ph_module.realmex3[3])
                re3_3=ph_module.realmex3[3]

            if('c15' in ph_name):
                img = ph_module.realmec15[0]
                re1=code_of_scrapper.amazon(ph_module.realmec15[1])
                re1_1=ph_module.realmec15[1]
                re2=code_of_scrapper.flipkart(ph_module.realmec15[2])
                re2_2=ph_module.realmec15[2]
                re3=code_of_scrapper.reliance(ph_module.realmec15[3])
                re3_3=ph_module.realmec15[3]

            if('c20' in ph_name):
                img = ph_module.realmec20[0]
                re1=code_of_scrapper.amazon(ph_module.realmec20[1])
                re1_1=ph_module.realmec20[1]
                re2=code_of_scrapper.flipkart(ph_module.realmec20[2])
                re2_2=ph_module.realmec20[2]
                re3=code_of_scrapper.reliance(ph_module.realmec20[3])
                re3_3=ph_module.realmec20[3]

            if('xseriesx7' in ph_name):
                img = ph_module.realmexseriesx7[0]
                re1=code_of_scrapper.amazon(ph_module.realmexseriesx7[1])
                re1_1=ph_module.realmexseriesx7[1]
                re2=code_of_scrapper.flipkart(ph_module.realmexseriesx7[2])
                re2_2=ph_module.realmexseriesx7[2]
                re3=code_of_scrapper.reliance(ph_module.realmexseriesx7[3])
                re3_3=ph_module.realmexseriesx7[3]

            if('8s' in ph_name):
                img = ph_module.realme8s[0]
                re1=code_of_scrapper.amazon(ph_module.realme8s[1])
                re1_1=ph_module.realme8s[1]
                re2=code_of_scrapper.flipkart(ph_module.realme8s[2])
                re2_2=ph_module.realme8s[2]
                re3=code_of_scrapper.reliance(ph_module.realme8s[3])
                re3_3=ph_module.realme8s[3]

            if('8pro' in ph_name):
                img = ph_module.realme8pro[0]
                re1=code_of_scrapper.amazon(ph_module.realme8pro[1])
                re1_1=ph_module.realme8pro[1]
                re2=code_of_scrapper.flipkart(ph_module.realme8pro[2])
                re2_2=ph_module.realme8pro[2]
                re3=code_of_scrapper.reliance(ph_module.realme8pro[3])
                re3_3=ph_module.realme8pro[3]

            if('c35' in ph_name):
                img = ph_module.realmec35[0]
                re1=code_of_scrapper.amazon(ph_module.realmec35[1])
                re1_1=ph_module.realmec35[1]
                re2=code_of_scrapper.flipkart(ph_module.realmec35[2])
                re2_2=ph_module.realmec35[2]
                re3=code_of_scrapper.reliance(ph_module.realmec35[3])
                re3_3=ph_module.realmec35[3]

            if('9' in ph_name):
                img = ph_module.realme9[0]
                re1=code_of_scrapper.amazon(ph_module.realme9[1])
                re1_1=ph_module.realme9[1]
                re2=code_of_scrapper.flipkart(ph_module.realme9[2])
                re2_2=ph_module.realme9[2]
                re3=code_of_scrapper.reliance(ph_module.realme9[3])
                re3_3=ph_module.realme9[3]
            
            if('10proplus5g' in ph_name or '10proplus' in ph_name):
                img = ph_module.realme10Proplus5g[0]
                re1=code_of_scrapper.amazon(ph_module.realme10Proplus5g[1])
                re1_1=ph_module.realme10Proplus5g[1]
                re2=code_of_scrapper.flipkart(ph_module.realme10Proplus5g[2])
                re2_2=ph_module.realme10Proplus5g[2]
                re3=code_of_scrapper.reliance(ph_module.realme10Proplus5g[3])
                re3_3=ph_module.realme10Proplus5g[3]

        if('vivo' in ph_name):
            if('y73' in ph_name):
                img = ph_module.vivoy73[0]
                re1=code_of_scrapper.amazon(ph_module.vivoy73[1])
                re1_1=ph_module.vivoy73[1]
                re2=code_of_scrapper.flipkart(ph_module.vivoy73[2])
                re2_2=ph_module.vivoy73[2]
                re3=code_of_scrapper.reliance(ph_module.vivoy73[3])
                re3_3=ph_module.vivoy73[3]

            if('y51' in ph_name):
                img = ph_module.vivoy51[0]
                re1=code_of_scrapper.amazon(ph_module.vivoy51[1])
                re1_1=ph_module.vivoy51[1]
                re2=code_of_scrapper.flipkart(ph_module.vivoy51[2])
                re2_2=ph_module.vivoy51[2]
                re3=code_of_scrapper.reliance(ph_module.vivoy51[3])
                re3_3=ph_module.vivoy51[3]

            if('y20a' in ph_name):
                img = ph_module.vivoy20a[0]
                re1=code_of_scrapper.amazon(ph_module.vivoy20a[1])
                re1_1=ph_module.vivoy20a[1]
                re2=code_of_scrapper.flipkart(ph_module.vivoy20a[2])
                re2_2=ph_module.vivoy20a[2]
                re3=code_of_scrapper.reliance(ph_module.vivoy20a[3])
                re3_3=ph_module.vivoy20a[3]

            if('y31' in ph_name):
                img = ph_module.vivoy31[0]
                re1=code_of_scrapper.amazon(ph_module.vivoy31[1])
                re1_1=ph_module.vivoy31[1]
                re2=code_of_scrapper.flipkart(ph_module.vivoy31[2])
                re2_2=ph_module.vivoy31[2]
                re3=code_of_scrapper.reliance(ph_module.vivoy31[3])
                re3_3=ph_module.vivoy31[3]

            if('v20' in ph_name):
                img = ph_module.vivov20[0]
                re1=code_of_scrapper.amazon(ph_module.vivov20[1])
                re1_1=ph_module.vivov20[1]
                re2=code_of_scrapper.flipkart(ph_module.vivov20[2])
                re2_2=ph_module.vivov20[2]
                re3=code_of_scrapper.reliance(ph_module.vivov20[3])
                re3_3=ph_module.vivov20[3]

            if('x50' in ph_name):
                img = ph_module.vivox50[0]
                re1=code_of_scrapper.amazon(ph_module.vivox50[1])
                re1_1=ph_module.vivox50[1]
                re2=code_of_scrapper.flipkart(ph_module.vivox50[2])
                re2_2=ph_module.vivox50[2]
                re3=code_of_scrapper.reliance(ph_module.vivox50[3])
                re3_3=ph_module.vivox50[3]

            if('y19' in ph_name):
                img = ph_module.vivox19[0]
                re1=code_of_scrapper.amazon(ph_module.vivoy19[1])
                re1_1=ph_module.vivoy19[1]
                re2=code_of_scrapper.flipkart(ph_module.vivoy19[2])
                re2_2=ph_module.vivoy19[2]
                re3=code_of_scrapper.reliance(ph_module.vivoy19[3])
                re3_3=ph_module.vivoy19[3]

            if('v25pro5g' in ph_name or 'v25pro' in ph_name):
                img = ph_module.vivov25pro5g[0]
                re1=code_of_scrapper.amazon(ph_module.vivov25pro5g[1])
                re1_1=ph_module.vivov25pro5g[1]
                re2=code_of_scrapper.flipkart(ph_module.vivov25pro5g[2])
                re2_2=ph_module.vivov25pro5g[2]
                re3=code_of_scrapper.reliance(ph_module.vivov25pro5g[3])
                re3_3=ph_module.vivov25pro5g[3]

        if('nokia'in ph_name):
            if('3.4' in ph_name):
                img = ph_module.nokia3_4[0]
                re1 = code_of_scrapper.amazon(ph_module.nokia3_4[1])
                re1_1 = ph_module.nokia3_4[1]
                re2 = code_of_scrapper.flipkart(ph_module.nokia3_4[2])
                re2_2=ph_module.nokia3_4[2]
                re3=code_of_scrapper.reliance(ph_module.nokia3_4[3])
                re3_3=ph_module.nokia3_4[3]
                
            if('g10' in ph_name):
                img = ph_module.nokiag10[0]
                re1=code_of_scrapper.amazon(ph_module.nokiag10[1])
                re1_1=ph_module.nokiag10[1]
                re2=code_of_scrapper.flipkart(ph_module.nokiag10[2])
                re2_2=ph_module.nokiag10[2]
                re3=code_of_scrapper.reliance(ph_module.nokiag10[3])
                re3_3=ph_module.nokiag10[3]

            if('g20' in ph_name):
                img = ph_module.nokiag20[0]
                re1=code_of_scrapper.amazon(ph_module.nokiag20[1])
                re1_1=ph_module.nokiag20[1]
                re2=code_of_scrapper.flipkart(ph_module.nokiag20[2])
                re2_2=ph_module.nokiag20[2]
                re3=code_of_scrapper.reliance(ph_module.nokiag20[3])
                re3_3=ph_module.nokiag20[3]

            if('c20' in ph_name):
                img = ph_module.nokiac20[0]
                re1=code_of_scrapper.amazon(ph_module.nokiac20[1])
                re1_1=ph_module.nokiac20[1]
                re2=code_of_scrapper.flipkart(ph_module.nokiac20[2])
                re2_2=ph_module.nokiac20[2]
                re3=code_of_scrapper.reliance(ph_module.nokiac20[3])
                re3_3=ph_module.nokiac20[3]

            if('3.2' in ph_name):
                img = ph_module.nokia3_2[0]
                re1=code_of_scrapper.amazon(ph_module.nokia3_2[1])
                re1_1=ph_module.nokia3_2[1]
                re2=code_of_scrapper.flipkart(ph_module.nokia3_2[2])
                re2_2=ph_module.nokia3_2[2]
                re3=code_of_scrapper.reliance(ph_module.nokia3_2[3])
                re3_3=ph_module.nokia3_2[3]

            if('c01' in ph_name):
                img = ph_module.nokiac01[0]
                re1=code_of_scrapper.amazon(ph_module.nokiac01[1])
                re1_1=ph_module.nokiac01[1]
                re2=code_of_scrapper.flipkart(ph_module.nokiac01[2])
                re2_2=ph_module.nokiac01[2]
                re3=code_of_scrapper.reliance(ph_module.nokiac01[3])
                re3_3=ph_module.nokiac01[3]

            if('c3' in ph_name):
                img = ph_module.nokiac3[0]
                re1=code_of_scrapper.amazon(ph_module.nokiac3[1])
                re1_1=ph_module.nokiac3[1]
                re2=code_of_scrapper.flipkart(ph_module.nokiac3[2])
                re2_2=ph_module.nokiac3[2]
                re3=code_of_scrapper.reliance(ph_module.nokiac3[3])
                re3_3=ph_module.nokiac3[3]
            
            if('2.3' in ph_name):
                img = ph_module.nokia2_3[0]
                re1=code_of_scrapper.amazon(ph_module.nokia2_3[1])
                re1_1=ph_module.nokia2_3[1]
                re2=code_of_scrapper.flipkart(ph_module.nokia2_3[2])
                re2_2=ph_module.nokia2_3[2]
                re3=code_of_scrapper.reliance(ph_module.nokia2_3[3])
                re3_3=ph_module.nokia2_3[3]

            if('5.4' in ph_name):
                img = ph_module.nokia5_4[0]
                re1=code_of_scrapper.amazon(ph_module.nokia5_4[1])
                re1_1=ph_module.nokia5_4[1]
                re2=code_of_scrapper.flipkart(ph_module.nokia5_4[2])
                re2_2=ph_module.nokia5_4[2]
                re3=code_of_scrapper.reliance(ph_module.nokia5_4[3])
                re3_3=ph_module.nokia5_4[3]

        if('motorola' in ph_name):
            if('e7power' in ph_name):
                img = ph_module.motorolae7power[0]
                re1=code_of_scrapper.amazon(ph_module.motorolae7power[1])
                re1_1=ph_module.motorolae7power[1]
                re2=code_of_scrapper.flipkart(ph_module.motorolae7power[2])
                re2_2=ph_module.motorolae7power[2]
                re3=code_of_scrapper.reliance(ph_module.motorolae7power[3])
                re3_3=ph_module.motorolae7power[3]
                
            if('g60' in ph_name):
                img = ph_module.motorolag60[0]
                re1=code_of_scrapper.amazon(ph_module.motorolag60[1])
                re1_1=ph_module.motorolag60[1]
                re2=code_of_scrapper.flipkart(ph_module.motorolag60[2])
                re2_2=ph_module.motorolag60[2]
                re3=code_of_scrapper.reliance(ph_module.motorolag60[3])
                re3_3=ph_module.motorolag60[3]
                
            if('razr' in ph_name):
                img = ph_module.motorolarazr[0]
                re1=code_of_scrapper.amazon(ph_module.motorolarazr[1])
                re1_1=ph_module.motorolarazr[1]
                re2=code_of_scrapper.flipkart(ph_module.motorolarazr[2])
                re2_2=ph_module.motorolarazr[2]
                re3=code_of_scrapper.reliance(ph_module.motorolarazr[3])
                re3_3=ph_module.motorolarazr[3]
                
            if('g31' in ph_name):
                img = ph_module.motorolag31[0]
                re1=code_of_scrapper.amazon(ph_module.motorolag31[1])
                re1_1=ph_module.motorolag31[1]
                re2=code_of_scrapper.flipkart(ph_module.motorolag31[2])
                re2_2=ph_module.motorolag31[2]
                re3=code_of_scrapper.reliance(ph_module.motorolag31[3])
                re3_3=ph_module.motorolag31[3]

            if('edge20' in ph_name):
                img = ph_module.motorolaedge20[0]
                re1=code_of_scrapper.amazon(ph_module.motorolaedge20[1])
                re1_1=ph_module.motorolaedge20[1]
                re2=code_of_scrapper.flipkart(ph_module.motorolaedge20[2])
                re2_2=ph_module.motorolaedge20[2]
                re3=code_of_scrapper.reliance(ph_module.motorolaedge20[3])
                re3_3=ph_module.motorolaedge20[3]

            if('g30' in ph_name):
                img = ph_module.motorolag30[0]
                re1=code_of_scrapper.amazon(ph_module.motorolag30[1])
                re1_1=ph_module.motorolag30[1]
                re2=code_of_scrapper.flipkart(ph_module.motorolag30[2])
                re2_2=ph_module.motorolag30[2]
                re3=code_of_scrapper.reliance(ph_module.motorolag30[3])
                re3_3=ph_module.motorolag30[3]

            if('motog51' in ph_name):
                img = ph_module.motorolamotog51[0]
                re1=code_of_scrapper.amazon(ph_module.motorolamotog51[1])
                re1_1=ph_module.motorolamotog51[1]
                re2=code_of_scrapper.flipkart(ph_module.motorolamotog51[2])
                re2_2=ph_module.motorolamotog51[2]
                re3=code_of_scrapper.reliance(ph_module.motorolamotog51[3])
                re3_3=ph_module.motorolamotog51[3]

            if('g40' in ph_name):
                img = ph_module.motorolag40[0]
                re1=code_of_scrapper.amazon(ph_module.motorolag40[1])
                re1_1=ph_module.motorolag40[1]
                re2=code_of_scrapper.flipkart(ph_module.motorolag40[2])
                re2_2=ph_module.motorolag40[2]
                re3=code_of_scrapper.reliance(ph_module.motorolag40[3])
                re3_3=ph_module.motorolag40[3]

            if('edge30ultra5g' in ph_name or 'edge30ultra' in ph_name):
                img = ph_module.motorolaedge30ultra5g[0]
                re1=code_of_scrapper.amazon(ph_module.motorolaedge30ultra5g[1])
                re1_1=ph_module.motorolaedge30ultra5g[1]
                re2=code_of_scrapper.flipkart(ph_module.motorolaedge30ultra5g[2])
                re2_2=ph_module.motorolaedge30ultra5g[2]
                re3=code_of_scrapper.reliance(ph_module.motorolaedge30ultra5g[3])
                re3_3=ph_module.motorolaedge30ultra5g[3]

        if('oneplus' in ph_name):
            if('7' in ph_name):
                img = ph_module.oneplus7[0]
                re1=code_of_scrapper.amazon(ph_module.oneplus7[1])
                re1_1=ph_module.oneplus7[1]
                re2=code_of_scrapper.flipkart(ph_module.oneplus7[2])
                re2_2=ph_module.oneplus7[2]
                re3=code_of_scrapper.reliance(ph_module.oneplus7[3])
                re3_3=ph_module.oneplus7[3]

            if('8t' in ph_name):
                img = ph_module.oneplus8t[0]
                re1=code_of_scrapper.amazon(ph_module.oneplus8t[1])
                re1_1=ph_module.oneplus8t[1]
                re2=code_of_scrapper.flipkart(ph_module.oneplus8t[2])
                re2_2=ph_module.oneplus8t[2]
                re3=code_of_scrapper.reliance(ph_module.oneplus8t[3])
                re3_3=ph_module.oneplus8t[3]

            if('9' in ph_name):
                img = ph_module.oneplus9[0]
                re1=code_of_scrapper.amazon(ph_module.oneplus9[1])
                re1_1=ph_module.oneplus9[1]
                re2=code_of_scrapper.flipkart(ph_module.oneplus9[2])
                re2_2=ph_module.oneplus9[2]
                re3=code_of_scrapper.reliance(ph_module.oneplus9[3])
                re3_3=ph_module.oneplus9[3]

            if('10pro' in ph_name):
                img = ph_module.oneplus10pro[0]
                re1=code_of_scrapper.amazon(ph_module.oneplus10pro[1])
                re1_1=ph_module.oneplus10pro[1]
                re2=code_of_scrapper.flipkart(ph_module.oneplus10pro[2])
                re2_2=ph_module.oneplus10pro[2]
                re3=code_of_scrapper.reliance(ph_module.oneplus10pro[3])
                re3_3=ph_module.oneplus10pro[3]

            if('nordce2' in ph_name):
                img = ph_module.oneplusnordce2[0]
                re1=code_of_scrapper.amazon(ph_module.oneplusnordce2[1])
                re1_1=ph_module.oneplusnordce2[1]
                re2=code_of_scrapper.flipkart(ph_module.oneplusnordce2[2])
                re2_2=ph_module.oneplusnordce2[2]
                re3=code_of_scrapper.reliance(ph_module.oneplusnordce2[3])
                re3_3=ph_module.oneplusnordce2[3]

            elif('nord2' in ph_name):
                img = ph_module.oneplusnord2[0]
                re1=code_of_scrapper.amazon(ph_module.oneplusnord2[1])
                re1_1=ph_module.oneplusnord2[1]
                re2=code_of_scrapper.flipkart(ph_module.oneplusnord2[2])
                re2_2=ph_module.oneplusnord2[2]
                re3=code_of_scrapper.reliance(ph_module.oneplusnord2[3])
                re3_3=ph_module.oneplusnord2[3]

            if('nordce2lite5g' in ph_name or 'nordce2lite' in ph_name):
                img = ph_module.oneplusNordCE2Lite5g[0]
                re1=code_of_scrapper.amazon(ph_module.oneplusNordCE2Lite5g[1])
                re1_1=ph_module.oneplusNordCE2Lite5g[1]
                re2=code_of_scrapper.flipkart(ph_module.oneplusNordCE2Lite5g[2])
                re2_2=ph_module.oneplusNordCE2Lite5g[2]
                re3=code_of_scrapper.reliance(ph_module.oneplusNordCE2Lite5g[3])
                re3_3=ph_module.oneplusNordCE2Lite5g[3]
            
    
        return render(request, "result.html",{'img':img,'phname':phcap,'ph_name':ph_name,'ph_name1':re1,'ph_name2':re2,'ph_name3':re3,'min_value':code_of_scrapper.mini(),'link1':re1_1,'link2':re2_2,'link3':re3_3})
    except UnboundLocalError:
        return HttpResponse("Something went wrong")

def About(request):

    return render(request,"About.html")