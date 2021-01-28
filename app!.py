
import os
import shutil


image_formats = ["jpg", "png", "jpeg", "tiff", "webp", "gif", "bmp", "jfif"]
audio_formats = ["mp3", "m4a", "wav"]
video_formats = ["mp4", "avi", "webm", "mov", "wmv", "avi"]
doc_formats = ["txt", "docx", "doc", "html", "pdf", "ppt", "pptx", "xls", "xlsx"]
photoshop_formats = ["psd"]
videditing_formats = ["wfp", "aep", "prproj"]

while True:
    files = os.listdir("./")

    for file in files:
        if os.path.isfile(file) and file != "app!.py":
            ext = (file.split(".")[-1]).lower()
        
            if ext in image_formats:
                shutil.move(file,"Images/"+file)
            elif ext in audio_formats:
                shutil.move(file,"Audios/"+file)
            elif ext in video_formats:
                shutil.move(file,"Videos/"+file)
            elif ext in doc_formats:
                shutil.move(file,"Documents/"+file)
            elif ext in photoshop_formats:
                shutil.move(file,"PSD files/"+file)
            elif ext in videditing_formats:
                shutil.move(file,"Video Editing files/"+file)
            else:
                shutil.move(file,"other stuff/"+file) 