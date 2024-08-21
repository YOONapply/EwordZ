import firebase_admin
from firebase_admin import credentials, storage
import json

# Firebase 인증 및 초기화
cred = credentials.Certificate('ewordz-dynamic-firebase-adminsdk-fy91u-833bab29a8.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'ewordz-dynamic.appspot.com'
})

# Firebase Storage 버킷 참조
bucket = storage.bucket()

# 로컬 JSON 파일 읽기 및 수정
local_file_path = 'test.json'
with open(local_file_path, 'r') as file:
    data = json.load(file)

# JSON 데이터 수정 (예: 특정 필드 업데이트)
data['new_field'] = 'new_value'

# 수정된 JSON 파일 저장
with open(local_file_path, 'w') as file:
    json.dump(data, file, indent=4)

# 수정된 JSON 파일을 Firebase Storage에 업로드
blob = bucket.blob('test.json')  # 업로드할 파일 경로 및 이름
blob.upload_from_filename(local_file_path)

print(f"File '{local_file_path}' uploaded to Firebase Storage as 'test.json'.")
