from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm  # 提出ファイルからインポート

# --------------------------
# 1. 自作の ft_tqdm のテスト
# --------------------------
for elem in ft_tqdm(range(333)):
    sleep(0.005)
    # ft_tqdmがyieldで要素を返すたびに、このブロックが実行されます。
    # ft_tqdmはyieldする直前にプログレスバーを更新します。

# --------------------------
# 2. オリジナルの tqdm のテスト (比較用)
# --------------------------
for elem in tqdm(range(333)):
    sleep(0.005)
