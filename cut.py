from PIL import Image
from math import *
from test import get_projected_pics

base_dir = '/Users/dingweiqi/Documents/projected4/'
pics = get_projected_pics(base_dir)
'''
    E + 
    W -
    S +
    N -
'''
lat_input = 14
lng_input = 15

for pic in pics:
    ''' 
        经度小于15度补偿100像素
        经度大于15度补偿-100像素
        经度大于20度补偿-150像素
        经度大于25度补偿-200像素
    '''
    lng = lng_input*2*pi/360
    lat = lat_input*2*pi/360
    x = 2048 * sin(lng)-100
    y = 2048 * sin(lat)
    # print(x)
    # print(y)
    img = Image.open(base_dir + pic)
    # print(img.size)
    line = 2048
    img = img.crop((line+int(x)-400, line-int(y)-400, line+int(x)+400, line-int(y)+400))
    img = img.resize((100, 100))
    img.save('/Users/dingweiqi/Documents/finished5/' + pic)
    lng_input += 0.1

