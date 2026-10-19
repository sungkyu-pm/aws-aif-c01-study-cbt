#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIF-C01 (AWS Certified AI Practitioner)
문서 및 문제은행 데이터를 JS 번들(portal-docs-data.js, questions-data.js)로 자동 동기화
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
QUESTIONS_DIR = os.path.join(BASE_DIR, 'questions')

def sync_docs():
    file_map = {
        'exam_guide': '00_AIF-C01_EXAM_GUIDE.md',
        'glossary': '01_GLOSSARY_KR_EN.md',
        'domain1': '02_DOMAIN_1_AI_ML_FUNDAMENTALS.md',
        'domain2': '03_DOMAIN_2_GENERATIVE_AI_FM.md',
        'domain3': '04_DOMAIN_3_FM_APPLICATIONS.md',
        'domain4': '05_DOMAIN_4_RESPONSIBLE_AI.md',
        'domain5': '06_DOMAIN_5_SECURITY_GOVERNANCE.md',
        'aws_services': '07_AWS_AI_SERVICES_CHEAT_SHEET.md'
    }

    docs = {}
    for key, filename in file_map.items():
        filepath = os.path.join(DOCS_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                docs[key] = f.read()
        else:
            print(f"Warning: {filename} does not exist!")

    js_content = f"// AWS Certified AI Practitioner (AIF-C01) Docs Bundle\nconst PORTAL_DOCS = {json.dumps(docs, ensure_ascii=False, indent=2)};\n\nif (typeof window !== 'undefined') {{\n  window.PORTAL_DOCS = PORTAL_DOCS;\n}}\n"
    
    target_path = os.path.join(BASE_DIR, 'portal-docs-data.js')
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"✓ Updated portal-docs-data.js ({len(js_content)} bytes)")

def sync_questions():
    domains = {}
    all_qs = []
    
    for i in range(1, 6):
        d_key = f"domain{i}"
        filepath = os.path.join(QUESTIONS_DIR, f"questions_domain{i}.json")
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                d_data = json.load(f)
                domains[d_key] = d_data
                all_qs.extend(d_data)
                print(f"  - Domain {i}: {len(d_data)} questions")
        else:
            domains[d_key] = []
            print(f"Warning: {filepath} missing!")

    mock_file = os.path.join(QUESTIONS_DIR, 'mock_exam_1.json')
    if os.path.exists(mock_file):
        with open(mock_file, 'r', encoding='utf-8') as f:
            mock1_data = json.load(f)
            print(f"  - Mock Exam 1: {len(mock1_data)} questions")
    else:
        mock1_data = all_qs[:65]

    exam_data = {
        "domain1": domains['domain1'],
        "domain2": domains['domain2'],
        "domain3": domains['domain3'],
        "domain4": domains['domain4'],
        "domain5": domains['domain5'],
        "mock1": mock1_data,
        "all_pool": all_qs
    }

    js_content = f"// AWS Certified AI Practitioner (AIF-C01) Full Question Bank\nconst EXAM_DATA = {json.dumps(exam_data, ensure_ascii=False, indent=2)};\n\nif (typeof window !== 'undefined') {{\n  window.EXAM_DATA = EXAM_DATA;\n}}\nif (typeof module !== 'undefined' && module.exports) {{\n  module.exports = EXAM_DATA;\n}}\n"

    target_root = os.path.join(BASE_DIR, 'questions-data.js')
    with open(target_root, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"✓ Updated questions-data.js ({len(js_content)} bytes, {len(all_qs)} questions)")

    target_cbt = os.path.join(BASE_DIR, 'cbt-app', 'questions-data.js')
    with open(target_cbt, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"✓ Updated cbt-app/questions-data.js")

if __name__ == '__main__':
    sync_docs()
    sync_questions()
