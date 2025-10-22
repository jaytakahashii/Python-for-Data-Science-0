def echo(string: str, object: any) -> None:
  if string == "Empty":
    print(f"{string}:", type(object))
  else:
    print(f"{string}:", object, type(object))

def NULL_not_found(object: any) -> int:
  if object is None:
    echo("Nothing", object)
  elif type(object) is float and object != object:
    echo("Cheese", object)
  elif type(object) is int and object == 0:
    echo("Zero", object)
  elif object == '':
    echo("Empty", object)
  elif object is False:
    echo("Fake", object)
  else:
    print("Type not Found")

  return 1
