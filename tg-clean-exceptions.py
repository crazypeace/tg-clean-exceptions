import time
from telethon import TelegramClient
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsBanned, ChatBannedRights


# 到这里申请 https://my.telegram.org/apps
api_id = 12345678
api_hash = 'f9847f9847f9847f9847f9847f984747'

# 群组的 username 或 ID
group = -100xxxxxxxxxx #私有群是负整数
#group = 'groupusername' #公开群的username字符串

# 登录的用户的手机号
phone_number = '+8613812345678'

client = TelegramClient('session_' + phone_number, api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    # 获取群实体
    entity = await client.get_entity(group)
    
    # 获取群成员的默认权限
    default_rights = entity.default_banned_rights

    print(f"群组: {entity.title}")
#    print(f"default_banned_rights: {default_rights}")

    removed_count = 0
    checked_count = 0

    # 遍历Exceptions列表
    async for p in client.iter_participants(entity, filter=ChannelParticipantsBanned, limit=None):
        time.sleep(0.5)  # 避免向telegram服务器发送命令过快

        checked_count += 1

        # 检查用户是否已销号
        if p.deleted:
            print(f"🗑️ 检测到 Deleted Account: {p.id}，正在清理...")
            try:
                await client(EditBannedRequest(entity, p.id, ChatBannedRights(until_date=None)))  # 清除例外项
            except Exception as e:
                print(f"⚠️ 清理 {uid} 时出错: {e}")
                continue
            removed_count += 1
            continue

        # 获取 Exceptions 中设置了什么权限
        rights = getattr(p.participant, 'banned_rights', None)
        if not isinstance(rights, ChatBannedRights):
            continue
#        print(f"rights: {rights}")
        
        # 比较与默认权限是否一致
        if rights == default_rights:
            print(f"🧹 清理: {p.id} ({p.first_name or ''} {p.last_name or ''})")
            try:
              await client(EditBannedRequest(entity, p.id, ChatBannedRights(until_date=None)))  # 清除例外项
            except Exception as e:
              print(f"清理: {p.id} 时遇到错误 {e}")
              continue
            removed_count += 1
        else:
            print(f"✅ 保留: {p.id} ({p.first_name or ''} {p.last_name or ''})（权限不同）")

    print(f"\n完成检查，共检查 {checked_count} 条 Exception，清理 {removed_count} 条 Exception")

with client:
    client.loop.run_until_complete(main())
