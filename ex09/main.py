# test_script.py
from ft_package import count_in_list

# 課題のテストケース
print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0

# 別のテストケース（例外処理の確認）
print(count_in_list(12345, "tutu"))  # output: 0 (and an error message)
