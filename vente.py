from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox

class Vente:
    def __init__(self, root):
        self.root = root
        self.root.title("Vente")
        self.root.geometry("1050x555+302+140")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_nfacture = StringVar()
        self.liste_facture = []

        ##### Titre

        titre = Label(self.root , text="Consultater la facture des clients", font=("times new roman" , 20) , cursor="hand2" ,bg="cyan", bd=3, relief=RIDGE, fg="black").pack(side=TOP, fill=X)

        lbl_N_facture = Label(self.root , text=" Numero Facture", font=("times new roman" , 18) , cursor="hand2" ,bg="white", fg="black").place(x=0 , y=70)
        lbl_N_facture = Entry(self.root, textvariable=self.var_nfacture, font=("time new roman", 18), bg="lightyellow").place(x=170, y=70, width=150)

        btn_recherche = Button(self.root, text="Recherche", command=self.rechercher, font=("time new roman", 18), cursor="hand2", bg="green").place(x=325, y=70, height=35, width=130)
        btn_reini = Button(self.root, text="Réinitialiser", command=self.reini, font=("time new roman", 18), cursor="hand2", bg="gray").place(x=460, y=70, height=35, width=130)

        #### stockages des numero facture

        Vente_Frame = Frame(self.root , bd=3 , relief=RIDGE)
        Vente_Frame.place(x=0 , y=102 , height=450 , width=250)
        scroll_y = Scrollbar(Vente_Frame , orient=VERTICAL)
        self.liste_vente = Listbox(Vente_Frame, font=("goudy old style ",15), bg="white", yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_y.config(command=self.liste_vente.yview)
        self.liste_vente.pack(fill=BOTH, expand=1)
        self.liste_vente.bind("<ButtonRelease-1>", self.recuperDonner)

        ###### espace sortir du facture

        Facture_Frame = Frame(self.root , bd=3 , relief=RIDGE,)
        Facture_Frame.place(x=250 , y=110 , height=445 , width=440)

        lbl_factureclient = Label(Facture_Frame, text=" Facture du client", font=("times new roman" , 18) , cursor="hand2" ,bg="orange", fg="black").pack(side=TOP, fill=X)
        scroll_y2 = Scrollbar(Facture_Frame , orient=VERTICAL)
        self.espaceFacture = Listbox(Facture_Frame, font=("goudy old style ",12), bg="lightyellow", yscrollcommand=scroll_y2.set)
        scroll_y2.pack(side=RIGHT , fill=Y)
        scroll_y2.config(command=self.espaceFacture.yview)
        self.espaceFacture.pack(fill=BOTH, expand=1)

        self.facture = Image.open( r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\images\cat2.jpg")
        self.facture = self.facture.resize((345 , 555) , Image.LANCZOS)
        self.facture = ImageTk.PhotoImage(self.facture)

        self.lbl_ima_cat2 = Label(self.root , bd=2 , relief=RAISED , image=self.facture)
        self.lbl_ima_cat2.place(x=690 , y=40)

        self.afficher()

    def afficher(self):
        del self.liste_facture[:]
        self.liste_vente.delete(0, END)
        for i in os.listdir(r"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Facture"):
            if i.split(".")[-1]=="txt":
                self.liste_vente.insert(END, i)
                self.liste_facture.append(i.split(".")[0])

    def recuperDonner(self, ev):
        index_ = self.liste_vente.curselection()
        if index_:
            nom_fichier = self.liste_vente.get(index_)
            fichier_ouvert = open(fr"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Facture\{nom_fichier}","r")
            self.espaceFacture.delete(0, END)
            for i in fichier_ouvert:
                self.espaceFacture.insert(END, i)
            fichier_ouvert.close()

    def rechercher(self):
        if self.var_nfacture.get()=="":
            messagebox.showerror("Erreur", "Donnez un Numero de facture")
        else:
            if self.var_nfacture.get() in self.liste_facture:
                fichier_ouvert = open(fr"C:\Users\Utilisateur\PycharmProjects\MypythonProject3\GESTION_SUPERMACHE\Facture\{self.var_nfacture.get()}.txt","r")
                self.espaceFacture.delete(0, END)
                for i in fichier_ouvert:
                    self.espaceFacture.insert(END, i)
                fichier_ouvert.close()
            else:
                messagebox.showerror("Erreur", "Numero de facture Ivalide")

    def reini(self):
        self.afficher()
        self.espaceFacture.delete("0", END)
        self.var_nfacture.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Vente(root)
    root.mainloop()