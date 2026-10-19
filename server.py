#!/usr/bin/env python3
"""
AWS Certified AI Practitioner (AIF-C01) Local Backend Server
- Built using only Python 3 standard libraries (No external pip packages required).
- Serves static assets (HTML/CSS/JS/Docs).
- Provides REST APIs for Questions, Dynamic Docs, Exam History, and Submissions.
"""

import os
import sys
import json
import time
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORT = int(os.environ.get('PORT', 8001))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
HISTORY_FILE = os.path.join(DATA_DIR, 'history.json')
QUESTIONS_DIR = os.path.join(BASE_DIR, 'questions')
DOCS_DIR = os.path.join(BASE_DIR, 'docs')

os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=2)


class AIFExamServerHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        # API 라우팅
        if path == '/api/status':
            self.handle_api_status()
        elif path == '/api/docs':
            self.handle_api_docs(query)
        elif path == '/api/questions':
            self.handle_api_questions(query)
        elif path == '/api/history':
            self.handle_api_history()
        else:
            # 정적 파일 서빙 (루트 접근 시 index.html)
            if path == '/':
                self.path = '/index.html'
            super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/api/submit':
            self.handle_api_submit()
        elif path == '/api/history/clear':
            self.handle_api_clear_history()
        elif path == '/api/questions/add':
            self.handle_api_add_question()
        else:
            self.send_error(404, "Endpoint not found")

    # ==========================
    # API 핸들러들
    # ==========================

    def send_json_response(self, data, status_code=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def handle_api_status(self):
        """서버 상태 및 데이터베이스 요약 정보 반환"""
        total_questions = 0
        for i in range(1, 6):
            df = os.path.join(QUESTIONS_DIR, f'questions_domain{i}.json')
            if os.path.exists(df):
                with open(df, 'r', encoding='utf-8') as f:
                    total_questions += len(json.load(f))

        exam_count = 0
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                exam_count = len(json.load(f))

        self.send_json_response({
            "status": "online",
            "server": "AIF-C01 Local Backend",
            "total_questions": total_questions,
            "total_exams_taken": exam_count,
            "time": datetime.now().isoformat()
        })

    def handle_api_docs(self, query):
        """docs 디렉토리의 마크다운 내용 실시간 반환"""
        doc_key = query.get('key', [None])[0]
        file_map = {
            'overview': '00_AIF-C01_EXAM_GUIDE.md',
            'glossary': '01_GLOSSARY_KR_EN.md',
            'domain1': '02_DOMAIN_1_AI_ML_FUNDAMENTALS.md',
            'domain2': '03_DOMAIN_2_GENERATIVE_AI_FM.md',
            'domain3': '04_DOMAIN_3_FM_APPLICATIONS.md',
            'domain4': '05_DOMAIN_4_RESPONSIBLE_AI.md',
            'domain5': '06_DOMAIN_5_SECURITY_GOVERNANCE.md',
            'aws_services': '07_AWS_AI_SERVICES_CHEAT_SHEET.md'
        }

        if doc_key:
            filename = file_map.get(doc_key)
            if filename:
                filepath = os.path.join(DOCS_DIR, filename)
                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        return self.send_json_response({"key": doc_key, "content": f.read()})
            return self.send_json_response({"error": "Document not found"}, status_code=404)

        # 전체 목록 반환
        all_docs = {}
        for k, filename in file_map.items():
            filepath = os.path.join(DOCS_DIR, filename)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    all_docs[k] = f.read()
        self.send_json_response(all_docs)

    def handle_api_questions(self, query):
        """문제 세트 조회 (mock1, domain1 ~ domain5)"""
        set_name = query.get('set', ['mock1'])[0]
        file_map = {
            'mock1': 'mock_exam_1.json',
            'domain1': 'questions_domain1.json',
            'domain2': 'questions_domain2.json',
            'domain3': 'questions_domain3.json',
            'domain4': 'questions_domain4.json',
            'domain5': 'questions_domain5.json',
        }

        filename = file_map.get(set_name)
        if not filename:
            return self.send_json_response({"error": f"Unknown set name: {set_name}"}, status_code=400)

        filepath = os.path.join(QUESTIONS_DIR, filename)
        if not os.path.exists(filepath):
            return self.send_json_response({"error": f"File not found: {filename}"}, status_code=404)

        with open(filepath, 'r', encoding='utf-8') as f:
            questions = json.load(f)

        self.send_json_response({
            "set": set_name,
            "total": len(questions),
            "questions": questions
        })

    def handle_api_history(self):
        """응시 이력 목록 반환"""
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
        else:
            history = []
        self.send_json_response(history)

    def handle_api_clear_history(self):
        """응시 이력 전체 초기화"""
        try:
            with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=2)
            self.send_json_response({"status": "cleared", "message": "History has been reset"})
        except Exception as e:
            self.send_json_response({"error": str(e)}, status_code=500)

    def handle_api_submit(self):
        """시험 제출 처리 및 채점 저장"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            submission = json.loads(body.decode('utf-8'))

            # 이력 저장
            history = []
            if os.path.exists(HISTORY_FILE):
                with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                    history = json.load(f)

            submission_entry = {
                "id": f"EXAM-{int(time.time())}",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "set": submission.get("set", "unknown"),
                "mode": submission.get("mode", "unknown"),
                "total_questions": submission.get("total_questions", 0),
                "correct_count": submission.get("correct_count", 0),
                "accuracy": submission.get("accuracy", 0),
                "scaled_score": submission.get("scaled_score", 0),
                "passed": submission.get("passed", False),
                "time_spent_seconds": submission.get("time_spent_seconds", 0),
                "domain_scores": submission.get("domain_scores", {}),
                "wrong_questions": submission.get("wrong_questions", [])
            }

            history.insert(0, submission_entry)

            with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(history, f, ensure_ascii=False, indent=2)

            self.send_json_response({
                "status": "success",
                "result": submission_entry
            })
        except Exception as e:
            self.send_json_response({"error": str(e)}, status_code=500)

    def handle_api_add_question(self):
        """신규 문제 추가 API"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            q_data = json.loads(body.decode('utf-8'))

            domain = q_data.get('domain', 'Domain 1')
            domain_map = {
                'Domain 1': 'questions_domain1.json',
                'Domain 2': 'questions_domain2.json',
                'Domain 3': 'questions_domain3.json',
                'Domain 4': 'questions_domain4.json',
                'Domain 5': 'questions_domain5.json',
            }

            filename = domain_map.get(domain, 'questions_domain1.json')
            filepath = os.path.join(QUESTIONS_DIR, filename)

            questions = []
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    questions = json.load(f)

            if 'id' not in q_data:
                code_map = {'Domain 1': 'D1', 'Domain 2': 'D2', 'Domain 3': 'D3', 'Domain 4': 'D4', 'Domain 5': 'D5'}
                code = code_map.get(domain, 'D1')
                q_data['id'] = f"{code}-Q{len(questions)+1:03d}"

            questions.append(q_data)

            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(questions, f, ensure_ascii=False, indent=2)

            self.send_json_response({
                "status": "success",
                "question_id": q_data['id'],
                "file": filename
            })
        except Exception as e:
            self.send_json_response({"error": str(e)}, status_code=500)


def run_server():
    server_address = ('', PORT)
    httpd = ThreadingHTTPServer(server_address, AIFExamServerHandler)
    print("=" * 60)
    print(f"🚀 AWS Certified AI Practitioner (AIF-C01) Server Running")
    print(f"🌐 Local URL: http://localhost:{PORT}")
    print(f"📂 Workspace: {BASE_DIR}")
    print("=" * 60)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")
        httpd.server_close()


if __name__ == '__main__':
    run_server()
