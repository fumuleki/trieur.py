
# Trier les fichiers d'un repertoire par type
import glob
import shutil
import os
from os import path

extensionsDocuments = ['.doc', '.pdf', '.pptx']
extensionsMedia = ['.png', '.jpeg', '.avi', '.mkv', '.mp4']
extensionsSource = ['.zip', '.exe', '.7z', '.msi']

base_folder = "C:/foutoir"

docFiles = os.path.join(base_folder, 'documents')
mediaFiles = os.path.join(base_folder, 'media')
sourceFiles = os.path.join(base_folder, 'sources')


# LISTER LE CONTENU DU REPERTOIRE
files = glob.glob(os.path.join(base_folder,"*"))

for file in files:
    #print(file)
    # trouver l'extension
    extension = os.path.splitext(file)[1].lower()
    if extension in extensionsDocuments:
        #deplace dans dossier documents
        if not path.exists(docFiles):
            os.mkdir(docFiles)
        shutil.move(file, docFiles)
    if extension in extensionsMedia:
        if not path.exists(mediaFiles):
             os.mkdir(mediaFiles)
        shutil.move(file,mediaFiles)
    if extension in extensionsSource:
        if not path.exists(sourceFiles):
            os.mkdir(sourceFiles)
        shutil.move(file,sourceFiles)
