import os

file_list = []
base_dir = '/Users/dingweiqi/Documents/datas/JSOC_20190414_017/'
files = os.listdir(base_dir)
for file in files:
    if 'jpg' in file:
        file_list.append(file)
print(file_list)

file_list.sort()

count = 1
for pic in file_list:
    os.rename(base_dir + pic, '/Users/dingweiqi/Documents/projected5/' + f'{count}.jpg')
    count += 1
