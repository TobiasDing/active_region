import tensorflow as tf
import numpy as np
from PIL import Image
import os
 
# 这是设置的路径，可以根据您的需要修改
image_train_path='/Users/'
label_train_path='./mnist_data_jpg/mnist_train_jpg_60000.txt'
tfRecord_train='./data/mnist_train.tfrecords'
image_test_path='./mnist_data_jpg/mnist_test_jpg_10000/'
label_test_path='./mnist_data_jpg/mnist_test_jpg_10000.txt'
tfRecord_test='./data/mnist_test.tfrecords'
data_path='./data'
# 设置长宽像素点个数
resize_height = 28
resize_width = 28
 
# 生成tfrecords文件
def write_tfRecord(tfRecordName, image_path, label_path):
    writer = tf.python_io.TFRecordWriter(tfRecordName)  # 新建一个writer
    num_pic = 0 
    f = open(label_path, 'r')
    contents = f.readlines()    # 一次全部读入，速度比较快
    f.close()   
    for content in contents:
        '''
        该目录下的文件下的txt内容为：
        0_5.jpg 5
        1_0.jpg 0
        2_4.jpg 4
        .......
        '''
        value = content.split() # 用空格分开
        img_path = image_path + value[0] 
        img = Image.open(img_path)
        img_raw = img.tobytes() # 转化为二进制文件
        labels = [0] * 10  
        labels[int(value[1])] = 1 # 设置标签位为1 
        
        # 用tf.train.Example的协议存储训练数据，训练数据的特征用键值对的形式表示
        example = tf.train.Example(features=tf.train.Features(feature={
                'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
                'label': tf.train.Feature(int64_list=tf.train.Int64List(value=labels))
                }))     # 把每张图片和标签封装到example中
        writer.write(example.SerializeToString())   # 将example序列化(把数据序列化成字符串存储)
        num_pic += 1 
        print ("the number of picture:", num_pic)
    writer.close() # 关闭writer
    print("write tfrecord successful")
 
# 产生数据集
def generate_tfRecord():
	isExists = os.path.exists(data_path)  # 判断路径是否存在
	if not isExists: # 如果不存在
		os.makedirs(data_path)   # 新建一个目录
		print ('The directory was created successfully')
	else:
		print ('directory already exists')
    # 生成tfRecords文件
	write_tfRecord(tfRecord_train, image_train_path, label_train_path)
	write_tfRecord(tfRecord_test, image_test_path, label_test_path)
 
# 解析tfrecords文件 
def read_tfRecord(tfRecord_path):
    # [tfRecord_path]为文件的路径，如果文件比较大可以写多个
    filename_queue = tf.train.string_input_producer([tfRecord_path], shuffle=True)
    reader = tf.TFRecordReader() # 新建一个reader
    _, serialized_example = reader.read(filename_queue) # 将读出的每个样本保存在serialize_example中
    features = tf.parse_single_example(serialized_example, 
                                       features={
                                        'label': tf.FixedLenFeature([10], tf.int64), # 10分类写10
                                        'img_raw': tf.FixedLenFeature([], tf.string)
                                        })  # 解序列化
    img = tf.decode_raw(features['img_raw'], tf.uint8)  # 恢复img_raw 到 img
    img.set_shape([784])  # 把img的shape设为[1,784]
    img = tf.cast(img, tf.float32) * (1. / 255) # 归一化到0-1
    label = tf.cast(features['label'], tf.float32)  # 同时把label值也设为浮点型
    return img, label 
 
# 批获取训练集或测试集的内容和标签
def get_tfrecord(num, isTrain=True):
    if isTrain: # 获取训练集，isTrain参数设置为True
        tfRecord_path = tfRecord_train
    else:       # 获取测试集，isTrain参数设置为False
        tfRecord_path = tfRecord_test
    img, label = read_tfRecord(tfRecord_path)
    # 从总样本中顺序获取capactiy组数据，打乱顺序，每次输出batch_size组，用了2个线程
    img_batch, label_batch = tf.train.shuffle_batch([img, label],
                                                    batch_size = num,
                                                    num_threads = 2,
                                                    capacity = 1000,
                                                    min_after_dequeue = 700)
    return img_batch, label_batch
 
def main():
    generate_tfRecord()
 
if __name__ == '__main__':
    main()
