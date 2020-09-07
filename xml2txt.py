import os
from os import listdir, getcwd
from os.path import join
if __name__ == '__main__':
    source_folder='VOCdevkit/VOC2020/JPEGImages/'
    dest='VOCdevkit/VOC2020/ImageSets/Main/train.txt'
    dest2='VOCdevkit/VOC2020/ImageSets/Main/val.txt'
    file_list=os.listdir(source_folder)
    train_file=open(dest,'a')
    val_file=open(dest2,'a')
    file_num=0
    for file_obj in file_list:
        file_path=os.path.join(source_folder,file_obj)

        file_name,file_extend=os.path.splitext(file_obj)

        if(file_num<96):

            train_file.write(file_name+'\n')
        else :
            val_file.write(file_name+'\n')
        file_num=file_num+1
    train_file.close()
val_file.close()
