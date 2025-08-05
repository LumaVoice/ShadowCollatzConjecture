# Shadow Collatz Conjecture / シャドウ・コラッツ予想

Python tools for exploring and exporting the **Shadow Collatz Conjecture** –  
a novel integer mapping hypothesized to converge to `-1` for all nonzero integers.

すべての非ゼロ整数が `-1` に収束すると予想される新しい整数写像  
**シャドウ・コラッツ予想** の計算と出力を行う Python ツール集です。

---

## 📖 About the Conjecture / 予想について

The **Shadow Collatz mapping** is defined as:

**シャドウ・コラッツ写像**は次のように定義されます：

\[
T(n) =
\begin{cases}
n / (-2), & \text{if } n \text{ is even} \\
3n - 1, & \text{if } n \text{ is odd}
\end{cases}
\]

**Conjecture / 予想**:  
For all integers \( n \neq 0 \), repeated iteration of \( T(n) \) eventually reaches `-1`.

全ての整数 \( n \neq 0 \) に対し、この写像を繰り返し適用すると最終的に `-1` に到達すると予想します。

---

## 🗂 Scripts / スクリプト一覧

| Script name | Description (English) | 説明 (日本語) |
|-------------|------------------------|--------------|
| [`export_shadow_collatz.py`](export_shadow_collatz.py) | Full range scan, convergence check, and export to wide CSV + summary CSV + log | 全範囲走査・収束判定・ワイドCSV+サマリーCSV+ログ出力 |
| `example.py` | Minimal demonstration of generating a Shadow Collatz trajectory | シャドウ・コラッツの軌道生成を最小限のコードで実演 |
| `analyze_max_steps.py` | Analyze maximum steps and initial values across a given range | 指定範囲での最大ステップ数と初期値の解析 |

---

## 🚀 Features / 機能

- **Full-range scan / 全範囲走査**: 任意の開始値・終了値を指定（0は自動で除外）
- **Excel-friendly / Excel対応**: 各ステップを別の列に格納
- **Summary output / サマリー出力**: ステップ数・最大値・最小値・収束判定のみ
- **UTF-8 BOM encoding / UTF-8 BOM付きエンコード**: Excelで文字化けせずに読み込み可能
- **Progress display / 進捗表示**: 大規模実行時の進捗表示
- **Custom step limit / カスタムステップ上限**（デフォルト 1000）

---

## 📦 Requirements / 必要環境

- Python 3.8+
- No external dependencies（標準ライブラリのみ使用）

---

## ⚙️ Usage / 使い方

1. **Clone the repository / リポジトリをクローン**
```bash
git clone https://github.com/LumaVoice/ShadowCollatzConjecture.git
cd ShadowCollatzConjecture
```

2. **Edit settings at the top of the script / スクリプト冒頭の設定を編集**  
   Example from `export_shadow_collatz.py`:
```python
START: int = -1000
END: int = 1000
STEP_LIMIT: int = 1000
OUT_WIDE_CSV: str = "shadow_collatz_wide_-1000_to_1000.csv"
WRITE_SUMMARY_CSV: bool = True
OUT_SUMMARY_CSV: str = "shadow_collatz_summary_-1000_to_1000.csv"
LOG_NONCONVERGED: bool = True
OUT_NONCONVERGED_TXT: str = "shadow_collatz_nonconverged.txt"
PROGRESS_EVERY: int = 5000
```

3. **Run the script / スクリプトを実行**
```bash
python3 export_shadow_collatz.py
```

---

## 📂 Output Example / 出力例

**Wide CSV** (`shadow_collatz_wide_-1000_to_1000.csv`):

| initial | steps | max | min | converged | step1 | step2 | step3 | ... |
|---------|-------|-----|-----|-----------|-------|-------|-------|-----|
| -1000   | 10    | 1024 | -1024 | YES | -1000 | 500 | -250 | ... |
| -999    | 15    | ... | ... | YES | -999  | -2998 | 1499 | ... |

**Summary CSV** (`shadow_collatz_summary_-1000_to_1000.csv`):

| initial | steps | max | min | converged |
|---------|-------|-----|-----|-----------|
| -1000   | 10    | 1024 | -1024 | YES |
| -999    | 15    | ... | ... | YES |

**Non-convergence log / 非収束ログ** (`shadow_collatz_nonconverged.txt`):
```
# Non-converged within 1000 steps
123456    steps=1000
...
```

---

## 📜 License / ライセンス

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

このプロジェクトは MITライセンス で公開されています。詳細は [LICENSE](LICENSE) をご覧ください。

---

## ✍️ Author / 作者

- **Ryosuke Miyazawa**  
- Proposer of the Shadow Collatz Conjecture / シャドウ・コラッツ予想提唱者  
- Contact / 連絡先: luma.voice@proton.me

---

## 🔗 External Links / 外部リンク

- **arXiv author page**: [https://arxiv.org/a/lumavoice.html](https://arxiv.org/a/lumavoice.html)
- **Zenodo record**: [https://doi.org/XXXXX](https://doi.org/XXXXX)  <!-- DOIが発行されたら置き換え -->
- **OEIS profile**: [https://oeis.org/wiki/User:Ryosuke_Miyazawa](https://oeis.org/wiki/User:Ryosuke_Miyazawa)
