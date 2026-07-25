# love_audio — 音源からおすすめEQを提案するツール

## 概要
love_audio は、楽曲ファイルから特徴量を抽出し学習済みモデル（RandomForest 等）を使って、その楽曲に対するおすすめのEQ設定を提案するプロジェクトです。ローカル実行を主目的に設計しており、必要に応じてサーバーへデプロイできます。

## 目次
- [特徴](#特徴)
- [前提条件](#前提条件)
- [インストール](#インストール)
- [使い方（ローカル実行）](#使い方ローカル実行)
- [ディレクトリ構成](#ディレクトリ構成)
- [著作権・注意事項](#著作権・注意事項)
- [開発者・ライセンス](#開発者ライセンス)

## 特徴
- 音源（例: .mp3）から特徴量を抽出してモデルでEQを提案します。
- 学習済みモデル（`model/learn-model.joblib`）を利用して高速に推論します。
- アップロードされた音源はオンメモリで解析し、サーバーにファイルを残さない運用を推奨します。

## 前提条件
- Python 3.8 以上
- 必要なライブラリは [requirements.txt](requirements.txt) を参照してください。

## インストール
1. リポジトリをクローンします。

```bash
git clone <repo-url>
cd love_audio
```

2-a. Conda を使う（推奨）

```bash
conda env create -f create_env.yml
conda activate loveaudio_env
```

2-b. venv + pip を使う場合

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## 使い方（ローカル実行）
- `main.py` や `main_api.py` の引数に合わせて実行してください。例:

```bash
python main.py --input path/to/song.mp3 --output eq_suggestion.json
```

- `.env` に API キー等を保存する設計です。`.env` は必ず `.gitignore` に登録してコミットしないでください。

## ディレクトリ構成（抜粋）
- `app/`
  - `core/` — 特徴量抽出・推論（`analyzer.py`, `learn_model.py` 等）
  - `database/` — DB 接続・リポジトリ
- `moduls/` — スキーマなど補助モジュール
- `model/` — 学習済みモデル（`learn-model.joblib`）

## 著作権・注意事項
- 本プロジェクトは音源そのものを配布しません。著作権法等に配慮して、特徴量のみを抽出・利用する設計です。
- 外部から音源ファイルを受け取る実装を行う場合は、オンメモリ解析に留めるなどファイル保存を避ける運用を推奨します。法律的な判断が必要な場面は専門家に相談してください。

## 開発メモ
- 仮想環境名（例）: `loveaudio_env`
- `.env` として秘密情報を保持します。ローカル環境のみで使用してください。

## 開発者・ライセンス
- 作成者: リポジトリの所有者
- ライセンス: 適切なライセンス（例: MIT）を明示してください

---


