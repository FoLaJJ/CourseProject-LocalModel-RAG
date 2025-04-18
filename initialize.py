from document_processor import DocumentProcessor
from vector_store import VectorStore
from config.settings import VECTOR_STORE_CONFIG
import shutil


def initialize_system():
    """初始化系统"""
    try:
        # 检查向量存储目录是否存在
        vector_store_path = VECTOR_STORE_CONFIG["index_path"]
        if vector_store_path.exists():
            print("检测到已存在的向量存储，是否要重新初始化？(y/n)")
            choice = input().lower()
            if choice == 'y':
                print("正在删除旧的向量存储...")
                if vector_store_path.is_file():
                    # 如果是文件，直接删除
                    vector_store_path.unlink()
                else:
                    # 如果是目录，递归删除
                    shutil.rmtree(vector_store_path)
            else:
                print("取消初始化")
                return
        
        # 创建文档处理器和向量存储实例
        print("正在初始化文档处理器...")
        document_processor = DocumentProcessor()
        vector_store = VectorStore()
        
        # 处理文档
        print("开始处理文档...")
        texts = document_processor.process_all_documents()
        
        if not texts:
            print("警告：没有找到任何文档！请确保在以下目录中放置了文档：")
            for path_type, path in document_processor.DOCUMENT_PATHS.items():
                print(f"- {path_type}: {path}")
            return
        
        print(f"成功处理了 {len(texts)} 个文档片段")
        
        # 添加到向量存储
        print("开始创建向量存储...")
        vector_store.add_documents(texts)
        
        # 保存向量存储
        print("保存向量存储...")
        vector_store.save()
        
        print("系统初始化完成！")
        
    except Exception as e:
        print(f"初始化过程中出现错误：{str(e)}")
        raise

if __name__ == "__main__":
    initialize_system() 