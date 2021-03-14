# python-trier-deplacer les fichier d'un repertoire

Il s'agit d'un script qui s'exécute à la demande ou de manière automatique qui regarde tous nos fichiers dans ce dossier petrit par les images, films, et fichiers d'archive.

Avant de realiser cet  script il faut:
   - lister le contenu du repertoire
   - Identifier les types de fichiers(videos, images, archive, pdf,...)
   - Deplacer les fichiers dans le bon dossier
  
#vous devez import les éléments comme:
  - import glob
  - import shutil
  - import os
  - from os import path 
  
#vous devez trier les fichiers d'un repertoire par type des extensions
  - extensionsDocuments = ['.doc', '.pdf', '.pptx']
  - extensionsMedia = ['.png', '.jpeg', '.avi', '.mkv', '.mp4']
  - extensionsSource = ['.zip', '.exe', '.7z', '.msi']
  
#vous devez donner la variable de repertoire où se trouve les fichiers
  - base_folder = "C:/foutoir"

#LISTER LE CONTENU DU REPERTOIRE
  - docFiles = os.path.join(base_folder, 'documents')
  - mediaFiles = os.path.join(base_folder, 'media')
  - sourceFiles = os.path.join(base_folder, 'sources')
  
files = glob.glob(os.path.join(base_folder,"*"))

#trouver l'extension
  - for file in files:
  - extension = os.path.splitext(file)[1].lower() 

#vous devez deplacer dans dossier documents 

    if extension in extensionsDocuments:
        #deplace dans dossier documents
        if not path.exists(docFiles):
            os.mkdir(docFiles)
        shutil.move(file, docFiles)
#vous devez deplacer dans dossier Media

    if extension in extensionsMedia:
        if not path.exists(mediaFiles):
             os.mkdir(mediaFiles)
        shutil.move(file,mediaFiles)
#vous devez deplacer dans dossier Source

    if extension in extensionsSource:
        if not path.exists(sourceFiles):
            os.mkdir(sourceFiles)
        shutil.move(file,sourceFiles)
        
