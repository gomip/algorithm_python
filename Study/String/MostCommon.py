# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며 구두점 또한 무시

import re
import collections
from typing import List

paragraph = "Bob hit a ball , the hit BALL flew far after it was hit."
banned = ["hit"]


def get_common( s: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', s).lower().split()
             if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


if __name__ == '__main__':
    res = get_common(paragraph, banned)
    print(res)
