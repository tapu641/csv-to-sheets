import gspread
from google.oauth2.service_account import Credentials
import csv

# ① 認証
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
gc = gspread.authorize(creds)

# ② スプレッドシートを開く
SPREADSHEET_ID = "1gFlWw1Odc0W5QLe2PSU75J-ilmkLhgrVvDYCE29rIdo"
sh = gc.open_by_key(SPREADSHEET_ID)
worksheet = sh.get_worksheet(0)  # 1枚目のシートを選択

# ③ CSVを読み込む
with open("sample.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)

# ④ A1〜C11に書き込む
worksheet.update("A1:C11", data)

print("書き込み完了しました")

