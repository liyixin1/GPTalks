# GPTalks

[![Pylint](https://github.com/liyixin1/GPTalks/actions/workflows/pylint.yml/badge.svg)](https://github.com/liyixin1/GPTalks/actions/workflows/pylint.yml)

![图片](https://github.com/liyixin1/GPTalks/assets/87890585/fdd9dbcb-ce57-4165-adf3-feae61e55db3)

## 打包软件
```shell
pyinstaller --onefile --windowed main.py -n GPTalks.exe
cp config.toml dist/
cp ai_model.json dist/
```

