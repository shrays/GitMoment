PRINT_SMILEY=True # Set to false to not print smiley face

"""
Runs func, then prints a smiley if necessary.
Intended to be used as a decorator (@print_with_smiley)
"""
def print_with_smiley(func):
  def wrapper():
    func()
    if PRINT_SMILEY:
      print(f"\033[F\033[{len('Hello, World!')}G :)")

  return wrapper


@print_with_smiley
def main():
  print('Hello, World!')

if(__name__ == "__main__"):
  main()
