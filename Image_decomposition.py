import sys
import cv2 as cv
import numpy as np

def main(argv):

    default_file = 'test.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1

    def resize_img(img):
        scale_percent = 500 / img.shape[1]
        w = int(img.shape[1] * scale_percent)
        h = int(img.shape[0] * scale_percent)
        dim = (w, h)
        new_img = cv.resize(img, dim)
        return new_img

    new_img = resize_img(src)


    gray = cv.cvtColor(new_img, cv.COLOR_BGR2GRAY)

    gray = cv.medianBlur(gray, 5)

    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=100, param2=30,
                              minRadius=1, maxRadius=70)

    circle_img = new_img
    numero_piece = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            '''''''''
            center = (i[0], i[1])
            
            # circle center
            cv.circle(circle_img, center, 1, (0, 100, 100), 3)
            # circle outline
            '''''''''
            radius = i[2]
            '''''''''
            cv.circle(circle_img, center, radius, (255, 0, 255), 3)
            '''''''''
            img_name = str ('piece' + str(numero_piece))
            img_cropped = new_img[i[1]-(radius+5):i[1]+(radius+5),i[0]-(radius+5):i[0]+(radius+5),]
            numero_piece += 1
            cv.imshow(img_name, img_cropped)
            cv.imwrite(img_name + '.jpg', img_cropped)




    cv.imshow("detected circles", circle_img)

    cv.waitKey(0)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
