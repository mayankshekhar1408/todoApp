import PySimpleGUI as sg
import zipfile
import pathlib

def make_archive(filepaths,dest_dir):
    dest_path=pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)

label1=sg.Text("Select files to compress:")
input1=sg.Input()
choose_button1=sg.FileBrowse("Choose",key="files")

label2=sg.Text("Select destination folde29.57353*r:")
input2=sg.Input()
choose_button2=sg.FolderBrowse("Choose",key="folder")

compress_button=sg.Button("Compress")
print(sg.Text("H"))
window=sg.Window("File Compressor", layout=[[label1,input1, choose_button1],
                                            [label2,input2,choose_button2],
                                            [compress_button]])

event,values=window.read()
print(event,values)
filepaths=values["files"].split(';')
folder=values["folder"]
print(filepaths)
print(folder)
make_archive(filepaths,folder)
window.close()

