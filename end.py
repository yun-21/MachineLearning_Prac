import pandas as pd
import subprocess

def run_ollama_prompt(prompt):
    # ollama를 호출하여 프롬프트를 처리하는 명령어
    result = subprocess.run(['ollama', 'llama', '--prompt', prompt], capture_output=True, text=True)
    return result.stdout.strip()

def clean_text(text):
    # ollama로 텍스트 정제
    return run_ollama_prompt(f"Clean and standardize this text: {text}")

# 데이터 읽기
df = pd.read_csv('books.csv')

# 데이터 정제 (예: 제목과 가격 정제)
df['cleaned_title'] = df['title'].apply(clean_text)
# df['cleaned_price'] = df['price'].apply(clean_text)

# 정제된 데이터 저장
df.to_csv('cleaned_books.csv', index=False)
