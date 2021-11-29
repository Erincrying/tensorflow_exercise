# 图片的读取与展示
import cv2

'''
  cv2.imread-图片读取
  cv2.imread('图片名称', 读取类型)
  读取类型：如果为0-读取灰度图片；1-读取彩色图片
'''
# D:\LearningData\deepLearning\tensorflow_exercise\img_base\image0.jpg
img = cv2.imread('./img_base/image0.jpg', 1) 



'''
  cv2.imshow-图片展示
  cv2.imshow('窗体名称', 展示内容)
'''
cv2.imshow('image', img)




'''
  stop当前程序
  只有stop了才能展示当前的图片效果
'''
cv2.waitKey(0)