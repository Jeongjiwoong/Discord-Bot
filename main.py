import os
import discord
import re
from discord.ext import commands
from keep_alive import keep_alive

keep_alive()

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

def remove_prefix(nick):
    """닉네임에서 〘...〙 또는 『...』 패턴 제거"""
    return re.sub(r"^(〘.*?〙|『.*?』)\s*", "", nick or "").strip()

# 역할 ID와 prefix를 리스트로 관리
role_prefixes = [
    (1363895628349968545, "『 예술홍보장 』"),
    (1363895628349968545, "『 관객도움장 』"),
    (1363895516869558372, "『 기획운영장 』"),
    (1363456145909350473, "『 로비안내장 』"),
    (1363456099096854609, "『 시설보안장 』"),
    (1363455653586141224, "『 예술홍보 』"),
    (1363455704467505273, "『 로비안내 』"),
    (1363895655713734727, "『 관객도움 』"),
    (1363895578999652512, "『 기획운영 』"),
    (1363455582484561991, "『 시설보안 』"),
    (1368978559720226826, "〘🔱〙"),
    (1365686790996099145, "〘👑〙"),
    (1368933162767355964, "〘𝐃𝐫𝐚𝐜𝐮𝐥𝐚〙"),
    (1368933325632307271, "〘𝐌𝐢𝐧𝐚〙"),
    (1363456345621135552, "〘 관객 〙"),
    (1363493664239652874, "〘 첫관객 〙"),
]

@bot.event
async def on_ready():
    print(f'✅ {bot.user.name} 봇이 온라인입니다!')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

@bot.event
async def on_member_update(before, after):
    # 멤버가 가진 역할 중 prefix가 지정된 역할만 추출
    member_roles = [role for role in after.roles if role.id in dict(role_prefixes)]
    if not member_roles:
        # 해당 역할이 없으면 prefix 제거
        base_nick = remove_prefix(after.display_name)
        if after.display_name != base_nick:
            try:
                await after.edit(nick=base_nick)
                print(f"[닉네임 복원] {after.name} → {base_nick}")
            except discord.Forbidden:
                print(f"⚠️ {after.name} 닉네임 복원 권한 없음")
        return

    # 가장 높은 position의 역할 찾기
    highest_role = max(member_roles, key=lambda r: r.position)
    prefix = dict(role_prefixes)[highest_role.id]
    base_nick = remove_prefix(after.display_name)
    new_nick = f"{prefix} {base_nick}"

    if after.display_name != new_nick:
        try:
            await after.edit(nick=new_nick)
            print(f"[닉네임 변경] {after.name} → {new_nick}")
        except discord.Forbidden:
            print(f"⚠️ {after.name} 닉네임 변경 권한 없음")

token = os.getenv('DISCORD_BOT_TOKEN')
if not token:
    raise ValueError("❌ 토큰 오류")

bot.run(token)
