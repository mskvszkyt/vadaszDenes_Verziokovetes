import os, shutil, ctypes
from tkinter.tix import DirList

# class Commit():

#     def __init__(self):                 #,szulo,szerzo,datum,commit_leiras,valtozott,commits=1
#         # self.commits = commits
#         # self.szulo = szulo
#         # self.szerzo = szerzo
#         pass

#     def commit_datails(self):
#         adatok_listaja = ["Szulo: ","Szerzo: ","Datum: ","Commit leiras: ","Valtozott: ",]

#         with open(f"{2}.commit.details.txt", "w", encoding="utf8") as f:
#             for adat in adatok_listaja:
#                 f.write(f"{adat} \n")

# Commit().Commit_datails()

path_here = os.getcwd()

# for e in os.listdir():
#     if e.name == ".dusza":
#         os.remove(".dusza")
os.mkdir(".dusza")
os.system("attrib +h myFile.txt")

source = f"{path_here}\\probaMappa"
destination = f"{path_here}\\probaMappa\\.dusza\\1.commit"



shutil.copytree(source, destination)



