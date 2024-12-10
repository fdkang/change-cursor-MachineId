import uuid
import json
import os
import platform
import sys

def generate_random_id():
    return str(uuid.uuid4())

def get_config_path():
    # 统一处理配置文件路径
    if getattr(sys, 'frozen', False):
        # 如果是打包后的可执行文件
        application_path = os.path.dirname(sys.executable)
    else:
        # 如果是脚本运行
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    if platform.system() == 'Darwin':  # macOS
        return os.path.expanduser('~/Library/Application Support/Cursor/User/globalStorage/storage.json')
    else:  # Windows
        return os.path.join(os.getenv('APPDATA'), 'Cursor', 'User', 'globalStorage', 'storage.json')

def update_storage_json(new_uuid):
    config_path = get_config_path()
    
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        
        config["telemetry.macMachineId"] = new_uuid
        
        with open(config_path, 'w', encoding='utf-8') as file:
            json.dump(config, file, indent=4)
            
        print(f"成功更新 UUID 为: {new_uuid}")
        
    except FileNotFoundError:
        print(f"错误：找不到配置文件\n路径: {config_path}")
    except json.JSONDecodeError:
        print("错误：配置文件格式不正确")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    new_id = generate_random_id()
    update_storage_json(new_id)
    input("\n按回车键退出...")

