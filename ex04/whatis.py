import sys

def EvenOrOdd(num: int) -> bool:
  Even: bool = True
  Odd: bool = False
  if num % 2 == 0:
    return Even
  else:
    return Odd

if __name__ == "__main__":
  if len(sys.argv) == 1:
    sys.exit(0)

  if len(sys.argv) != 2:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)

  try:
    number = int(sys.argv[1])
  except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)

  if EvenOrOdd(number):
    print("I'm Even.")
  else:
    print("I'm Odd.")
