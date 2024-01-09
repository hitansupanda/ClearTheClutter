import os

files = os.listdir()
print(files)
files.remove("main.py")


def createifnotexsist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


createifnotexsist("Images")
createifnotexsist("Docs")
createifnotexsist("Media")
createifnotexsist("Others")

imgext = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgext]

docext = [".txt", ".pdf", ".doc", ".docx"]
document = [doc for doc in files if os.path.splitext(doc)[1].lower() in docext]

mediaext = [".mp4", ".mp3", ".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaext]

Others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (
        ext not in imgext
        and ext not in docext
        and ext not in mediaext
        and os.path.isfile(file)
    ):
        Others.append(file)


def move(foldernames, files):
    for file in files:
        os.replace(file, f"{foldernames}/{file}")


move("Images", images)
move("Media", medias)
move("Docs", document)
move("Others", Others)
