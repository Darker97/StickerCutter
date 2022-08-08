from PIL import Image

from os import listdir
from os.path import isfile, join

from tqdm import tqdm

def SearchForFiles():
    mypath = 'images/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and (".jpg" in f or ".jpeg" in f or ".webp" in f)]

    print("files found: ", len(onlyfiles))
    return mypath,onlyfiles

def remove_white(datas):
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
            continue
        if item[0] == 248 and item[1] == 248 and item[2] == 248:
            newData.append((255, 255, 255, 0))
            continue
        newData.append(item)
    return newData

def main():
    mypath, onlyfiles = SearchForFiles()

    counter = 0
    for i in tqdm(onlyfiles):
        img = Image.open(join(mypath, i))
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = remove_white(datas)

        img.putdata(newData)
        newpath = 'cuted/'
        img.save(join(newpath,str(counter) + ".png"), "PNG")
        counter = counter + 1
