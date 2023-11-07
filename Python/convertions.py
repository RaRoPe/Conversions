# -*- coding: utf-8 -*-
import getopt
import logging
import os.path
from pathlib import Path
import subprocess
import sys

def convertToPdf(inputFile, tempOutputFolder):
    print("Converting file to PDF...")

    runnable = '"C:\\Program Files\\LibreOffice\\program\\soffice"'  # Path to LibreOffice runnable
    option1 = '"--headless"'  # Execute without graphic interface
    option2 = '--convert-to pdf'  # Specify the type of file to convert
    option3 = '"--outdir"'  # Command to set the output directory

    command = f'{runnable} {option1} {option2} {inputFile} {option3} {tempOutputFolder}'

    subprocess.run(command)

def convertPdfToImages(inputFile, outputFolder, filetype):
    print("Converting PDF to images...")

    runnable = 'pdftoppm'  # Path to runnable of Poppler package to convert PDF to images
    option1 = '-r 300'  # Image resolution

    command = f'{runnable} -{filetype} {option1} {inputFile} {outputFolder}'

    subprocess.run(command)

def returnNameAndPath(inputFile):
    filename = Path(inputFile).name

    #Extract the extension from filename
    onlyFilename = filename.split(".")
    filename = onlyFilename[0]
    extension = onlyFilename[1]

    return filename, extension

def validateFileAndFolder(file, folder):
    if not os.path.isfile(file):
        print("The input file is invalid. Verify if the path and the name of the file are correct.")
        exit(0)
    if not os.path.isdir(folder):
        print("The folder entered is invalid. Verify if the path and the name of the folder are correct. If it doesn't exist, create one with the name entered")
        exit(0)

def main():
    # Arguments:
    # inputFile - Path of the file to be converted (PDF, PPTX, PPT, XLSX, XLS)
    # tempOutputPDFFolder
    # outputImages

    if len(sys.argv) < 7:
        if (sys.argv[1] == '-h' or sys.argv[1] == '--Help'):
            print("Converting DOC/DOCX, PPT/PPTX, XLS/XLSX files to PDF and then to PNG/JPG. Also, convert PDF files to PNG/JPG")
            print("Usage: python main.py -i <input_file> -o <output_folder> -f <image_format>")
            print("-i <input_file>\t\t\t: Path of the file to be converted (PDF, PPTX, PPT, XLSX, XLS, DOC, DOCX)")
            print("-o <output_folder>\t\t\t: Folder where the converted images files will be stored")
            print("-f <image_format>\t\t\t: Format of images that will be converted (PNG/JGP)\n")
        else:
            print("Invalid arguments. Try -h or --Help for help.")
        exit(0)

    inputFile = sys.argv[2]
    outputFolder = sys.argv[4]
    imageOutputFormat = sys.argv[6]

    validateFileAndFolder(inputFile, outputFolder)

    filename, extension = returnNameAndPath(inputFile)

    try:
        if extension != "pdf":
            # Function to convert the Word/LibreOffice files to PDF
            convertToPdf(f'"{inputFile}"', f'"{outputFolder}"')

            # Function to convert PDF to the selected image format
            convertPdfToImages(f'"{outputFolder}\\{filename}.pdf"', f'"{outputFolder}\\page"', imageOutputFormat)
        else: #If the file entered is a PDF
            convertPdfToImages(f'"{inputFile}"', f'"{outputFolder}\\page"', imageOutputFormat)
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()
