# helper function

import re
from typing import List


def generate_regex(keywords: List[str]):
    # 使用join方法将关键词列表中的所有关键词连接在一起，并使用竖线分隔
    regex = '|'.join(map(re.escape, keywords))
    # 返回生成的正则表达式
    return regex
