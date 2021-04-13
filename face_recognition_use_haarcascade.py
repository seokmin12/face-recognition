import cv2
import glob

face_cascade = cv2.CascadeClassifier('/Users/seokmin/Desktop/python/haarcascade_frontalface_default.xml')

count_num_path = '/Users/seokmin/Desktop/teachable machine/얼굴형/역삼각형 여자/가인/*.jpg'
num = len(glob.glob(count_num_path))
print(num)

for i in range(num):
    img = cv2.imread(f'/Users/seokmin/Desktop/teachable machine/얼굴형/역삼각형 여자/가인/가인{i}.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    for (x, y, w, h) in faces:
        img2 = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        cv2.imwrite(f'/Users/seokmin/Desktop/teachable machine/얼굴형/역삼각형 여자/가인 결과 흑백/가인{i}_흑백.jpg', roi_gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
