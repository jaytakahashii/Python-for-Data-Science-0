# ft_package

A sample test package created for the 'My first package creation' exercise.

## Installation

```bash
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
