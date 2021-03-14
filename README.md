# Automatisation et Python: organisation des fichiers

Ecrire des scripts pour automatiser les tâches est génial, mais automatiser des scripts est encore mieux. Donc, ici dans cet projet, j'ai touché les deux couches pour résoudre le problème d'organisation de nos fichiers et dossiers. Je dois montrer comment l'automatisation peut nous aider. je viens d'ecrire un script pour automatiser la tâche de déplacement de nos fichiers vers des dossiers respectifs en fonction de leur type de fichier, puis j'ai automatisé l'exécution de ce script.
Il s'agit d'un script qui s'exécute à la demande ou de manière automatique qui regarde tous nos fichiers dans ce dossier petrit par les images, films, et fichiers d'archive.

Avant d'écrire ce script il faut:
   - lister le contenu du repertoire
   - Identifier les types de fichiers(videos, images, archive, pdf,...)
   - Deplacer les fichiers dans le bon dossier
  
1. Ecrire un script pour automatiser le déplacement des fichiers - En cela, j'ai utilisé python pour écrire un script pour déplacer automatiquement nos differents fichiers du dossier foutir vers différents dossiers en fonction de leur type de fichier. Par exemple, si nous avons une image, elle sera automatiquement déplacée vers le dossier Media, si nous avons un document pdf, il sera déplacé vers le dossier Documents, si nous avons un fichier zip, il sera déplace vers le dossier Source et ainsi de suite. Nous utiliserons les modules os et shutil de python pour cela.
2. Automatiser l'exécution du script - En cela, nous allons en quelque sorte demander à notre système d'exploitation d'exécuter automatiquement notre script toutes les heures (ou quel que soit l'intervalle de temps que vous souhaitez).
  
# Rédaction de script pour automatiser le déplacement des fichiers et créations des dossiers
Pré-requis: assurez-vous que python3 est installé sur votre système et que vous avez une certaine connaissance de python pour comprendre le script.
Accédez maintenant à votre dossier Téléchargements et créez un fichier appelé trieur.py 

#vous devez import les modules python comme:
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
        
