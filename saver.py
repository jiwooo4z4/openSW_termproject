import cv2
import os

def save_image(img, original_filename, output_folder="output"):
    """
    변환된 이미지를 저장하는 함수
    """
    # 출력 폴더가 없으면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # 파일명 생성 (예: photo.jpg -> photo_mosaic.jpg)
    name, ext = os.path.splitext(os.path.basename(original_filename))
    new_filename = f"{name}_mosaic{ext}"
    
    save_path = os.path.join(output_folder, new_filename)
    
    # TODO: cv2.imwrite를 사용하여 이미지 저장
    success = cv2.imwrite(save_path, img)
    
    if success:
        print(f"[Saver] 저장 완료: {save_path}")
    else:
        print("[Saver] 저장 실패")
