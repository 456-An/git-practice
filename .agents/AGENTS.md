# 專案說明
這是一個 Python 工具庫練習專案，包含：
- calculator.py：四則運算與次方計算
- string_utils.py：字串處理工具函數
- debug_challenge.py：除錯練習

## 程式設計規範
- 所有函數必須有 type hints
- 使用 raise 而不是 return 錯誤字串
- 不在函數內使用 print
- 內部工具函數使用 type hints 做型別約束，不需要 isinstance() runtime 型別檢查

## Git 規範
遵守業界主流的 commit message 規範叫 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)：
```text
<type>: <description>

常見的 type：
feat:     新功能
fix:      修 bug
docs:     文件
refactor: 重構（不改功能）
chore:    雜事（設定檔、依賴更新）
test:     測試
```

```text
範例：
git commit -m "feat: add user login page"
git commit -m "fix: resolve crash on empty input"
git commit -m "docs: update API documentation"
```

## 禁止事項
- 禁止不跟使用者確認規格就自行執行任務內容
- 禁止改動與該任務不相關的程式碼、檔案
