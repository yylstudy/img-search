import os

############### Milvus Configuration ###############
MILVUS_HOST = os.getenv("MILVUS_HOST", "127.0.0.1")
MILVUS_PORT = int(os.getenv("MILVUS_PORT", "19530"))
VECTOR_DIMENSION = int(os.getenv("VECTOR_DIMENSION", "2048"))
INDEX_FILE_SIZE = int(os.getenv("INDEX_FILE_SIZE", "1024"))
METRIC_TYPE = os.getenv("METRIC_TYPE", "L2")
DEFAULT_TABLE = os.getenv("DEFAULT_TABLE", "milvus_img_search")
TOP_K = int(os.getenv("TOP_K", "10"))

UPLOAD_PATH = os.getenv("UPLOAD_PATH", "tmp/search-images")

############### Number of log files ###############
LOGS_NUM = int(os.getenv("logs_num", "0"))

