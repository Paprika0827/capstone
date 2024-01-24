import torch
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

def picture_dotting(img_path,img_name,cordinations,classes):
    points = []
    colors = ['red','blue']
    for i in range(len(cordinations)):
        cord = cordinations[i]
        cord = (((cord[0]+cord[2])/2).item(),((cord[1]+cord[3])/2).item())
        color = colors[int(classes[i].item())]
        points.append((cord,color))
    img = Image.open(img_path)
    #img = img.rotate(90)
    draw = ImageDraw.Draw(img)
    for point, color in points:
        draw.rectangle((point[0]-4, point[1]-4, point[0]+4, point[1]+4), fill=color)
    path = f'./dottedResults/dotted_{img_name}.jpg'
    img.save(path)    
    img_show = np.asarray(img)
    plt.imshow(img_show)
    
    