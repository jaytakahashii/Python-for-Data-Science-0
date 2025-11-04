# ft_package

A sample test package created for the 'My first package creation' exercise.

## Installation

To build the package, run the following command in the root directory of the project:

```bash
python -m build
```

if you don't have the `build` module installed, you can install it using pip:

```bash
pip install build
```

Then, you can install the package using pip:

```bash
# recommended way to install the package
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

# or
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
# Output: 2

print(count_in_list(["toto", "tata", "toto"], "tutu"))
# Output: 0
```

# License

This project is licensed under the MIT License, see the LICENSE file for details
