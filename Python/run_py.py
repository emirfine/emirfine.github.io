# Compiler 언어의 실행흐름 (C, C++, JAVA)
#   - 실행코드를 기계가 해독할 수 있는 언어로 변환한다음에, 실행파일을 실행 (속도가 빠르다.)


# Interpreter 언어의 실행흐름 (Python, Ruby)
#   - 코드를 순서대로 (위에서 아래로 실행)
#   - 속도가 느리다. (실행 중간에 변환까지 진행)


print('실행 1')

class Crawler:
    def __init__(self) -> None:
        pass

def crawl_func():
    return 'abc'

if __name__ == '__main__': ## 'run_py' != '__main__'
    print('이것이 실행파일일 때 실행할 코드블럭')
    crawler = Crawler()
    print(crawler)
    print(crawl_func())