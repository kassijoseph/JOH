from tkinter import *
from PIL import Image , ImageTk
import os
from tkinter import messagebox,ttk
import time
import sqlite3


class Fournisseur :
    def __init__(self, root):
        self.root = root
        self.root.title("Fournisseur")
        self.root.geometry("1050x555+302+140")
        self.root.config(bg="white")
        self.root.focus_force()

        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        cur.execute( "CREATE TABLE IF NOT EXISTS fournisseur(forid text PRIMARY KEY, nom text, contact text, description text)")
        con.commit()

        ##### les variables

        self.var_fourni_id = StringVar()
        self.var_recherche = StringVar()
        self.var_fourni_nom = StringVar()
        self.var_fourni_contact = StringVar()

        ######Option recherche

        reche_option = Label(self.root, text="Recherche par ID Fournisseur", font=("times new roman", 15), bg="white")
        reche_option.place(x=400, y=70, width=250)
        reche_txt = Entry(self.root, textvariable=self.var_recherche, font=("times new roman", 15), bg="lightyellow",).place(x=650, y=70, width=150)
        recherche_btn = Button(self.root, command=self.Rechercher, text="Recherche", font=("time new roman", 15, "bold"), cursor="hand2", bg="blue", fg="white").place(x=810, y=70, height=28)
        Tous_btn = Button(self.root , text="Tous", command=self.affficher, font=("time new roman", 15, "bold"), cursor="hand2", bg="lightgray", fg="black").place(x=940, y=70, height=28)

        titre = Label(self.root , text="Formulaire Fournisseur" , font=("times new roman", 15), cursor="hand2", bg="cyan", fg="black").place(x=0 , y=0 , width=1050)

        ### Contenu

        #### ligne1

        self.lbl_fourid= Label(self.root , text="ID Fournisseur" , font=("goudy old style" , 15), bg="white").place(x=10 ,y=70)
        self.txt_fourid = Entry(self.root, textvariable=self.var_fourni_id,font=("goudy old style" , 15) , bg="lightyellow")
        self.txt_fourid.place(x=150, y=70, width=150)

        ####ligne2
        self.lbl_nom = Label(self.root , text="Nom" , font=("goudy old style" , 15) , bg="white").place( x=10 , y=120)
        self.txt_nom = Entry(self.root, textvariable=self.var_fourni_nom, font=("goudy old style" , 15) , bg="lightyellow").place(x=150 , y=120 , width=150)

        ####ligne3
        self.lbl_contact = Label(self.root , text="Contact" , font=("goudy old style" , 15) , bg="white").place(x=10 , y=170)
        self.txt_contact = Entry(self.root , textvariable=self.var_fourni_contact, font=("goudy old style" , 15) , bg="lightyellow").place(x=150 , y=170 ,width=150)

        ####ligne2
        self.lbl_description = Label(self.root , text="Description", font=("goudy old style" , 15) , bg="white").place(x=10 , y=225)
        self.txt_description = Text(self.root , font=("goudy old style" , 15) , bg="lightyellow")
        self.txt_description.place(x=150 , y=220 ,width=200, height=90)

        self.btn_ajout = Button(self.root , text="Ajouter", command=self.ajouter, state="normal",font=("goudy old style" , 20 , "bold") , cursor="hand2" , bg="green")
        self.btn_ajout.place(x=80 , y=320 , height=30)

        self.btn_modifier = Button(self.root , text="Modifier", command=self.modifier, state="disabled" ,font=("goudy old style" , 20 , "bold") , cursor="hand2" , bg="yellow")
        self.btn_modifier.place(x=250 , y=320 , height=30)

        self.btn_supprimer = Button(self.root , text="Supprimer", command=self.Supprimer, state="disabled" ,font=("goudy old style", 20, "bold"), cursor="hand2" , bg="red")
        self.btn_supprimer.place(x=80 , y=400 , height=30)

        btn_reini = Button(self.root , text="Reinitialiser", command=self.reini, font=("goudy old style" , 20 , "bold") , cursor="hand2" , bg="lightgray").place(x=250, y=400, height=30)

        ######### listes des employes

        listeFrame = Frame(self.root , bd=3 , relief=RIDGE)
        listeFrame.place(x=400 , y=100 , height=450 , width=645)
        scroll_y = Scrollbar(listeFrame , orient=VERTICAL)
        scroll_y.pack(side=RIGHT , fill=Y)

        scroll_x = Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.fournisseurliste = ttk.Treeview(listeFrame , column=("forid", "nom", "contact", "description"),yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.config(command=self.fournisseurliste.xview)
        scroll_y.config(command=self.fournisseurliste.yview)

        self.fournisseurliste.heading("forid", text="ID")
        self.fournisseurliste.heading("nom", text="Nom")
        self.fournisseurliste.heading("contact", text="Contact")
        self.fournisseurliste.heading("description", text="Description")

        self.fournisseurliste["show"] = "headings"

        self.fournisseurliste.pack(fill=BOTH, expand=1)
        self.affficher()
        self.fournisseurliste.bind("<ButtonRelease-1>" , self.get_donne)

    def ajouter(self) :
        con = sqlite3.connect(
            database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try :
            if self.var_fourni_id.get() == "" or self.var_fourni_nom.get()=="" or self.var_fourni_contact.get()=="":
                messagebox.showerror("Erreur" , "Veuillez mettre un ID")
            else :
                cur.execute("select * from fournisseur WHERE forid=?" , (self.var_fourni_id.get() ,))
                row = cur.fetchone()
                if row != None :
                    messagebox.showerror("Erreur" , "L'ID de fournisseur existe déjà")
                else :
                    cur.execute("insert into fournisseur(forid, nom, contact, description) values (?,?,?,?)",(
                        self.var_fourni_id.get() ,
                        self.var_fourni_nom.get() ,
                        self.var_fourni_contact.get() ,
                        self.txt_description.get("1.0", END)
                    ))
                    con.commit()
                    self.affficher()
                    messagebox.showinfo("Succès", "Ajout effectué avec succès")

        except Exception as ex:
            messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")
    ######les fonctions

    def affficher(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            cur.execute("select * from fournisseur")
            rows = cur.fetchall()
            self.fournisseurliste.delete(*self.fournisseurliste.get_children())
            for row in rows:
                self.fournisseurliste.insert("", END, values=row)

        except Exception as ex:
          messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def get_donne(self, ev):
        self.btn_ajout.config(state="disabled")
        self.btn_modifier.config(state="normal")
        self.btn_supprimer.config(state="normal")
        self.txt_fourid.config(state="readonly")
        r = self.fournisseurliste.focus()
        if r:
            contenu = self.fournisseurliste.item(r)
            row = contenu["values"]
            if row:
                self.var_fourni_id.set(row[0])
                self.var_fourni_nom.set(row[1])
                self.var_fourni_contact.set(row[2])
                self.txt_description.delete("1.0", END)
                self.txt_description.insert(END, row[3])


    def modifier(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()

        try:
            cur.execute("update fournisseur set nom=?, contact=?, description=? WHERE forid=?",(
                self.var_fourni_nom.get(),
                self.var_fourni_contact.get(),
                self.txt_description.get("1.0", END),
                self.var_fourni_id.get()
            ))
            con.commit()
            self.affficher()
            messagebox.showinfo("Succes", "Modification éffectuée")
        except Exception as ex:
          messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def Supprimer(self) :
        con = sqlite3.connect(
            database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try :
            op = messagebox.askyesno("Confirmation" , "Voulez-vous vraiment Supprimer?")
            if op == True :
                cur.execute("delete from fournisseur WHERE forid=?", (self.var_fourni_id.get(),))
                con.commit()
                self.affficher()
                messagebox.showinfo("Succes", "Suppression effectué")
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def reini(self):

        self.btn_ajout.config(state="normal")
        self.btn_modifier.config(state="disabled")
        self.btn_supprimer.config(state="disabled")
        self.txt_fourid.config(state="normal")
        self.var_fourni_id.set("")
        self.var_fourni_nom.set("")
        self.var_fourni_contact.set("")
        self.var_recherche.set("")
        self.txt_description.delete("1.0", END)

    def Rechercher(self) :
        con = sqlite3.connect(
            database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try :
            if self.var_recherche.get() == "":
                messagebox.showerror("Erreur" , "Qu'est-ce que vous rechercher?")
            else :
                cur.execute("SELECT * FROM fournisseur WHERE forid=?", (self.var_recherche.get() ,))
                rows = cur.fetchall()
                if rows :
                    self.fournisseurliste.delete(*self.fournisseurliste.get_children())
                    for row in rows :
                        self.fournisseurliste.insert("" , END , values=row)
                else :
                    messagebox.showerror("Erreur" , "Aucun resultat trouvé")

        except Exception as ex :
            messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")


if __name__ == "__main__" :
    root = Tk()
    obj = Fournisseur(root)
    root.mainloop()
