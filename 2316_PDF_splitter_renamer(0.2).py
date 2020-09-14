#! python3
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from PyPDF2 import PdfFileReader, PdfFileWriter
from datetime import datetime

def instructions():
## lines 13-14 info more accurate for earlier version
    mb.showinfo('Instructions', '''1. Make sure first that the order of the list of filenames
    matches with the page order of the scannned 2316 forms.
2. If the order of the two does not match, this app won't
    completely accomplish its task or may return an error and
    exit abruptly without warning.        
3. In case of duplicate/multiple copies in a batch of scanned
    forms, make sure to provide each copy a different/slightly
    different filename. Giving two or more files the same
    filename in the same directory will also cause the app to
    halt and suddenly exit.
4. Proceed and click the button "Open_pdf&Extract_pages"
    to open the *.pdf file for splitting and renaming.''')

def get_list():
    mb.showinfo('Get filenames', "Paste and enter in terminal window the pre-arranged list or column of filenames.")
    print('Paste and enter the filenames below:')
    mb.showinfo('Reminder', "Don't forget to hit 'Enter' after pasting filenames in terminal")
    new_filename = input()
    filenames = []
    while new_filename != '':
        filenames.append(new_filename)
        new_filename = input()

    return filenames

def callback_fd_extract_rename():  ## 'extract' may not be a totally accurate label for this function
    pdf_file = fd.askopenfile(mode='rb', title='Select *.pdf file for splitting and renaming...')
    pdf_file_dir = pdf_file.name
    while pdf_file_dir[-1] != '/':
        pdf_file_dir = pdf_file_dir.rstrip(pdf_file_dir[-1])
    new_filenames = get_list()
    print('Splitting each page of', "'" + pdf_file.name + "'", '''and extracting to
same folder/directory''', "'" + pdf_file_dir + "'", '...')
    print('')
    pdf = PdfFileReader(pdf_file)
    for page in range(pdf.getNumPages()):
        pdfWriter = PdfFileWriter()
        pdfWriter.addPage(pdf.getPage(page))
        re_name = new_filenames[page] + '.pdf'
        filepath = pdf_file_dir + new_filenames[page] + '.pdf'
        with open(filepath, 'wb') as f:
            pdfWriter.write(f)
            f.close()
        print('Page', page + 1, 'extracted and renamed as', new_filenames[page] + '.pdf', '...')
    print('All pages successfully extracted and renamed!')
    pdf_file.close()
    mb.showinfo('For info po...', "All pages successfully extracted and renamed!")
    
##    return pdf_file, pdf_file_dir

def callback_end():
    root.withdraw()
    mb.showinfo('DevInfo', """2316_PDF_splitter_renamer is being developed by:

    RFSO 8, PNP - Finance Service
    Camp Ruperto K. Kangleon,
    Barangay Campetic, Palo
    Leyte, Philippines

    For queries or feedback, contact details:
    email: rfsopro8@gmail.com
    Office phone no.: (6353) 832-4373""")
    

root = tk.Tk()    ##('2316 PDF Splitter_Renamer', '2316 PDF Splitter_Renamer')
##root.withdraw()
C = tk.Canvas(root, bg="green")   ##tk.Canvas(top, bg="green", height=250, width=300) green bg appears when background_label.place for y is altered
filename = tk.PhotoImage(file = "bg.gif")
background_label = tk.Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.iconbitmap('app.ico') ##there could be a problem here after pyinstaller compilation
root.title('2316 PDF Splitter_Renamer')
root.geometry("355x250")
##if datetime.now() < datetime(2020, 12, 31) and datetime.now() > datetime(2020, 9, 1):
b1 = tk.Button(text='(1) ReadMe', command=instructions).pack() ##pack(fill=tk.X) ## assigning b(n) for buttons intended for possibly binding values generated from buttons for future dev versions 
b2 = tk.Button(text='(2) Open_pdf&Extract_pages', command=callback_fd_extract_rename).pack() ##pack(fill=tk.X)  ##or tk.BROWSE???? create another button within callback_fd...() to determine directory where pages will be extracted
##b3 = tk.Button(text='(3) Get Filenames', command=get_list).pack(fill=tk.X)  ##tk.Entry( perhaps??? or tk.StringVar(    ...... create another mb.showinfo or another canvas?? where filenames array can be shown or pasted into...
##tk.Button(text='(4) Split *.pdf and rename', command=
b3 = tk.Button(text='Quit', command=callback_end).pack() ##pack(fill=tk.X)
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)
tk.mainloop()
