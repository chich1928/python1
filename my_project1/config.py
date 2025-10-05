import os

# 取得目前檔案所在資料夾的絕對路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 指定 input.txt 的完整路徑
DATA_FILE = os.path.join(BASE_DIR, "input.txt")

# 其他設定（可擴充）
DEFAULT_LANGUAGE = "zh-TW"
ENABLE_LOGGING = True
