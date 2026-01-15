---
marp: true
theme: custom
footer: "**SAMURAI　データベース基礎講座 ワーク集 解答例**"
paginate: true

title: "データベース基礎講座 ワーク集 解答例"
subtitle: "SQL学習用演習問題の解答と解説"
author: "SAMURAI"
date: "2025-11-01"

---

<!-- _class: title -->

# データベース基礎講座
## ワーク集 解答例

---

<!-- _class: title -->

# 1章 データベースの概要を学ぼう
## ワーク解答

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

## 1章 ワーク2: チャレンジ問題の解答例（続き）

4. **複雑な検索とレポート生成**
   - Excel: 複雑な条件での検索に時間がかかる
   - データベース: インデックスにより高速検索が可能、複数テーブルを結合した分析も容易

5. **データのバックアップと復旧**
   - Excel: ファイル単位でのバックアップのみ
   - データベース: 自動バックアップ、ポイントインタイムリカバリが可能

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

<!-- _class: title-top challenge -->

## 1章 ワーク3: チャレンジ問題の解答例

### **図書館システムのテーブル設計：**

**1. 書籍テーブル（books）**
- book_id（書籍ID、主キー）
- title（書籍タイトル）
- author（著者名）
- isbn（ISBN番号）
- category（カテゴリ）

---

<!-- _class: title-top challenge -->

## 1章 ワーク3: チャレンジ問題の解答例

**2. 会員テーブル（members）**
- member_id（会員ID、主キー）
- name（会員名）
- email（メールアドレス）
- phone（電話番号）
- registration_date（登録日）

---

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

## 2章 ワーク1: チャレンジ問題の解答例

**1. SELECT → DROP → SELECTの結果：**

エラーが発生します。理由：
- 1回目の`SELECT * FROM users;`は成功（テーブルが存在するため）
- `DROP TABLE users;`でusersテーブルが削除される
- 2回目の`SELECT * FROM users;`でエラー発生
- エラーメッセージ：「Table 'users' doesn't exist」
- DROP文は取り消せないので、テーブルを再度作成する必要がある

---

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

## 2章 ワーク2: チャレンジ問題の解答例

**3. nameとpriceカラムのみ表示**

```sql
SELECT name, price FROM products WHERE price >= 5000;
```

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

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

## 3章 ワーク2: チャレンジ問題の解答例

**1. クレジットカード番号（16桁）**
- **推奨**: `CHAR(16)` または `VARCHAR(19)`（ハイフン含む場合）
- **理由**: 固定長16桁なので`CHAR`が最適。数値計算しないので文字列型を使う
- **注意**: セキュリティ上、暗号化して保存すべき

**2. 口座残高（マイナスあり、小数点以下2桁）**
- **推奨**: `DECIMAL(15, 2)`
- **理由**: 金額計算で正確性が必要。負の値も扱えるため

---

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

## 3章 ワーク4: チャレンジ問題の解答例

**ケース1：電話番号をINT型で保存**

問題点：
1. **先頭の0が消える**：「090-1234-5678」を数値として保存すると「9012345678」になり、先頭の0が失われる
2. **ハイフンが保存できない**：「090-1234-5678」の形式が保存できない
3. **国際電話番号に対応できない**：「+81」などの記号が保存できない
4. **範囲オーバー**：INT型の最大値を超える電話番号がある

正解：`VARCHAR(20)`を使用

---

<!-- _class: title-top challenge -->

## 3章 ワーク4: チャレンジ問題の解答例

**ケース2：商品価格をFLOAT型で保存**

発生する問題：
- **丸め誤差**：100.10円が100.0999...円のように保存される
- **合計計算のずれ**：複数の商品価格を合計すると、実際の金額とずれる
- 例：1.1 + 2.2 ≠ 3.3（浮動小数点演算の誤差）

正解：`DECIMAL(10, 2)`を使用

---

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

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
## ワーク解答

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
## ワーク解答

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
## ワーク解答

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
## ワーク解答

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
## ワーク解答

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
## ワーク解答

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

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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
## ワーク解答

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

<!-- _class: title-top challenge -->

## 18章 ワーク1: チャレンジ問題の解答例

**1. 必要なテーブル**:
- members（会員）
- books（本）
- authors（著者）
- book_authors（本と著者の中間テーブル）
- genres（ジャンル）
- rentals（貸出履歴）

---

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

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

<!-- _class: title-top challenge -->

## 18章 ワーク1: チャレンジ問題の解答例（続き2）

**3. リレーションシップ**:
- 会員 1 : N 貸出履歴
- 本 1 : N 貸出履歴
- 本 M : N 著者（中間テーブル：book_authors）
- ジャンル 1 : N 本

---

<!-- _class: title -->

# おつかれさまでした

**SQL学習を継続しましょう！**
