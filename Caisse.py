from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox,ttk
import time
import sqlite3
import tempfile

class Caisse:
    def __init__(self, root):
        self.root = root
        self.root.title("Caisse")
        self.root.geometry("1820x1010+0+0")
        self.root.config(bg="white")

        self.cart_liste = []
        self.ck_print = 0

        titre = Label(self.root, text="Caisse du super marche st joseph", font=("Algerian", 44, "bold"), bg="cyan", fg="black")
        titre.place(x=0, y=0, width=1390)

        self.cat2 = Image.open( r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\images\im3.jpg")
        self.cat2 = self.cat2.resize((150, 80), Image.LANCZOS)
        self.cat2 = ImageTk.PhotoImage(self.cat2)

        self.lbl_ima_cat2 = Label(self.root, bd=2, relief=RAISED, image=self.cat2 , bg="cyan")
        self.lbl_ima_cat2.place(x=0, y=0, height=70)

        # buton deconnecter
        btn_deconnecter = Button(self.root, text="Deconnecter", command=self.Deconnecter, font=("times new roman", 15, "bold"), cursor="hand2", bg="orange").place(x=1240, y=10, width=115, height=40)

        # heure
        self.lbl_heure = Label(self.root, text="Bienvenue Super au sur marche st joseph kassi\t\t Date : DD-MM-YYYY\t\t Heure : HH:MM:SS" ,font=("times new roman", 15), bg="black" , fg="white")
        self.lbl_heure.place(x=0, y=70, relwidth=1, height=40)
        self.modifier_heure()

        ###les produits

        self.var_recherche = StringVar()

        product_frame1 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        product_frame1.place(x=10, y=110, height=580, width=560)

        titre = Label(product_frame1, text="Tous les  Produits", font=("goudy old style" , 15) , bg="cyan").pack(side=TOP, fill=X)

        product_frame2 = Frame(product_frame1, bd=3 , relief=RIDGE , bg="white")
        product_frame2.place(x=5 , y=35 , height=150 , width=546)

        lbl_recherche = Label(product_frame2, text="Recherche Produit | Par Nom ", font=("goudy old style", 15, "bold"), bd=2, relief=RIDGE, bg="green", fg="white").place(x=10, y=10, width=260, height=30)
        lbl_nom = Label(product_frame2, text=" Nom du Produit", font=("goudy old style", 15, "bold"), bg="white", fg="black").place(x=0, y=50, width=150, height=30)
        txt_recherche = Entry(product_frame2, textvariable=self.var_recherche, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=50, width=190, height=30)
        recherche = Button(product_frame2, text="Recherche", command=self.Rechercher, font=("times new roman", 15), cursor="hand2", bg="blue", fg="white").place(x=345, y=50, width=110, height=30)
        btn_tous = Button(product_frame2, text="Tous", command=self.afficher, font=("times new roman", 15), cursor="hand2", bg="gray", fg="white").place(x=460, y=50, width=70, height=30)

        ######### listes des produits

        produitframe3 = Frame(self.root , bd=3 , relief=RIDGE)
        produitframe3.place(x=15 , y=250 , height=400 , width=550)
        scroll_y = Scrollbar(produitframe3 , orient=VERTICAL)
        scroll_y.pack(side=RIGHT , fill=Y)

        scroll_x = Scrollbar(produitframe3 , orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM , fill=X)

        self.produit_table = ttk.Treeview(produitframe3, columns=("pid", "Nom" , "Prix" , "Quantite" , "Status") , yscrollcommand=scroll_y.set ,xscrollcommand=scroll_x.set)
        scroll_x.config(command=self.produit_table.xview)
        scroll_y.config(command=self.produit_table.yview)

        self.produit_table.heading("pid" , text="ID", anchor="w")
        self.produit_table.heading("Nom", text="Nom", anchor="w")
        self.produit_table.heading("Prix", text="Prix", anchor="w")
        self.produit_table.heading("Quantite", text="Quantite", anchor="w")
        self.produit_table.heading("Status", text="Status", anchor="w")

        self.produit_table["show"] = "headings"

        self.produit_table.pack(fill=BOTH , expand=1)

        self.produit_table.bind("<ButtonRelease-1>", self.get_donne)

        self.afficher()

        ####note

        lbl_note = Label(product_frame1, text="Note : Entrer 0 quantite pour retirer le produit du panier", anchor="w", font=("times new roman", 15), bg="white", fg="red").pack(side=BOTTOM, fill=X)

        #####frame client et les variables

        self.var_nom = StringVar()
        self.var_contact = StringVar()

        client_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        client_frame.place(x=570, y=110, height=70, width=430)

        titre = Label(client_frame, text="Detail du Client", font=("goudy old style", 15), bg="yellow").pack(side=TOP, fill=X)

        lbl_nom = Label(client_frame, text="Nom", font=("goudy old style", 15), bg="white").place(x=0, y=30)
        txt_nom = Entry(client_frame,textvariable=self.var_nom, font=("goudy old style", 15), bg="lightyellow").place(x=45, y=35, width=150)

        lbl_contact = Label(client_frame , text="Contact" , font=("goudy old style" , 15) , bg="white").place(x=195 , y=30)
        txt_contact = Entry(client_frame, textvariable=self.var_contact, font=("goudy old style" , 15) , bg="lightyellow").place(x=265 , y=35 , width=150)

        #################Machine calcul
        self.var_cal_input = StringVar()

        Cal_cart_Frame = Frame(self.root , bd=2 , bg="white" , relief=RIDGE)
        Cal_cart_Frame.place(x=565 , y=185 , width=435 , height=410)

        CalFrame = Frame(Cal_cart_Frame , bd=2 , bg="white" , relief=RIDGE)
        CalFrame.place(x=5 , y=5 , width=205, height=410)

        self.var_cal_input = Entry(CalFrame , textvariable=self.var_cal_input, font=("goudy old style" , 20), justify=RIGHT, bd=2, relief=RAISED, bg="white")
        self.var_cal_input.pack(side=TOP, fill=X)

        btn_7 = Button(CalFrame, text="7",font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input(7)).place(x=0 , y=40 , height=95 , width=50)
        btn_8 = Button(CalFrame , text="8" , font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input(8)).place(x=50 , y=40, height=95 , width=50)
        btn_9 = Button(CalFrame , text="9" ,font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input(9)).place(x=100 , y=40 ,height=95 , width=50)
        btn_addition = Button(CalFrame , text="+",font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input("+")).place(x=150 , y=40 , height=95 , width=50)

        btn_4 = Button(CalFrame , text="4",font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input(4)).place(x=0 , y=130 , height=95 , width=50)
        btn_5 = Button(CalFrame , text="5",font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input(5)).place(x=50 , y=130 , height=95 , width=50)
        btn_6 = Button(CalFrame , text="6",font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input(6)).place(x=100 , y=130 , height=95 , width=50)
        btn_mul = Button(CalFrame , text="*",font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input("*")).place(x=150 , y=130 , height=95 , width=50)

        btn_1 = Button(CalFrame , text="1" , font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input(1)).place(x=0 , y=220 , height=95 , width=50)
        btn_2 = Button(CalFrame , text="2" ,font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input(2)).place(x=50 , y=220 , height=95 , width=50)
        btn_3 = Button(CalFrame , text="3",font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input(3)).place(x=100 , y=220 , height=95 , width=50)
        btn_soustr = Button(CalFrame , text="-",font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input("-")).place(x=150 , y=220 , height=95 , width=50)

        btn_0 = Button(CalFrame , text="0",font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input(0)).place(x=0 , y=310 , height=95, width=50)
        btn_c = Button(CalFrame , text="C" , font=("time new roman" , 15 , "bold"), bg="gray", command=self.clear_cal).place(x=50 ,y=310 ,height=95 ,width=50)
        btn_egal = Button(CalFrame , text="=", font=("time new roman" , 15 , "bold"), bg="gray", command=self.resultat).place(x=150, y=310 , height=95 ,width=50)
        btn_div = Button(CalFrame , text="/" , font=("time new roman" , 15 , "bold"), bg="gray", command=lambda:self.get_input("/")).place(x=100 , y=310, height=95 , width=50)

        Cart_Frame = Frame(Cal_cart_Frame , bd=2 , bg="white" , relief=RIDGE)
        Cart_Frame.place(x=210 , y=30 , width=220 , height=375)

        self.lbl_titre = Label(Cal_cart_Frame, text="Produit Total du Panier:[0]", font=("goudy old style", 14), bg="yellow")
        self.lbl_titre.place(x=210, y=0)

        scroll_y = Scrollbar(Cart_Frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT , fill=Y)


        scroll_x = Scrollbar(Cart_Frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM , fill=X)

        self.CartTable = ttk.Treeview(Cart_Frame, columns=("pid", "Nom" , "Prix" , "Quantite" , "Status"), yscrollcommand=scroll_y.set , xscrollcommand=scroll_x.set)

        scroll_x.config(command=self.CartTable.xview)
        scroll_y.config(command=self.CartTable.yview)

        self.CartTable.heading("pid" , text="ID" , anchor="w")
        self.CartTable.heading("Nom" , text="Nom" , anchor="w")
        self.CartTable.heading("Prix" , text="Prix" , anchor="w")
        self.CartTable.heading("Quantite" , text="Quantite" , anchor="w")
        self.CartTable.heading("Status" , text="Status", anchor="w")

        self.CartTable["show"] = "headings"

        self.CartTable.pack(fill=BOTH, expand=1)

        self.CartTable.bind("<ButtonRelease-1>", self.get_donne_cart)

        ####ajoute panier

        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_prix = StringVar()
        self.var_qte = StringVar()
        self.var_stock = StringVar()

        button_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        button_frame.place(x=570, y=600, height=100, width=750)

        lbl_p_nom = Label(button_frame, text="Nom du Produit", font=("goudy old style", 15), bg="white").place(x=155, y=0)
        txt_p_nom = Entry(button_frame, font=("goudy old style", 15), textvariable=self.var_pname, bg="lightyellow", state="r").place(x=160, y=30, width=180)

        lbl_p_prix = Label(button_frame , text="Prix Produit" , font=("goudy old style" , 15) , bg="white").place(x=380 , y=0)
        txt_p_prix = Entry(button_frame , font=("goudy old style" , 15) , textvariable=self.var_prix , bg="lightyellow" ,state="r").place(x=360 , y=30 , width=180)

        lbl_p_qte = Label(button_frame , text="Quantite du Produit" , font=("goudy old style" , 15) , bg="white").place(x=550 , y=0)
        txt_p_qte = Entry(button_frame , font=("goudy old style" , 15), textvariable=self.var_qte,  bg="lightyellow" , ).place(x=550 , y=30 , width=180)

        self.lbl_p_stock = Label(button_frame , text="En Stock", font=("goudy old style" , 18), bg="white")
        self.lbl_p_stock.place( x=0 , y=55)

        btn_ajout_modif = Button(button_frame , text="Ajouter | Modifier", command=self.ajout_modifier, font=("goudy old style" , 15) , bg="yellow").place(x=550 , y=60, height=35)

        btn_reini = Button(button_frame , text="Reinitiliser", command=self.clear_cart, font=("goudy old style" , 15), bg="gray" ).place(x=300 , y=60 , width=150, height=35)

        ###zone facture

        fact_frame = Frame(self.root , bd=4 , relief=RIDGE , bg="white")
        fact_frame.place(x=1000 , y=110 , height=380 , width=355)

        lbl_titre = Label(fact_frame, text="Zone de Facture Client", font=("goudy old style", 15), bg="lightblue", bd=3, relief=RIDGE).pack(side=TOP, fill=X)

        scroll_y = Scrollbar(fact_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.txt_space_fact = Text(fact_frame, yscrollcommand = scroll_y.set)
        self.txt_space_fact.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_space_fact.yview)

        ####"les boutons

        FactMenuframe = Frame(self.root, bd=4 , relief=RIDGE , bg="white")
        FactMenuframe.place(x=1000 , y=490 , height=110 , width=355)

        self.lbl_montantfact = Label(FactMenuframe , text="Montant Facture \n[0]" , bd=2, bg="blue" , relief=RAISED ,fg="white" , font=("goudy old style" , 13, "bold"))
        self.lbl_montantfact.place(x=0 , y=0 , height=50 , width=125)

        self.lbl_remise = Label(FactMenuframe , text="Remise\n[0]" , bd=2 , bg="lightgreen" , relief=RAISED , fg="white" , font=("goudy old style" , 13, "bold"))
        self.lbl_remise.place(x=133 , y=0 , height=50 , width=100)

        self.lbl_netpaye = Label(FactMenuframe , text="Net à Payer \n[0]" , bd=2 , bg="gray" , relief=RAISED ,fg="white" , font=("goudy old style" , 13, "bold"))
        self.lbl_netpaye.place(x=240 , y=0 , height=50 , width=100)

        btn_imprimer = Button(FactMenuframe, text="Imprimer", command=self.imprimer_facture, font=("goudy old style" , 15), bg="yellow" ).place(x=0 , y=55, width=90)

        btn_reini = Button(FactMenuframe, text="Reinitiliser Tous", command=self.clear_all, font=("goudy old style" , 15), bg="lightgray" ).place(x=95 , y=55 , width=150)

        btn_generer = Button(FactMenuframe , text="Generer", command=self.generer_facture, font=("goudy old style" , 15), bg="green" ).place(x=250 , y=55 , width=90)

        ### footer

        lbl_footer = Label(self.root ,text="Developper par Joseph KASSI\t\t kassi8362@gmail.com\t\t +2250700695327/+2250546694409\n@Copyright 2023" ,font=("times new roman, " , 10) , bg="black" , fg="white").pack(pady=10 , side=BOTTOM , fill=X)

    ########Fonctions
    def get_input(self , num) :
        current_input = self.var_cal_input.get()
        new_input = current_input + str(num)
        self.var_cal_input.delete(0 , "end")
        self.var_cal_input.insert(0 , new_input)

    def clear_cal(self) :
        self.var_cal_input.delete(0 , "end")

    def resultat(self) :
        try :
            expression = self.var_cal_input.get()
            result = eval(expression)
            self.var_cal_input.delete(0 , "end")
            self.var_cal_input.insert(0 , result)
        except Exception as e :
            print("Erreur de calcul :" , e)

    def afficher(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            cur.execute("select  pid, Nom, Prix, Quantite, Status FROM produit WHERE Status='Active'")
            rows = cur.fetchall()
            self.produit_table.delete(*self.produit_table.get_children())
            for row in rows:
                self.produit_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def Rechercher(self) :
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try :
            if self.var_recherche.get() == "" :
                messagebox.showerror("Erreur" , "Saisir le Produit à rechercher")
            else :
                cur.execute("SELECT pid, Nom, Prix, Quantite, Status FROM produit WHERE Nom LIKE'%"+self.var_recherche.get()+"%' and Status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0 :
                    self.produit_table.delete(*self.produit_table.get_children())
                    for row in rows :
                        self.produit_table.insert("" , END , values=row)
                else :
                    messagebox.showerror("Erreur" , "Aucun résultat trouvé")

        except Exception as ex :
            messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

    def get_donne(self, ev) :
        r = self.produit_table.focus()
        contenu = self.produit_table.item(r)
        row = contenu["values"]
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_prix.set(row[2])
        self.lbl_p_stock.config(text=f"En Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qte.set(1)

    def get_donne_cart(self, ev) :
        r = self.CartTable.focus()
        contenu = self.CartTable.item(r)
        row = contenu["values"]
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_prix.set(row[2])
        self.var_qte.set(row[3])
        self.lbl_p_stock.config(text=f"En Stock [{str(row[4])}]")
        self.var_stock.set(row[4])

    def ajout_modifier(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Erreur", "Selection un produit")
        elif self.var_qte.get()=="":
            messagebox.showerror("Erreur", "Donnez la quantite" )
        elif int(self.var_qte.get()) > int(self.var_stock.get()):
            messagebox.showerror("Erreur", "La quantité n'est pas disponible")
        else:
            prix_cal = self.var_prix.get()
            cart_donne = [self.var_pid.get(), self.var_pname.get(), self.var_prix.get(), self.var_qte.get(), self.var_stock.get()]

            present = "non"
            index_ = 0
            for row in self.cart_liste:
                if self.var_pid.get()==row[0]:
                    present = "oui"
                    break
                index_+=1

            if present =="oui":
                op = messagebox.askyesno("Confirmer", "Le produit est déjà présent \nVoulez-vous vraiment modifier | Supprimer de la liste ?" )
                if op==True:
                    if self.var_qte.get()=="0":
                        self.cart_liste.pop(index_)
                    else:
                        self.cart_liste[index_][3]=self.var_qte.get()
            else:
                self.cart_liste.append(cart_donne)
            self.afficher_cart()
            self.facture_modifier()

    def afficher_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_liste:
                self.CartTable.insert("",END, values=row)
        except Exception as ex:
            messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

    def facture_modifier(self):
        self.montant_facture = 0
        self.net_payer = 0
        self.remise = 0
        for row in self.cart_liste:
            self.montant_facture = self.montant_facture+(float(row[2])*int(row[3]))

        self.remise = (self.montant_facture * 0.2)/100
        self.net_payer = self.montant_facture-self.remise

        self.lbl_montantfact.config(text=f"Montant Facture \n [{str(self.montant_facture)}]")
        self.lbl_netpaye.config(text=f"Net à Payer \n[{str(self.net_payer)}]")
        self.lbl_remise.config(text=f"Remise \n[{str(self.remise)}]")
        self.lbl_titre.config(text=f"Produit Total du Panier : [{str(len(self.cart_liste))}]")

    def generer_facture(self):
        if self.var_nom.get()=="":
            messagebox.showerror("Erreur" , "Saisir le nom du client")
        elif len(self.cart_liste)==0:
            messagebox.showerror("Erreur" , "Ajouter des produits dans le panier")
        else:
            self.enente_facture()
            self.corp_facture()
            self.footer_facture()

            fp = open(fr"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Facture\{str(self.facture)}.txt", "w")
            fp.write(self.txt_space_fact.get("1.0", "end-1c"))
            fp.close()
            messagebox.showinfo("Sauvegarder", "Enregistrement/Génération effectué avec succès")
            self.ck_print = 1

    def enente_facture(self):
        self.facture = int(time.strftime("%H%M%S") + time.strftime("%d%m%y"))
        facture_ente = f'''
Magasin JOSEPH KASSI 
Tel : +225 0700695327 
Adresse: Abidjan yop Niangon Cite CEI
{str("m" * 40)}
Nom du Client : {self.var_nom.get()}
Tel du Client : {self.var_contact.get()}
Numero Facture : {str(self.facture)}
Date: {str(time.strftime("%d-%m-%Y"))} à \t{str(time.strftime("%H:%M:%S"))}

{str("m" * 40)}
Nom du Produit \t\tquantité\t\tPrix
{str("m" * 40)}
'''
        self.txt_space_fact.delete("1.0", END)
        self.txt_space_fact.insert("1.0", facture_ente)

    def corp_facture(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            for row in self.cart_liste:
                pid = row[0]
                nom = row[1]
                quantite = int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status = "Inactive"
                if int(row[3])!=int(row[4]):
                    status = "Active"

                prix = float(row[2])*float(row[3])
                prix = str(prix)
                self.txt_space_fact.insert(END, "\n"+nom+"\t\t\t"+row[3]+"\t"+ prix)
                cur.execute("update produit set Quantite=?, Status=? WHERE pid=?",(
                    quantite,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.afficher()
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def footer_facture(self):
        facture_footer=f'''
{str("m"*40)}
Montant Facture : \t\t\t {self.montant_facture}
Remise : \t\t\t {self.remise}
Net à payer : \t\t\t {self.net_payer}
{str("m"*40)}
        '''
        self.txt_space_fact.insert(END, facture_footer)
    def clear_cart(self):
        self.var_pid.set("")
        self.var_pname.set("")
        self.var_prix.set("")
        self.var_qte.set("")
        self.lbl_p_stock.config(text=f"En Stock")
        self.var_stock.set("")

    def clear_all(self):
        del self.cart_liste[:]
        self.var_nom.set("")
        self.var_contact.set("")
        self.txt_space_fact.delete("1.0", END)
        self.lbl_titre.config(text=f"Produit Total du Panier:[0]")
        self.var_recherche.set("")
        self.ck_print = 0
        self.clear_cart()
        self.afficher()
        self.afficher_cart()

    def Deconnecter(self) :
        self.root.destroy()
        self.obj = os.system("python C:/Users/Utilisateur/PycharmProjects/MypythonProject3/GESTION_SUPERMACHE/Login.py")

    def modifier_heure(self):
        heure_ = (time.strftime("%H:%M:%S"))
        date_ = (time.strftime("%d-%m-%y"))
        self.lbl_heure.config(text=f"Bienvenue Chez st joseph kassi\t\t Date : {str(date_)}\t\t Heure : {str(heure_)}")
        self.lbl_heure.after(100, self.modifier_heure)

    def imprimer_facture(self):
        if self.ck_print==1:
            messagebox.showinfo("Imprimer", "Veillez patienter pendant l'impression")
            fichier = tempfile.mktemp(".txt")
            open(fichier,"w").write(self.txt_space_fact.get("1.0", END))
            os.startfile(fichier, "print")

        else:
            messagebox.showerror("Erreur", "Veillez générer la facture")

if __name__ == "__main__":
    root = Tk()
    obj = Caisse(root)
    root.mainloop()