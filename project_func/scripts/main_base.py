#!/usr/bin/env python3
import prompt
import sys
sys.path.append('/home/admin/project_tsaregorodtsev_b24-505/project_func')
from cli import welcome # noqa: 402


def main():
    print('Первая попытка запустить проект!')
    name = prompt.string('May I have your name? ')
    print(name)
    welcome()


if __name__ == '__main__':
    main()
