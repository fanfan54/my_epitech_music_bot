#!/usr/bin/env python3
##
# EPITECH PROJECT, 2019
# my_epitech_music_bot
# File description:
# Simple discord.py bot that uses the Commands extension. TODO use cogs!
##

import discord
from discord.ext import commands

bot_token = ""
status_channel_id = 0

bot = commands.Bot(command_prefix="/",
                   description="I'm a bot made with discord.py. DM me to play music in the voice channel you're connected to! :-)")


async def set_now_playing(game_name):
    await bot.change_presence(activity=discord.Game(name=game_name))
    print("[INFO] Set the \"Now playing\" status to {0}".format(game_name))


async def say_hello_to_status_channel():
    status_channel = bot.get_channel(status_channel_id)
    await status_channel.send(":robot: :white_check_mark: I'm online! Try `/help` to ask me what I can do.")


async def say_goodbye_to_status_channel():
    status_channel = bot.get_channel(status_channel_id)
    await status_channel.send(":robot: :x: I'm going offline and will no longer respond to commands. Bye!")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def quit(ctx):
    print(
        "[CRITICAL] {0.author} sent a command to shutdown the bot. Closing connection...".format(ctx))
    await ctx.send("I'm going to sleep :sleeping: see you soon! :blush:")
    await say_goodbye_to_status_channel()
    await bot.logout()


@bot.command()
async def whoami(ctx):
    user = ctx.message.author
    await ctx.send(
        "<@{0.id}> Here is what I know about you:\n"
        "Display name: {0.display_name}\n"
        "Username: {0.name}\n"
        "Discriminator: {0.discriminator}\n"
        "ID: {0.id}\n".format(user))


@bot.command()
async def join(ctx):
    print("Joining {0.author}'s channel...".format(ctx))


@bot.command()
async def leave(ctx):
    print("Leaving {0.author}'s channel...".format(ctx))


@bot.command()
async def play(ctx, args):
    print("Playing ??? on {0.author}'s channel...".format(ctx))


@bot.listen()
async def on_ready():
    print("[INFO] Bot ready and connected to Discord")
    await set_now_playing("/help")
    await say_hello_to_status_channel()


bot.run(bot_token)
