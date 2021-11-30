'''
  jpg不同图片质量保存
  有损压缩
'''
import cv2

img = cv2.imread('./img_base/image0.jpg', 1) 
'''
  cv2.imwrite('图片名称', 图片数据, [压缩方式， 压缩比])
  这里的图片数据是已经解析之后的数据
  图片质量范围是[0,100]
'''
cv2.imwrite('imageTest.jpg', img, [cv2.IMWRITE_JPEG_CHROMA_QUALITY, 0])


'''
  png不同图片质量保存
  无损压缩
  并且可以设置透明度
'''
img = cv2.imread('./img_base/image0.jpg', 1) 
'''
  cv2.imwrite('图片名称', 图片数据, [压缩方式， 压缩比])
  这里的图片数据是已经解析之后的数据
  压缩比范围是[0,9]
'''
cv2.imwrite('imageTest.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])