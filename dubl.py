import os


def g():
    n = input('Введите пут:')
    if os.path.isdir(n) == True:
        return n
    else:
        g()
   


def dictionary():
  pass


def duplicate():
  pass


def duplicate2():
  pass


if __name__ == '__main__':
