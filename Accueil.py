from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time
import sqlite3

class accueil:
    def __init__(self, root):
        self.root = root
        self.root.title("Accueil")
        self.root.geometry("1820x1010+0+0")
        self.root.config(bg="white")

        titre = Label(self.root, text="Gestion Magasin st joseph kassi", font=("Algerian" , 44, "bold") , bg="cyan" ,fg="black")
        titre.place(x=0, y=0, width=1390)

        self.cat2 = Image.open(r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\images\logo.png")
        self.cat2 = self.cat2.resize((170, 65), Image.LANCZOS)
        self.cat2 = ImageTk.PhotoImage(self.cat2)

        self.lbl_ima_cat2 = Label(self.root, bd=2, relief=RAISED, image=self.cat2, bg="cyan")
        self.lbl_ima_cat2.place(x=0, y=0, height=70)

        #buton deconnecter
        btn_deconnecter = Button(self.root, text="Deconnecter", command=self.Deconnecter, font=("times new roman", 15, "bold"), cursor="hand2", bg="orange").place(x=1240, y=10, width=115, height=40)

        #heure
        self.lbl_heure = Label(self.root, text="Bienvenue Chez st joseph kassi\t\t Date : DD-MM-YYYY\t\t Heure : HH:MM:SS", font=("times new roman", 15), bg="black", fg="white")
        self.lbl_heure.place(x=0, y=70,relwidth=1, height=40)

        self.Menu_Frame = Frame(self.root, bd=2, relief=RAISED, bg="white")
        self.Menu_Frame.place(x=0, y=111, width=300, height=580)

        # Menu
        self.menulogo_pil = Image.open("C:/Users/Utilisateur/PycharmProjects/MypythonProject3/GESTION_SUPERMACHE/images/menu.jpg")
        self.menulogo_pil = self.menulogo_pil.resize((300, 200), Image.LANCZOS)
        self.menulogo = ImageTk.PhotoImage(self.menulogo_pil)

        self.lbl_image = Label(image=self.menulogo)
        self.lbl_image.place(x=0, y=112, width=300, height=200)

        self.lbl_menu = Label(self.Menu_Frame, text="Menu", font=("times new roman" , 40) , bg="orange", fg="black")
        self.lbl_menu.place(x=0 , y=185,relwidth=1)

        #boutons
        self.icon_menu = ImageTk.PhotoImage(file=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\images\side.png")

        btn_employe = Button(self.Menu_Frame, text="Employé", command=self.Employe, image = self.icon_menu, padx=10, anchor="w", compound=LEFT, font=("times new roman", 20, "bold"), bg="white", fg="black")
        btn_employe.pack(padx=0, pady=250, side=TOP, fill=X)

        btn_fournisseur = Button(self.Menu_Frame, text="Fournisseur", command=self.Fournisseur,  image = self.icon_menu, padx=10, anchor="w", compound=LEFT, font=("times new roman" , 20 , "bold") , bg="white" ,fg="black")
        btn_fournisseur.place(x=0, y=305, relwidth=1)

        btn_categorie = Button(self.Menu_Frame , text="Categorie", command=self.Categorie,  image = self.icon_menu, padx=10, anchor="w", compound=LEFT, font=("times new roman" , 20 , "bold") , bg="white" ,fg="black")
        btn_categorie.place(x=0 , y=360 , relwidth=1)

        btn_produit = Button(self.Menu_Frame , text="Produits", command=self.Produit,  image = self.icon_menu, padx=10, anchor="w", compound=LEFT, font=("times new roman" , 20 , "bold") , bg="white" ,fg="black")
        btn_produit.place(x=0 , y=415 , relwidth=1)

        btn_vente = Button(self.Menu_Frame , text="Vente", command=self.Vente,  image = self.icon_menu, padx=10, anchor="w", compound=LEFT, font=("times new roman" , 20 , "bold") , bg="white" ,fg="black")
        btn_vente.place(x=0 , y=470 , relwidth=1)

        btn_quitter = Button(self.Menu_Frame , text="Quitter",  image = self.icon_menu, padx=10, anchor="w", compound=LEFT, font=("times new roman" , 20 , "bold") , bg="white" ,fg="black")
        btn_quitter.place(x=0 , y=525 , relwidth=1)

        ## contenu

        self.lbl_totalemploye = Label(self.root, text="Total Employes \n[0]", bd=5,bg="green", relief=RAISED, fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_totalemploye.place(x=350, y=110, height=150, width=300)

        self.lbl_totalfournisseur = Label(self.root , text="Total Fournisseurs \n[0]" , bd=5 , bg="red" , relief=RAISED ,fg="white" , font=("goudy old style" , 20 , "bold"))
        self.lbl_totalfournisseur.place(x=700 , y=110 , height=150 , width=300)

        self.lbl_totalcategorie = Label(self.root , text="Total Categorie \n[0]" , bd=5 , bg="gold" , relief=RAISED ,fg="white" , font=("goudy old style" , 20 , "bold"))
        self.lbl_totalcategorie.place(x=1050 , y=110 , height=150 , width=300)

        self.lbl_totalproduit = Label(self.root , text="Total Produits \n[0]" , bd=5 , bg="gray" , relief=RAISED ,fg="white" , font=("goudy old style" , 20 , "bold"))
        self.lbl_totalproduit.place(x=350, y=270 , height=150 , width=300)

        self.lbl_totalvente = Label(self.root , text="Total Ventes \n[0]" , bd=5 , bg="blue" , relief=RAISED , fg="white" , font=("goudy old style" , 20 , "bold"))
        self.lbl_totalvente.place(x=700 , y=270 , height=150 , width=300)

        self.modifier()
        ### footer

        lbl_footer = Label(self.root, text="Developper par Joseph KASSI\t\t kassi8362@gmail.com\t\t +2250700695327/+2250546694409\n@Copyright 2023", font=("times new roman, ", 13), bg="black", fg="white").pack(pady=10, side=BOTTOM, fill=X)

    ##############Fonctions

    def Employe(self):
        self.obj = os.system("python C:/Users/Utilisateur/PycharmProjects/MypythonProject3/GESTION_SUPERMACHE/employe.py")

    def Categorie(self):
        self.obj = os.system("python C:/Users/Utilisateur/PycharmProjects/MypythonProject3/GESTION_SUPERMACHE/Categorie.py")

    def Fournisseur(self):
        self.obj = os.system("python C:/Users/Utilisateur/PycharmProjects/MypythonProject3/GESTION_SUPERMACHE/Fournisseur.py")

    def Produit(self):
        self.obj = os.system("python C:/Users/Utilisateur/PycharmProjects/MypythonProject3/GESTION_SUPERMACHE/Produit.py")

    def Vente(self):
        self.obj = os.system("python C:/Users/Utilisateur/PycharmProjects/MypythonProject3/GESTION_SUPERMACHE/Vente.py")

    def quitter(self):
        self.root.destroy()

    def Deconnecter(self):
        self.root.destroy()
        self.obj = os.system("python C:/Users/Utilisateur/PycharmProjects/MypythonProject3/GESTION_SUPERMACHE/Login.py")

    def modifier(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            cur.execute("select*from produit")
            produit = cur.fetchall()
            self.lbl_totalproduit.config(text=f"Total Produits \n[{str(len(produit))}]")

            cur.execute("select*from categorie")
            categorie = cur.fetchall()
            self.lbl_totalcategorie.config(text=f"Total Categorie \n[{str(len(categorie))}]")

            cur.execute("select*from fournisseur")
            fournisseur = cur.fetchall()
            self.lbl_totalfournisseur.config(text=f"Total Fournisseurs \n[{str(len(fournisseur))}]")

            cur.execute("select*from employe")
            employe = cur.fetchall()
            self.lbl_totalemploye.config(text=f"Total Employes \n[{str(len(employe))}]")

            nombre_facture = len(os.listdir(r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Facture"))
            self.lbl_totalvente.config(text=f"Total Ventes \n[{str(nombre_facture)}]")

            heure_ = (time.strftime("%H:%M:%S"))
            date_ = (time.strftime("%d-%m-%y"))
            self.lbl_heure.config(text=f"Bienvenue Chez st joseph kassi\t\t Date : {str(date_)}\t\t Heure : {str(heure_)}")
            self.lbl_heure.after(100 , self.modifier)

        except Exception as ex:
            messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = accueil(root)
    root.mainloop()
