import os
import numpy as np
from pycocotools.coco import COCO
import cv2
from matplotlib import pyplot as plt


def bgr2rgb(img):
    # 用cv自带的分割和合并函数
    B, G, R = cv2.split(img)
    return cv2.merge([R, G, B])


def coco_intruscapes():
    # 构建验证集
    root_path = '/data/szy4017/data/intruscapes'

    # 获取标注信息
    annFile_path = os.path.join(root_path, 'annotations', 'instances_train.json')
    coco = COCO(annFile_path)
    print(coco)

    # 获取类别标签信息
    print(coco.getCatIds())
    categories = coco.loadCats(coco.getCatIds())
    print(categories)
    names = [cat['name'] for cat in categories]
    print(names)
    catIds = coco.getCatIds(catNms='pedestrian')
    staIds = coco.getStaIds()
    print(staIds)
    print(catIds)
    imgIds = coco.getImgIds(catIds=catIds)
    print(imgIds)
    img_info = coco.loadImgs(imgIds[np.random.randint(0, len(imgIds))])
    img_info = img_info[0]
    print(img_info)

    imgFile_path = os.path.join(root_path, 'images', 'train', img_info['file_name'])
    print(imgFile_path)
    img = cv2.imread(imgFile_path)
    plt.imshow(bgr2rgb(img))
    annIds = coco.getAnnIds(imgIds=img_info['id'])
    print(annIds)
    anns = coco.loadAnns(annIds)
    print(anns)
    anns[0]['score'] = 0.99
    print(anns)
    print(anns[0]['bbox'])
    coco.showIntrusion(anns, simple_type=True)

    plt.show()


if __name__ == '__main__':
    coco_intruscapes()