# GPTalks

[![Pylint](https://github.com/liyixin1/GPTalks/actions/workflows/pylint.yml/badge.svg)](https://github.com/liyixin1/GPTalks/actions/workflows/pylint.yml)
[![Create Release](https://github.com/liyixin1/GPTalks/actions/workflows/release.yml/badge.svg)](https://github.com/liyixin1/GPTalks/actions/workflows/release.yml)

![图片](https://github.com/liyixin1/GPTalks/assets/87890585/fd18a52e-0d77-4fcb-aaae-f8139e991d7c)

## 打包软件
```shell
pyinstaller --onefile --windowed main.py -n GPTalks.exe
cp config.toml GPTalks/
cp ai_model.json GPTalks/
cp -r qss GPTalks/
cp LICENSE GPTalks/
cp -r --parents ui/image GPTalks/
```

