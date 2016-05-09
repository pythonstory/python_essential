# -*- coding: utf-8 -*-
import sys

# 결과 예시: 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)]
print(sys.version)

# 결과 예시: sys.version_info(major=3, minor=5, micro=1, releaselevel='final', serial=0)
print(sys.version_info)

# 인스턴스로 반환하여 애플리케이션의 파이썬 버전 의존성 확인에 활용 가능
print(sys.version_info.major)