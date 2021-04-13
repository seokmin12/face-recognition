import cv2
import cvlib as cv
import glob
import numpy as np

count_num_path = '/Users/seokmin/Desktop/teachable machine/*'
num = len(glob.glob(count_num_path))
print(num)

n = -1
for i in range(num):
    n += 1
    image_path = '/Users/seokmin/Desktop/teachable machine/가르마펌(tvN ''도깨비'').jpg'
    im = cv2.imread(image_path)  # 이미지 읽기
    # detect faces (얼굴 검출)
    faces, confidences = cv.detect_face(im)
    print(confidences)

    for face in faces:
        (startX, startY) = face[0], face[1]
        (endX, endY) = face[2], face[3]
        # draw rectangle over face
        cv2.rectangle(im, (startX, startY), (endX, endY), (0, 255, 0), 0)  # 검출된 얼굴 위에 박스 그리기
        gray_img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        face_crop = np.copy(gray_img[startY:endY, startX:endX])

        gray_result = cv2.imwrite('/Users/seokmin/Desktop/teachable machine/가르마 펌.jpg', face_crop)
