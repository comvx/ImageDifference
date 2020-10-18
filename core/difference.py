from PIL import Image



def image_entropy(img):
    histogram = img.histogram()
    histogram_length = sum(histogram)
    samples_probability = [float(h) / histogram_length for h in histogram]
    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])


image = Image.open(str(input("enter path: ")))
imageContent = image.load()
xWidth, yHeight = image.size
totalSize = xWidth * yHeight
rColor = 0.0
rWcolor = 0.0
gColor = 0.0
gWcolor = 0.0
bColor = 0.0
bWcolor = 0.0

count = 0
outputImageData = list()

for x in range(xWidth):
    for y in range(yHeight):
        count += 1
        rgb = str(imageContent[x,y])
        rgb = rgb.replace("(", "").replace(")", "").replace(" ", "")
        rgb = rgb.split(",")
        rColor += int(rgb[0])
        rWcolor += int(rgb[0]) / 255
        gColor += int(rgb[1])
        gWcolor += int(rgb[1]) / 255
        bColor += int(rgb[2])
        bWcolor += int(rgb[2]) / 255

rColor /= totalSize
gColor /= totalSize
bColor /= totalSize
rWcolor /= totalSize
gWcolor /= totalSize
bWcolor /= totalSize

img = ImageChops.difference(img1,img1)
img.save('test_diff1.png')


outputImageData.append([rColor, gColor, bColor, ((rColor+gColor+bColor)/3)], [rWcolor, gWcolor, bWcolor, ((rWcolor+gWcolor+bWcolor)/3)], [])
print(outputImageData)

        