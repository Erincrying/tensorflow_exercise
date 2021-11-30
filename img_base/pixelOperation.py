'''
  像素操作：像素的读取与写入
'''
import cv2

img = cv2.imread('./img_base/image0.jpg', 1) 
(b,g,r) = img[10,10] # opencv中读取是bgr
print(b,g,r, 'b,g,r')

# 从（10,100）到（110,100）进行读取
for i in range(1, 100): # 总共100个像素点
  # 写入一列蓝色
  img[10+i, 100] = (255, 0, 0) # bgr的形式，蓝色占比1，所以总体是蓝色

cv2.imshow('image', img)

cv2.waitKey(0) # 这里也可以给别的值，代表经过一定ms后，当前程序自动执行
