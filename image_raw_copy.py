import shutil
import os
def NIKON_copy_image():
    jpg_image=r'.\jpg'
    new_nef_image=r'.\nef'
    jpgs=os.listdir(jpg_image)
    for i in jpgs:
        jpgname=os.path.splitext(i)[0]
        shutil.copy('./nef1/'+jpgname+'.NEF',new_nef_image)
def CANON_copy_image():
    jpg_image=r'.\jpg'
    new_nef_image=r'.\cr3'
    jpgs=os.listdir(jpg_image)
    for i in jpgs:
        jpgname=os.path.splitext(i)[0]
        shutil.copy('./cr31/'+jpgname+'.CR3',new_nef_image)
raw=input('raw格式为（填小写）：')
if raw=='nef':
    NIKON_copy_image()
elif raw=='cr3':
    CANON_copy_image()

