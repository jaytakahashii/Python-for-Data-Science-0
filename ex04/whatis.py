import sys

def EvenOrOdd(num: int) -> str:
  if num % 2 == 0:
    return "Even"
  else:
    return "Odd"

if __name__ == "__main__":
  try:
    if len(sys.argv) == 1:
      exit()

    if len(sys.argv) > 2:
      raise AssertionError("more than one argument is provided")

    number = int(sys.argv[1])
    print(f"I'm {EvenOrOdd(number)}.")
  except ValueError:
    print("AssertionError: argument is not an integer")
  except AssertionError as e:
    print(f"AssertionError: {e}")
