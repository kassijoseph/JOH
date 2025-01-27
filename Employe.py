from tkinter import *
from tkinter import messagebox, ttk
import sqlite3

class Employe:
    def __init__(self, root):
        self.root = root
        self.root.title("Employé")
        self.root.geometry("1050x555+302+140")
        self.root.config(bg="white")
        self.root.focus_force()

        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS employe(eid text PRIMARY KEY, Nom text, Email text, Sexe text, Contact text, Naissance text, Adhesion text, Mot_de_passe text, Type text, Adresse text, Salaire text)")
        con.commit()
        ##### les variables

        self.var_recherche_type = StringVar()
        self.var_recherche_txt = StringVar()
        self.var_emplo_id = StringVar()
        self.var_sexe = StringVar()
        self.var_contact = StringVar()
        self.var_nom = StringVar()
        self.var_naissance = StringVar()
        self.var_adhesion = StringVar()
        self.var_email = StringVar()
        self.var_mot_de_passe = StringVar()
        self.var_type = StringVar()
        self.var_salaire = StringVar()

        ####Frame recherche

        reche_Frame = LabelFrame(self.root, text="Recherche Employé", font=("goudy old style", 20, "bold"), bd=2, relief=RIDGE, bg="white", fg="black")
        reche_Frame.place(x=300, y=0, width=530, height=70)

        ####option de recherche

        reche_option = ttk.Combobox(reche_Frame, textvariable = self.var_recherche_type, values=("Nom", "Email", "Contact"), font=("times new roman", 15), state="r", justify=CENTER)
        reche_option.current(0)
        reche_option.place(x=10, y=0, width=150)
        reche_txt = Entry(reche_Frame, textvariable=self.var_recherche_txt, font=("times new roman", 15), bg="lightyellow",).place(x=170, y=0, width=150)

        recherche = Button(reche_Frame, text="Recherche", command=self.Rechercher, font=("times new roman",15), cursor="hand2", bg="blue", fg="white").place(x=330, y=0, height=30)

        Tous = Button(reche_Frame , text="Tous", command=self.affficher, font=("times new roman" , 15) , cursor="hand2" , bg="lightgray" ,fg="black").place(x=450 , y=0 , height=30)

        ##### Titre

        titre = Label(self.root, text="Formulaire Employé", font=("times new roman", 15), cursor="hand2", bg="cyan", fg="black").place(x=0, y=80, width=1050)

        ### Contenu

        #### ligne1

        lbl_empid = Label(self.root, text="ID Employé" , font=("goudy old style" , 15), bg="white").place(x=20, y=130)
        lbl_sexe = Label(self.root, text="Sexe" , font=("goudy old style" , 15) , bg="white").place(x=450 , y=130)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style" , 15) , bg="white").place(x=750 , y=130)

        self.txt_empid = Entry(self.root, textvariable=self.var_emplo_id, font=("goudy old style" , 15) , bg="lightyellow")
        self.txt_empid.place(x=130 ,y=130)
        txt_sexe = ttk.Combobox(self.root, textvariable=self.var_sexe, values=("Homme", "Femme"), font=("goudy old style", 15), state="r", justify=CENTER )
        txt_sexe.current(0)
        txt_sexe.place(x=500 , y=130, width=100)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style" , 15) , bg="lightyellow").place(x=820 , y=130)

       #### ligne2

        lbl_nom = Label(self.root, text="Nom", font=("goudy old style" , 15), bg="white").place(x=20 , y=170)
        lbl_naissance = Label(self.root, text="Date Naissance", font=("goudy old style" , 15) , bg="white").place(x=340 , y=170)
        lbl_adhesion = Label(self.root, text="Date Adhesion" , font=("goudy old style" , 15) , bg="white").place(x=690 , y=170)

        txt_nom = Entry(self.root, textvariable=self.var_nom, font=("goudy old style" , 15) , bg="lightyellow").place(x=130 ,y=170)
        txt_naissance = Entry(self.root, textvariable=self.var_naissance, font=("goudy old style" , 15) , bg="lightyellow").place(x=470 , y=170)
        txt_adhesion = Entry(self.root, textvariable=self.var_adhesion, font=("goudy old style" , 15) , bg="lightyellow").place(x=820 ,y=170)

        #### ligne3

        lbl_email = Label(self.root , text="Email" , font=("goudy old style" , 15), bg="white").place(x=20 , y=220)
        lbl_password = Label(self.root , text="Mot de passe " , font=("goudy old style" , 15) , bg="white").place(x=340 , y=220)
        lbl_type = Label(self.root , text="Type" , font=("goudy old style" , 15) , bg="white").place(x=690 , y=220)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style" , 15) , bg="lightyellow").place(x=130 ,y=220)
        txt_password = Entry(self.root , textvariable=self.var_mot_de_passe, font=("goudy old style" , 15) , bg="lightyellow").place(x=470 , y=220)
        txt_type = ttk.Combobox(self.root , textvariable=self.var_type, values=("Admin" , "Employé") , font=("goudy old style" , 15) , state="r",justify=CENTER)
        txt_type.current(0)
        txt_type.place(x=820 , y=220 , width=100)

        #### ligne4

        lbl_adresse = Label(self.root , text="Adresse" , font=("goudy old style" , 15) , bg="white").place(x=20 , y=260)
        lbl_salaire = Label(self.root , text="Salaire" , font=("goudy old style" , 15) , bg="white").place(x=340 , y=260)

        self.txt_adresse = Text(self.root , font=("goudy old style", 15), bg="lightyellow")
        self.txt_adresse.place(x=130, y=255, height=70, width=200)

        self.txt_salaire = Entry(self.root, textvariable=self.var_salaire, font=("goudy old style" , 15) , bg="lightyellow").place(x=470 , y=260)

        self.btn_ajout = Button(self.root, text="Ajouter", command=self.ajouter, state="normal", font=("goudy old style" , 20, "bold"), cursor="hand2", bg="green")
        self.btn_ajout.place(x=370 , y=290, height=40)
        self.btn_modifier = Button(self.root, text="Modifier", command=self.Modifier, state="disabled", font=("goudy old style" , 20, "bold"), cursor="hand2", bg="yellow")
        self.btn_modifier.place(x=520 , y=290, height=40)
        self.btn_supprimer = Button(self.root, text="Supprimer", command=self.Supprimer, state="disabled", font=("goudy old style" , 20, "bold"), cursor="hand2", bg="red")
        self.btn_supprimer.place(x=680, y=290, height=40)
        btn_reini = Button(self.root , text="Reinitialiser", command=self.reini, font=("goudy old style", 20, "bold"), cursor="hand2", bg="lightgray").place(x=850 , y=290, height=40)

        #### listes des employes

        listeFrame = Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=0, y=330, height=225, relwidth=1)
        scroll_y = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = Scrollbar(listeFrame , orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM , fill=X)

        self.employeliste = ttk.Treeview(listeFrame, column=("eid", "Nom", "Email", "Sexe", "Contact", "Naissance", "Adhesion", "Mot_de_passe", "Type", "Adresse", "Salaire"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.config(command=self.employeliste.xview)
        scroll_y.config(command=self.employeliste.yview)

        self.employeliste.heading("eid", text="ID")
        self.employeliste.heading("Nom" , text="Nom")
        self.employeliste.heading("Email" , text="Email")
        self.employeliste.heading("Sexe" , text="Sexe")
        self.employeliste.heading("Contact" , text="Contact")
        self.employeliste.heading("Naissance" , text="Naissance")
        self.employeliste.heading("Adhesion" , text="Adhesion")
        self.employeliste.heading("Mot_de_passe" , text="Mot_de_passe")
        self.employeliste.heading("Type" , text="Type")
        self.employeliste.heading("Adresse" , text="Adresse")
        self.employeliste.heading("Salaire" , text="Salaire")

        self.employeliste["show"]="headings"
        self.employeliste.bind("<ButtonRelease-1>", self.get_donne)
        self.employeliste.pack(fill=BOTH, expand=1)

        self.affficher()

        #### Fonctions

    def ajouter(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            if self.var_emplo_id.get() == "" or self.var_type.get()=="":
                messagebox.showerror("Erreur", "Veuillez mettre un ID, Mot_de_passe et type")
            else:
                cur.execute("select * from employe WHERE eid=?", (self.var_emplo_id.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "L'ID d'employé existe déjà")
                else:
                    cur.execute("insert into employe(eid , Nom , Email, Sexe, Contact, Naissance, Adhesion, Mot_de_passe, Type, Adresse, Salaire) values(?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        self.var_emplo_id.get(),
                        self.var_nom.get(),
                        self.var_email.get(),
                        self.var_sexe.get(),
                        self.var_contact.get(),
                        self.var_naissance.get(),
                        self.var_adhesion.get(),
                        self.var_mot_de_passe.get(),
                        self.var_type.get(),
                        self.txt_adresse.get("1.0", END),
                        self.var_salaire.get()
                    ))
                    con.commit()
                    self.affficher()
                    self.reini()
                    messagebox.showinfo("Succès", "Ajout effectué avec succès")

        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def affficher(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            cur.execute("select * from employe")
            rows = cur.fetchall()
            self.employeliste.delete(*self.employeliste.get_children())
            for row in rows:
                self.employeliste.insert("", END, values=row)

        except Exception as ex:
          messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

    def get_donne(self , ev) :
        self.btn_ajout.config(state="disabled")
        self.btn_modifier.config(state="normal")
        self.btn_supprimer.config(state="normal")
        self.txt_empid.config(state="readonly")
        r = self.employeliste.focus()
        contenu = self.employeliste.item(r)
        row = contenu["values"]

        self.var_emplo_id.set(row[0]),
        self.var_nom.set(row[1]),
        self.var_email.set(row[2]),
        self.var_sexe.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_naissance.set(row[5]),
        self.var_adhesion.set(row[6]),
        self.var_mot_de_passe.set(row[7]),
        self.var_type.set(row[8]),
        self.txt_adresse.delete("1.0", END),
        self.txt_adresse.insert(END, row[9]),
        self.var_salaire.set(row[10])

    def Modifier(self):

        selected_item = self.employeliste.focus()
        if not selected_item :
            messagebox.showerror("Erreur" , "Sélectionnez un employé pour le modifier.")
            return

        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            cur.execute("update employe set Nom=? , Email=?, Sexe=?, Contact=?, Naissance=?, Adhesion=?, Mot_de_passe=?, Type=?, Adresse=?, Salaire=? WHERE eid=?",(
                        self.var_nom.get(),
                        self.var_email.get(),
                        self.var_sexe.get() ,
                        self.var_contact.get() ,
                        self.var_naissance.get() ,
                        self.var_adhesion.get() ,
                        self.var_mot_de_passe.get() ,
                        self.var_type.get() ,
                        self.txt_adresse.get("1.0" , END) ,
                        self.var_salaire.get(),
                        self.var_emplo_id.get()
            ))
            con.commit()
            self.affficher()
            self.reini()
            messagebox.showinfo("Succes", "Modification Succès")
        except Exception as ex:
            messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

    def Supprimer(self):

        selected_item = self.employeliste.focus()
        if not selected_item:
            messagebox.showerror("Erreur", "Sélectionnez un employé à supprimer.")
            return

        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            op=messagebox.askyesno("Confirmation" , "Voulez-vous vraiment Supprimer?")
            if op==True:
                cur.execute("delete from employe WHERE eid=?" , (self.var_emplo_id.get(),))
                con.commit()
                self.affficher()
                self.reini()
                messagebox.showinfo("Succes", "Suppression effectué")
        except Exception as ex :
            messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

    def reini(self):

        self.btn_ajout.config(state="normal")
        self.btn_modifier.config(state="disabled")
        self.btn_supprimer.config(state="disabled")
        self.txt_empid.config(state="normal")
        self.var_nom.set(""),
        self.var_email.set(""),
        self.var_sexe.set("Homme"),
        self.var_contact.set(""),
        self.var_naissance.set(""),
        self.var_adhesion.set(""),
        self.var_mot_de_passe.set(""),
        self.var_type.set("Admi"),
        self.txt_adresse.delete("1.0", END),
        self.var_salaire.set(""),
        self.var_emplo_id.set(""),
        self.var_recherche_txt.set(""),
        self.var_recherche_type.set("Nom")

    def Rechercher(self) :
        con = sqlite3.connect(
            database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try :
            if self.var_recherche_txt.get() == "" :
                messagebox.showerror("Erreur" , "Veuillez saisir dans le champ recherche")
            else :
                cur.execute(
                    "SELECT * FROM employe WHERE " + self.var_recherche_type.get() + " LIKE '%" + self.var_recherche_txt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0 :
                    self.employeliste.delete(*self.employeliste.get_children())
                    for row in rows :
                        self.employeliste.insert("" , END , values=row)
                else :
                    messagebox.showerror("Erreur" , "Aucun résultat trouvé")

        except Exception as ex :
            messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = Employe(root)
    root.mainloop()