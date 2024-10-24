#Saklah Lampu
print ('''
========={Saklar Lampu}==========
=========={ON/OFF}==========
       ''')
saklar = input("ON/OFF : ")
if saklar == "ON" :
    print ("Lampu Hidup")
elif saklar == "OFF" :
    print ("Lampu Mati")
else :
    print("Pilih ON/OFF")