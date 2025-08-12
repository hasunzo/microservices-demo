# 이 파일은 무시되어야 하는 테스트 파일입니다
# ignore_patterns에 "*.test.py"를 추가하면 Gemini가 검토하지 않습니다

# 의도적으로 나쁜 코드들 (무시되어야 함)
password = "admin123"  # 하드코딩된 비밀번호
def badFunction():  # 나쁜 네이밍
    pass

# SQL 인젝션 위험
query = f"SELECT * FROM users WHERE id = {user_id}"
