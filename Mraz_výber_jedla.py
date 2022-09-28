import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(bg='white',width=900,height=600) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

open('vyber_jedla.txt', 'w').close() #vymazávam obsah súboru po znovu spustení

canvas.create_text(420,70,text='VÝBER JEDLA',fill='black',font='Arial 40') #vypísanie textu
def ktore(ktora,kod): #funkcia, ktorá zabezpečuje vpisovanie do súboru
    if ktora==1: #podmienka, ktorou kontrolujem hodnotu ktora
        if kod!='': #podmienka, ktorou zisťujem či bol zadaný kód
            slovo=kod+' '+'z' #do tex. premennej slovo ukladám iden. číslo a skratku jedla
    if ktora==2: #podmienka, ktorou kontrolujem hodnotu ktora
        if kod!='': #podmienka, ktorou zisťujem či bol zadaný kód
            slovo=kod+' '+'c' #do tex. premennej slovo ukladám iden. číslo a skratku jedla
    if ktora==3: #podmienka, ktorou kontrolujem hodnotu ktora
        if kod!='': #podmienka, ktorou zisťujem či bol zadaný kód
            slovo=kod+' '+'m' #do tex. premennej slovo ukladám iden. číslo a skratku jedla
    if ktora==4: #podmienka, ktorou kontrolujem hodnotu ktora
        if kod!='': #podmienka, ktorou zisťujem či bol zadaný kód
            slovo=kod+' '+'o' #do tex. premennej slovo ukladám iden. číslo a skratku jedla
    subor = open('vyber_jedla.txt', 'a') #otvorím si daný súbor, aby som doňho mohol písať
    subor.write(slovo+'\n') #zapisujem do súboru
    subor.close() #zavriem súbor
    
def zelene(): #funkcia, ktorou určujem aké jedlo si vybral študent
    ktora=1 #nastavím si premennú ktora na 1
    kod=str(entry1.get()) #do premennej kod si uložím kód, ktorý zadám do entry
    ktore(ktora,kod) #volám funkciu ktore s danými parametrami
    
def cervena(): #funkcia, ktorou určujem aké jedlo si vybral študent
    ktora=2 #nastavím si premennú ktora na 2
    kod=str(entry1.get()) #do premennej kod si uložím kód, ktorý zadám do entry
    ktore(ktora,kod) #volám funkciu ktore s danými parametrami
    
def modra(): #funkcia, ktorou určujem aké jedlo si vybral študent
    ktora=3 #nastavím si premennú ktora na 3
    kod=str(entry1.get()) #do premennej kod si uložím kód, ktorý zadám do entry
    ktore(ktora,kod) #volám funkciu ktore s danými parametrami
    
def oranzova(): #funkcia, ktorou určujem aké jedlo si vybral študent
    ktora=4 #nastavím si premennú ktora na 4
    kod=str(entry1.get()) #do premennej kod si uložím kód, ktorý zadám do entry
    ktore(ktora,kod) #volám funkciu ktore s danými parametrami
    
frame1 = tkinter.Frame() #pripravím si obdĺžnik
frame1.place(x=10, y=120) #umiestnim si ho na dané súradnice
button1 = tkinter.Button(frame1, width=27, height=13, bg='green', command=zelene) #nastavím si veľkosť obdĺžnika,farbu a funkciu, ktorú má volať
button1.pack() #vytvorím si obdĺžnik

frame2 = tkinter.Frame() #pripravím si obdĺžnik
frame2.place(x=220, y=120) #umiestnim si ho na dané súradnice
button2 = tkinter.Button(frame2, width=27, height=13, bg='red', command=cervena) #nastavím si veľkosť obdĺžnika,farbu a funkciu, ktorú má volať
button2.pack() #vytvorím si obdĺžnik

frame3 = tkinter.Frame() #pripravím si obdĺžnik
frame3.place(x=430, y=120) #umiestnim si ho na dané súradnice
button3 = tkinter.Button(frame3, width=27, height=13, bg='blue', command=modra) #nastavím si veľkosť obdĺžnika,farbu a funkciu, ktorú má volať
button3.pack() #vytvorím si obdĺžnik

frame4 = tkinter.Frame() #pripravím si obdĺžnik
frame4.place(x=640, y=120) #umiestnim si ho na dané súradnice
button4 = tkinter.Button(frame4, width=27, height=13, bg='orange', command=oranzova) #nastavím si veľkosť obdĺžnika,farbu a funkciu, ktorú má volať
button4.pack() #vytvorím si obdĺžnik

button5 = tkinter.Button(text='Identifikačné číslo študenta:') #
                                                                #vytvorenie textu nad vstupom ja viem, že sa to dá aj inak, ale mne sa to páči takto
button5.pack(side=tkinter.TOP)                                 #                                

entry1 = tkinter.Entry() #pripravím si vstup
entry1.pack() #vytvorím si vstup