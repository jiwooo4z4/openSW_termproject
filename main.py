import os
# 팀원들이 만든 모듈 가져오기 (파일 이름과 같아야 함)
from loader import load_image
from detector import detect_faces
from processor import apply_mosaic
from saver import save_image

def main():
    # 입력 폴더와 출력 폴더 설정
    input_folder = "data"
    
    # data 폴더가 없으면 경고
    if not os.path.exists(input_folder):
        print(f"'{input_folder}' 폴더를 만들고 안에 사진을 넣어주세요!")
        return

    # 폴더 내의 모든 파일에 대해 반복
    image_files = os.listdir(input_folder)
    
    print(f"--- 총 {len(image_files)}개의 파일 처리를 시작합니다 ---")

    for filename in image_files:
        # jpg, png 파일만 처리
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
            
        full_path = os.path.join(input_folder, filename)
        
        # 1. 불러오기 (팀원 A)
        img = load_image(full_path)
        if img is None: continue
        
        # 2. 얼굴 찾기 (팀원 B)
        faces = detect_faces(img)
        
        # 3. 효과 주기 (팀원 C)
        result_img = apply_mosaic(img, faces)
        
        # 4. 저장하기 (팀원 D)
        save_image(result_img, full_path)
        
    print("--- 모든 작업이 완료되었습니다 ---")

if __name__ == "__main__":
    main()