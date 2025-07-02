from keep_alive import keep_alive

keep_alive()

import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
import sqlite3

# ➜ Charge les variables d'environnement
load_dotenv()
TOKEN = os.getenv('TOKEN')

# ➜ Déclare les intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Si tu gères les membres

# ➜ Crée ton bot avec les intents
bot = commands.Bot(command_prefix='!', intents=intents)

DB = 'config.db'  # Ta base SQLite

@bot.event
async def on_ready():
    print(f'✅ Connecté en tant que {bot.user}')

# ➜ Commande !annonce
@bot.command()
async def annonce(ctx):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT announcement_message FROM config WHERE id = 1')
    result = c.fetchone()
    if result:
        await ctx.send(result[0])
    else:
        await ctx.send("❌ Aucun message d'annonce trouvé.")
    conn.close()

# ➜ Commande !mute
@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        await ctx.send("❌ Le rôle 'Muted' n'existe pas. Crée-le d'abord.")
        return

    await member.add_roles(role, reason=reason)
    await ctx.send(f"🔇 {member.mention} a été mute. Raison : {reason}")

# ➜ Commande !unmute
@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        await ctx.send("❌ Le rôle 'Muted' n'existe pas.")
        return

    await member.remove_roles(role)
    await ctx.send(f"🔊 {member.mention} a été unmute.")

# ➜ Lance le bot
bot.run(TOKEN)
