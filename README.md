# Cursor MachineId 重置工具 🚀

> 🔥 一秒重置Cursor设备ID，告别封禁困扰！
> 
> ⚡️ 支持 Windows/macOS 双平台，一键解决设备限制问题（如：Too many free trials.）

## ✨ 为什么选择这个工具？

- 🛠 全自动操作，无需手动修改配置文件
- 🌈 支持 Windows 和 macOS 双平台
- ⚡️ 一键重置，3秒内搞定
- 🎯 精准定位配置文件，零出错
- 💾 智能备份，确保数据安全
- 🎨 保留原有配置，仅更新设备ID

## 功能特点

- 自动生成新的设备 ID
- 支持 Windows 和 macOS 双平台
- 一键重置，操作简单
- 自动定位配置文件位置
- 保留原有配置，仅修改设备 ID

## 使用方法

### 方法一：直接运行可执行文件

1. 从 [Releases](https://github.com/fdkang/change-cursor-MachineId/releases) 下载对应系统的可执行文件
2. 双击运行程序
3. 程序将自动生成新的设备 ID 并更新配置
4. 按回车键退出程序

### 方法二：运行源代码

1. 确保已安装 Python 3.6 或更高版本
2. 下载 `change_Cursor_MachineId.py` 文件
3. 打开终端或命令提示符，进入文件所在目录
4. 运行以下命令： 

  ```bash
  python change_Cursor_MachineId.py
  ```

  

## 配置文件位置

- Windows: `%APPDATA%\Cursor\User\globalStorage\storage.json`
- macOS: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`

## 注意事项

- 使用前请确保已关闭 Cursor 编辑器
- 建议在重置设备 ID 前备份配置文件
- 如遇到权限问题，请以管理员身份运行程序

## 常见问题

1. **找不到配置文件**
   - 确认是否已安装 Cursor 编辑器
   - 检查配置文件路径是否正确
   - 确认是否有足够的文件访问权限

2. **程序无法运行**
   - 确认是否下载了正确的系统版本
   - 检查是否有足够的运行权限
   - macOS 用户可能需要在终端执行 `chmod +x` 命令授予执行权限

## 免责声明

本工具仅供学习和研究使用。使用本工具可能违反 Cursor 编辑器的服务条款，请用户自行承担使用风险。作者不对使用本工具导致的任何问题负责。

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进这个工具。

## 许可证

MIT License
