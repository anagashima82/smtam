---
marp: true
theme: custom
footer: "**SAMURAI** __データベース基礎講座 ワーク集__"
paginate: true

title: "データベース基礎講座 ワーク集"
subtitle: "SQL学習用演習問題"
author: "SAMURAI"
date: "2025-11-01"

---

<!-- _class: title -->

# データベース基礎講座
## ワーク集

---

<!-- _class: title-top -->

## ワーク集の使い方

各ワークは、講義で学んだ内容を実際に手を動かして確認するための演習問題です。

<div style="margin-top: 30px; padding: 20px; background-color: #FFE5E5; border-radius: 10px;">

**推奨の進め方**：順番に取り組み、わからない場合は講義資料を振り返りましょう。

</div>

---

<!-- _class: title -->

# 1章 データベースの概要を学ぼう
## ワーク

---

<!-- _class: title-top -->

## 1章 ワーク1: 用語の理解

以下の用語について、簡潔に説明してください。

1. **データベース（DB）**
2. **DBMS**
3. **SQLクエリ**

<div style="margin-top: 50px; padding: 20px; background-color: #FCEEF0; border-radius: 10px;">

**ヒント**: 講義資料の1章を振り返りながら、自分の言葉で説明してみましょう。

</div>

---

<!-- _class: title-top -->

## 1章 ワーク1: チャレンジ問題

### 実務シナリオ

あなたは新しいプロジェクトのデータベース選定を任されました。以下の要件を考慮して、リレーショナルデータベース（MySQL）を選ぶべき理由を3つ挙げてください。

**要件**:
- 顧客情報と注文履歴を関連付けて管理したい
- データの整合性が重要（二重注文の防止など）
- 複数の担当者が同時にデータを更新する可能性がある

---

<!-- _class: title-top -->

## 1章 ワーク1: 解答例

1. **データベース（DB）**
   - 複数のデータをまとめて扱いやすくしたもの
   - 大量の複雑なデータを効率的に保存・管理できる

2. **DBMS**
   - Database Management System（データベース管理システム）の略
   - データベースの構築や操作を行うソフトウェア
   - 例: MySQL、PostgreSQL、Oracle Database など

3. **SQLクエリ**
   - データベースに対する命令文
   - クエリ（query）は「問い合わせ」という意味
   - データの取得・追加・更新・削除などを行う

---

<!-- _class: title-top -->

## 1章 ワーク1: チャレンジ問題の解答例

**リレーショナルデータベース（MySQL）を選ぶべき理由：**

1. **データの関連付けが容易**
   - 顧客テーブルと注文履歴テーブルを外部キーで結合できる
   - 顧客IDを使って注文データを簡単に紐付けられる

2. **データの整合性を保証**
   - トランザクション機能により、二重注文などを防げる
   - UNIQUE制約やPRIMARY KEY制約でデータの重複を防止

3. **同時アクセスの制御**
   - ロック機構により、複数の担当者が同時にデータを更新しても矛盾が起きない
   - ACIDプロパティによりデータの一貫性を保証

---

<!-- _class: title-top -->

## 1章 ワーク2: データベースの必要性

### 問題：以下のシナリオで、データベースがなぜ必要なのか説明してください。

#### シナリオ：オンライン書店

- 10万冊以上の書籍情報を管理
- 毎日数千人の顧客が商品を閲覧・購入
- 在庫管理、注文履歴、顧客情報を保存する必要がある

<div style="margin-top: 30px; padding: 20px; background-color: #FCEEF0; border-radius: 10px;">

**考えるポイント**:

- データの量
- データの種類
- データの関連性

</div>

---

<!-- _class: title-top -->

## 1章 ワーク2: チャレンジ問題

### 実務での判断

以下のシステムで、Excelではなくデータベースを使うべき理由を具体的に説明してください。

**シナリオ**: 社員管理システム（1000人規模）
- 社員情報（名前、部署、役職、給与）
- 勤怠記録（毎日の出退勤時刻）
- プロジェクト配置（複数プロジェクトに参加）

Excelと比較して、データベースの優位性を3つ以上挙げてください。

---

<!-- _class: title-top -->

## 1章 ワーク2: 解答例

1. **大量のデータを効率的に管理**
   - 10万冊以上の書籍情報を整理して保存
   - 素早く検索・取得が可能

2. **データの種類ごとに管理**
   - 書籍情報、顧客情報、注文履歴を別々のテーブルで管理
   - データの重複を防ぎ、効率的に保存

---

<!-- _class: title-top -->

## 1章 ワーク2: 解答例（続き）

3. **データ間の関連性を保つ**
   - 注文と顧客を紐付け
   - 注文と書籍を紐付け

4. **同時アクセスに対応**
   - 複数のユーザーが同時に閲覧・購入できる
   - データの一貫性を保ちながら処理

---

<!-- _class: title-top -->

## 1章 ワーク2: チャレンジ問題の解答例

**Excelと比較したデータベースの優位性：**

1. **データ量の制限**
   - Excel: 最大100万行程度が限界
   - データベース: 数億レコードでも効率的に処理可能

2. **同時編集と競合管理**
   - Excel: 複数人が同時編集すると競合が発生しやすい
   - データベース: トランザクション制御により安全な同時更新が可能

3. **データの整合性**
   - Excel: 手動入力によるミスが発生しやすい
   - データベース: 制約（UNIQUE、NOT NULLなど）で自動的に整合性を保証

---

<!-- _class: title-top -->

## 1章 ワーク2: チャレンジ問題の解答例（続き）

4. **複雑な検索とレポート生成**
   - Excel: 複雑な条件での検索に時間がかかる
   - データベース: インデックスにより高速検索が可能、複数テーブルを結合した分析も容易

5. **データのバックアップと復旧**
   - Excel: ファイル単位でのバックアップのみ
   - データベース: 自動バックアップ、ポイントインタイムリカバリが可能

---

<!-- _class: title-top -->

## 1章 ワーク3: リレーショナル型データベースの用語

### 問題

下記の表を見て、各用語が何を指すか答えてください。

| ID | 名前 | 年齢 | 職業 |
|----|------|------|------|
| 1 | 田中太郎 | 28 | エンジニア |
| 2 | 佐藤花子 | 32 | デザイナー |
| 3 | 鈴木一郎 | 45 | マネージャー |

1. **テーブル**は何を指しますか？
2. **カラム**は何を指しますか？
3. **レコード**は何を指しますか？
4. **フィールド**は何を指しますか？

---

<!-- _class: title-top -->

## 1章 ワーク3: チャレンジ問題

### テーブル設計

以下の「図書館システム」に必要なテーブルを考え、各テーブルに含めるべきカラム名を5つ以上挙げてください。

**必要なテーブル**:
1. 書籍テーブル（どんなカラムが必要？）
2. 会員テーブル（どんなカラムが必要？）
3. 貸出記録テーブル（どんなカラムが必要？）

各テーブルがどのように関連するかも簡単に説明してください。

---

<!-- _class: title-top -->

## 1章 ワーク3: 解答例

| ID | 名前 | 年齢 | 職業 |
|----|------|------|------|
| 1 | 田中太郎 | 28 | エンジニア |
| 2 | 佐藤花子 | 32 | デザイナー |
| 3 | 鈴木一郎 | 45 | マネージャー |

1. **テーブル**: 表全体（ユーザー情報テーブルなど）

2. **カラム**: 縦1列（例: 「名前」カラム、「年齢」カラム）

3. **レコード**: 横1行（例: 「1, 田中太郎, 28, エンジニア」）

4. **フィールド**: 1つひとつのデータ（例: 「田中太郎」、「28」）

---

<!-- _class: title-top -->

## 1章 ワーク3: チャレンジ問題の解答例

### **図書館システムのテーブル設計：**

**1. 書籍テーブル（books）**
- book_id（書籍ID、主キー）
- title（書籍タイトル）
- author（著者名）
- isbn（ISBN番号）
- category（カテゴリ）

---

<!-- _class: title-top -->

## 1章 ワーク3: チャレンジ問題の解答例

**2. 会員テーブル（members）**
- member_id（会員ID、主キー）
- name（会員名）
- email（メールアドレス）
- phone（電話番号）
- registration_date（登録日）

---

<!-- _class: title-top -->

## 1章 ワーク3: チャレンジ問題の解答例

**3. 貸出記録テーブル（rentals）**
- rental_id（貸出ID、主キー）
- book_id（書籍ID、外部キー）
- member_id（会員ID、外部キー）
- rental_date（貸出日）
- return_due_date（返却期限）
- return_date（返却日）

### **テーブル間の関連：**
- 貸出記録テーブルのbook_idが書籍テーブルのbook_idと紐付く
- 貸出記録テーブルのmember_idが会員テーブルのmember_idと紐付く
- これにより「誰が」「どの本を」「いつ借りたか」が管理できる

---

<!-- _class: title -->

# 2章 SQLの概要を学ぼう
## ワーク

---

<!-- _class: title-top -->

## 2章 ワーク1: SQLの分類

### 問題

以下のSQL文を、DDL・DML・DCLのいずれかに分類してください。

1. `CREATE TABLE users (id INT, name VARCHAR(50));`
2. `SELECT * FROM products WHERE price > 1000;`
3. `INSERT INTO orders (user_id, product_id) VALUES (1, 100);`
4. `GRANT SELECT ON database_name TO user_name;`
5. `ALTER TABLE customers ADD COLUMN email VARCHAR(100);`
6. `UPDATE products SET price = 1500 WHERE id = 5;`
7. `DROP TABLE old_data;`
8. `DELETE FROM logs WHERE created_at < '2024-01-01';`

---

<!-- _class: title-top -->

## 2章 ワーク1: チャレンジ問題

以下のSQL文を実行した場合、どのような結果になるか予測してください。また、なぜそうなるのか理由も説明してください。

1. `SELECT * FROM users;` を実行した後に `DROP TABLE users;` を実行し、再度 `SELECT * FROM users;` を実行したらどうなる？

2. `CREATE TABLE products;` というSQL文は正しいか？正しくない場合、何が不足しているか説明してください。

---

<!-- _class: title-top -->

## 2章 ワーク1: 解答例

| SQL文 | 分類 | 説明 |
|-------|------|------|
| `CREATE TABLE users ...` | **DDL** | テーブルを定義（作成） |
| `SELECT * FROM products ...` | **DML** | データを検索（取得） |
| `INSERT INTO orders ...` | **DML** | データを追加 |
| `GRANT SELECT ON ...` | **DCL** | アクセス権限を付与 |

---

<!-- _class: title-top -->

## 2章 ワーク1: 解答例（続き）

| SQL文 | 分類 | 説明 |
|-------|------|------|
| `ALTER TABLE customers ...` | **DDL** | テーブル構造を変更 |
| `UPDATE products SET ...` | **DML** | データを更新 |
| `DROP TABLE old_data` | **DDL** | テーブルを削除 |
| `DELETE FROM logs ...` | **DML** | データを削除 |

---

<!-- _class: title-top -->

## 2章 ワーク1: チャレンジ問題の解答例

**1. SELECT → DROP → SELECTの結果：**

エラーが発生します。理由：
- 1回目の`SELECT * FROM users;`は成功（テーブルが存在するため）
- `DROP TABLE users;`でusersテーブルが削除される
- 2回目の`SELECT * FROM users;`でエラー発生
- エラーメッセージ：「Table 'users' doesn't exist」
- DROP文は取り消せないので、テーブルを再度作成する必要がある

---

<!-- _class: title-top -->

## 2章 ワーク1: チャレンジ問題の解答例

**2. CREATE TABLE products;の問題点：**

正しくありません。不足している要素：
- **カラム定義が必要**：テーブルには最低1つのカラムが必要
- 正しい書き方の例：
  ```sql
  CREATE TABLE products (
      id INT PRIMARY KEY,
      name VARCHAR(100)
  );
  ```

---

<!-- _class: title-top -->

## 2章 ワーク2: SQL文の基本構造

### 問題

以下の説明に当てはまるSQL文を書いてください。

1. `products`テーブルから、すべてのデータを取得する
2. `users`テーブルから、`name`と`email`カラムのみを取得する
3. `orders`テーブルから、`price`が1000以上のデータを取得する
4. `customers`テーブルに、新しい顧客データ（id=1, name='山田太郎'）を追加する

<div style="margin-top: 30px; padding: 20px; background-color: #FCEEF0; border-radius: 10px;">

**ヒント**:

- SELECT文の基本: `SELECT カラム名 FROM テーブル名;`
- WHERE句: `WHERE 条件`
- INSERT文の基本: `INSERT INTO テーブル名 (カラム名) VALUES (値);`

</div>

---

<!-- _class: title-top -->

## 2章 ワーク2: チャレンジ問題

複数のSQL文を組み合わせて、以下の操作を実行してください。

**シナリオ**: 新商品登録システム

1. `products`テーブルに新商品3つを一度に追加する（INSERT文を1つで）
2. 追加した商品のうち、価格が5000円以上の商品のみを取得する
3. 取得した商品の`name`と`price`カラムのみを表示する

---

<!-- _class: title-top -->

## 2章 ワーク2: 解答例

1. **productsテーブルからすべてのデータを取得**

   ```sql
   SELECT * FROM products;
   ```

2. **usersテーブルからnameとemailカラムのみを取得**

   ```sql
   SELECT name, email FROM users;
   ```

3. **ordersテーブルからpriceが1000以上のデータを取得**

   ```sql
   SELECT * FROM orders WHERE price >= 1000;
   ```

4. **customersテーブルに新しい顧客データを追加**

   ```sql
   INSERT INTO customers (id, name) VALUES (1, '山田太郎');
   ```

---

<!-- _class: title-top -->

## 2章 ワーク2: チャレンジ問題の解答例

**1. 複数商品を一度に追加**

```sql
INSERT INTO products (name, price, category)
VALUES
    ('ワイヤレスマウス', 2980, '周辺機器'),
    ('USBメモリ 64GB', 1580, '記憶媒体'),
    ('HDMIケーブル', 980, 'ケーブル');
```

**2. 価格が5000円以上の商品を取得**

```sql
SELECT * FROM products WHERE price >= 5000;
```

---

<!-- _class: title-top -->

## 2章 ワーク2: チャレンジ問題の解答例

**3. nameとpriceカラムのみ表示**

```sql
SELECT name, price FROM products WHERE price >= 5000;
```

---

<!-- _class: title-top -->

## 2章 ワーク3: SQLとMySQLの違い

### 問題

以下の記述について、正しいものには○、誤っているものには×をつけ、誤っている場合は理由を説明してください。

1. SQLはMySQLでしか使えない
2. MySQLで学んだSQLは、PostgreSQLでも基本的に使える
3. SQLはデータベース操作専用の言語である
4. MySQLはデータベース管理システム（DBMS）の一種である
5. SQLの書き方はDBMSごとに完全に異なる

---

<!-- _class: title-top -->

## 2章 ワーク3: チャレンジ問題

実務でよくある質問に答えてください。

**質問1**: MySQLで学んだSQLをPostgreSQLプロジェクトで使うことになりました。注意すべき点は何ですか？

**質問2**: SQLの標準規格と各DBMSの独自機能（方言）の違いを理解することが、なぜ重要なのか説明してください。

---

<!-- _class: title-top -->

## 2章 ワーク3: 解答例

1. **SQLはMySQLでしか使えない** → **×**
   - SQLは世界標準の言語で、MySQL、PostgreSQL、Oracle Databaseなど、様々なDBMSで使える

2. **MySQLで学んだSQLは、PostgreSQLでも基本的に使える** → **○**
   - SQLは標準化されているため、基本的な構文は共通

3. **SQLはデータベース操作専用の言語である** → **○**
   - SQLはデータベースの構築や操作を行うための専用言語

4. **MySQLはデータベース管理システム（DBMS）の一種である** → **○**
   - MySQLはオープンソースのDBMS

5. **SQLの書き方はDBMSごとに完全に異なる** → **×**
   - 基本的な書き方は共通。ただし、細かい機能や拡張機能はDBMSごとに違いがある

---

<!-- _class: title-top -->

## 2章 ワーク3: チャレンジ問題の解答例

**質問1：MySQLからPostgreSQLへの移行時の注意点**

- **AUTO_INCREMENT vs SERIAL**：MySQLの`AUTO_INCREMENT`はPostgreSQLでは`SERIAL`を使う
- **文字列の連結**：MySQLは`CONCAT()`、PostgreSQLは`||`演算子も使える
- **LIMIT句の違い**：基本は同じだが、`LIMIT ... OFFSET`の書き方が若干異なる
- **日付関数**：`NOW()`は共通だが、日付計算の関数名が異なる場合がある
- **大文字小文字の扱い**：PostgreSQLは識別子の大文字小文字を区別する

**質問2：SQL標準と独自機能の違いを理解する重要性**

- **移植性の向上**：標準SQLを使えば、別のDBMSへの移行が容易
- **学習効率**：標準SQLを理解すれば、他のDBMSも学びやすい
- **保守性の向上**：独自機能に依存しすぎると、将来の変更が困難
- **チーム開発**：標準SQLの知識があれば、異なるDBMSの経験者同士でも協力しやすい

---

<!-- _class: title -->

# 3章 データ型の種類を学ぼう
## ワーク

---

<!-- _class: title-top -->

## 3章 ワーク1: 適切なデータ型の選択

### 問題

以下のデータに最適なデータ型を選んでください。

1. ユーザーの年齢（0〜150）
2. 商品名（最大50文字）
3. メールアドレス（最大100文字）
4. 商品の価格（小数点以下2桁まで）
5. ユーザーの自己紹介文（最大5000文字）
6. 会員登録日時
7. 商品の在庫数（-2147483648〜2147483647）
8. ユーザーのアクティブ状態（有効/無効の2択）

---

<!-- _class: title-top -->

## 3章 ワーク1: チャレンジ問題

以下のシナリオで、誤ったデータ型を選んだ場合に起こる問題を説明してください。

**ケース1**: 商品価格を`INT型`で保存した場合、どんな問題が起こりますか？

**ケース2**: ユーザーの自己紹介文を`VARCHAR(50)`で保存した場合、どんな問題が起こりますか？

**ケース3**: 会員登録日を`VARCHAR型`で「2025/11/10」という文字列として保存した場合、どんな問題が起こりますか？

---

<!-- _class: title-top -->

## 3章 ワーク1: 解答例

| データ | データ型 | 理由 |
|--------|----------|------|
| 1.ユーザーの年齢 | **INT** | 0〜255の範囲で十分。小さい整数型で効率的 |
| 2.商品名 | **VARCHAR(50)** | 可変長文字列、最大50文字 |
| 3.商品の価格 | **DECIMAL(10, 2)** | 小数点以下2桁の正確な計算が必要 |
| 4.自己紹介文 | **TEXT** | 長文テキスト（最大5000文字） |
| 5.データ | データ型 | 理由 |
| 6.会員登録日時 | **DATETIME** | 日付と時刻を記録 |
| 7.メールアドレス | **VARCHAR(100)** | 可変長文字列、最大100文字 |
| 8.商品の在庫数 | **INT** | 標準的な整数型 |
| 9.アクティブ状態 | **BOOLEAN** | TRUE/FALSEの2値 |

---

<!-- _class: title-top -->

## 3章 ワーク2: データ型の使い分け

### 問題

以下のシナリオで、なぜそのデータ型が適切なのか説明してください。

**シナリオ1**: ECサイトの商品価格
- `INT`ではなく`DECIMAL`を使う理由は？

**シナリオ2**: ユーザーのプロフィール画像URL
- `TEXT`ではなく`VARCHAR`を使う理由は？

---

<!-- _class: title-top -->

## 3章 ワーク2: データ型の使い分け

**シナリオ3**: ブログ記事の本文
- `VARCHAR`ではなく`TEXT`を使う理由は？

---

<!-- _class: title-top -->

## 3章 ワーク2: チャレンジ問題

実際のテーブル設計で、以下のカラムに最適なデータ型を選び、理由を説明してください。

1. **クレジットカード番号**（16桁）
2. **口座残高**（マイナスもあり得る、小数点以下2桁）
3. **ユーザーの生年月日**
4. **商品説明文**（平均500文字、最大10,000文字）
5. **メール送信済みフラグ**（送信済み/未送信）

---

<!-- _class: title-top -->

## 3章 ワーク2: 解答例

### シナリオ1: 商品価格に`DECIMAL`を使う理由

**理由**:

- 金額計算では小数点以下の正確な計算が必要
- `INT`では小数を扱えない（100円50銭を表現できない）
- `FLOAT`や`DOUBLE`は近似値のため、計算誤差が発生する可能性がある
- `DECIMAL`は正確な小数を扱える

**例**:

```sql
price DECIMAL(10, 2)  -- 最大10桁、小数点以下2桁
-- 例: 12345678.99
```

---

<!-- _class: title-top -->

## 3章 ワーク2: 解答例（続き）

### シナリオ2: 画像URLに`VARCHAR`を使う理由

**理由**:

- URLの長さには上限がある（通常200文字程度で十分）
- `VARCHAR`は最大文字数を指定でき、無駄なメモリを使わない
- `TEXT`は大きなデータ用で、短いURLには不向き
- インデックスを効率的に作成できる

**例**:

```sql
image_url VARCHAR(255)  -- 最大255文字
```

---

<!-- _class: title-top -->

## 3章 ワーク2: 解答例（続き2）

### シナリオ3: ブログ記事本文に`TEXT`を使う理由

**理由**:

- ブログ記事は数千〜数万文字になることがある
- `VARCHAR`の最大長（65,535バイト）を超える可能性がある
- `TEXT`は長文データに適している
- 文字数が不定のコンテンツに柔軟に対応

**例**:

```sql
content TEXT  -- 最大65,535文字
-- より長い場合は MEDIUMTEXT や LONGTEXT を使用
```

---

<!-- _class: title-top -->

## 3章 ワーク2: チャレンジ問題の解答例

**1. クレジットカード番号（16桁）**
- **推奨**: `CHAR(16)` または `VARCHAR(19)`（ハイフン含む場合）
- **理由**: 固定長16桁なので`CHAR`が最適。数値計算しないので文字列型を使う
- **注意**: セキュリティ上、暗号化して保存すべき

**2. 口座残高（マイナスあり、小数点以下2桁）**
- **推奨**: `DECIMAL(15, 2)`
- **理由**: 金額計算で正確性が必要。負の値も扱えるため

---

<!-- _class: title-top -->

## 3章 ワーク2: チャレンジ問題の解答例

**3. ユーザーの生年月日**
- **推奨**: `DATE`
- **理由**: 日付のみで時刻は不要。年齢計算などの日付演算が可能

**4. 商品説明文（平均500文字、最大10,000文字）**
- **推奨**: `TEXT`
- **理由**: `VARCHAR`の最大長は65,535バイトだが、`TEXT`の方が長文に適している

**5. メール送信済みフラグ（送信済み/未送信）**
- **推奨**: `BOOLEAN` または `TINYINT(1)`
- **理由**: 2値（TRUE/FALSE）を扱うのに最適。デフォルト値`FALSE`を設定可能

---

<!-- _class: title-top -->

## 3章 ワーク3: テーブル設計の実践

### 以下の要件を満たす「書籍管理テーブル（books）」を設計してください。

各カラムの名前とデータ型を定義してください。

- 書籍ID（主キー、自動採番）
- タイトル（最大100文字）
- 著者名（最大50文字）
- 価格（小数点以下2桁まで）
- ページ数
- 出版日
- ISBN（13桁の固定長文字列、ユニーク制約）
- 在庫あり/なし（フラグ、デフォルト値あり）

---

<!-- _class: title-top -->

## 3章 ワーク3: チャレンジ問題

以下の「ECサイト商品テーブル」を設計してください。

**要件**:
- 商品は複数のカテゴリに属することができる
- 商品には複数の画像を登録できる
- 在庫数は常に0以上
- 価格は税抜きと税込みの両方を保存

上記を実現するために、どのようなテーブル構成とカラムが必要か提案してください。（1つのテーブルでは実現困難な場合、複数テーブルを提案してOK）

---

<!-- _class: title-top -->

## 3章 ワーク3: 解答例

```sql
CREATE TABLE books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(50) NOT NULL,
    price DECIMAL(8, 2) NOT NULL,
    pages INT NOT NULL,
    published_date DATE NOT NULL,
    isbn CHAR(13) UNIQUE NOT NULL,
    in_stock BOOLEAN DEFAULT TRUE
);
```

---

<!-- _class: title-top -->

## 3章 ワーク3: 解答例（続き）

**ポイント**:

- `id`: 主キー、自動採番（AUTO_INCREMENT）
- `title`, `author`: 可変長文字列（VARCHAR）
- `price`: 正確な小数計算（DECIMAL）
- `pages`: 整数（INT）
- `published_date`: 日付（DATE）
- `isbn`: 固定長13文字（CHAR）、ユニーク制約
- `in_stock`: 真偽値（BOOLEAN）、デフォルトTRUE

---

<!-- _class: title-top -->

## 3章 ワーク3: チャレンジ問題の解答例

**ECサイト商品テーブルの設計提案：**

複数のテーブルに分割する必要があります：

**1. 商品テーブル（products）**
```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price_excluding_tax DECIMAL(10, 2) NOT NULL,
    price_including_tax DECIMAL(10, 2) NOT NULL,
    stock INT UNSIGNED DEFAULT 0,
    description TEXT
);
```

---

<!-- _class: title-top -->

## 3章 ワーク3: チャレンジ問題の解答例

**2. カテゴリテーブル（categories）**
```sql
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL
);
```

**3. 商品カテゴリ関連テーブル（product_categories）**
```sql
CREATE TABLE product_categories (
    product_id INT,
    category_id INT,
    PRIMARY KEY (product_id, category_id)
);
```

---

<!-- _class: title-top -->

## 3章 ワーク3: チャレンジ問題の解答例

**4. 商品画像テーブル（product_images）**
```sql
CREATE TABLE product_images (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    image_url VARCHAR(255),
    display_order INT
);
```

---

<!-- _class: title-top -->

## 3章 ワーク4: データ型の理解度チェック

### 問題（○×クイズ）

以下の記述が正しければ○、誤っていれば×を答えてください。

1. `VARCHAR(50)`は必ず50バイトのメモリを使用する
2. `CHAR(10)`は常に10バイトのメモリを使用する
3. `INT`は負の数を扱えない
4. `DECIMAL(5, 2)`は「123.45」を格納できる
5. `TEXT`型のカラムには最大255文字まで格納できる
6. `DATETIME`は日付と時刻の両方を記録できる
7. `BOOLEAN`は実際には`TINYINT(1)`として扱われる
8. 金額計算には`FLOAT`が最適である

---

<!-- _class: title-top -->

## 3章 ワーク4: チャレンジ問題

### 実務でよくあるデータ型の選択ミスについて、以下のケースを評価してください。

**ケース1**: 電話番号を`INT型`で保存している
→ 問題点を2つ以上挙げてください

**ケース2**: 商品価格を`FLOAT型`で保存している
→ どんな計算エラーが発生する可能性がありますか？

**ケース3**: 日付を`VARCHAR型`で「2025-11-10」という文字列で保存している
→ 日付の範囲検索（例：2025年1月以降）を行う場合、どんな問題がありますか？

---

<!-- _class: title-top -->

## 3章 ワーク4: 解答例

1. `VARCHAR(50)`は必ず50バイトのメモリを使用する → **×**
   - 可変長なので、実際に格納されたデータ量だけメモリを使用

2. `CHAR(10)`は常に10バイトのメモリを使用する → **○**
   - 固定長なので、常に指定した長さ分のメモリを使用

3. `INT`は負の数を扱えない → **×**
   - デフォルトでは負の数も扱える（-2147483648〜2147483647）

4. `DECIMAL(5, 2)`は「123.45」を格納できる → **○**
   - 全体5桁、小数点以下2桁なので「123.45」は格納可能

---

<!-- _class: title-top -->

## 3章 ワーク4: 解答例（続き）

5. `TEXT`型のカラムには最大255文字まで格納できる → **×**
   - `TEXT`は最大65,535バイト（約65KB）まで格納可能

6. `DATETIME`は日付と時刻の両方を記録できる → **○**
   - 「2025-11-01 14:30:00」のような形式で記録

7. `BOOLEAN`は実際には`TINYINT(1)`として扱われる → **○**
   - MySQLでは`BOOLEAN`は`TINYINT(1)`のエイリアス

8. 金額計算には`FLOAT`が最適である → **×**
   - `FLOAT`は近似値のため、計算誤差が発生する可能性がある
   - 金額計算には`DECIMAL`が最適

---

<!-- _class: title-top -->

## 3章 ワーク4: チャレンジ問題の解答例

**ケース1：電話番号をINT型で保存**

問題点：
1. **先頭の0が消える**：「090-1234-5678」を数値として保存すると「901234567 8」になり、先頭の0が失われる
2. **ハイフンが保存できない**：「090-1234-5678」の形式が保存できない
3. **国際電話番号に対応できない**：「+81」などの記号が保存できない
4. **範囲オーバー**：INT型の最大値を超える電話番号がある

正解：`VARCHAR(20)`を使用

---

<!-- _class: title-top -->

## 3章 ワーク4: チャレンジ問題の解答例

**ケース2：商品価格をFLOAT型で保存**

発生する問題：
- **丸め誤差**：100.10円が100.0999...円のように保存される
- **合計計算のずれ**：複数の商品価格を合計すると、実際の金額とずれる
- 例：1.1 + 2.2 ≠ 3.3（浮動小数点演算の誤差）

正解：`DECIMAL(10, 2)`を使用

---

<!-- _class: title-top -->

## 3章 ワーク4: チャレンジ問題の解答例（続き）

**ケース3：日付をVARCHAR型で保存**

発生する問題：
- **範囲検索が正しく動作しない**：文字列比較では「2025-02-01」>「2025-10-01」となる（文字列順）
- **日付関数が使えない**：`YEAR()`、`MONTH()`、`DATEDIFF()`などの関数が使えない
- **不正な値の混入**：「2025/13/40」のような不正な日付も保存できてしまう

正解：`DATE`型を使用

---

<!-- _class: title -->

# 4章 データベースとテーブルを作ろう
## ワーク

---

<!-- _class: title-top -->

## 4章 ワーク1: CREATE文の理解

### 問題

以下のSQL文を実行して、データベースとテーブルを作成してください。

1. `lesson`という名前のデータベースを作成する
2. `students`テーブルを作成する（id: INT PRIMARY KEY AUTO_INCREMENT, name: VARCHAR(50) NOT NULL, age: INT）

<div style="margin-top: 30px; padding: 20px; background-color: #FCEEF0; border-radius: 10px;">

**ヒント**: CREATE DATABASE文とCREATE TABLE文を使います。

</div>

---

<!-- _class: title-top -->

## 4章 ワーク1: チャレンジ問題

以下の要件を満たす「注文管理テーブル」を設計し、CREATE TABLE文を書いてください。

**要件**:
- 注文ID（主キー、自動採番）
- 顧客ID（必須、整数）
- 商品名（最大100文字、必須）
- 数量（必須、整数、デフォルト値1）
- 合計金額（小数点以下2桁）
- 注文日時（現在日時をデフォルト値として自動設定）
- ステータス（最大20文字、デフォルト値「pending」）

---

<!-- _class: title-top -->

## 4章 ワーク1: 解答例

1. **データベースの作成**

   ```sql
   CREATE DATABASE lesson;
   ```

2. **テーブルの作成**

   ```sql
   USE lesson;

   CREATE TABLE students (
       id INT PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(50) NOT NULL,
       age INT
   );
   ```

---

<!-- _class: title-top -->

## 4章 ワーク1: チャレンジ問題の解答例

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    total_amount DECIMAL(10, 2),
    order_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'pending'
);
```

---

<!-- _class: title-top -->

## 4章 ワーク1: チャレンジ問題の解答例（続き）

**ポイント**:
- `order_id`: 主キー、自動採番
- `customer_id`, `product_name`, `quantity`: NOT NULL制約で必須化
- `quantity`: デフォルト値1を設定
- `order_datetime`: CURRENT_TIMESTAMPで現在日時を自動設定
- `status`: デフォルト値「pending」

---

<!-- _class: title -->

# 5章 データベースとテーブルを取得しよう
## ワーク

---

<!-- _class: title-top -->

## 5章 ワーク1: SHOW文とUSE文の使い方

### 問題

1. 現在のMySQLサーバーにあるすべてのデータベース一覧を取得する
2. `lesson`データベースを使用状態にする
3. `lesson`データベース内のすべてのテーブル一覧を取得する

---

<!-- _class: title-top -->

## 5章 ワーク1: チャレンジ問題

実務シナリオ：新しいプロジェクトに参画し、既存のデータベース構造を調査する必要があります。

1. どのデータベースが存在するか確認するSQL文を書いてください
2. `shop`データベースに切り替えるSQL文を書いてください
3. `shop`データベース内のすべてのテーブルを確認するSQL文を書いてください
4. `products`テーブルの構造（カラム名、データ型など）を確認するSQL文を書いてください（ヒント：`DESCRIBE`または`SHOW COLUMNS`）

---

<!-- _class: title-top -->

## 5章 ワーク1: 解答例

1. **データベース一覧の取得**

   ```sql
   SHOW DATABASES;
   ```

2. **データベースの使用**

   ```sql
   USE lesson;
   ```

3. **テーブル一覧の取得**

   ```sql
   SHOW TABLES;
   ```

---

<!-- _class: title-top -->

## 5章 ワーク1: チャレンジ問題の解答例

1. **データベース一覧の確認**: `SHOW DATABASES;`
2. **shopデータベースに切り替え**: `USE shop;`
3. **テーブル一覧の確認**: `SHOW TABLES;`
4. **productsテーブルの構造確認**:
   ```sql
   DESCRIBE products;
   -- または
   SHOW COLUMNS FROM products;
   ```

---

<!-- _class: title -->

# 6章 データベースとテーブルを削除しよう
## ワーク

---

<!-- _class: title-top -->

## 6章 ワーク1: DROP文の使い方

### 問題

1. `test_table`という名前のテーブルを削除する
2. `test_db`という名前のデータベースを削除する

<div style="margin-top: 30px; padding: 20px; background-color: #FCEEF0; border-radius: 10px;">

**注意**: DROP文は元に戻せないので、実行前に必ず確認しましょう。

</div>

---

<!-- _class: title-top -->

## 6章 ワーク1: チャレンジ問題

実務での安全な削除手順を考えてください。

**シナリオ**: `old_products`テーブルを削除したいが、このテーブルが他のシステムで使われていないか確認する必要があります。

1. テーブルを削除する前に、どんな確認作業をすべきですか？（3つ以上挙げてください）
2. 誤って重要なテーブルを削除してしまった場合、どう対処すべきですか？
3. DROP文の代わりに、データだけを削除してテーブル構造を残す方法はありますか？そのSQL文を書いてください。

---

<!-- _class: title-top -->

## 6章 ワーク1: 解答例

1. **テーブルの削除**

   ```sql
   DROP TABLE test_table;
   ```

2. **データベースの削除**

   ```sql
   DROP DATABASE test_db;
   ```

---

<!-- _class: title -->

# 7章 データを取得しよう
## ワーク

---

<!-- _class: title-top -->

## 7章 ワーク1: SELECT文の基本

### 問題

`users`テーブル（id, name, email, age）があります。以下のSQL文を書いてください。

1. すべてのカラムのデータを取得する
2. `name`と`email`カラムのみを取得する
3. `age`カラムのみを取得する

---

<!-- _class: title-top -->

## 7章 ワーク1: チャレンジ問題

実務での複雑なSELECT文を書いてください。

`employees`テーブル（id, name, department, salary, hire_date）があります。

1. すべての従業員の名前と給与のみを取得するSQL文
2. 重複を除いた部署名の一覧を取得するSQL文（ヒント：`DISTINCT`）
3. 従業員数が何人いるか数えるSQL文（ヒント：`COUNT`）

---

<!-- _class: title-top -->

## 7章 ワーク1: 解答例

1. **すべてのカラムを取得**

   ```sql
   SELECT * FROM users;
   ```

2. **特定のカラムを取得（nameとemail）**

   ```sql
   SELECT name, email FROM users;
   ```

3. **特定のカラムを取得（age）**

   ```sql
   SELECT age FROM users;
   ```

---

<!-- _class: title -->

# 8章 データを追加・更新しよう
## ワーク

---

<!-- _class: title-top -->

## 8章 ワーク1: INSERT文とUPDATE文

### 問題

`products`テーブル（id, name, price, stock）があります。

1. 新しい商品を追加する（id=1, name='ノートPC', price=80000, stock=10）
2. id=1の商品の価格を75000に更新する
3. id=1の商品の在庫を5減らす（stock=5にする）

---

<!-- _class: title-top -->

## 8章 ワーク1: チャレンジ問題

実務でのデータ操作シナリオ。

`orders`テーブル（id, customer_id, product_name, quantity, total_price, status）があります。

1. 複数の注文を一度に追加するSQL文を書いてください（3件以上）
2. 顧客ID=5のすべての注文のステータスを「completed」に更新するSQL文
3. 合計金額が10000円未満の注文のみ、配送料500円を追加するSQL文（total_priceに500を加算）

---

<!-- _class: title-top -->

## 8章 ワーク1: 解答例

1. **データの追加**

   ```sql
   INSERT INTO products (id, name, price, stock)
   VALUES (1, 'ノートPC', 80000, 10);
   ```

2. **価格の更新**

   ```sql
   UPDATE products SET price = 75000 WHERE id = 1;
   ```

3. **在庫の更新**

   ```sql
   UPDATE products SET stock = 5 WHERE id = 1;
   ```

---

<!-- _class: title -->

# 9章 データを削除しよう
## ワーク

---

<!-- _class: title-top -->

## 9章 ワーク1: DELETE文の使い方

### 問題

`orders`テーブル（id, user_id, product_id, created_at）があります。

1. id=5の注文を削除する
2. 2024年1月1日より前の注文をすべて削除する

<div style="margin-top: 30px; padding: 20px; background-color: #FCEEF0; border-radius: 10px;">

**注意**: WHERE句を忘れるとすべてのデータが削除されます！

</div>

---

<!-- _class: title-top -->

## 9章 ワーク1: チャレンジ問題

実務での安全なデータ削除。

`user_logs`テーブル（id, user_id, action, created_at）があります。

1. 特定のユーザー（user_id=10）のログをすべて削除するSQL文
2. 90日以上前のログを削除するSQL文（ヒント：`DATE_SUB`関数または`INTERVAL`）
3. DELETE文を実行する前に、削除対象のレコード数を確認する方法を説明してください

---

<!-- _class: title-top -->

## 9章 ワーク1: 解答例

1. **特定のIDの削除**

   ```sql
   DELETE FROM orders WHERE id = 5;
   ```

2. **日付条件での削除**

   ```sql
   DELETE FROM orders WHERE created_at < '2024-01-01';
   ```

---

<!-- _class: title -->

# 10章 WHERE句で特定のデータを検索しよう
## ワーク

---

<!-- _class: title-top -->

## 10章 ワーク1: WHERE句と比較演算子

### 問題

`employees`テーブル（id, name, age, salary, department）があります。

1. 年齢が30歳以上の従業員を取得する
2. 給与が50000以下の従業員を取得する
3. 部署が'営業部'の従業員を取得する
4. 年齢が25歳ではない従業員を取得する

---

<!-- _class: title-top -->

## 10章 ワーク1: チャレンジ問題

複雑な条件での検索。

`products`テーブル（id, name, category, price, stock, created_at）があります。

1. 価格が1000円以上5000円以下で、在庫が10個以上ある商品を取得
2. カテゴリが「家電」で価格が10000円以上、または在庫が0の商品を取得
3. 商品名に「iPhone」という文字列が含まれる商品を取得（ヒント：`LIKE`）

---

<!-- _class: title-top -->

## 10章 ワーク1: 解答例

1. **年齢が30歳以上**

   ```sql
   SELECT * FROM employees WHERE age >= 30;
   ```

2. **給与が50000以下**

   ```sql
   SELECT * FROM employees WHERE salary <= 50000;
   ```

3. **部署が営業部**

   ```sql
   SELECT * FROM employees WHERE department = '営業部';
   ```

4. **年齢が25歳ではない**

   ```sql
   SELECT * FROM employees WHERE age != 25;
   ```

---

<!-- _class: title-top -->

## 10章 ワーク2: 論理演算子（AND、OR）

### 問題

`employees`テーブルを使って、以下の条件でデータを取得してください。

1. 年齢が30歳以上かつ給与が60000以上の従業員
2. 部署が'営業部'または'開発部'の従業員
3. 年齢が25歳以上35歳以下の従業員

---

<!-- _class: title-top -->

## 10章 ワーク2: チャレンジ問題

実務での複雑な検索条件。

`orders`テーブル（id, customer_name, product_name, quantity, price, status, order_date）があります。

1. ステータスが「pending」または「processing」で、注文金額（quantity × price）が50000円以上の注文を取得
2. 顧客名が「田中」で始まり、かつ2025年に注文された商品を取得（ヒント：`LIKE 'pattern%'`と`YEAR()`関数）
3. 数量が10個以上または単価が5000円以上で、ステータスが「completed」の注文を取得

---

<!-- _class: title-top -->

## 10章 ワーク2: 解答例

1. **AND演算子の使用**

   ```sql
   SELECT * FROM employees
   WHERE age >= 30 AND salary >= 60000;
   ```

2. **OR演算子の使用**

   ```sql
   SELECT * FROM employees
   WHERE department = '営業部' OR department = '開発部';
   ```

3. **BETWEEN句の使用**

   ```sql
   SELECT * FROM employees
   WHERE age BETWEEN 25 AND 35;
   ```

---

<!-- _class: title -->

# 11章 より複雑なデータを検索しよう
## ワーク

---

<!-- _class: title-top -->

## 11章 ワーク1: BETWEEN, IN, LIKE句

### 問題

`products`テーブル（id, name, category, price, stock）があります。

1. 価格が1000円以上5000円以下の商品を取得する（BETWEEN使用）
2. カテゴリが「家電」「書籍」「食品」のいずれかに該当する商品を取得する（IN使用）
3. 商品名に「USB」という文字列が含まれる商品を取得する（LIKE使用）
4. 商品名が「ノート」で始まる商品を取得する（LIKE使用）

---

<!-- _class: title-top -->

## 11章 ワーク1: 解答例

1. **BETWEEN句を使用**
   ```sql
   SELECT * FROM products WHERE price BETWEEN 1000 AND 5000;
   ```

2. **IN句を使用**
   ```sql
   SELECT * FROM products WHERE category IN ('家電', '書籍', '食品');
   ```

3. **LIKE句（部分一致）**
   ```sql
   SELECT * FROM products WHERE name LIKE '%USB%';
   ```

4. **LIKE句（前方一致）**
   ```sql
   SELECT * FROM products WHERE name LIKE 'ノート%';
   ```

---

<!-- _class: title-top -->

## 11章 ワーク1: チャレンジ問題

実務での複雑な検索条件を組み合わせてください。

`products`テーブル（id, name, category, price, stock, created_at）があります。

1. カテゴリが「家電」または「PC周辺機器」で、価格が3000円以上10000円以下の商品を取得
2. 商品名に「ワイヤレス」「Bluetooth」「無線」のいずれかが含まれる商品を取得
3. 在庫が10個以下で、かつ価格が5000円以上の商品を、価格の高い順に上位5件取得

---

<!-- _class: title-top -->

## 11章 ワーク1: チャレンジ問題の解答例

1. **複数条件の組み合わせ**
   ```sql
   SELECT * FROM products
   WHERE category IN ('家電', 'PC周辺機器')
   AND price BETWEEN 3000 AND 10000;
   ```

2. **複数LIKE条件のOR**
   ```sql
   SELECT * FROM products
   WHERE name LIKE '%ワイヤレス%'
   OR name LIKE '%Bluetooth%'
   OR name LIKE '%無線%';
   ```

3. **WHERE + ORDER BY + LIMIT**
   ```sql
   SELECT * FROM products
   WHERE stock <= 10 AND price >= 5000
   ORDER BY price DESC
   LIMIT 5;
   ```

---

<!-- _class: title -->

# 12章 LIMIT句で取得するデータ数の上限を設定しよう
## ワーク

---

<!-- _class: title-top -->

## 12章 ワーク1: LIMIT句の使い方

### 問題

`users`テーブル（id, name, age, created_at）があります。

1. 最初の10件のユーザーを取得する
2. 11件目から20件目のユーザーを取得する（OFFSETを使用）
3. 最も新しく登録された5人のユーザーを取得する

---

<!-- _class: title-top -->

## 12章 ワーク1: 解答例

1. **最初の10件**
   ```sql
   SELECT * FROM users LIMIT 10;
   ```

2. **11件目から20件目**
   ```sql
   SELECT * FROM users LIMIT 10 OFFSET 10;
   ```

3. **最新の5人**
   ```sql
   SELECT * FROM users ORDER BY created_at DESC LIMIT 5;
   ```

---

<!-- _class: title-top -->

## 12章 ワーク1: チャレンジ問題

実務でのページネーション実装を考えてください。

`articles`テーブル（id, title, author, view_count, created_at）に1000件の記事データがあります。

1. 人気記事ランキング（閲覧数が多い順）のトップ10を取得する
2. 人気記事ランキングの11位〜20位を取得する（2ページ目）
3. 最新記事を1ページあたり20件表示する場合、3ページ目（41件目〜60件目）を取得する

---

<!-- _class: title-top -->

## 12章 ワーク1: チャレンジ問題の解答例

1. **トップ10（1ページ目）**
   ```sql
   SELECT * FROM articles
   ORDER BY view_count DESC
   LIMIT 10;
   ```

2. **11位〜20位（2ページ目）**
   ```sql
   SELECT * FROM articles
   ORDER BY view_count DESC
   LIMIT 10 OFFSET 10;
   ```

---

<!-- _class: title-top -->

## 12章 ワーク1: チャレンジ問題の解答例

3. **3ページ目（41件目〜60件目）**
   ```sql
   SELECT * FROM articles
   ORDER BY created_at DESC
   LIMIT 20 OFFSET 40;
   ```

**ポイント**: OFFSETの値は `(ページ番号 - 1) × 1ページあたりの件数` で計算します。

---

<!-- _class: title -->

# 13章 ORDER BY句で取得するデータを並び替えよう
## ワーク

---

<!-- _class: title-top -->

## 13章 ワーク1: ORDER BY句

### 問題

`products`テーブル（id, name, price, stock, created_at）があります。

1. 商品を価格の安い順に並び替える
2. 商品を価格の高い順に並び替える
3. 在庫数が多い順、在庫数が同じ場合は価格が安い順に並び替える

---

<!-- _class: title-top -->

## 13章 ワーク1: 解答例

1. **価格の安い順（昇順）**
   ```sql
   SELECT * FROM products ORDER BY price ASC;
   ```

2. **価格の高い順（降順）**
   ```sql
   SELECT * FROM products ORDER BY price DESC;
   ```

3. **複数カラムでの並び替え**
   ```sql
   SELECT * FROM products ORDER BY stock DESC, price ASC;
   ```

---

<!-- _class: title-top -->

## 13章 ワーク1: チャレンジ問題

実務での複雑な並び替えを実装してください。

`employees`テーブル（id, name, department, salary, hire_date, performance_score）があります。

1. 部署ごとにグループ化し、各部署内で給料が高い順に並び替える
2. 評価スコアが高い順、同じスコアの場合は入社日が古い順に並び替える
3. 給料がNULLの社員を最後に表示し、それ以外は給料が高い順に並び替える

---

<!-- _class: title-top -->

## 13章 ワーク1: チャレンジ問題の解答例

1. **部署ごとに給料でソート**
   ```sql
   SELECT * FROM employees
   ORDER BY department ASC, salary DESC;
   ```

2. **複数条件での並び替え**
   ```sql
   SELECT * FROM employees
   ORDER BY performance_score DESC, hire_date ASC;
   ```

3. **NULLを最後に表示**
   ```sql
   SELECT * FROM employees
   ORDER BY salary IS NULL ASC, salary DESC;
   ```

### **ポイント**: `IS NULL`はTRUE(1)またはFALSE(0)を返すため、NULLでない行が先に表示されます。

---

<!-- _class: title -->

# 14章 関数を使ってデータを集計しよう
## ワーク

---

<!-- _class: title-top -->

## 14章 ワーク1: 集計関数

### 問題

`orders`テーブル（id, customer_id, product_name, quantity, price）があります。

1. 注文の総数を取得する（COUNT）
2. 注文の合計金額を計算する（SUM）
3. 注文の平均金額を計算する（AVG）
4. 最も高い注文金額を取得する（MAX）
5. 最も安い注文金額を取得する（MIN）

---

<!-- _class: title-top -->

## 14章 ワーク1: 解答例

1. **注文総数**
   ```sql
   SELECT COUNT(*) FROM orders;
   ```

2. **合計金額**
   ```sql
   SELECT SUM(price) FROM orders;
   ```

3. **平均金額**
   ```sql
   SELECT AVG(price) FROM orders;
   ```

4. **最高金額**
   ```sql
   SELECT MAX(price) FROM orders;
   ```

5. **最低金額**
   ```sql
   SELECT MIN(price) FROM orders;
   ```

---

<!-- _class: title-top -->

## 14章 ワーク1: チャレンジ問題

複数の集計関数を組み合わせた分析を行ってください。

`sales`テーブル（id, product_id, quantity, unit_price, sale_date）があります。

1. 売上件数、合計売上金額、平均売上金額、最高売上金額、最低売上金額を1つのクエリで取得する
2. 数量が10個以上の注文だけを対象に、合計売上金額を計算する
3. 売上が発生した商品の種類数（重複を除いたproduct_idの数）を取得する

---

<!-- _class: title-top -->

## 14章 ワーク1: チャレンジ問題の解答例

1. **複数の集計関数を同時に使用**
   ```sql
   SELECT
     COUNT(*) AS sale_count,
     SUM(quantity * unit_price) AS total_sales,
     AVG(quantity * unit_price) AS avg_sales,
     MAX(quantity * unit_price) AS max_sales,
     MIN(quantity * unit_price) AS min_sales
   FROM sales;
   ```

2. **WHERE句と組み合わせ**
   ```sql
   SELECT SUM(quantity * unit_price) AS total_sales
   FROM sales
   WHERE quantity >= 10;
   ```

3. **DISTINCT（重複排除）とCOUNT**
   ```sql
   SELECT COUNT(DISTINCT product_id) AS product_count
   FROM sales;
   ```

---

<!-- _class: title -->

# 15章 GROUP BY句でデータをグループ化しよう
## ワーク

---

<!-- _class: title-top -->

## 15章 ワーク1: GROUP BYとHAVING

### 問題

`orders`テーブル（id, customer_id, product_name, price）があります。

1. 顧客ごとの注文回数を取得する
2. 顧客ごとの合計購入金額を取得する
3. 合計購入金額が10000円以上の顧客のみを取得する（HAVING使用）

---

<!-- _class: title-top -->

## 15章 ワーク1: 解答例

1. **顧客ごとの注文回数**
   ```sql
   SELECT customer_id, COUNT(*) AS order_count
   FROM orders
   GROUP BY customer_id;
   ```

2. **顧客ごとの合計購入金額**
   ```sql
   SELECT customer_id, SUM(price) AS total_amount
   FROM orders
   GROUP BY customer_id;
   ```

3. **HAVING句で条件指定**
   ```sql
   SELECT customer_id, SUM(price) AS total_amount
   FROM orders
   GROUP BY customer_id
   HAVING SUM(price) >= 10000;
   ```

---

<!-- _class: title-top -->

## 15章 ワーク1: チャレンジ問題

GROUP BY、HAVING、ORDER BYを組み合わせた複雑なクエリを作成してください。

`sales`テーブル（id, product_id, category, quantity, unit_price, sale_date）があります。

1. カテゴリごとの売上件数、合計売上金額を取得し、売上金額が高い順に並び替える
2. 売上件数が5件以上のカテゴリのみを取得する（HAVING使用）
3. カテゴリごとの平均販売単価を取得し、平均単価が1000円以上のカテゴリを単価が高い順に表示する

---

<!-- _class: title-top -->

## 15章 ワーク1: チャレンジ問題の解答例

1. **GROUP BY + ORDER BY**
   ```sql
   SELECT category,
          COUNT(*) AS sale_count,
          SUM(quantity * unit_price) AS total_sales
   FROM sales
   GROUP BY category
   ORDER BY total_sales DESC;
   ```

2. **GROUP BY + HAVING**
   ```sql
   SELECT category, COUNT(*) AS sale_count
   FROM sales
   GROUP BY category
   HAVING COUNT(*) >= 5;
   ```

---

<!-- _class: title-top -->

## 15章 ワーク1: チャレンジ問題の解答例

3. **GROUP BY + HAVING + ORDER BY の組み合わせ**
   ```sql
   SELECT category, AVG(unit_price) AS avg_price
   FROM sales
   GROUP BY category
   HAVING AVG(unit_price) >= 1000
   ORDER BY avg_price DESC;
   ```

---

<!-- _class: title -->

# 16章 JOIN句でテーブルを結合しよう
## ワーク

---

<!-- _class: title-top -->

## 16章 ワーク1: INNER JOIN

### 問題

`users`テーブル（id, name）と`orders`テーブル（id, user_id, product_name, price）があります。

1. ユーザー名と注文情報を結合して取得する
2. ユーザーIDが3の人の注文履歴を取得する
3. 注文したユーザーの名前と合計購入金額を取得する

---

<!-- _class: title-top -->

## 16章 ワーク1: 解答例

1. **INNER JOINで結合**
   ```sql
   SELECT users.name, orders.product_name, orders.price
   FROM users
   INNER JOIN orders ON users.id = orders.user_id;
   ```

2. **WHERE句で条件指定**
   ```sql
   SELECT users.name, orders.product_name, orders.price
   FROM users
   INNER JOIN orders ON users.id = orders.user_id
   WHERE users.id = 3;
   ```

3. **GROUP BYと組み合わせ**
   ```sql
   SELECT users.name, SUM(orders.price) AS total_amount
   FROM users
   INNER JOIN orders ON users.id = orders.user_id
   GROUP BY users.name;
   ```

---

<!-- _class: title-top -->

## 16章 ワーク1: チャレンジ問題

LEFT JOINを使った実務的なクエリを作成してください。

`users`テーブル（id, name, email）と`orders`テーブル（id, user_id, total_price, order_date）があります。

1. すべてのユーザーと、そのユーザーの注文回数を取得する（注文していないユーザーも含む）
2. 注文していないユーザーのみを取得する
3. ユーザーごとの合計購入金額を取得し、購入金額が多い順に並び替える（注文していないユーザーは0円として表示）

---

<!-- _class: title-top -->

## 16章 ワーク1: チャレンジ問題の解答例

1. **LEFT JOINで全ユーザーを取得**
   ```sql
   SELECT users.name, COUNT(orders.id) AS order_count
   FROM users
   LEFT JOIN orders ON users.id = orders.user_id
   GROUP BY users.id, users.name;
   ```

2. **注文していないユーザーのみ**
   ```sql
   SELECT users.name, users.email
   FROM users
   LEFT JOIN orders ON users.id = orders.user_id
   WHERE orders.id IS NULL;
   ```

---

<!-- _class: title-top -->

## 16章 ワーク1: チャレンジ問題の解答例

3. **LEFT JOIN + 集計 + ORDER BY**
   ```sql
   SELECT users.name,
          COALESCE(SUM(orders.total_price), 0) AS total_amount
   FROM users
   LEFT JOIN orders ON users.id = orders.user_id
   GROUP BY users.id, users.name
   ORDER BY total_amount DESC;
   ```

**ポイント**: `COALESCE`関数でNULLを0に変換できます。

---

<!-- _class: title -->

# 17章 3つ以上のテーブルを結合しよう
## ワーク

---

<!-- _class: title-top -->

## 17章 ワーク1: 複数テーブルの結合

### 問題

`users`（id, name）、`orders`（id, user_id, product_id, quantity）、`products`（id, name, price）の3つのテーブルがあります。

1. ユーザー名、注文した商品名、商品価格を取得する
2. ユーザーごとの合計購入金額を取得する

---

<!-- _class: title-top -->

## 17章 ワーク1: 解答例

1. **3つのテーブルを結合**
   ```sql
   SELECT users.name, products.name AS product_name, products.price
   FROM users
   INNER JOIN orders ON users.id = orders.user_id
   INNER JOIN products ON orders.product_id = products.id;
   ```

2. **集計と組み合わせ**
   ```sql
   SELECT users.name, SUM(products.price * orders.quantity) AS total_amount
   FROM users
   INNER JOIN orders ON users.id = orders.user_id
   INNER JOIN products ON orders.product_id = products.id
   GROUP BY users.name;
   ```

---

<!-- _class: title-top -->

## 17章 ワーク1: チャレンジ問題

4つ以上のテーブルを結合した複雑なクエリを作成してください。

以下のテーブルがあります：
- `users`（id, name）
- `orders`（id, user_id, order_date）
- `order_items`（id, order_id, product_id, quantity）
- `products`（id, name, price, category_id）
- `categories`（id, name）

1. ユーザー名、注文日、商品名、カテゴリ名を取得する（4テーブル結合）
2. カテゴリごとの売上合計を取得する（5テーブル結合 + 集計）
3. 最も購入金額が高いユーザーのトップ3を取得する

---

<!-- _class: title-top -->

## 17章 ワーク1: チャレンジ問題の解答例

1. **4テーブル結合**
   ```sql
   SELECT users.name, orders.order_date,
          products.name AS product_name, categories.name AS category_name
   FROM users
   INNER JOIN orders ON users.id = orders.user_id
   INNER JOIN order_items ON orders.id = order_items.order_id
   INNER JOIN products ON order_items.product_id = products.id
   INNER JOIN categories ON products.category_id = categories.id;
   ```

---

<!-- _class: title-top -->

## 17章 ワーク1: チャレンジ問題の解答例（続き）

2. **5テーブル結合 + 集計**
   ```sql
   SELECT categories.name,
          SUM(products.price * order_items.quantity) AS total_sales
   FROM categories
   INNER JOIN products ON categories.id = products.category_id
   INNER JOIN order_items ON products.id = order_items.product_id
   INNER JOIN orders ON order_items.order_id = orders.id
   INNER JOIN users ON orders.user_id = users.id
   GROUP BY categories.name;
   ```

---

<!-- _class: title-top -->

## 17章 ワーク1: チャレンジ問題の解答例（続き）

3. **複雑な集計とLIMIT**
   ```sql
   SELECT users.name,
          SUM(products.price * order_items.quantity) AS total_amount
   FROM users
   INNER JOIN orders ON users.id = orders.user_id
   INNER JOIN order_items ON orders.id = order_items.order_id
   INNER JOIN products ON order_items.product_id = products.id
   GROUP BY users.id, users.name
   ORDER BY total_amount DESC
   LIMIT 3;
   ```

---

<!-- _class: title -->

# 18章 データベース設計を学ぼう
## ワーク

---

<!-- _class: title-top -->

## 18章 ワーク1: ER図の理解

### 問題

以下の要件を満たすER図を設計してください。

**ECサイトの要件**:
- 顧客は複数の注文ができる
- 1つの注文には複数の商品が含まれる
- 商品は複数のカテゴリに属することができる

エンティティ、アトリビュート、リレーションシップを考えてください。

---

<!-- _class: title-top -->

## 18章 ワーク1: 解答例

**エンティティ**:
- 顧客（customers）
- 注文（orders）
- 注文詳細（order_details）
- 商品（products）
- カテゴリ（categories）
- 商品カテゴリ関連（product_categories）

**リレーションシップ**:
- 顧客 1 : N 注文
- 注文 1 : N 注文詳細
- 商品 1 : N 注文詳細
- 商品 M : N カテゴリ（中間テーブル：product_categories）

---

<!-- _class: title-top -->

## 18章 ワーク1: チャレンジ問題

実務のデータベース設計課題に取り組んでください。

**図書館システムの要件**:
- 会員は複数の本を借りることができる
- 本は1冊ずつ管理され、著者情報がある
- 1冊の本には複数の著者がいる場合がある
- 貸出履歴を記録する必要がある
- 本のジャンル分類が必要

1. 必要なテーブル（エンティティ）を列挙する
2. 各テーブルに必要なカラム（アトリビュート）を設計する
3. テーブル間のリレーションシップ（1:N、M:N）を定義する
4. 正規化の観点から設計が適切か確認する

---

<!-- _class: title-top -->

## 18章 ワーク1: チャレンジ問題の解答例

**1. 必要なテーブル**:
- members（会員）
- books（本）
- authors（著者）
- book_authors（本と著者の中間テーブル）
- genres（ジャンル）
- rentals（貸出履歴）

---

<!-- _class: title-top -->

## 18章 ワーク1: チャレンジ問題の解答例

**2. テーブル設計**:
```sql
-- 会員テーブル
CREATE TABLE members (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  join_date DATE
);
```

---

<!-- _class: title-top -->

## 18章 ワーク1: チャレンジ問題の解答例（続き）

```sql
-- 本テーブル
CREATE TABLE books (
  id INT PRIMARY KEY,
  title VARCHAR(200),
  genre_id INT,
  isbn VARCHAR(20),
  published_date DATE
);

-- 著者テーブル
CREATE TABLE authors (
  id INT PRIMARY KEY,
  name VARCHAR(100)
);

-- 本と著者の中間テーブル（M:N）
CREATE TABLE book_authors (
  book_id INT,
  author_id INT,
  PRIMARY KEY (book_id, author_id)
);
```

---

<!-- _class: title-top -->

## 18章 ワーク1: チャレンジ問題の解答例（続き2）

```sql
-- ジャンルテーブル
CREATE TABLE genres (
  id INT PRIMARY KEY,
  name VARCHAR(50)
);

-- 貸出履歴テーブル
CREATE TABLE rentals (
  id INT PRIMARY KEY,
  member_id INT,
  book_id INT,
  rental_date DATE,
  return_date DATE
);
```

---

<!-- _class: title-top -->

## 18章 ワーク1: チャレンジ問題の解答例（続き2）

**3. リレーションシップ**:
- 会員 1 : N 貸出履歴
- 本 1 : N 貸出履歴
- 本 M : N 著者（中間テーブル：book_authors）
- ジャンル 1 : N 本

---

<!-- _class: title -->

# グループワーク
## 実データを使った解析業務

---

<!-- _class: title-top -->

## グループワーク: オープンデータで学ぶSQL

### 実践形式

このグループワークでは、実際のオープンデータをダウンロードして、データベース設計から分析までを実践します。

### 使用するデータ

**総務省統計局「家計調査」CSVデータ**
- データ元：e-Stat（政府統計の総合窓口）
- URL: https://www.e-stat.go.jp/
- 内容：世帯の収入・支出データ（匿名化済み）

---

<!-- _class: title-top -->

## ステップ1: データのダウンロード

### 手順

1. **e-Statにアクセス**
   - https://www.e-stat.go.jp/ にアクセス
   - 「家計調査」で検索

2. **CSVファイルのダウンロード**
   - 「年次」→「世帯属性別」データを選択
   - CSV形式でダウンロード
   - ファイル名: `household_data.csv`

3. **データの確認**
   - Excelまたはテキストエディタで開いて構造を確認

---

<!-- _class: title-top -->

## ステップ2: テーブル設計

### 課題（15分）

CSVデータの構造を確認し、以下のテーブルを設計してください。

1. **householdsテーブル（世帯情報）**
   - 世帯ID、世帯人数、年齢層、地域、年収層

2. **expensesテーブル（支出データ）**
   - 支出ID、世帯ID、年月、カテゴリ、金額

3. **incomesテーブル（収入データ）**
   - 収入ID、世帯ID、年月、収入種別、金額

---

<!-- _class: title-top -->

## ステップ3: CREATE TABLE文の作成

```sql
-- householdsテーブル
CREATE TABLE households (
  household_id INT PRIMARY KEY,
  household_size INT,
  age_group VARCHAR(20),
  region VARCHAR(50),
  income_level VARCHAR(20)
);

-- expensesテーブル
CREATE TABLE expenses (
  expense_id INT PRIMARY KEY AUTO_INCREMENT,
  household_id INT,
  year_month DATE,
  category VARCHAR(50),
  amount DECIMAL(10, 2)
);
```

---

<!-- _class: title-top -->

## ステップ4: CSVデータのインポート

### MySQLでのインポート方法

```sql
LOAD DATA INFILE '/path/to/household_data.csv'
INTO TABLE households
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

**または**、Pythonスクリプトを使用：
```python
import pandas as pd
import mysql.connector
df = pd.read_csv('household_data.csv')
# データベースに挿入
```

---

<!-- _class: title-top -->

## ステップ5: 分析課題（60分）

### 課題1: 地域別支出分析

1. 地域ごとの平均支出額を計算
2. 支出カテゴリ別（食費、住居費、交通費など）の傾向を分析
3. 最も支出が多い地域と少ない地域を特定

### 課題2: 年齢層別の消費傾向

1. 年齢層ごとの平均支出額を比較
2. 年齢層によって支出カテゴリに差があるか分析
3. 若年層と高齢層の消費パターンの違いを明確化

---

<!-- _class: title-top -->

## ステップ5: 分析課題（続き）

### 課題3: 収入と支出の関係

1. 年収層別の平均支出額を計算
2. 収入に対する支出の比率（エンゲル係数など）を算出
3. 貯蓄率が高い世帯の特徴を分析

### 課題4: 時系列分析

1. 月別の支出推移をグラフ化
2. 季節要因（冬のボーナス時期、夏の旅行シーズンなど）の影響を分析
3. 年間を通じた消費パターンの傾向をレポート

---

<!-- _class: title-top -->

## 補足: 仮想データの追加（オプション）

実データに加えて、金融機関の視点からの分析を行う場合：

```sql
-- 仮想データ：金融商品の保有状況
CREATE TABLE financial_products (
  product_id INT PRIMARY KEY,
  household_id INT,
  product_type VARCHAR(50),
  balance DECIMAL(12, 2),
  start_date DATE
);

-- サンプルデータ
INSERT INTO financial_products VALUES
(1, 1, '普通預金', 5000000, '2020-01-01'),
(2, 1, '定期預金', 10000000, '2021-06-01');
```

---

<!-- _class: title-top -->

## 実施ガイドライン

### 進め方（合計120分）

1. **データダウンロードと確認（10分）**
2. **テーブル設計とCREATE文作成（20分）**
3. **データインポート（15分）**
4. **SQL分析クエリ作成・実行（60分）**
5. **レポート作成と発表準備（15分）**

### チーム内での役割分担

- データベース設計担当
- SQLクエリ作成担当
- データ分析・可視化担当
- レポート作成・発表担当

---

<!-- _class: title-top -->

## 評価ポイント

### 技術面

- テーブル設計の適切性（正規化、データ型選択）
- CREATE TABLE文の正確性
- SQLクエリの効率性と可読性
- データインポートの成功

### 分析面

- データから得られた洞察の深さ
- ビジネス視点での解釈
- グラフや表を使った効果的な可視化
- 実務への応用可能性

---

<!-- _class: title-top -->

## 参考リンク

### オープンデータソース

- **e-Stat（政府統計の総合窓口）**: https://www.e-stat.go.jp/
- **オープンデータカタログサイト**: https://www.data.go.jp/
- **東京都オープンデータ**: https://portal.data.metro.tokyo.lg.jp/

### データ形式

- CSV（カンマ区切り）
- Excel（.xlsx）
- JSON

**注意**: 個人情報保護のため、すべて匿名化・集計済みデータを使用