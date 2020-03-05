import cv2
import numpy as np
import colour
import vonKriesAdaptor

# 利用 opencv 讀入影像
img_source = cv2.imread('test.png')

# 獲取 CIE 標轉光源的參考白（a/b/c/e/d50/d55/d65/d75/icc）：
ref_white = vonKriesAdaptor.white("d65")

# 或是利用 colour 函式庫獲取某色溫對應的 xyz 值
# ref_white = colour.xy_to_XYZ(colour.CCT_to_xy(12000))

# 光源轉換
img_target = vonKriesAdaptor.adapt(img_source, ref_white)

cv2.imwrite("result.png", img_target)
cv2.imshow("result", img_target / 255)
cv2.waitKey(0)