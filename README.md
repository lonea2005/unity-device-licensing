# Unity Device Licensing System

Unity 設備授權系統 - 基於設備硬體碼的軟體授權保護方案

A device-based software licensing protection system for Unity applications.

## 功能特點 / Features

- 🔐 **設備綁定授權** - 每個授權密碼只對特定設備有效
- 🎮 **Unity 原生支持** - 可直接在 Unity 專案中使用
- 🐍 **Python 授權生成器** - 開發者可輕鬆生成授權密碼
- 💾 **自動保存授權** - 授權狀態自動保存，無需重複輸入

## 工作原理 / How It Works

```
1. 用戶啟動應用 → 應用根據設備硬體資訊生成唯一的「設備碼」
2. 用戶將設備碼發送給開發者
3. 開發者使用 license_generator.py 生成對應的「授權密碼」
4. 用戶輸入授權密碼 → 僅在該設備上有效，其他設備無法使用
```

## 目錄結構 / Project Structure

```
unity-device-licensing/
├── UnityClient/
│   └── Scripts/
│       ├── DeviceLicenseManager.cs  # 核心授權管理器
│       ├── LicenseUIManager.cs      # UI 管理器（可選）
│       └── LicenseExample.cs        # 使用範例
├── license_generator.py             # Python 授權密碼生成器
└── README.md
```

## 快速開始 / Quick Start

### 1. Unity 客戶端設置

將 `UnityClient/Scripts/` 資料夾中的腳本複製到您的 Unity 專案中。

#### 基本使用

```csharp
using DeviceLicensing;
using UnityEngine;

public class MyGame : MonoBehaviour
{
    void Start()
    {
        // 確保 DeviceLicenseManager 存在
        if (DeviceLicenseManager.Instance == null)
        {
            GameObject obj = new GameObject("DeviceLicenseManager");
            obj.AddComponent<DeviceLicenseManager>();
        }
        
        // 檢查授權狀態
        if (DeviceLicenseManager.Instance.IsLicensed)
        {
            // 已授權，開始遊戲
            StartGame();
        }
        else
        {
            // 未授權，顯示設備碼
            string deviceCode = DeviceLicenseManager.Instance.DeviceCode;
            Debug.Log($"設備碼: {deviceCode}");
            // 顯示授權輸入介面...
        }
    }
    
    public void OnUserEnterPassword(string password)
    {
        // 驗證用戶輸入的密碼
        bool success = DeviceLicenseManager.Instance.ValidateLicense(password);
        if (success)
        {
            StartGame();
        }
        else
        {
            Debug.Log("密碼無效");
        }
    }
    
    void StartGame()
    {
        // 您的遊戲邏輯
    }
}
```

### 2. 開發者生成授權密碼

使用 Python 腳本為用戶生成授權密碼：

```bash
# 方法1：命令列參數
python license_generator.py XXXX-XXXX-XXXX-XXXX

# 方法2：互動式輸入
python license_generator.py
# 然後輸入設備碼
```

輸出範例：
```
===========================================
    設備授權密碼生成器
    Device License Password Generator
===========================================

-------------------------------------------
設備碼 / Device Code: ABCD-1234-EFGH-5678
授權密碼 / License Password: FC69-4B3C-E460-CDFD
-------------------------------------------

請將此密碼發送給用戶。
Please send this password to the user.
```

## API 參考 / API Reference

### DeviceLicenseManager

| 屬性/方法 | 說明 |
|-----------|------|
| `Instance` | 單例實例 |
| `IsLicensed` | 當前是否已授權 |
| `DeviceCode` | 設備碼（用戶需發送給開發者） |
| `ValidateLicense(string password)` | 驗證授權密碼，返回是否成功 |
| `ClearLicense()` | 清除當前授權 |
| `OnLicenseStatusChanged` | 授權狀態變更事件 |

## 安全說明 / Security Notes

- ⚠️ 此系統適用於基本的軟體保護，不適合高安全性需求的場景
- 🔒 建議對代碼進行混淆處理以增加破解難度
- 📝 授權密鑰保存在本地，用戶清除應用數據後需重新授權

## 系統需求 / Requirements

- **Unity 客戶端**: Unity 2019.4 或更高版本
- **授權生成器**: Python 3.6 或更高版本

## 授權 / License

MIT License