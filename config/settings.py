import os
from pathlib import Path

# 基础路径配置
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
VECTOR_STORE_DIR = BASE_DIR / "vector_store"

# 确保目录存在
DATA_DIR.mkdir(exist_ok=True)
VECTOR_STORE_DIR.mkdir(exist_ok=True)

# 文档目录配置
DOCUMENT_PATHS = {
    "ppts": DATA_DIR / "ppts",
    "pdfs": DATA_DIR / "pdfs",
    "markdown": DATA_DIR / "markdown"
}

# 向量存储配置
VECTOR_STORE_CONFIG = {
    "index_path": VECTOR_STORE_DIR / "faiss_index.pkl",
    "embedding_model": "bge-m3:latest",  # 嵌入模型名称
    "reranker_model": "linux6200/bge-reranker-v2-m3:latest",  # 重排模型名称
    "search_k": 5,  # 检索返回的文档数量
    "dimension": 1024,  # bge-m3的嵌入维度
    "base_url": "http://localhost:11434"  # Ollama API地址
}

# 模型配置
MODEL_CONFIG = {
    "local_models": {
        "deepseek-r1":"deepseek-r1:7b",
        "qwen2.5-7b-instruct": "yasserrmd/Qwen2.5-7B-Instruct-1M:latest",
        "gemma3-4b": "gemma3:4b",
        "qwen2.5-coder": "qwen2.5-coder:3b"
    }
}

# Ollama配置
OLLAMA_CONFIG = {
    "base_url": "http://localhost:11434",  # Ollama API地址
    "model_name": "yasserrmd/Qwen2.5-7B-Instruct-1M:latest",  # 使用的模型名称
    "temperature": 0.7,  # 温度参数
    "max_tokens": 2000  # 最大生成token数
}

# RAG配置
RAG_CONFIG = {
    "chunk_size": 1000,  # 文本分块大小
    "chunk_overlap": 200,  # 文本分块重叠大小
    "context_window": 4000,  # 上下文窗口大小
    "use_reranker": True  # 是否使用重排
}

# Web界面配置
WEB_CONFIG = {
    "title": "研究生课程--信息安全工程问答系统",
    "page_icon": "📚",
    "layout": "wide",
    "default_rag": True  # 默认启用RAG
}

# 创建必要的目录
for path in DOCUMENT_PATHS.values():
    path.mkdir(exist_ok=True) 