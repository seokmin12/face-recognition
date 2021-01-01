import cv2
import cvlib as cv
import numpy as np
import glob

count_num_path = '/Users/seokmin/Desktop/teachable machine/얼굴형/둥근형 남자/신동/*.jpg'
num = len(glob.glob(count_num_path))
print(num)

i = -1
while True:
    i = i + 1
    if i == num:
        break

    image_path = f'/Users/seokmin/Desktop/teachable machine/얼굴형/둥근형 남자/신동/신동{i}.jpg'
    im = cv2.imread(image_path)  # 이미지 읽기
    # detect faces (얼굴 검출)
    faces, confidences = cv.detect_face(im)

    for face in faces:
        (startX, startY) = face[0], face[1]
        (endX, endY) = face[2], face[3]
        # draw rectangle over face
        cv2.rectangle(im, (startX, startY), (endX, endY), (0, 255, 0), 0)  # 검출된 얼굴 위에 박스 그리기
        face_crop = np.copy(im[startY:endY, startX:endX])

        # gender detection (성별 검출)
        (label, confidence) = cv.detect_gender(face_crop)

        print(confidence)
        print(label)

        idx = np.argmax(confidence)
        label = label[idx]

        label = "{}: {:.2f}%".format(label, confidence[idx] * 100)

        Y = startY - 10 if startY - 10 > 10 else startY + 10

        cv2.putText(im, label, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 0)  # 박스 위에 남자인지 여자인지 라벨과 확률 쓰기

        result = cv2.imwrite(f'/Users/seokmin/Desktop/teachable machine/얼굴형/둥근형 남자/신동 결과/신동{i}.jpg', face_crop)  # 이미지 쓰기

        result_img_path = f'/Users/seokmin/Desktop/teachable machine/얼굴형/둥근형 남자/신동 결과/신동{i}.jpg'
        result_img = cv2.imread(result_img_path)

        gray_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2GRAY)

        gray_result = cv2.imwrite(f'/Users/seokmin/Desktop/teachable machine/얼굴형/둥근형 남자/신동 결과 흑백/신동{i}_흑백.jpg', gray_img)
