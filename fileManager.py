import os
import sys
import shutil

def pdfExtractor(srcFolder, mvOrCp):
    pdfFolder = os.path.join(os.path.expanduser("~"), srcFolder, "pdf")
    if not os.path.exists(pdfFolder):
        os.makedirs(pdfFolder)

    for root, dirs, files in os.walk(srcFolder):
        for file in files:
            if file.endswith(".pdf"):
                pdfPath = os.path.join(root, file)
                dstPath = os.path.join(pdfFolder, file)

                if os.path.abspath(pdfPath) != os.path.abspath(dstPath):
                    if mvOrCp == "s":
                        shutil.move(pdfPath, pdfFolder)
                    elif mvOrCp == "c":
                        shutil.copy2(pdfPath, pdfFolder)

def genericFileExtractor(srcFolder, mvOrCp):
    fileFolder = os.path.join(os.path.expanduser("~"), srcFolder, "__files")

    if not os.path.exists(fileFolder):
        os.makedirs(fileFolder)

    for root, dirs, files in os.walk(srcFolder):
        for file in files:
            filePath = os.path.join(root, file)
            dstPath = os.path.join(fileFolder, file)

            if os.path.abspath(filePath) != os.path.abspath(dstPath):
                if mvOrCp == "s":
                    shutil.move(filePath, dstPath)
                elif mvOrCp == "c":
                    shutil.copy2(filePath, dstPath)

def jpgRawExtractor(srcFolder, mvOrCp):
    jpgFolder = os.path.join(os.path.expanduser("~"), srcFolder, "jpg")
    rawFolder = os.path.join(os.path.expanduser("~"), srcFolder, "raw")

    if not os.path.exists(jpgFolder):
        os.makedirs(jpgFolder)
    if not os.path.exists(rawFolder):
        os.makedirs(rawFolder)

    for root, dirs, files in os.walk(srcFolder):
        for file in files:
            if file.endswith(".JPG"):
                jpgPath = os.path.join(root, file)
                dstPath = os.path.join(jpgFolder, file)

                if os.path.abspath(jpgPath) != os.path.abspath(dstPath):
                    if mvOrCp == "s":
                        shutil.move(jpgPath, jpgFolder)
                    elif mvOrCp == "c":
                        shutil.copy2(jpgPath, jpgFolder)
            if file.endswith(".ARW") or file.endswith(".NEF") or file.endswith(".DNG"):
                rawPath = os.path.join(root, file)
                dstPath = os.path.join(rawFolder, file)

                if os.path.abspath(rawPath) != os.path.abspath(dstPath):
                    if mvOrCp == "s":
                        shutil.move(rawPath, rawFolder)
                    elif mvOrCp == "c":
                        shutil.copy2(rawPath, rawFolder)

def heicMovExtractor(srcFolder, mvOrCp):
    heicFolder = os.path.join(os.path.expanduser("~"), srcFolder, "heic")
    movFolder = os.path.join(os.path.expanduser("~"), srcFolder, "mov")

    if not os.path.exists(heicFolder):
        os.makedirs(heicFolder)
    if not os.path.exists(movFolder):
        os.makedirs(movFolder)

    for root, dirs, files in os.walk(srcFolder):
        for file in files:
            if file.endswith(".HEIC"):
                heicPath = os.path.join(root, file)
                dstPath = os.path.join(heicFolder, file)

                if os.path.abspath(heicPath) != os.path.abspath(dstPath):
                    if mvOrCp == "s":
                        shutil.move(heicPath, heicFolder)
                    elif mvOrCp == "c":
                        shutil.copy2(heicPath, heicFolder)

            if file.endswith(".MOV"):
                movPath = os.path.join(root, file)
                dstPath = os.path.join(movFolder, file)

                if os.path.abspath(movPath) != os.path.abspath(dstPath):
                    if mvOrCp == "s":
                        shutil.move(movPath, movFolder)
                    elif mvOrCp == "c":
                        shutil.copy2(movPath, movFolder)

def fileOrderer(srcFolder):
    # funzione del cazzo, non mi ricordo manco perchè l'ho scritta - non testata
    dst_folder = os.path.join(os.path.expanduser("~"), srcFolder, "Ordered")

    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for file in os.listdir(srcFolder):
        file_path = os.path.join(srcFolder, file)
        if os.path.isfile(file_path):
            month = file[3:5]
            month_folder = os.path.join(dst_folder, month)
            if not os.path.exists(month_folder):
                os.makedirs(month_folder)
            shutil.copy2(file_path, os.path.join(month_folder, file))

def folderCreator(srcFolder, nFolders):
    nCifre = int(len(str(nFolders)))
    for i in range(1, nFolders + 1):
        folder = os.path.join(srcFolder, f"{i:0{nCifre}d}")
        if not os.path.exists(folder):
            os.makedirs(folder)

def getOperation():
    print("Inserire il numero associato all'operazione da eseguire:"
          "\n1.     Estrarre dei tutti i file pdf da una cartella in modo ricorsivo"
          "\n2.     Estrarre tutti i file di qualsiasi estensione da una cartella in modo ricorsivo"
          "\n3.     Estrarre tutti i file jpg e raw da una cartella in modo ricorsivo, dividendo i file in due cartelle diverse"
          "\n4.     Estrarre tutti i file heic e mov da una cartella in modo ricorsivo, dividendo i file in due cartelle diverse"
          "\n5.     Creare n cartelle numerate da 1 a n all'interno di una cartella"
          "\n6.     Ordinare i file in una cartella in base al mese di creazione")
    choice = input("Inserisi un numero 1 - 6: ")

    if choice in ["1", "2","3", "4", "5", "6"]:
        return choice
    else:
        print("Inserimento non valido")
        getOperation()

def getSrcPath():
    src_folder = input("Inserire la cartella di origine: ")

    if src_folder == "":
        print("Inserimento non valido")
        getSrcPath()
    else:
        return src_folder

def moveOrCopy():
    choice = input("Vuoi copiare o spostare i file? (c/s): ")

    if choice in ["c", "s"]:
        return choice
    else:
        print("Inserimento non valido")
        moveOrCopy()

if __name__ == '__main__':
    operation = getOperation()
    src = getSrcPath()
    if operation in ["1", "2", "3", "4"]:
        mvOrCp = moveOrCopy()

    if operation == "1":
        pdfExtractor(src, mvOrCp)
    elif operation == "2":
        genericFileExtractor(src, mvOrCp)
    elif operation == "3":
        jpgRawExtractor(src, mvOrCp)
    elif operation == "4":
        heicMovExtractor(src, mvOrCp)
    elif operation == "5":
        nFolders = int(input("Quante cartelle vuoi creare? "))
        if nFolders > 0:
            folderCreator(src, nFolders)
    elif operation == "6":
        fileOrderer(src)
