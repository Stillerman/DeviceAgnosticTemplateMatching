# Device Agnostic Mobile Automation with OpenCV

This paper will examine the task of template matching on smartphone screenshots. It is useful to be able to locate a button on the screen for mobile automation and testing purposes, but classical template matching requires the template to be taken from the same device we are searching, but ideally a single template should be able to be used for devices of any screen size and pixel density. We will be exploring multiple techniques in an attempt to locate the Snapchat add friend button on the screen.

![add_button.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQIAAABzCAYAAABzRgyAAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAUGVYSWZNTQAqAAAACAACARIAAwAAAAEAAQAAh2kABAAAAAEAAAAmAAAAAAADoAEAAwAAAAEAAQAAoAIABAAAAAEAAAECoAMABAAAAAEAAABzAAAAANQl7SoAAAIzaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA2LjAuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4xNjk8L2V4aWY6UGl4ZWxZRGltZW5zaW9uPgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjEwODA8L2V4aWY6UGl4ZWxYRGltZW5zaW9uPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KY3Ws4gAAD7NJREFUeAHtXXusFNUd/t3d+0ABoYC8CVRQ8QGiEqtWBRFBo2ikYqwmirUmUv+rfUUT9Q+baKO2f9Si/lOrYLTxVTVK5BEjokBihXrRRkVLjNwr8rpGQS57Lz3fWc69u3t3Zndn5sycnf1OspmdOa/f+c75ffM7z2k6opzQEQEi0NAIZBq69Cw8ESACGgESARsCESACQiJgIyACRIBEwDZABIiAkAjYCIgAESARsA0QASKgEOAYAZsBESACJAK2ASJABGgRsA0QASKgEGDXgM2ACBABEgHbABEgArQI2AaIABFQCLBrwGZABIgAiYBtgAgQAVoEbANEgAgoBJrTggKOVcj/RF97j96jfDxyIS217FY5mpqatEC4ZtQPVzzKX/N+bknsLU2TUpK6PZikt7dXoPC9vYYE6rYo3jVEn7pDwBBBJpMniEzG/aG4uiMCKH3vEUUAPXkSqLtWQoEbDgFYC5lsRlkN6qfIwUVXF0QAoyX/5lfKf/Tt7yKYlIkI+CGguxCwEpSFgJ9LlOA8EfQo878Hb391pSMCaUEARJBVVkLWkW6Ds0QAAoDygwToiEBaEQAZaFJImBCcIwJ0A6D8PT09wqG/tDZ/lqsQAcw0ZDNZbSGg+5CEc4oIYAHk2A1Ioh0wTwcQgGXQfNRCiFscZ4gAVkAOVkD9zmbGXXfML4UIwCJozuatgziL5wQR5HI9mgTiLDjzIgIuIwAyaG7OxiZioisLMQYAEsB4AB0RIAL9CMA6hssqMohj1CAxiwBdABSWswL9lc9/RKAUAcwqwDqwPYiYyNpHkkBpdfOeCJRHIK6xs0SIID89yPUB5aueT4lAMQJx6EvsRMCBweJK5h0RqAYBdKOhO7ZcrESgC8OBQVt1yXRTjoBN/YmNCLBZiAODKW+pLJ51BHqUVQBditrFQgT5wcEcFwtFXXtMr+EQ0FPuPdHrUixEkN9AFD2LNVwrYIGJgEJAW9cR78a1TgRaaIuDHGwZRKAREUA3O8ougnUiwAAHbYFGbKoss00EzFqcqPKwSgT6TMGITZioCs50iEC9IxClflkjgvyghr15z3qvRMpPBKJAANv2o3DWiCDPVuwURFFJTIMIeCEAPcNgfFhnbfchThmmq4zAgQMHZOfOndK1f78c6j6kTqnJyrHHDpYJE8bLiBEjKyfAEA2PAHQt7NmHVogAAxk4cpzOH4Ft27bJG6+/LuvWrZVPPvlE9u7dK22DBsmkiRNlzpw5cuWiq2T27NkyePBg/4To29AIQNegc2F2KFrZhmx7XXS91zrOX3jnnXfkL39+RFatWuVZnFNPPVWWLr1FbrjxBhk5cpRnuEb1uHLxjQOK/tqLKwc8q/WBrXRrlaOW8DjEBNuVgzorYwRRzm8GLZjL8d59d4P88f77Zc2aNb5ifvzxx/LIIw/LiqdXyA8//OAblp6NjUBYnYu8axDllEYaq/brr7+WJ//+pGzatFHtJsv5FhHmXmdnpzzzzEqZMXOmzJs3zzd8Ep7l3p5GjijeziYtXv0RMHqHA1CDuGCxfHLCF4novBHYvHmzbN68Sbq7u70Dlfh89NFHsnr1m/Ldd9+V+PCWCPQjEEb3LFgE6ScC9PG3tbfLs889q89bvOmmm+W0007rrxGPf4cPH5atW7fIjh07PEKUfwzLYcsHH8gXX3whM2bMKB+ITxseAd09CDhMEDkRwJxNu/vyyy/lwT89KC++8IIu6uo335SNmzZLa2urZ9GBS1fXfvlm1zcCQqjVYYpxz549tUazGt6vW4CM4c/ugdUqKEo8jO5F2jWAaRJGmKJSOXzT0bFTPv/88z4JMai3e/fuvvtyfzC1g40iWDcQxMEq4GnPQZBrnDjQvaDdg0iJ4IiFAxNcrMZy87XV9PlbWpqlra0tUJGGDR8uQ4a4s56gkjVgClltOBOe13AIBNXBaImgAboFqKagVs/QocfJ6DGj1Ycrau+RjT7+eBk2bHi4VsLYqUcgaNusvUX6QKk6Bj6+9GppaZGpU6fKqFGj9LRgLYhMmfJjGTd2bC1RrIX1estjPMDLr1Zh/NIJM+5gK91ay2crfFAdjJYIUsoD+/ftk65vv9WWABi3s6NTug8dKqrLzs6OomWe6AJA4aH8he6U6afI5MlTaiICrCqcMXOGHDdsWGFSdfMfylet8vopqilwLekVxjH/va5B0vVKK6nnQY3yiIkgXUyAQcA//P53ai/AugEDdaUm2MVz5/bVPcYQ4H/OOT+Rfzz1lEyZMqXP74xZs2TO3DmybVt7VesCkNZMRQLnn//TUGvJ+wSw9KdaRffLvhoSMPFdCGtkcela2i6rlY1jBD5IrVm9WjZs2KBXAALgwp9PNB0O/lg49MLzzxcFxe7CK664Qk5QXYRyg45FgdUNrICLL54nJ510UqlXIveVFNCLECrFS6QwKcw0KBFEahGkDde2QW3SgrUB338fqGgYFBw8ZMiAuGefPVsWX7NYtn/2mUraO22QxpnKgrhm8WK9PXlAQo488FL+WsTzI4rC9P3ClcvPL3yYdMvlVc/PSAQ+tXfRRXPk59dfL+++917RmMDBgwd1H79wI9DkyZPVOQLH9qWGsYGzzjpbFi5c2PfM/IGCL73lFnn/3+/Lq6+8Yh4PuE6aNEluv32ZTJs2bYBfEg/8lKpQHihYtWEL45X7X6is8Df3YdM36Zg8zX3YdE169XYlEfjU2Mknnyx3/ua3cu2O/6nVgP0bhLD2/2+P/lU+U2904+697z51mMhEfQvzDNtCTzhhqowZM8YEKbri+T333CvtH36olw4XeR69uevuu+Wyyy8v51WXz6BkRuEKC+ClfOXCFsar9N9WupXyrUd/EoFPraEPP2HCBP0rDNba2iJDhg4tfCTnnXd+0aBgkafHzemnny6XXrpAnnji8QEhjlfrBpYsuS7wAqQBCYZ84JpSgSS8ZApTVFvphpEpjriREoHSGzVQFofYyeZRzSBfNRJiNSJmJsq5fWrK8r/Kb9aZZ5bzduZZrcqI8GHf9M4U3kFBoINBXKSzBk0SUIogkicYJ+jILERGXIwxoHtx3ZJrZf36t8uWBHsLLrtsoTz++GOyTx1hhns6IlAJgaA6GC0RZBqDCDAb0NLcv1AIg39+Ow9ReTg4AguTtm7ZosYXHpVrf7ZYnTGw2rdeu7q65O677pJlv1qmzzb86quvEiGEWt/6voVSnqXpBbEQStMol6etdMvl5cqzpoA6GHHXoDGIYPz4CfpcgPb2D/WW4nPPPU9Gjx7t2RZgAeBAkrVr18hrr74qn376adUKjenFf738sqx/e73Mv3S+nnacO3euYBNS2p2tboStdF2oj6Dd1kiJwAUg4pBh/Pjxcttttwmm93Lqy7QLFizw3EgEK2D58uXy0ksv6vGAoCb+3r175J/PPScb1VTmVVdfLbfe+kuZPn269eL6vXmreeP6xa9G+FKlDZueydNWuib9ertGeooxTkjpDnDoRr2BZuTFYB8YuHQ/gfHHASYPP/SQrFjxtO/CIRO+2ivyu+SSS+TXd94pF154UbXRAoXzUrxqSAAZesWHX2kafmERvhpXmibi2Eq3GnniDtOq2kYmQPcgUosAI5ZQjDCDaXEDFya/SuMCjz22XFauXBEpCUBenHCEE5BBRPgISjXHpIUpZ5i4UMwoFDGMDI0SF7oHHQzioh0s1IIElCSI9A7H2b59u7z11luRk4ApMroYH6iBx3Vr15pHkV+9FLjcWzdI5qXp15KuC2GDlNlmnDwRBNO/SIkAhQxiltgEJ6m0cZQZPmNm0zr6Vs0qYODRdVer0lYKX8m/HB6IUyleJf9y6br0LIzuRTpGAFAwTdZdsBzXJaDilOU/W7eqAb1fSLs67diWw5kHty9bJg888KCtLJhuHSHQqo7Cc+a7BhAkE7SjUkegVxJ12oknyhlnzKq4vqBSOl7+MAMxa4GNUXREADoXlASAXuRdA51o1kqydVXb2Il4xx13yPz5863IPW7cOLn55qWKCOzOGlgRnolGjkAmpM5F3jVACdE9wG69Bth2ULFC8cXjVW+8IRs3vqd3K3Z0dOgBxFrXE4BYsBFpzJixgl2RixYtkgsuuEB+NGJERRkYIP0IhOkWAB0rRICEMU4AQqATvbdg165d6gMnXeq7Bt+rD5oekj3qOwid6juIOTUVuHvP7gGnFY1U04J66XJbq0ycOEmGDx8mxww6Ro5RhDBcrSrESsYwpiDrJT0IoB2ACMI4a0SAj3kc5kaZsnWDmQR8rARWgflfGhAkYKaDsICISl+KEO8NAi1q70vWxa4BBMR25MO5w8oqYAfBVBivRCBqBDBlCCLASyOMszaqB7nwVqMjAkTAHgLGcgybgzUigGBZ1XcJa7KELSDjE4G0IgDdgo5F4aJJxUeSbCbf1/UJQi8iQARqRABdAehWVM46EaAPQ6sgqupiOkQgjwB0KsyS4lIcrRMBMoT5EqXQpYXgPRFoJAT0yzWiLoHBLRYi0GbM0ekwkzGvRIAI1I4AdKk5G36WoDTnWIgAmcIqaOYsQin+vCcCNSEAHbJhXcdGBCgt+jUkg5rqnYGJQB8C0B1b422xEgFKhC8A2SpMH2L8QwRShoB+iSrdseViJwIURDNbxIMdtgBiukQgaQTi6FYnQgR6wAPro0kGSbcx5u84ApoEIlhCXKmYiRABhMISZHYTKlUP/RsZAdMdgK7YdtZ2H1YrOLYk5XI9ejdetXEYjgikHQHsIcCLMgYO0FAmTgSmQnNqWy62Lts87NPkxSsRcBUBvP01CcQ81e4MEaBicJAJyKCHB5q42k4pl0UEMB6A7kASZ084RQTAGF2FHtVVgIVARwQaBYH8GgFs0EumxM4RgYEBVgGsAx53ZhDhNY0I4O0PKyDpGTRnicBUOoggR0IwcPCaEgRcIQADp/NEYAQ1YwcYTOSAokGF13pCAGZ/U1P+7Q8rwCVXN0RgQIOFgHMQe4/kr+Y5r0TAVQSwSQgWQNiPkNgsX90RQSEYmhSUhQBioKVQiAz/J4kAVs7ipwlAX916+5fDpq6JoLBAeSLA6cnKUtDdh7yv6UaYa2Ec/icCQRGAosP1X9VnwzQBZPTIv3keNP2446WGCOIGjvkRgTQh4L7Nkia0WRYi4CgCJAJHK4ZiEYE4ESARxIk28yICjiJAInC0YigWEYgTARJBnGgzLyLgKAIkAkcrhmIRgTgRIBHEiTbzIgKOIkAicLRiKBYRiBMBEkGcaDMvIuAoAiQCRyuGYhGBOBEgEcSJNvMiAo4iQCJwtGIoFhGIEwESQZxoMy8i4CgCJAJHK4ZiEYE4ESARxIk28yICjiJAInC0YigWEYgTARJBnGgzLyLgKAL/BzWpfgGj66urAAAAAElFTkSuQmCC)

## Classical Template Matching

First, let us explore the classical template matching capabilities of OpenCV


```python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv.imread('SnapDataset/pixel2/IMG_0574.PNG')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('SnapDataset/pixel2/ab.png',0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    print (pt)
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

plt.imshow(img_rgb)
plt.title('Detecting Add Button')
plt.show()
```

    (147, 286)
    (147, 431)
    (147, 576)
    (147, 721)
    (147, 887)
    (147, 888)
    (147, 1054)
    (147, 1055)
    (147, 1199)
    (147, 1200)
    (147, 1344)
    (147, 1345)



    
![png](output_2_1.png)
    


As you can see, we have successfully detected the Add button on the pixel 2 screenshot (although there are a few duplicates). The challenge will be if we can detect the Add button on the other screenshots while still using the pixel 2 template. By fiddling with the threshold amount, you can see that if you lower the threshold you can still find matches.


```python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

@interact_manual(threshold=(0.4,1.0, 0.01))
def run(threshold):
    for imgPath in ['SnapDataset/Nexus7/Screenshot_20210419-153719.png', 'SnapDataset/iphoneXR/IMG_0578.PNG']:
        print ("Running for", imgPath)
        img_rgb = cv.imread(imgPath)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread('SnapDataset/pixel2/ab.png',0)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
        loc = np.where( res >= threshold)

        count = 0
        for pt in zip(*loc[::-1]):
            count += 1
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        print (count, "matches found")


        plt.imshow(img_rgb)
        plt.title('Detecting Add Button')
        plt.show()
```


    interactive(children=(FloatSlider(value=0.69, description='threshold', max=1.0, min=0.4, step=0.01), Button(de…


With enough fiddling, you can find a "tipping point" we will call the **critical threshold** that allow the template to be detected for each device

**Nexus 7** (0.64 I have 24 matches, 0.65 I have zero)

**iPhone XR** (0.60 I have 21 matches, 0.61 I have zero)

Note that the critical threshold is device specific.

## Finding the critical threshold
Now, we will adapt the code to find the critical threshold automatically!


```python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


for imgPath in ['SnapDataset/Nexus7/Screenshot_20210419-153719.png', 'SnapDataset/iphoneXR/IMG_0578.PNG']:
    print ("Running for", imgPath)
    img_rgb = cv.imread(imgPath)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('SnapDataset/pixel2/ab.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    
    # Set threshold to be the most strict it can be while still producing matches
    threshold = res.max()
    
    print ("Critical Threshold found at", threshold)
    
    loc = np.where( res >= threshold)

    count = 0
    for pt in zip(*loc[::-1]):
        count += 1
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    print (count, "matches found")


    plt.imshow(img_rgb)
    plt.title('Detecting Add Button')
    plt.show()
```

    Running for SnapDataset/Nexus7/Screenshot_20210419-153719.png
    Critical Threshold found at 0.6428843
    1 matches found



    
![png](output_6_1.png)
    


    Running for SnapDataset/iphoneXR/IMG_0578.PNG
    Critical Threshold found at 0.60761774
    6 matches found



    
![png](output_6_3.png)
    


## What happened here?
We are no longer detecting all of the buttons. This is because the critical threshold is the tipping point where the first match is able to be found. Due to slight variations in the rasterization of the graphics, all the add buttons are not uniform and will not match as well as the best matching button. We must reduce the critical threshold by some epsilon, and we will round down to 2 decimal points as a way to achieve this.


```python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import math

for imgPath in ['SnapDataset/Nexus7/Screenshot_20210419-153719.png', 'SnapDataset/iphoneXR/IMG_0578.PNG']:
    print ("Running for", imgPath)
    img_rgb = cv.imread(imgPath)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('SnapDataset/pixel2/ab.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    
    threshold = math.floor(res.max()*100)/100.0
    
    print ("Critical Threshold found at", threshold)
    
    loc = np.where( res >= threshold)

    count = 0
    for pt in zip(*loc[::-1]):
        count += 1
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    print (count, "matches found")


    plt.imshow(img_rgb)
    plt.title('Detecting Add Button')
    plt.show()
```

    Running for SnapDataset/Nexus7/Screenshot_20210419-153719.png
    Critical Threshold found at 0.64
    24 matches found



    
![png](output_8_1.png)
    


    Running for SnapDataset/iphoneXR/IMG_0578.PNG
    Critical Threshold found at 0.6
    21 matches found



    
![png](output_8_3.png)
    


## Making this useful

Now that we have a method of detecting the buttons on the screen, we need to do some modification to make it actually useful.

1. In images with no add buttons, we do not want false positives. This method as-is will lower the threshold until it finds a match no matter what.
2. Due to relaxed threshold, each button is getting detected multiple times. We would like to detect only the number of buttons on the screen with no duplications.

## Tackling #1


```python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import math

def detect(templatePath, imagePath, minThresh):
        print ("Running for", imagePath)
        img_rgb = cv.imread(imagePath)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread(templatePath,0)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

        # Enforcing lower bound of the threshold
        threshold = max(math.floor(res.max()*100)/100.0, minThresh)

        print ("Critical Threshold found at", threshold)

        loc = np.where( res >= threshold)

        count = 0
        for pt in zip(*loc[::-1]):
            count += 1
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        print (count, "matches found")


        plt.imshow(img_rgb)
        plt.title('Detecting Add Button')
        plt.show()
        
for imgPath in ['SnapDataset/Nexus7/Screenshot_20210419-153719.png', 'SnapDataset/iphoneXR/IMG_0578.PNG', 'SnapDataset/random_screenshot.png']:
    detect('SnapDataset/pixel2/ab.png', imgPath, 0.55)
    
```

    Running for SnapDataset/Nexus7/Screenshot_20210419-153719.png
    Critical Threshold found at 0.64
    24 matches found



    
![png](output_10_1.png)
    


    Running for SnapDataset/iphoneXR/IMG_0578.PNG
    Critical Threshold found at 0.6
    21 matches found



    
![png](output_10_3.png)
    


    Running for SnapDataset/random_screenshot.png
    Critical Threshold found at 0.55
    0 matches found



    
![png](output_10_5.png)
    


By enforcing a minimum threshold, we can stop the algorithm from finding false positives.

## Solving #2


```python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import math

def detect(templatePath, imagePath, minThresh, collapseRng):
        print ("Running for", imagePath)
        img_rgb = cv.imread(imagePath)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread(templatePath,0)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

        threshold = max(math.floor(res.max()*100)/100.0, minThresh)

        print ("Critical Threshold found at", threshold)

        loc = np.where( res >= threshold)

        points = []
        
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            points.append(pt)

        print (points)
        
        unique_points = []
        
        # collapse points that are within collapseRng from each other
        for point in points:
            unique = True
            for upoint in unique_points:
                if ((point[0]-upoint[0])**2 + (point[1]-upoint[1])**2)**0.5 < collapseRng:
                    unique = False
            
            if unique:
                unique_points.append(point)
            

        print(unique_points)
        print(len(unique_points))

        plt.imshow(img_rgb)
        plt.title('Detecting Add Button')
        plt.show()
        
for imgPath in ['SnapDataset/Nexus7/Screenshot_20210419-153719.png', 'SnapDataset/iphoneXR/IMG_0578.PNG', 'SnapDataset/random_screenshot.png']:
    detect('SnapDataset/pixel2/ab.png', imgPath, 0.55, 5)
```

    Running for SnapDataset/Nexus7/Screenshot_20210419-153719.png
    Critical Threshold found at 0.64
    [(928, 263), (929, 263), (928, 395), (929, 395), (928, 527), (929, 527), (928, 659), (929, 659), (928, 791), (929, 791), (928, 923), (929, 923), (928, 1055), (929, 1055), (928, 1187), (929, 1187), (928, 1319), (929, 1319), (928, 1451), (929, 1451), (928, 1583), (929, 1583), (928, 1715), (929, 1715)]
    [(928, 263), (928, 395), (928, 527), (928, 659), (928, 791), (928, 923), (928, 1055), (928, 1187), (928, 1319), (928, 1451), (928, 1583), (928, 1715)]
    12



    
![png](output_12_1.png)
    


    Running for SnapDataset/iphoneXR/IMG_0578.PNG
    Critical Threshold found at 0.6
    [(558, 391), (559, 391), (558, 525), (559, 525), (558, 659), (559, 659), (558, 793), (559, 793), (558, 927), (559, 927), (558, 1061), (559, 1061), (558, 1195), (559, 1195), (558, 1329), (559, 1329), (558, 1463), (559, 1463), (558, 1597), (559, 1597), (559, 1731)]
    [(558, 391), (558, 525), (558, 659), (558, 793), (558, 927), (558, 1061), (558, 1195), (558, 1329), (558, 1463), (558, 1597), (559, 1731)]
    11



    
![png](output_12_3.png)
    


    Running for SnapDataset/random_screenshot.png
    Critical Threshold found at 0.55
    []
    []
    0



    
![png](output_12_5.png)
    


# Putting it all together

Now that we have worked out the issues in the code, lets make the function useful by having it output all the matches in JSON format


```python
import cv2 as cv
import numpy as np
import math
import json

def detect(templatePath, imagePath, minThresh, collapseRng):
        img_rgb = cv.imread(imagePath)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread(templatePath,0)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

        threshold = max(math.floor(res.max()*100)/100.0, minThresh)

        loc = np.where( res >= threshold)

        points = []
        
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            points.append(pt)
        
        unique_points = []
        
        # collapse points that are within collapseRng from each other
        for point in points:
            unique = True
            for upoint in unique_points:
                if ((point[0]-upoint[0])**2 + (point[1]-upoint[1])**2)**0.5 < collapseRng:
                    unique = False
            
            if unique:
                # Add to list and convert int64 tuple to int array
                unique_points.append([int(point[0]), int(point[1])])
            
        print(json.dumps(unique_points))

        
for imgPath in ['SnapDataset/Nexus7/Screenshot_20210419-153719.png', 'SnapDataset/iphoneXR/IMG_0578.PNG', 'SnapDataset/random_screenshot.png']:
    print("\n\n\n OUTPUT FOR", imgPath, "\n\n\n")
    detect('SnapDataset/pixel2/ab.png', imgPath, 0.55, 5)
```

    
    
    
     OUTPUT FOR SnapDataset/Nexus7/Screenshot_20210419-153719.png 
    
    
    
    [[928, 263], [928, 395], [928, 527], [928, 659], [928, 791], [928, 923], [928, 1055], [928, 1187], [928, 1319], [928, 1451], [928, 1583], [928, 1715]]
    
    
    
     OUTPUT FOR SnapDataset/iphoneXR/IMG_0578.PNG 
    
    
    
    [[558, 391], [558, 525], [558, 659], [558, 793], [558, 927], [558, 1061], [558, 1195], [558, 1329], [558, 1463], [558, 1597], [559, 1731]]
    
    
    
     OUTPUT FOR SnapDataset/random_screenshot.png 
    
    
    
    []


# Conclusion

We have been able to successfully identify the coordinates of all add buttons on the screen by finding a critical threshold that does not trigger false negatives or positives. The same algorithm with the same template can be applied across all devices, operating systems, and screen sizes! 

|Issue|Solution|
|-----|--------|
|Critical threshold too strict|reduce the critical threshold by some epsilon (we used rounding down as a stand in)|
|Matches always found even when there are none|Set a lower bound on possible critical threshold|
|Matches show up in bunches|Collapse matches that are within the `collapseRng`|

The programmer must decide on the minimum threshold and collapseRng values, but those values once found have been working across all device types, so this is a truely device agnostic template matching algorithm!


```python

```
