import cv2
import sys
import colour
import vonKriesAdaptor
import numpy as np
import matplotlib.pyplot as plt

img_path = sys.argv[1]
print(img_path)

img_ori = cv2.imread(img_path)

fig, ax = plt.subplots(1,1)
im = ax.imshow(cv2.cvtColor(img_ori, cv2.COLOR_BGR2RGB))
fig.canvas.draw_idle()
plt.pause(0.001)
    
while True:
    k = int(input("Colour Temperature:"))
    ref_white = colour.xy_to_XYZ(colour.CCT_to_xy(k))
    img = vonKriesAdaptor.adapt(img_ori, ref_white)
    im.set_data(cv2.cvtColor(np.clip(img/255,0,1), cv2.COLOR_BGR2RGB))
    fig.canvas.draw_idle()
    plt.pause(0.001)