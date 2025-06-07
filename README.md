# 文件大小转换工具

一个简单的Python命令行工具，用于将字节大小转换为更易读的格式（如KB、MB、GB等）。

## 功能特点

- 支持交互式模式
- 支持直接通过命令行参数输入
- 支持大数字转换（最大支持YB）
- 简单易用的命令行界面

## 安装

1. 确保已安装Python 3.6或更高版本
2. 克隆此仓库
3. 安装依赖：

```bash
pip install -r requirements.txt
```

## 使用方法

### 直接转换

```bash
python filesize_converter.py 1024
# 输出: 1024 字节 = 1.0 KB
```

### 交互模式

```bash
python filesize_converter.py --interactive
# 或
python filesize_converter.py -i
```

然后按照提示输入要转换的字节大小。

## 示例

```bash
# 直接转换
$ python filesize_converter.py 1048576
1048576 字节 = 1.0 MB

# 交互模式
$ python filesize_converter.py -i
请输入字节大小 (输入 'q' 退出): 1024
转换结果: 1.0 KB
请输入字节大小 (输入 'q' 退出): 1500000
转换结果: 1.43 MB
请输入字节大小 (输入 'q' 退出): q
```

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT
