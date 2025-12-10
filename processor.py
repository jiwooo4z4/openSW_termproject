import cv2

def apply_mosaic(img, faces, ratio=0.05):
    """
    얼굴 좌표에 모자이크 처리를 하는 함수
    ratio: 모자이크 강도 (작을수록 많이 뭉개짐)
    """
    if len(faces) == 0:
        return img

    result_img = img.copy()

    for (x, y, w, h) in faces:
        # 1. 얼굴 영역(ROI) 잘라내기
        roi = result_img[y:y+h, x:x+w]
        
        # 2. 아주 작게 축소하기 (픽셀 정보 손실)
        # TODO: cv2.resize 함수를 사용해 w, h에 ratio를 곱한 크기로 줄이기
        small = cv2.resize(roi, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        
        # 3. 다시 원본 크기로 확대하기 (깨진 픽셀 상태로 확대됨)
        mosaic = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
        
        # 4. 원본 이미지에 덮어쓰기
        result_img[y:y+h, x:x+w] = mosaic

    print("[Processor] 모자이크 처리 완료")
    return result_img