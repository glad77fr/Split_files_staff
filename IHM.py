from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
#from tkinter.filedialog import *
import tkinter
import pandas as pd
import glob
from Split_Data import split, staff

class Application(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.title("Transformation de données")
        self.resizable(width=False, height=False)
        self.mainloop()

    def initialize(self):
        self.control_menu = Frame(self)
        self.control_menu.pack()

        self.conf_menu = LabelFrame(self.control_menu, text="Configuation", width=430, height=300, labelanchor='n')
        self.conf_menu.grid(row=1, column=1, pady=10, padx=10)


        self.rep_source_affiche = StringVar()
        self.rep_cible_affiche = StringVar()


        self.entree_label = Label(self.conf_menu, text="Fichier référentiel STAFF")
        self.entree_label.grid(row=1, column=1, padx=20,sticky=W)

        self.entree = Entry(self.conf_menu, textvariable=self.rep_source_affiche, width=50)
        self.entree.grid(row=1, column=2,sticky=W, padx=0)

        self.imp_Button = Button(self.conf_menu, text="Sélection...", command=self.import_file)
        self.imp_Button.grid(row=1, column=3, padx=15, pady=10,sticky=W)

        self.cible_label = Label(self.conf_menu, text="Répertoire source de données")
        self.cible_label.grid(row=2,column=1, padx=20,sticky=W)

        self.cible_entree = Entry(self.conf_menu, textvariable=self.rep_cible_affiche, width=50)
        self.cible_entree.grid(row=2, column=2, sticky=W, padx=0)

        self.cible_Button = Button(self.conf_menu, text="Sélection...", command = self.rep_cible)
        self.cible_Button.grid(row=2, column=3, padx=15, pady=10,sticky=W)

        self.ex_menu = LabelFrame(self.control_menu, text="Execution", width=430, height=200, labelanchor='n')
        self.ex_menu.grid(row=1, column=2,padx=10, pady=10)

        self.ex_Button = Button(self.ex_menu, text="Executer", command = self.ex_programme,height = 1, width = 18)
        self.ex_Button.grid(row=3, column=1, padx=10, pady=10,sticky=W)

    def import_file(self):
        rep = filedialog.askopenfilename(initialdir="/", title="Select file",
                                         filetypes=(("Csv files", "*.csv"), ("all files", "*.*")))
        self.rep_source_affiche.set(rep)


    def rep_cible(self):
        self.rep_cible = filedialog.askdirectory()
        self.rep_cible_affiche.set(self.rep_cible)

    def ex_programme(self):

        if self.rep_source_affiche.get() == "":
            messagebox.showerror("Ficher référentiel STAFF non défini", "Veuillez sélectionner le fichier référentiel STAFF")

        if self.rep_cible_affiche.get() =="":
            messagebox.showerror("Répertoire source non défini", "Veuillez sélectionner le répertoire source contenant les fichiers à découper")

        if self.rep_source_affiche.get() != "" and self.rep_cible_affiche.get() != "":
            try:
                path = self.rep_cible_affiche.get()
                source = self.rep_source_affiche.get()
                ref_staff = staff(source)
                all_files = glob.glob(path + "/*.csv")
                for val in all_files:
                    split(val, ref_staff)
                messagebox.showinfo("Succès", "Les fichiers ont été créés")
            except:
                messagebox.showerror("Une erreur est survenue")


toto = Application(None)
toto.mainloop()