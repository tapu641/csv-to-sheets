# CSV → Googleスプレッドシート書き込み

## やりたいこと
credentials.jsonを使ってGoogleに認証し、
sample.csvの内容をスプレッドシートのA1〜C11に書き込む

---

## 使用ライブラリ

| ライブラリ | 役割 |
|---|---|
| `gspread` | スプレッドシートの読み書き操作 |
| `google.oauth2.service_account` | Googleへの認証 |
| `csv` | CSVファイルの読み込み |

---

## コード解説

### ① 認証
```python
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
gc = gspread.authorize(creds)
```
* `scope` はプログラムに与える権限の範囲（スプレッドシートとDriveへのアクセス）
* `credentials.json` を読み込んでGoogleに認証させる

### ② スプレッドシートを開く
```python
sh = gc.open_by_key(SPREADSHEET_ID)
worksheet = sh.get_worksheet(0)
```
* `SPREADSHEET_ID` はスプレッドシートのURLの中に含まれるID
* `get_worksheet(0)` で1枚目のシートを選択（0始まり）

### ③ CSVを読み込む
```python
with open("sample.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
```
* `csv.reader` で1行ずつ読み込む
* `list()` で全行をリストに変換する

### ④ スプレッドシートに書き込む
```python
worksheet.update("A1:C11", data)
```
* A1〜C11の範囲にCSVのデータを一括で書き込む

---

## 実行方法

```
docker-compose build
```
* Dockerfileを元にPython環境を構築
* requirements.txtのライブラリをインストール

```
docker-compose run app
```
* コンテナを起動
* main.pyが実行される
* スプレッドシートにCSVの内容が書き込まれる

## 参考
* [gspreadの使い方 - Qiita](https://qiita.com/plumfield56/articles/dab6230512f3381fdcad)
