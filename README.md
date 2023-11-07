# Conversions
Repo that implements convertions of PDF, PPT/PPTX, XLS/XLSX, DOC/DOCX to PNG or JPG

Note: 
- In convertions folder I have a project made on Java to make a convertion of PDF to PNG/JPG.
- In Python folder I have a code that make convertions of PDF, PPT/PPTX, XLS/XLSX, DOC/DOCX to PNG or JPG.

Python Project:
```
Converting DOC/DOCX, PPT/PPTX, XLS/XLSX files to PDF and then to PNG/JPG. Also, convert PDF files to PNG/JPG
Usage: python convertions.py -i <input_file> -o <output_folder> -f <image_format>
-i <input_file>                         : Path of the file to be converted (PDF, PPTX, PPT, XLSX, XLS, DOC, DOCX)
-o <output_folder>                      : Folder where the converted images files will be stored
-f <image_format>                       : Format of images that will be converted (PNG/JGP)
```

-------Requisites-------

Poppler and Soffice (LibreOffice runnable)

Windows Users:
- Poppler (It can be found at https://github.com/oschwartz10612/poppler-windows/releases/)
  To use it, you must add the poppler bin folder to your PATH variable, on environment variables of system.
- LibreOffice program
  To use the soffice runnable, you must install LibreOffice and then add the runnable in user PATH of environment variables. If the installation was made with default configurations, the file can be found at C:\Program Files\LibrOffice\program\soffice.

Linux Users:
- If pdftoppm is not installed natively, you must install it with the package poppler-utils
- Installation of LibreOffice program

MAC Users:
- Use brew install poppler
- Installation of LibreOffice program
