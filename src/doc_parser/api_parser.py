from markitdown import MarkItDown
import os

# src_path = "/root/NetAutoTest/data/raw_documents/API_docs/TesterLibrary.html"
src_path = "/root/NetAutoTest/data/raw_documents/API_docs/testerlibrary.pdf"
dst_path = "/root/NetAutoTest/data/raw_documents/API_docs/TesterLibrary.md"



markitdown = MarkItDown()
# print(f"src_path: {src_path}, path: {path}, filename: {filename}")
result = markitdown.convert(src_path)
with open(dst_path, 'w', encoding='utf-8') as f:
    f.write(result.text_content)