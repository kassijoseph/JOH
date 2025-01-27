from tkinter import *
from tkinter import messagebox,ttk
import sqlite3

class Produit:
    def __init__(self, root):
        self.root = root
        self.root.title("Produit")
        self.root.geometry("1050x555+302+140")
        self.root.config(bg="white")
        self.root.focus_force()

        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS produit(pid INTEGER PRIMARY KEY, Categorie text, Fournisseur text, Nom text, Prix text, Quantite text, Status text)")
        con.commit()

        ##### les variables

        self.var_recherche_type_txt = StringVar()
        self.var_recherche = StringVar()
        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_fourn = StringVar()
        self.var_nom = StringVar()
        self.var_prix = StringVar()
        self.var_qte = StringVar()
        self.var_status = StringVar()

        self.four_liste = []
        self.liste_four()

        product_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        product_frame.place(x=10, y=10, height=455, width=450)

        titre = Label(product_frame, text="Detail Produit", font=("goudy old style", 15), bg="cyan").pack(side=TOP, fill=X)

        lbl_categorie = Label(product_frame, text="Categorie", font=("goudy old style", 20), bg="white").place(x=20, y=70)
        lbl_fournisseur = Label(product_frame, text="Fournisseur", font=("goudy old style" , 20), bg="white").place(x=20, y=120)
        lbl_nomproduit = Label(product_frame, text="Nom", font=("goudy old style" , 20), bg="white").place(x=20 , y=170)
        lbl_prixe = Label(product_frame, text="Prix", font=("goudy old style" , 20), bg="white").place(x=20 , y=220)
        lbl_quantite = Label(product_frame, text="Quantité", font=("goudy old style" , 20), bg="white").place(x=20 , y=270)
        lbl_status = Label(product_frame, text="Status", font=("goudy old style" , 20), bg="white").place(x=20 , y=320)

        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        cur.execute("select nom from categorie")
        rows = cur.fetchall()

        txt_categorie = ttk.Combobox(product_frame, values= rows, state="r", textvariable=self.var_cat, justify=CENTER, font=("goudy old style", 18))
        txt_categorie.place(x=200, y=70, width=200)
        txt_categorie.set("Select")

        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        cur.execute("select nom from fournisseur")
        rows = cur.fetchall()

        txt_fournisseur = ttk.Combobox(product_frame, values=self.four_liste, state="r", textvariable=self.var_fourn, justify=CENTER, font=("goudy old style" , 18))
        txt_fournisseur.place(x=200, y=120, width=200)
        txt_fournisseur.current(0)

        txt_nom = Entry(product_frame, font=("goudy old style", 20), textvariable=self.var_nom, bg="lightyellow").place(x=200, y=170, width=200)
        txt_quantite = Entry(product_frame, font=("goudy old style", 20), textvariable=self.var_qte, bg="lightyellow").place(x=200, y=220, width=200)
        txt_prix = Entry(product_frame, font=("goudy old style", 20), textvariable=self.var_prix, bg="lightyellow").place(x=200, y=275, width=200)

        txt_status = ttk.Combobox(product_frame, values=("Active", "Inative"), textvariable=self.var_status, state="r", justify=CENTER, font=("goudy old style" , 18))
        txt_status.place(x=200, y=320, width=200)
        txt_status.current(0)

        ##### boutons

        self.btn_ajout = Button(product_frame , text="Ajouter", command=self.ajouter, state="normal" ,font=("goudy old style" , 20 , "bold") , cursor="hand2" , bg="green")
        self.btn_ajout.place(x=80 , y=370 , height=30)

        self.btn_modifier = Button(product_frame, text="Modifier", command=self.modifier, state="disabled", font=("goudy old style" , 20 , "bold"), cursor="hand2" , bg="yellow")
        self.btn_modifier.place(x=250, y=370, height=30)

        self.btn_supprimer = Button(product_frame, text="Supprimer", command=self.Supprimer, state="disabled", font=("goudy old style", 20, "bold"), cursor="hand2" , bg="red")
        self.btn_supprimer.place(x=80, y=420 , height=30)

        self.btn_reinitialise = Button(product_frame, text="Renitialiser", command=self.reini, state="normal", font=("goudy old style", 20, "bold"), cursor="hand2" , bg="gray")
        self.btn_reinitialise.place(x=250, y=420, height=30)

        ####Frame recherche

        reche_Frame = LabelFrame(self.root, text="Recherche Produit", font=("goudy old style", 20, "bold"), bd=2, relief=RIDGE, bg="white", fg="black")
        reche_Frame.place(x=470, y=0, width=550, height=70)

        ####option de recherche

        reche_option = ttk.Combobox(reche_Frame, textvariable=self.var_recherche, values=("Categorie", "Fournisseur","Nom",), font=("times new roman", 15), state="r", justify=CENTER)
        reche_option.current(0)
        reche_option.place(x=10, y=0, width=150)

        reche_txt = Entry(reche_Frame, font=("times new roman", 15), textvariable=self.var_recherche_type_txt, bg="lightyellow",).place(x=170, y=0, width=150)

        recherche = Button(reche_Frame, text="Recherche", command=self.Rechercher, font=("times new roman",20), cursor="hand2", bg="blue", fg="white").place(x=330, y=0, width=120, height=30)
        Tous = Button(reche_Frame, text="Tous", command=self.afficher, font=("times new roman", 20), cursor="hand2", bg="lightgray" ,fg="black").place(x=460, y=0, height=30)

 ######### listes des produits

        listeFrame = Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=459, y=70, height=503, width=580)
        scroll_y = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.produitliste = ttk.Treeview(listeFrame, columns=("pid", "Categorie", "Fournisseur", "Nom", "Prix", "Quantite", "Status"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.config(command=self.produitliste.xview)
        scroll_y.config(command=self.produitliste.yview)

        self.produitliste.heading("pid", text="ID", anchor="w")
        self.produitliste.heading("Categorie", text="Categorie", anchor="w")
        self.produitliste.heading("Fournisseur", text="Fournisseur", anchor="w")
        self.produitliste.heading("Nom", text="Nom", anchor="w")
        self.produitliste.heading("Prix", text="Prix", anchor="w")
        self.produitliste.heading("Quantite", text="Quantite", anchor="w")
        self.produitliste.heading("Status", text="Status", anchor="w")

        self.produitliste["show"] = "headings"
        self.produitliste.pack(fill=BOTH, expand=1)
        self.produitliste.bind("<ButtonRelease-1>", self.get_donne)
        self.afficher()

    def liste_four(self):
        self.four_liste.append("Vide")
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try :
            cur.execute("select nom from fournisseur")
            fournisseurs = cur.fetchall()
            if len(fournisseurs) > 0 :
                self.four_liste = ["Select"] + [fournisseur[0] for fournisseur in fournisseurs]

        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    ####les fonctions
    def ajouter(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_fourn.get()=="Select" or self.var_nom.get()=="":
                messagebox.showerror("Erreur", "Veuillez saisir les obligatoire")
            else:
                cur.execute("select * from produit WHERE Nom=?" , (self.var_nom.get() ,))
                row = cur.fetchone()
                if row != None :
                    messagebox.showerror("Erreur" , "Le Produit existe déjà")
                else :
                    cur.execute("insert into produit(Categorie, Fournisseur, Nom, Quantite, Prix, Status) values (?,?,?,?,?,?)",(
                        self.var_cat.get(),
                        self.var_fourn.get(),
                        self.var_nom.get(),
                        self.var_prix.get(),
                        self.var_qte.get(),
                        self.var_status.get()
                    ))
                    con.commit()
                    self.afficher()
                    messagebox.showinfo("Succès", "Ajout effectué avec succès")

        except Exception as ex:
            messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

    def afficher(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            cur.execute("select * from produit")
            rows = cur.fetchall()
            self.produitliste.delete(*self.produitliste.get_children())
            for row in rows:
                self.produitliste.insert("", END, values=row)

        except Exception as ex:
          messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def get_donne(self, ev):
        self.btn_ajout.config(state="disabled")
        self.btn_modifier.config(state="normal")
        self.btn_supprimer.config(state="normal")
        r = self.produitliste.focus()
        if r:
            contenu = self.produitliste.item(r)
            row = contenu["values"]
            if row:
                self.var_pid.set(row[0])
                self.var_cat.set(row[1])
                self.var_fourn.set(row[2])
                self.var_nom.set(row[3])
                self.var_qte.set(row[4])
                self.var_prix.set(row[5])
                self.var_status.set(row[6])

    def modifier(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()

        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Erreur", "Selection un ID")
            else:
                cur.execute("Select * from produit where pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Erreur", "Veillez selectionner un produit sur la liste")
                else:
                    cur.execute("update produit set Categorie=?, Fournisseur=?, Nom=?, Prix=?, Quantite=?, Status=? WHERE pid=?",(
                        self.var_cat.get(),
                        self.var_fourn.get(),
                        self.var_nom.get(),
                        self.var_qte.get() ,
                        self.var_prix.get(),
                        self.var_status.get(),
                        self.var_pid.get()
                    ))
                    con.commit()
                    self.afficher()
                    self.reini()
                    messagebox.showinfo("Succes", "Modification éffectuée")
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def Supprimer(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            op = messagebox.askyesno("Confirmation" , "Voulez-vous vraiment Supprimer?")
            if op == True :
                cur.execute("delete from produit WHERE pid=?" , (self.var_pid.get() ,))
                con.commit()
                self.afficher()
                self.reini()
                messagebox.showinfo("Succes" , "Suppression effectué")
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def reini(self):

        self.btn_ajout.config(state="normal")
        self.btn_modifier.config(state="disabled")
        self.btn_supprimer.config(state="disabled")
        self.var_pid.set("")
        self.var_cat.set("Select")
        self.var_fourn.set("Select")
        self.var_nom.set("")
        self.var_prix.set("")
        self.var_qte.set("")
        self.var_status.set("Active")
        self.var_recherche_type_txt.set("")

    def Rechercher(self) :
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            if self.var_recherche_type_txt.get() == "":
                messagebox.showerror("Erreur", "Qu'est-ce que vous recherchez?")
            else:
                cur.execute("SELECT * FROM produit WHERE " + self.var_recherche.get() + " LIKE '%" + self.var_recherche_type_txt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) !=0:
                   self.produitliste.delete(*self.produitliste.get_children())
                   for row in rows :
                       self.produitliste.insert("" , END , values=row)
                else:
                    messagebox.showerror("Erreur", "Aucun résultat trouvé")

        except Exception as ex:
          messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = Produit(root)
    root.mainloop()