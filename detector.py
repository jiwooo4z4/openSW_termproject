import cv2

def detect_faces(img):
    """
    이미지에서 얼굴을 찾아 좌표(x, y, w, h) 리스트를 반환하는 함수
    """
    if img is None:
        return []

    # 성능을 위해 흑백으로 변환 (인식률 향상)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # OpenCV 내장 얼굴 인식 모델 로드 (Haar Cascade)
    # 깃허브에 'haarcascade_frontalface_default.xml' 파일이 필요할 수도 있음
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # TODO: detectMultiScale 함수 파라미터(scaleFactor 등)를 조정해서 인식률 높여보기
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"[Detector] 발견된 얼굴 수: {len(faces)}")
    return faces