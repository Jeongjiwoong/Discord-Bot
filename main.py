import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
import re

keep_alive()

# (로컬에서 실행할 경우 .env 파일 지원)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # Replit에서는 dotenv가 필요 없음

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user.name} 봇이 온라인입니다!')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

@bot.event
async def on_member_update(before, after):
    target_role_id = 1368978559720226826  # 여기에 실제 역할 ID 입력
    # 역할이 새로 추가된 경우만 닉네임 변경
    def remove_prefix(nick):
        # 닉네임 앞의 〘...〙 패턴을 제거
        return re.sub(r"^〘.*?〙\s*", "", nick or "")

        @bot.event
        async def on_member_update(before, after):
            role_prefixes = {
                1368978559720226826: "〘 🔱 〙",
                1363493664239652874: "〘 첫관객 〙",
                1363456345621135552: "〘 관객 〙",
                1365686790996099145: "〘 👑 〙"
            }

            for role_id, prefix in role_prefixes.items():
                if role_id in [role.id for role in after.roles] and role_id not in [role.id for role in before.roles]:
                    # 기존 접두사 제거
                    base_nick = remove_prefix(after.display_name)
                    new_nick = f"{prefix}{base_nick}"
                    try:
                        await after.edit(nick=new_nick)
                        print(f"{after.display_name} 닉네임을 {new_nick}으로 변경함")
                    except discord.Forbidden:
                         print("권한이 부족합니다!")
                    except Exception as e:
                         print(f"오류 발생: {e}")

# 환경변수에서 토큰 불러오기
token = os.getenv('DISCORD_BOT_TOKEN')
if not token:
    raise ValueError("❌ DISCORD_BOT_TOKEN 환경 변수가 설정되지 않았습니다.")

bot.run(token)
