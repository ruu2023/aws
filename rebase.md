# Rebase による大きな改修の切り出し手順

## シナリオ

develop ブランチに大きな改修（リファクタリング等）が入った後、複数人が小さな改修を重ねた。
大きな改修のリリース延期が決まり、小さな改修だけをリリースする必要が生じた。

```
[現状の develop]
init → 大きな改修 → 小さな改修1 → 小さな改修2 → 小さな改修3 → ...

[目標]
init → 小さな改修1(適応済) → 小さな改修2(適応済) → 小さな改修3(適応済) → ...
```

小さな改修は大きな改修の影響（リファクタリング後の構造）を受けているため、
そのままでは大きな改修なしに動かない。適応作業が必要。

---

## 事前確認

force push の影響範囲を把握する。

```bash
# 大きな改修が触ったファイルを確認
git show <大きな改修のハッシュ> --stat

# 小さな改修それぞれが触ったファイルを確認
git log --stat <大きな改修のハッシュ>..HEAD
```

**影響を受ける開発者の条件：**
- force push 後に `pull --rebase` で replay されるコミットが、割り込みコミットと同じファイル・同じ行を触っている場合にコンフリクトが発生する
- 別ファイルまたは別の行であれば自動解決される

---

## チームへの事前通知

force push 前に必ず全員へ周知する。

```
【通知内容】
・大きな改修を develop から切り出します
・○月○日○時に force push を実施します
・作業中の変更は一時停止してください
・force push 後に pull --rebase をお願いします
・コンフリクトが発生した場合は個別に連絡してください
```

---

## 各開発者の準備（force push 前）

```bash
# バックアップブランチを作成しておく
git branch backup/before-rebase

# 現在の状態を確認
git log --oneline
```

---

## 実施手順

### Step 1: 作業ブランチを作成

大きな改修が入る直前のコミットから作業ブランチを切る。

```bash
# 大きな改修直前のハッシュを確認
git log --oneline develop

# 作業ブランチを作成
git checkout -b work/small-fixes-only <大きな改修直前のハッシュ>
```

### Step 2: 小さな改修を適応させながら取り込む

大きな改修前の構造（旧構造）で動くように各コミットを修正しながら追加する。

```bash
# cherry-pick して旧構造に合わせて修正
git cherry-pick <小さな改修1のハッシュ>
# 必要に応じてファイルを編集して旧構造に適応
git add .
git commit --amend

# 同様に残りの小さな改修も取り込む
```

### Step 3: develop で rebase -i を開始

```bash
git checkout develop

# rebase -i のシーケンスを設定するスクリプト
cat > /tmp/seq_editor.py << 'EOF'
import sys
with open(sys.argv[1], encoding='utf-8') as f:
    lines = f.readlines()
result = ['break\n']
for line in lines:
    stripped = line.strip()
    if not stripped or stripped.startswith('#'):
        continue
    parts = stripped.split(None, 2)
    if len(parts) < 2:
        continue
    action, hash_val = parts[0], parts[1]
    msg = parts[2] if len(parts) > 2 else ''
    # 残したいコミットのハッシュだけ pick、他は drop
    if hash_val in ['<残したいハッシュ1>', '<残したいハッシュ2>']:
        result.append(f'pick {hash_val} {msg}\n')
    else:
        result.append(f'drop {hash_val} {msg}\n')
with open(sys.argv[1], 'w', encoding='utf-8') as f:
    f.writelines(result)
EOF

GIT_SEQUENCE_EDITOR="python3 /tmp/seq_editor.py" git rebase -i <大きな改修直前のハッシュ>
```

### Step 4: break で停止したら cherry-pick を挟む

```bash
# 作業ブランチの適応済みコミットを挟み込む
git cherry-pick <小さな改修1適応済> <小さな改修2適応済> <小さな改修3適応済>

# コンフリクトが発生した場合
git add app.py
git rebase --continue
```

### Step 5: rebase を完了させる

```bash
git rebase --continue
# drop 指定のコミットはスキップされ、pick のコミットが適用される
```

### Step 6: 結果を確認

```bash
# 履歴を確認
git log --oneline

# ファイルの中身を確認
git show HEAD:app.py
```

### Step 7: force push

```bash
git push --force-with-lease origin develop
```

`--force-with-lease` はリモートが自分の知らない間に更新されていた場合に push を拒否する。
通常の `--force` より安全。

---

## 各開発者の対応（force push 後）

### pull --rebase を実行

```bash
git pull --rebase origin develop
```

### コンフリクトが発生した場合

どのコミットで止まっているかを確認する：

```bash
git status
```

**判断基準：**

| コミットの種類 | 対応 |
|---|---|
| 大きな改修・旧クラス版の小さな改修 | `git rebase --skip`（新 develop に適応済みのため） |
| 自分のコミットで大きな改修に依存していたもの | `git rebase --skip` の後に書き直し |
| 自分のコミットで独立したもの | 自動適用される |

```bash
# コンフリクトしたコミットをスキップ
git rebase --skip

# コンフリクトを手動解決する場合
# ファイルを編集 → git add → git rebase --continue
git add <ファイル>
git rebase --continue
```

### わからなくなったら abort して戻る

```bash
git rebase --abort

# バックアップブランチに戻る
git checkout backup/before-rebase
```

---

## 注意点

### force push の影響を受ける人の条件

| 条件 | 意味 |
|---|---|
| **影響を受ける（pull --rebase で replay 対象になる）** | force push で書き換えられたコミットより後に自分のコミットがある |
| **その中でコンフリクトになる** | さらに同じファイルの同じ行を触っている |
| **その中で自動解決される** | 別ファイルまたは別の行 |

```
書き換えられた履歴
    ↓
[ここより後に自分のコミットがある] → pull --rebase の replay 対象
    ├─ 同じ行を触っている → コンフリクト（手動解決）
    └─ 別ファイル・別行   → 自動解決

[ここより後に自分のコミットがない] → replay なし、そのまま更新
```

### コンフリクトの発生条件

```
割り込みコミットが触ったファイル ∩ 自分のコミットが触ったファイル = 空
  → 自動解決

割り込みコミットが触った行 = 自分のコミットが触った行
  → コンフリクト（人間が判断）
```

### incoming と HEAD の向き（rebase 中）

rebase 中のコンフリクトは merge と向きが逆になる。

| | HEAD 側 `<<<<<<<` | incoming 側 `>>>>>>>` |
|---|---|---|
| `git merge` | 自分のブランチ | 取り込む側 |
| `git rebase` | 新ベース（新 develop） | 自分の古いコミット |

`-X` オプションで自動選択も可能だが意図しない結果になる場合がある：

```bash
git pull --rebase -X ours    # 新ベース優先（自分のコミットが消える可能性）
git pull --rebase -X theirs  # 自分のコミット優先（大きな改修が復活する可能性）
```

### 重複コミットについて

`pull --rebase` によってハッシュは変わるが、同じ内容のコミットが重複することはない。
git は差分（patch-id）で同一性を判断する。

### reset --hard との使い分け

| 状況 | 推奨 |
|---|---|
| 自分だけのコミットがある | `pull --rebase` |
| 追加コミットがない（develop をそのまま追っていた） | `git fetch && git reset --hard origin/develop` |

---

## force push 失敗・巻き戻し手順

### バックアップブランチから develop を戻す

```bash
git checkout develop
git reset --hard backup/before-rebase
```

### リモートも巻き戻す（force push してしまった後）

```bash
git push --force-with-lease origin develop
```

### シナリオ別の対処

| 状況 | 対処 |
|---|---|
| force push 前に気づいた | ローカルで `git reset --hard backup/before-rebase` だけで OK |
| force push 後、誰も pull していない | ローカルを戻して再度 force push |
| force push 後、誰かが pull してしまった | その人も `git reset --hard` が必要になる |

### `--force-with-lease` が守ってくれること

自分が知らない間に誰かが push していた場合、force push を自動で弾く。
意図しない上書きを防ぐために `--force` ではなく必ず `--force-with-lease` を使う。

force push 後はすぐにチームへ通知し、各自に `pull --rebase` してもらうこと。
