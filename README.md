# von Kries Adaptation

## 轉換結果

|                           原始影像                           |                             D65                              |                            12000K                            |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="https://raw.githubusercontent.com/Petingo/von-Kries-Adaptation/master/image/test.png" alt="test" style="zoom:50%; margin: 12pt 0pt;" /> | <img src="/Users/petingo/p/auto-white-balance/result_D65.png" alt="test" style="zoom:50%; margin: 12pt 0pt;" /> | <img src="/Users/petingo/p/auto-white-balance/result_12000K.png" alt="test" style="zoom:50%; margin: 12pt 0pt;" /> |

## 說明

本次作業實作了 von Kries Adaptation，我總共寫了兩個東西，分別是：
##### vonKriesAdaptor.py
von Kries Adaptation 的函數本體，給定影像和參考白的 xyz 值，輸出轉換後的影像。範例如下：
``` python
import cv2
import numpy as np
import colour

import vonKriesAdaptor

# 利用 opencv 讀入影像
img_source = cv2.imread('test.png')

# 獲取標轉光源的參考白（a/b/c/e/d50/d55/d65/d75/icc）：
ref_white = vonKriesAdaptor.white("d65")

# 或是利用 colour 函式庫獲取某色溫對應的 xyz 值
ref_white = colour.xy_to_XYZ(colour.CCT_to_xy(6000))

# 光源轉換
img_target = vonKriesAdaptor.adapt(img_source, ref_white)
```

---

##### interactive.py

互動式的光源轉換，讀入指定影像後可輸入色溫並即時轉換與顯示。

![interactive_example](/Users/petingo/p/auto-white-balance/interactive_example.png)

