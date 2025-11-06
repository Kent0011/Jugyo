## 概要
授業で使うリポジトリ.
webカメラの映像をリアルタイムで処理し表示するGUI

## 環境構築
uvを使うと楽。

1. uvをインストール
```
# macOS/Linux
$ curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
$ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
2. 依存環境を同期
```
$ uv sync
```
3. uvで実行
```
$ uv run cas_test/test.py
```

これだけ！