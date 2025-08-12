# 🧪 Gemini Code Assist 설정 테스트 가이드

## 📋 테스트 파일 설명

### `test_gemini_features.py`
다양한 심각도의 문제를 포함한 메인 테스트 파일:

#### 🔴 CRITICAL 문제들
- 하드코딩된 비밀번호 (`DATABASE_PASSWORD`, `API_KEY`)
- SQL 인젝션 취약점 (`get_user_by_id`)
- 명령어 인젝션 위험 (`command_injection_risk`)

#### 🟠 HIGH 문제들  
- 메모리 누수 위험 (`memory_leak_function`)
- 안전하지 않은 역직렬화 (`unsafe_deserialization`)
- 성능 문제 (`performance_issue_1`, `performance_issue_2`)

#### 🟡 MEDIUM 문제들
- 비효율적인 알고리즘 (`inefficient_search`)
- 예외 처리 부족 (`risky_file_operation`) 
- 파일 리소스 누수

#### 🟢 LOW 문제들
- 네이밍 컨벤션 위반 (`CalculateSum`)
- 매직 넘버 사용 (`calculate_tax`)
- 포맷팅 문제

### `.gemini/styleguide.md`
커스텀 스타일 가이드로 Gemini가 참고할 규칙들 정의

### `should_be_ignored.test.py`
`ignore_patterns` 테스트용 파일 (무시되어야 함)

## 🔧 설정 파일들

### 현재 설정 (`config.yml`)
```yaml
have_fun: true                     # 재미있는 기능 활성화
comment_severity_threshold: MEDIUM # 보통 이상만 표시
max_review_comments: -1           # 무제한 댓글
```

### 엄격한 설정 (`config_strict.yml`)
```yaml
comment_severity_threshold: LOW   # 모든 문제 표시
max_review_comments: 5           # 최대 5개 댓글
ignore_patterns: ["*.test.py"]   # 테스트 파일 무시
```

### 최소 설정 (`config_minimal.yml`)
```yaml
comment_severity_threshold: CRITICAL  # 심각한 문제만
summary: false                       # 요약 비활성화
```

## 🧪 테스트 시나리오

### 1. 기본 설정 테스트
1. `test_gemini_features.py`로 풀 요청 생성
2. Gemini가 MEDIUM 이상 문제들을 찾는지 확인
3. `have_fun: true`로 인한 재미있는 요소 확인

### 2. 심각도 임계값 테스트
1. `config.yml`의 `comment_severity_threshold`를 변경
   - `LOW`: 모든 문제 표시
   - `HIGH`: 중요한 문제만 표시
   - `CRITICAL`: 심각한 문제만 표시

### 3. 댓글 수 제한 테스트
1. `max_review_comments`를 `3`으로 변경
2. 3개 이상의 문제가 있어도 3개만 표시되는지 확인

### 4. ignore_patterns 테스트
1. `ignore_patterns: ["*.test.py"]` 추가
2. `should_be_ignored.test.py`가 검토에서 제외되는지 확인

### 5. 스타일 가이드 테스트
1. `styleguide.md`의 규칙들이 검토에 반영되는지 확인
2. 커스텀 규칙에 따른 피드백 확인

## 🎯 예상 결과

### CRITICAL 문제들
- 하드코딩된 크리덴셜 경고
- SQL/명령어 인젝션 위험 지적
- 보안 취약점 수정 제안

### HIGH 문제들  
- 메모리 누수 위험 경고
- 성능 최적화 제안
- 리소스 관리 개선 제안

### MEDIUM 문제들
- 알고리즘 효율성 개선 제안
- 예외 처리 추가 권장
- 코드 구조 개선 제안

### LOW 문제들
- 네이밍 컨벤션 수정 제안
- 포맷팅 개선 제안
- 코드 스타일 통일 권장

## 📝 테스트 명령어

풀 요청에서 사용할 수 있는 명령어들:

```bash
/gemini summary          # 변경사항 요약
/gemini review          # 상세 코드 검토  
/gemini help            # 도움말 표시
/gemini 보안 관점에서 검토해주세요  # 맞춤 요청
```

## 🔄 설정 변경 방법

1. `.gemini/config.yml` 파일 수정
2. 변경사항을 커밋하고 푸시
3. 새로운 풀 요청 생성하여 테스트

이 가이드를 따라 Gemini Code Assist의 다양한 기능들을 체계적으로 테스트해보세요! 🚀
