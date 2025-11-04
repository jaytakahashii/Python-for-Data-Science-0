# Python-for-Data-Science-0

## check the require tool

### brew

```bash
brew --version
```

if not installed, install it via:

```bash
curl -fsSL https://rawgit.com/gcamerli/42brew/master/set.sh | zsh
```

### pyenv

```bash
pyenv --version
```

if not installed, install it via brew:

```bash
brew install pyenv
```

## set the python version

### check the python version and already installed versions

```bash
pyenv versions
```

### install the required python version

```bash
pyenv install 3.10.0
```

### set the local python version

```bash
pyenv local 3.10.0
```

### check the python version

```bash
python --version
```

## create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## install the required packages

```bash
pip install -r requirements.txt
```
