# tg-clean-exceptions
Telegram 清除 Exceptions 中 权限与群组默认权限一样的记录

<img width="699" height="293" alt="image" src="https://github.com/user-attachments/assets/d19320b5-ef33-4816-a96b-45f9efbedafd" />

api_id, api_hash 需要自己申请  
https://my.telegram.org/apps  
具体步骤不写了, 自己去问 google 和 gpt  


## 搭环境
```
apt install -y python3-pip
pip3 install telethon --break-system-packages
```

## 运行
```
python3 tg-clean-exceptions.py
```

## 运行结果示例
```
群组: test
🧹 清理: 6611601789 (蛙 女)
✅ 保留: 6701294471 (新 希望)（权限不同）

完成检查，共检查 2 条 Exception，清理 1 条无效 Exception
```
