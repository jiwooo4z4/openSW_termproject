import cv2
import os

def load_image(path):
    """
    경로에 있는 이미지를 불러오는 함수
    """
    # 파일이 존재하는지 확인
    if not os.path.exists(path):
        print(f"[Error] 파일이 없습니다: {path}")
        return None
    
    # TODO: cv2.imread를 사용하여 이미지 읽어오기
    # 한글 경로가 있으면 에러가 날 수 있으니 주의
    img = cv2.imread(path)
    
    if img is None:
        print("[Error] 이미지 파일을 읽을 수 없습니다.")
        return None
        
    print(f"[Loader] 이미지 로드 성공: {path}")
    return img
