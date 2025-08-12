# 🧪 Gemini Code Assist 기능 테스트용 파일
# 다양한 심각도의 문제들을 포함하여 설정 테스트

import os
import subprocess
import hashlib
import requests  # 보안 취약점 테스트용

# ❌ CRITICAL: 하드코딩된 비밀번호 (보안 문제)
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

# ❌ HIGH: SQL 인젝션 취약점
def get_user_by_id(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL 인젝션 위험
    return execute_query(query)

# ❌ HIGH: 메모리 누수 위험
def memory_leak_function():
    data = []
    while True:  # 무한 루프
        data.append("x" * 1000000)  # 메모리 계속 증가
        if len(data) > 1000:
            break
    return data

# ❌ MEDIUM: 비효율적인 코드
def inefficient_search(items, target):
    result = []
    for i in range(len(items)):  # range(len()) 안티패턴
        for j in range(len(items)):  # O(n²) 복잡도
            if items[i] == target:
                result.append(items[i])
    return result

# ❌ MEDIUM: 예외 처리 부족
def risky_file_operation(filename):
    file = open(filename, 'r')  # 파일 닫지 않음, 예외 처리 없음
    content = file.read()
    return content.upper()

# ❌ LOW: 네이밍 컨벤션 위반
def CalculateSum(a,b):  # 함수명이 PascalCase
    return a+b  # 공백 없음

# ❌ LOW: 매직 넘버 사용
def calculate_tax(amount):
    return amount * 0.1  # 매직 넘버

# ✅ 올바른 코드 (비교용)
def proper_function(items: list, target: str) -> list:
    """
    올바르게 작성된 함수 예시
    
    Args:
        items: 검색할 아이템 리스트
        target: 찾을 대상
        
    Returns:
        매칭되는 아이템들의 리스트
    """
    try:
        return [item for item in items if item == target]
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

# 🔧 설정 테스트용 함수들
class ConfigTester:
    def test_severity_threshold(self):
        """comment_severity_threshold: MEDIUM 테스트"""
        pass
    
    def test_max_comments(self):
        """max_review_comments: -1 테스트"""
        pass
    
    def test_fun_feature(self):
        """have_fun: true 테스트 - 시 생성 확인용"""
        print("🎭 This function tests the fun feature!")
        return "poetry"

# 🎯 특정 보안 취약점들
def insecure_random():
    """의사 난수 생성기 사용 (보안 취약)"""
    import random
    return random.random()  # 암호학적으로 안전하지 않음

def command_injection_risk(user_input):
    """명령어 인젝션 위험"""
    os.system(f"echo {user_input}")  # 사용자 입력 직접 실행

def unsafe_deserialization(data):
    """안전하지 않은 역직렬화"""
    import pickle
    return pickle.loads(data)  # 임의 코드 실행 가능

# 🔥 성능 문제들
def performance_issue_1():
    """문자열 연결 성능 문제"""
    result = ""
    for i in range(10000):
        result += str(i)  # 비효율적인 문자열 연결
    return result

def performance_issue_2(data):
    """중복 계산"""
    results = []
    for item in data:
        expensive_calculation = sum(range(1000))  # 반복적으로 동일한 계산
        results.append(item * expensive_calculation)
    return results

# 📝 문서화 부족
def undocumented_function(x, y, z):
    return (x + y) * z

# 🧹 코드 품질 문제들
def code_quality_issues():
    a=1;b=2;c=3  # 세미콜론 사용, 공백 없음
    if a==1:print("bad formatting")  # 나쁜 포맷팅
    
    # 중복 코드
    if a > 0:
        print("positive")
        result = a * 2
        return result
    else:
        print("not positive")  
        result = a * 2  # 중복
        return result
