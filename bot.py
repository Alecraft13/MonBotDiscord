import os
from dotenv import load_dotenv
import discord

load_dotenv()  # Charge le fichier .env
TOKEN = os.getenv('DISCORD_TOKEN')  # Récupère le token

client = discord.Client()

@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')  # Confirme la connexion

client.run(TOKEN)  # Lance le bot


import discord
from discord.ext import commands
import sqlite3

# ➜ Déclare les intents
intents = discord.Intents.default()
intents.message_content = True

# ➜ Crée ton bot avec les intents
bot = commands.Bot(command_prefix='!', intents=intents)

DB = 'config.db'

@bot.event
async def on_ready():
    print(f'✅ Connecté en tant que {bot.user}')

@bot.command()
async def annonce(ctx):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT announcement_message FROM config WHERE id = 1')
    message = c.fetchone()[0]
    conn.close()

    await ctx.send(message)

bot.run('TOKEN')

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Important pour gérer les membres

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Connecté en tant que {bot.user}')

# ➜ Commande !mute
@bot.command()
@commands.has_permissions(manage_roles=True)  # Seulement pour les modérateurs/admins
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

bot.run('TOKEN')

