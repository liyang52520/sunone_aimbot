# Aimbot

## Note

1. only for apex
2. only for intel gpu (openVino)
3. only use makcu for moving your mouse

## Start

1. install base requirements
```shell
pip install -r requirements.txt
```

2. install torch for intel gpu
```shell
python -m pip install torch==2.8.0 torchvision==0.23.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/xpu
python -m pip install intel-extension-for-pytorch==2.8.10+xpu --index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/cn/
```