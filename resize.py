'''
resize.py

Function:
    Resize the images data to a same size(100*100) and rename.

Finished in 2019/04/28
'''

from PIL import Image
import os


def get_files(dir):
    files = []
    files_dir = os.listdir(dir)
    for file in files_dir:
        if 'jpg' in file:

            files.append(file)
        else:
            continue
    return files


def resize(file, base_dir, save_dir):
    img = Image.open(base_dir + '/' + file)
    img.resize((100, 100))
    img.save(save_dir + '/' + file)
    print('Save!')



if __name__ == '__main__':
    base_dir = '/Users/dingweiqi/Desktop/datas/f'
    save_dir = '/Users/dingweiqi/Desktop/datas/projected/f'
    files = get_files(base_dir)
    for file in files:
        resize(file, base_dir, save_dir)
