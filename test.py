import os
import re

base_dir = '/Users/dingweiqi/Documents/projected/'

def get_projected_pics(base_dir):

    files = os.listdir(base_dir)
    pics = []
    for file in files:
        if 'jpg' in file:
            pics.append(file)
    def sort_key(s):
        # 排序关键字匹配
        # 匹配开头数字序号
        if s:
            try:
                c = re.findall('^\d+', s)[0]
            except:
                c = -1
            return int(c)

    pics.sort(key=sort_key, reverse=True)
    return pics

if __name__ == '__main__':
    print(get_projected_pics(base_dir))