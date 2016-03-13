__author__ = 'mjob'

import math, cv2, glob

def drawClock(name):
    img = cv2.imread(name)
    overlay = img.copy()
    date = name.rsplit('.', 1)[0]
    time = date.split('.', 1)[1].split('-')

    seconds = int(time[2]) + 60.0 * ( int(time[1]) + 60 * int(time[0])) % (12 * 3600)

    small = seconds / ( 12 * 3600 )
    big   = seconds % 3600 / 3600

    small_degree = math.radians((1 - small) * 360)
    big_degree = math.radians((1 - big) * 360)

    x = img.shape[0]
    y = img.shape[1]
    radius = int(math.floor(x / 20))
    thickness = int(math.floor(radius / 10))
    small_radius = int(math.floor(radius * .8))
    smallest_radius = int(math.floor(radius * .4))
    small_thickness = int(thickness * .5)
    margin = int(math.floor(x * 0.1))
    center = (y - margin, x - margin)

    cv2.circle(overlay, center, radius, (255, 255, 255), thickness)

    x_end = math.sin(big_degree) * small_radius
    y_end = math.cos(big_degree) * small_radius

    x_end2 = math.sin(small_degree) * smallest_radius
    y_end2 = math.cos(small_degree) * smallest_radius

    center_end = (center[0] - int(x_end), center[1] - int(y_end))
    center_end2 = (center[0] - int(x_end2), center[1] - int(y_end2))

    cv2.line(overlay, center, center_end, (255, 255, 255), small_thickness)
    cv2.line(overlay, center, center_end2, (255, 255, 255), small_thickness)

    opacity = 0.4
    cv2.addWeighted(overlay, opacity, img, 1 - opacity, 0, img)

    cv2.imwrite(date + '-clock.jpg', img)

files = glob.glob('*.jpg')

filesToProcess = []

for file in files:
    if '-clock.jpg' not in file and file.replace('.jpg', '-clock.jpg') not in files:
        #print("\tappend " + file)
        filesToProcess.append(file)

total = len(filesToProcess)
i = 1

print("%i file(s) to process" % total)
for file in filesToProcess:
    print('%i/%i draw %s' % (i, total, file))
    drawClock(file)
    i += 1