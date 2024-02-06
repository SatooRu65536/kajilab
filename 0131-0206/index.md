# mocopiとaction slam(SVM)

## 出席率
- 3年セミナー：??%

## スケジュール
### 短期的な予定
- [ ] mocopi と action slam2
    - [x] シーンとランドマークを決める(~2月上旬)
    - [x] SVM で動作判別する
    - [ ] ?
    - [ ] 論文書く
    - [ ] 発表

### 長期的な予定
- ~?月 シーン検知?をする
- ~?月 論文を書く
- ~?月 論文発表したい

## 進捗報告
## 目標
一連の動作から特定の動作(ランドマーク)を見つけて位置推定をする.
まずは、ランドマークを見つけるところから

今回は梶研内で色々な動作をする中で以下の3つに分類する
- 冷蔵庫を開ける(1, 青)
- 冷蔵庫を閉める(2, 黄)
- その他(0, 白)

## 使用する特徴量
- 平均
- 分散
- 相関
- ゼロ交差率
- エネルギー
    - 未実装

## 前回
window_size = 30 (0.5s)
<img width="1632" alt="image.png (54.6 kB)" src="https://img.esa.io/uploads/production/attachments/21347/2024/01/28/148142/5c3501d1-5c70-4b9a-9265-a664d30455c5.png">

- そこそこの精度ではできた
- 1回の "開け" or "閉め" の中で確実に "開け" or "閉め" をしている部分があればいい
- 滑らかにする
    - "開ける"が一瞬の間隔で連続で出てくることはない
- データをもっと取りたい
- (処理を早くしたい)

## 滑らかにした
<img width="1632" alt="image.png (54.6 kB)" src="https://img.esa.io/uploads/production/attachments/21347/2024/02/06/148142/de6e5815-485e-4642-90f5-1c4454e6972e.png">

window_size = 30 (0.5s)
<img width="1632" alt="image.png (55.9 kB)" src="https://img.esa.io/uploads/production/attachments/21347/2024/02/06/148142/121c6793-faa3-4cd9-8de0-e6eabab5c31a.png">

window_size = 60 (1.0s)
<img width="1632" alt="image.png (55.2 kB)" src="https://img.esa.io/uploads/production/attachments/21347/2024/02/06/148142/d1600c47-3304-42d8-a61b-6feb7a27e56d.png">

## より多くのデータを取る
### 問題点
動画を元に手動でラベル付けするのは面倒すぎる

```py:サンプル
labels = [
    {'num': 1, 'title': '冷蔵庫を開ける', 'times': [[11.366666666666665, 12.8], [34.26666666666666, 36.13333333333333], [40.39999999999999, 42.7], [56.433333333333344, 58.39999999999999], [78.46666666666667, 79.86666666666669], [104.89999999999999, 106.43333333333332], [134.1, 135.90000000000003]]},
    {'num': 2, 'title': '冷蔵庫を閉める', 'times': [[13.833333333333334, 15.833333333333334], [36.36666666666667, 38.73333333333333], [42.800000000000004, 44.73333333333333], [58.73333333333333, 60.39999999999999], [83.40000000000002, 84.79999999999998], [107.26666666666667, 108.83333333333333], [136.2666666666667, 138.4333333333333]]}
]
```

もっと楽にしたい
→ 冷蔵庫の扉センシング

<img width="2976" alt="IMG_6036.JPG (1.8 MB)" src="https://img.esa.io/uploads/production/attachments/21347/2024/02/06/148142/f3114a47-9ece-40b3-af3b-904c55470036.JPG">

<img width="869" alt="image.png (61.1 kB)" src="https://img.esa.io/uploads/production/attachments/21347/2024/02/06/148142/638c4a90-1cfb-44e5-8abf-15bbba58376d.png">

加速度が +0.05以上は開け, -0.05以下は閉めとし、
間隔が 0.5s 以下は削除
<img width="1256" alt="image.png (89.0 kB)" src="https://img.esa.io/uploads/production/attachments/21347/2024/02/06/148142/69140665-e848-4f8f-b75e-5933c9519311.png">

場合に合わせてパラメータを変えればうまく取れるためOK

### 結果(SVM)
<img width="1632" alt="image.png (63.8 kB)" src="https://img.esa.io/uploads/production/attachments/21347/2024/02/06/148142/58e07f3b-a2cb-4713-9ddb-2f59bc0da573.png">
<img width="1632" alt="image.png (62.0 kB)" src="https://img.esa.io/uploads/production/attachments/21347/2024/02/06/148142/08230443-5177-4cc4-8b19-3249c1d446ea.png">

とてもひどい
→ ラベル付けが上手くいってなかった？

### TODO
- ラベリングを冷蔵庫の扉センシング
- (滑らかにした後の次の段階)
- エネルギーを出す

## 進路関係
### バイト始めます
外山さんの紹介で [pluszero](https://plus-zero.co.jp/) に応募し、面接した
面接→コーディングテストの直後に合格と言われた(早すぎる)

## 余談
### 学生課からの依頼でWebアプリ作ってます
> 新入生に向けて教室や建物の位置を知れるサイトを作って欲しい

[AITガイド](https://ait-guide.sysken.net/)

<img width="2160" alt="image.png (476.3 kB)" src="https://img.esa.io/uploads/production/attachments/21347/2024/02/06/148142/198a8927-0da5-4237-931c-cd301ae77b5e.png">
