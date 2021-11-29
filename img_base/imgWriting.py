'''
  图片写入
  1、文件读取；2、分装格式解析；3、数据解码；4、数据加载
  现在的分装格式一般有jpg、png
'''

import cv2

# cv2.imread已经完成1、文件读取；2、分装格式解析
img = cv2.imread('./img_base/image0.jpg', 1) 

cv2.imwrite('image1.jpg', img) # cv2.imwrite('图片名称', 图片数据)，这里的图片数据是已经解析之后的数据