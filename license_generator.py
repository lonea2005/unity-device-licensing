#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
設備授權密碼生成器 - 開發者工具
Device License Password Generator - Developer Tool

用法 / Usage:
    python license_generator.py XXXX-XXXX-XXXX-XXXX
    或 / or:
    python license_generator.py (然後輸入設備碼 / then enter device code)
"""

import hashlib
import sys


def generate_license_password(device_code: str) -> str:
    """
    根據設備碼生成授權密碼
    Generate license password based on device code
    
    重要：此算法必須與 Unity 客戶端中的 GenerateExpectedPassword 方法完全一致！
    Important: This algorithm must be exactly the same as GenerateExpectedPassword in Unity client!
    
    Args:
        device_code: 用戶的設備碼 / User's device code
        
    Returns:
        授權密碼 / License password
    """
    # 使用設備碼和鹽值生成密碼
    # 這個鹽值必須與 Unity 客戶端中的完全一致
    combined = device_code + "License_Password_Salt_2024"
    hash_bytes = hashlib.sha256(combined.encode('utf-8')).digest()
    
    # 取第8-15字節作為密碼（與客戶端一致）
    password_hex = ''.join(f'{b:02X}' for b in hash_bytes[8:16])
    
    # 格式化為 XXXX-XXXX-XXXX-XXXX 格式
    return f"{password_hex[0:4]}-{password_hex[4:8]}-{password_hex[8:12]}-{password_hex[12:16]}"


def is_valid_device_code_format(code: str) -> bool:
    """
    驗證設備碼格式
    Validate device code format
    
    Args:
        code: 設備碼 / Device code
        
    Returns:
        格式是否正確 / Whether format is correct
    """
    # 預期格式：XXXX-XXXX-XXXX-XXXX
    if len(code) != 19:
        return False
    
    parts = code.split('-')
    if len(parts) != 4:
        return False
    
    for part in parts:
        if len(part) != 4:
            return False
        if not part.isalnum():
            return False
    
    return True


def main():
    print("===========================================")
    print("    設備授權密碼生成器")
    print("    Device License Password Generator")
    print("===========================================")
    print()
    
    # 獲取設備碼
    if len(sys.argv) > 1:
        device_code = sys.argv[1]
    else:
        device_code = input("請輸入設備碼 / Please enter device code: ")
    
    if not device_code or not device_code.strip():
        print("錯誤：設備碼不能為空！")
        print("Error: Device code cannot be empty!")
        sys.exit(1)
    
    # 標準化設備碼格式
    device_code = device_code.strip().upper()
    
    # 驗證設備碼格式
    if not is_valid_device_code_format(device_code):
        print("警告：設備碼格式可能不正確，預期格式為 XXXX-XXXX-XXXX-XXXX")
        print("Warning: Device code format may be incorrect, expected format is XXXX-XXXX-XXXX-XXXX")
    
    # 生成密碼
    password = generate_license_password(device_code)
    
    print()
    print("-------------------------------------------")
    print(f"設備碼 / Device Code: {device_code}")
    print(f"授權密碼 / License Password: {password}")
    print("-------------------------------------------")
    print()
    print("請將此密碼發送給用戶。")
    print("Please send this password to the user.")


if __name__ == "__main__":
    main()
