import os
import re
import anim
import discord
from discord.ext import commands
from collections import Counter
import graphviz


print("starting...")



class make_scene(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='make_scene', aliases=["ms"])
    async def make_scene(self, ctx, arg):
            await ctx.message.delete()
            scene_count = int(arg)

            if not isinstance(scene_count, int) or scene_count <= 0:
                return
            

            messages = await ctx.channel.history(limit = scene_count).flatten()

            for message in messages:
                if not message.content:
                    message.content = "Attachment"
                else:
                    pass

            messages.reverse()

            init = await ctx.send("Making the video..")

            # handle metadata
            print(f"handling metadata...")
            authors = [comment.author.name for comment in messages]
            most_common = [t[0] for t in Counter(authors).most_common()]


            # generate video
            output_filename = f"{ctx.message.id}.mp4"
            print(f"generating video {output_filename}...")
            characters = trial.get_characters(most_common)
            out = trial.comments_to_scene(
                messages, characters, output_filename=output_filename
            )

            # upload video
            print(f"uploading video...")
            final = bytes(out.node.kwargs["filename"], encoding='utf8')

            await init.delete()
            await ctx.send(file=discord.File(final, f'{output_filename}.mp4'))

            return


def setup(bot):
    bot.add_cog(make_scene(bot))
