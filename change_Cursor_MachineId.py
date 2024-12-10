import uuid, json, os, platform

def update_machine_id():
    try:
        path = os.path.join(
            os.path.expanduser('~/Library/Application Support/Cursor') if platform.system() == 'Darwin' 
            else os.path.join(os.getenv('APPDATA'), 'Cursor'),
            'User/globalStorage/storage.json'
        )
        
        with open(path, 'r+', encoding='utf-8') as f:
            config = json.load(f)
            config["telemetry.macMachineId"] = str(uuid.uuid4())
            f.seek(0)
            json.dump(config, f, indent=4)
            f.truncate()
            print(f"成功更新 UUID 为: {config['telemetry.macMachineId']}")
    except Exception as e:
        print(f"错误: {e}\n配置文件路径: {path}")

if __name__ == "__main__":
    update_machine_id()
    input("\n按回车键退出...")

