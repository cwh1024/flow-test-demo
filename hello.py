"""flow-test-demo: 一个用来练习 GitHub 流程的小脚本。"""


def greet(name: str = "GitHub") -> str:
    return f"Hello, {name}! 试着修改这一行，然后提交一个 PR。"


if __name__ == "__main__":
    print(greet())
