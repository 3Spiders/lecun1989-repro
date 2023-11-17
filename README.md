fork from https://github.com/karpathy/lecun1989-repro

## 安装流程

### 创建虚拟环境和安装依赖

```
python3 -m venv lecun1989
source lecun1989/bin/activate
pip install torch numpy torchvision matplotlib tensorboardX
```

### 执行 prepro.py

```
python3 prepro.py
```

## 执行查看下载内容

```
python3 show_image_py
```

## 执行模型训练

```
python3 repro.py
```
