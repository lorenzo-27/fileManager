#!/usr/bin/env python

import os
import shutil

def createFolder(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

def extractFiles(srcFolder, targetFolder, extensions, mvOrCp):
    createFolder(targetFolder)

    for root, dirs, files in os.walk(srcFolder):
        for file in files:
            if file.endswith(tuple(extensions)):
                sourcePath = os.path.join(root, file)
                destinationPath = os.path.join(targetFolder, file)

                if os.path.abspath(sourcePath) != os.path.abspath(destinationPath):
                    if mvOrCp == "s":
                        shutil.move(sourcePath, targetFolder)
                    elif mvOrCp == "c":
                        shutil.copy2(sourcePath, targetFolder)

def fileOrganizer(srcFolder):
    dstFolder = os.path.join(os.path.expanduser("~"), srcFolder, "Ordered")

    if not os.path.exists(dstFolder):
        os.makedirs(dstFolder)

    for file in os.listdir(srcFolder):
        filePath = os.path.join(srcFolder, file)
        if os.path.isfile(filePath):
            month = file[3:5]
            monthFolder = os.path.join(dstFolder, month)
            createFolder(monthFolder)
            shutil.copy2(filePath, os.path.join(monthFolder, file))

def folderCreator(srcFolder, nFolders):
    nDigits = len(str(nFolders))
    for i in range(1, nFolders + 1):
        folder = os.path.join(srcFolder, f"{i:0{nDigits}d}")
        createFolder(folder)

def getOperation():
    print("Inserire il numero associato all'operazione da eseguire:"
          "\n1.     Estrarre tutti i file pdf da una cartella in modo ricorsivo"
          "\n2.     Estrarre tutti i file di qualsiasi estensione da una cartella in modo ricorsivo"
          "\n3.     Estrarre tutti i file jpg e raw da una cartella in modo ricorsivo, dividendo i file in due cartelle diverse"
          "\n4.     Estrarre tutti i file heic e mov da una cartella in modo ricorsivo, dividendo i file in due cartelle diverse"
          "\n5.     Creare n cartelle numerate da 1 a n all'interno di una cartella"
          "\n6.     Ordinare i file in una cartella in base al mese di creazione")
    choice = input("Inserisi un numero 1 - 6: ")

    if choice in ["1", "2", "3", "4", "5", "6"]:
        return choice
    else:
        print("Inserimento non valido")
        return getOperation()

def getSrcPath():
    srcFolder = input("Inserire la cartella di origine: ")

    if not srcFolder:
        print("Inserimento non valido")
        return getSrcPath()
    else:
        return srcFolder

def moveOrCopy():
    choice = input("Vuoi copiare o spostare i file? (c/s): ")

    if choice in ["c", "s"]:
        return choice
    else:
        print("Inserimento non valido")
        return moveOrCopy()

if __name__ == '__main__':
    operation = getOperation()
    src = getSrcPath()

    if operation in ["1", "2", "3", "4"]:
        mvOrCp = moveOrCopy()

    if operation == "1":
        extractFiles(src, os.path.join(os.path.expanduser("~"), src, "__pdf"), [".pdf"], mvOrCp)
    elif operation == "2":
        extractFiles(src, os.path.join(os.path.expanduser("~"), src, "__files"), [], mvOrCp)
    elif operation == "3":
        extractFiles(src, os.path.join(os.path.expanduser("~"), src, "__jpg"), [".JPG"], mvOrCp)
        extractFiles(src, os.path.join(os.path.expanduser("~"), src, "__raw"), [".ARW", ".NEF", ".DNG"], mvOrCp)
    elif operation == "4":
        extractFiles(src, os.path.join(os.path.expanduser("~"), src, "__heic"), [".HEIC"], mvOrCp)
        extractFiles(src, os.path.join(os.path.expanduser("~"), src, "__mov"), [".MOV"], mvOrCp)
    elif operation == "5":
        nFolders = int(input("Quante cartelle vuoi creare? "))
        if nFolders > 0:
            folderCreator(src, nFolders)
    elif operation == "6":
        fileOrganizer(src)
