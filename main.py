import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

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
    if target_role_id in [role.id for role in after.roles] and \
       target_role_id not in [role.id for role in before.roles]:
        new_nick = f"〘🔱〙{after.display_name}"
        try:
            await after.edit(nick=new_nick)
            print(f"{after.display_name} 닉네임을 {new_nick}으로 변경함")
        except discord.Forbidden:
            print("권한이 부족합니다!")
        except Exception as e:
            print(f"오류 발생: {e}")
    target_role_id1 = 1363493664239652874  # 여기에 실제 역할 ID 입력
    # 역할이 새로 추가된 경우만 닉네임 변경
    if target_role_id1 in [role.id for role in after.roles] and \
       target_role_id1 not in [role.id for role in before.roles]:
        new_nick = f"〘 첫관객 〙{after.display_name}"
        try:
            await after.edit(nick=new_nick)
            print(f"{after.display_name} 닉네임을 {new_nick}으로 변경함")
        except discord.Forbidden:
            print("권한이 부족합니다!")
        except Exception as e:
            print(f"오류 발생: {e}")
    target_role_id2 = 1363456345621135552  # 여기에 실제 역할 ID 입력
    # 역할이 새로 추가된 경우만 닉네임 변경
    if target_role_id2 in [role.id for role in after.roles] and \
       target_role_id2 not in [role.id for role in before.roles]:
        new_nick = f"〘 관객 〙{after.display_name}"
        try:
            await after.edit(nick=new_nick)
            print(f"{after.display_name} 닉네임을 {new_nick}으로 변경함")
        except discord.Forbidden:
            print("권한이 부족합니다!")
        except Exception as e:
            print(f"오류 발생: {e}")
    target_role_id3 = 1365686790996099145
    # 역할이 새로 추가된 경우만 닉네임 변경
    if target_role_id3 in [role.id for role in after.roles] and \
       target_role_id3 not in [role.id for role in before.roles]:
        new_nick = f"〘 👑 〙{after.display_name}"
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
