#!/usr/bin/env python3
"""
文件大小转换工具

将字节大小转换为更易读的格式（如KB、MB、GB等）
"""
import math
import click
from typing import Union

def convert_size(size_bytes: int) -> str:
    """
    将字节大小转换为更易读的格式
    
    Args:
        size_bytes: 字节大小
        
    Returns:
        str: 格式化后的字符串，如 "1.5 MB"
    """
    if size_bytes == 0:
        return "0 B"
    
    units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    size = round(size_bytes / p, 2)
    
    return f"{size} {units[i]}"

@click.command()
@click.argument('size', type=int, required=False)
@click.option('--interactive', '-i', is_flag=True, help='交互模式')
def main(size: Union[int, None], interactive: bool):
    """文件大小转换工具"""
    if interactive or size is None:
        while True:
            try:
                size_input = input("\n请输入字节大小 (输入 'q' 退出): ").strip()
                if size_input.lower() == 'q':
                    break
                size = int(size_input)
                print(f"转换结果: {convert_size(size)}")
            except ValueError:
                print("错误: 请输入有效的数字")
    else:
        print(f"{size} 字节 = {convert_size(size)}")

if __name__ == "__main__":
    main()
