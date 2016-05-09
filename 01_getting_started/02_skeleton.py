# -*- coding: utf-8 -*-

"""
표준 라이브러리 import
서드 파티 라이브러리 impport
개발자 사용자 정의 모듈 import
상대경로 import는 명시적으로 import
"""
import sys, os, traceback


# 클래스 및 함수의 정의
def main():
    global options, args

    # 메인 작업 처리
    print('Hello Python!')


if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt as e:
        raise e
    except SystemExit as e:
        raise e
    except Exception as e:
        print(str(e))
        traceback.print_exc()
        os._exit(1)
