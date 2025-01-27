from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox,ttk
import sqlite3

class Categorie:
    def __init__(self, root):
        self.root = root
        self.root.title("Categorie")
        self.root.geometry("1050x555+302+140")
        self.root.config(bg="white")
        self.root.focus_force()

        ##### les variables

        self.var_cat_cid = StringVar()
        self.var_cat_nom = StringVar()

        ####base de donnee
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS categorie(cid INTEGER PRIMARY KEY AUTOINCREMENT, nom text)")
        con.commit()

        ##### Titre

        titre = Label(self.root, text="Gestion de Categorie", font=("times new roman", 20), cursor="hand2", bg="cyan", fg="black").place(x=0, y=10, width=1050)

        #####contenu

        lbl_categorie = Label(self.root , text="Saisir Categorie Produit", font=("goudy old style", 15), bg="white").place(x=20, y=130)
        self.txt_categorie = Entry(self.root, textvariable=self.var_cat_nom, font=("goudy old style", 15), bg="lightyellow")
        self.txt_categorie.place(x=20, y=158)

        self.btn_ajout = Button(self.root, text="Ajouter", command=self.ajouter, font=("goudy old style", 20, "bold"), cursor="hand2", bg="green")
        self.btn_ajout.place(x=240, y=150, height=35)


        self.btn_supprimer = Button(self.root , text="Supprimer", command=self.Supprimer,  font=("goudy old style", 20 , "bold") , cursor="hand2" , bg="red")
        self.btn_supprimer.place(x=360, y=150, height=35)

        #### listes des categorie

        listeFrame = Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=500, y=50, height=185, width=540)
        scroll_y = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.categorieliste = ttk.Treeview(listeFrame, column=("cid", "nom"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.config(command=self.categorieliste.xview)
        scroll_y.config(command=self.categorieliste.yview)

        self.categorieliste.heading("cid", text="ID")
        self.categorieliste.heading("nom", text="Nom")

        self.categorieliste["show"]="headings"
        self.categorieliste.bind("<ButtonRelease-1>", self.get_donne)
        self.categorieliste.pack(fill=BOTH, expand=1)
        self.affficher()
        self.get_donne(None)

    def get_donne(self, ev):
        r = self.categorieliste.focus()
        if r:
            contenu = self.categorieliste.item(r)
            row = contenu["values"]
            if row :
                self.var_cat_cid.set(row[0])
                self.var_cat_nom.set(row[1])
        #####IM1

        self.cat1 = Image.open(r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\images\cat1.png")
        self.cat1 = self.cat1.resize((495,365), Image.LANCZOS)
        self.cat1 = ImageTk.PhotoImage(self.cat1)

        self.lbl_ima_cat1 = Label(self.root, bd=2, relief=RAISED, image=self.cat1)
        self.lbl_ima_cat1.place(x=0, y=185)

        ###IM2

        self.cat2 = Image.open( r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\images\cat2.jpg")
        self.cat2 = self.cat2.resize((535, 315), Image.LANCZOS)
        self.cat2 = ImageTk.PhotoImage(self.cat2)

        self.lbl_ima_cat2 = Label(self.root, bd=2, relief=RAISED, image=self.cat2)
        self.lbl_ima_cat2.place(x=500, y=235)

    def ajouter(self):
            con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
            cur = con.cursor()
            try:
                if self.var_cat_nom.get() =="":
                    messagebox.showerror("Erreur", "Veuillez saisir une categorie de produit")
                else :
                    cur.execute("select * from categorie WHERE nom=?", (self.var_cat_nom.get(),))
                    row = cur.fetchone()
                    if row != None :
                        messagebox.showerror("Erreur" , "La categorie existe déjà")
                    else :
                        cur.execute("insert into categorie(nom) values(?)", ( self.var_cat_nom.get(),))
                        con.commit()
                        self.affficher()
                        messagebox.showinfo("Succès", "Enregistrement effectué avec succès")
                        self.var_cat_cid.set("")
                        self.var_cat_nom.set("")

            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def affficher(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            cur.execute("select * from categorie")
            rows = cur.fetchall()
            self.categorieliste.delete(*self.categorieliste.get_children())
            for row in rows:
                self.categorieliste.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def Supprimer(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
           if self.var_cat_cid.get() == "":
               messagebox.showerror("Erreur", "Veillez selectionner une categorie à partir de la liste")
           else:
               cur.execute("select * from categorie WHERE cid=?", (self.var_cat_cid.get(),))
               row = cur.fetchone()
               if row is None:
                   messagebox.showerror("Erreur", "L'id n'existe pas")
               else:
                   op = messagebox.askyesno("Confirmation", "Voulez-vous vraiment Supprimer?")
                   if op:
                       cur.execute("delete from categorie WHERE cid=?", (self.var_cat_cid.get(),))
                       con.commit()
                       self.affficher()
                       self.var_cat_cid.set("")
                       self.var_cat_nom.set("")
                       messagebox.showinfo("Succes", "Suppression effectué")
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = Categorie(root)
    root.mainloop()