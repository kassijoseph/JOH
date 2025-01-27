from tkinter import *
from PIL import Image , ImageTk
import os
from tkinter import messagebox
import time
import sqlite3
import smtplib
import email_pass


class Login :
    def __init__(self , root) :
        self.root = root
        self.root.title("Login")
        self.root.geometry("470x470+300+100")
        self.root.config(bg="white")
        self.root.focus_force()

        self.code_force = ""

        login_frame = Frame(self.root , bg="cyan")
        login_frame.place(x=10 , y=10 , height=450 , width=450)

        tilte = Label(login_frame , text="connexion" , font=("algerian" , 30 , "bold") , bg="cyan" , fg="black").pack(side=TOP , fill=X)

        lb_id = Label(login_frame , text="ID Employé" , font=("time new roman" , 20 , "bold") , bg="cyan" ,fg="black").place(x=150 , y=100)

        lb_password = Label(login_frame , text="Mot de passe" , font=("time new roman" , 20 , "bold") , bg="cyan" ,fg="black").place(x=150 , y=210)

        self.txt_id_employe = Entry(login_frame , font=("time new roman" , 20 , "bold") , bg="lightgray" , fg="black")
        self.txt_id_employe.place(x=150 , y=150 , width=150)

        self.txt_password = Entry(login_frame , font=("time new roman" , 20 , "bold") , bg="lightgray" , fg="black")
        self.txt_password.place(x=150 , y=250 , width=180)

        connexion_btn = Button(login_frame , text="Connexion" , command=self.connexion , cursor="hand2" ,font=("time new roman" , 20 , "bold") , bg="green" , fg="black")
        connexion_btn.place(x=150 , y=320 , width=150 , height=40)

        oubli_btn = Button(login_frame , text="Mot de passe oublié", command=self.password_oublié, cursor="hand2" , font=("time new roman" , 10) , bg="cyan" , bd=0 , fg="red" , activebackground="cyan")
        oubli_btn.place(x=150 , y=400 , width=150)

    def password_oublié(self):
        if self.txt_id_employe.get() == "":
            messagebox.showerror("Erreur", "Veillez saisir votre ID Employé")
        else:
            con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
            cur = con.cursor()
            try:
                cur.execute("select email from employe where eid=?", (self.txt_id_employe.get(),))
                email = cur.fetchone()
                if email == None :
                    messagebox.showerror("Erreur", "L'ID employé est invalide")
                else:
                    chk = self.envoie_mail(email[0])

                    if chk == "f":
                        messagebox.showerror("Erreur", "Veillez verifier votre connexion")
                    else:
                        self.var_code = StringVar()
                        self.var_new_pass = StringVar()
                        self.var_conf_pass = StringVar()

                        self.root2 = Toplevel()
                        self.root2.title("Réinitialiser mot de passse")
                        self.root2.config(bg="white")
                        self.root2.geometry("400x400+780+130")
                        self.root2.focus_force()
                        self.root2.grab_set()

                        tilte = Label(self.root2, text="Mot de passe oublié", font=("algerian" , 15 , "bold"), fg="red").pack(side=TOP, fill=X)

                        #code
                        aff_code = Label(self.root2, text="Saisir le code reçu par mail", font=("algerian" , 15 , "bold"), bg="white").place(x=20,y=50)
                        txt_reeset = Entry(self.root2, textvariable=self.var_code, font=("time new roman", 15), bg="lightgray").place(x=20,y=90)
                        self.valide_btn = Button(self.root2, text="Valider", command=self.code_valide,cursor="hand2" , font=("time new roman" , 15, "bold"), bg="green" , fg="red")
                        self.valide_btn.place(x=150,y=350)

                        #####nouveau mot de paase

                        nouveau_password = Label(self.root2, text="Nouveau mot de passe", font=("algerian" , 15 , "bold"), bg="white").place(x=20,y=150)
                        txt_new_pass = Entry(self.root2, textvariable=self.var_new_pass, font=("time new roman", 15), bg="lightgray").place(x=20, y=180)

                        confirme_password = Label(self.root2, text="Confirmer mot de passe", font=("algerian" , 15 , "bold"), bg="white").place(x=20,y=250)
                        txt_confi = Entry(self.root2, textvariable=self.var_conf_pass, font=("time new roman", 15), bg="lightgray").place(x=20, y=300)

                        ### modifier mot de passe

                        self.changer_btn = Button(self.root2, text="Modifier", cursor="hand2", state=DISABLED, command=self.Modifier, font=("time new roman", 15, "bold"),bg="yellow")
                        self.changer_btn.place(x=30, y=350)

            except Exception as ex :
                messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

    def connexion(self):
        con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
        cur = con.cursor()
        try:
            if self.txt_id_employe.get() == "" or self.txt_password.get() == "" :
                messagebox.showerror("Erreur" , "Veuillez donner votre ID et Mot de passe")
            else:
                cur.execute("select type from employe where eid=? AND Mot_de_passe=?" ,(self.txt_id_employe.get() , self.txt_password.get()))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror("Erreur" , "L'ID Employé/Mot de passe n'est pas correcte ")
                else:
                    if user[0] == "Admin":
                        self.root.destroy()
                        os.system("python C:/Users/Utilisateur/PycharmProjects/MypythonProject3/GESTION_SUPERMACHE/Accueil.py")
                    else:
                        self.root.destroy()
                        os.system("python C:/Users/Utilisateur/PycharmProjects/MypythonProject3/GESTION_SUPERMACHE/Caisse.py")

        except Exception as ex :
            messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

    def Modifier(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Erreur", "Veillez saisir votre mot de passe")
        elif self.var_new_pass.get()!=self.var_conf_pass.get():
            messagebox.showerror("Erreur", "Le nouveau mot de passe et le confirme mot de passe doivent etre identique")
        else:
            try:
                con = sqlite3.connect(database=r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Données\Gestion.db")
                cur = con.cursor()
                cur.execute("update employe set mot_de_passe=? where eid=?", (self.var_new_pass.get(), self.txt_id_employe.get(),))
                con.commit()
                messagebox.showinfo("Succès", "Mot de passe modifier avec succès")
                self.root2.destroy()


            except Exception as ex:
                messagebox.showerror("Erreur" , f"Erreur de connexion {str(ex)}")

    def code_valide(self) :
        if int(self.code_envoie) == int(self.var_code.get()) :
            self.changer_btn.config(state=NORMAL)
            self.valide_btn.config(state=DISABLED)
        else :
            messagebox.showerror("Erreur" , "Code invalide")

    def envoie_mail(self , to_):
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        email_ = email_pass.email_
        pass_ = email_pass.pass_

        s.login(email_, pass_)

        self.code_envoie = int(time.strftime("%H%S%M"))+int(time.strftime("%S"))

        subj = "Magasin st joseph Kassi Code de reinitialisation"
        msg = f"Bonjour Monsieur/Madame ! \n\n votre code de reinitialisation est : {self.code_envoie}\n\nmerci d'avoir utiliser notre service"
        msg = "subject:{}\n\n{}".format(subj, msg)
        s.sendmail(email_, to_, msg)
        chk = s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'

if __name__ == "__main__" :
    root = Tk()
    obj = Login(root)
    root.mainloop()
