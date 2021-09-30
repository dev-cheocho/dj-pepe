import discord.ext.commands as commands 
import discord

from classes.FormatDuration import formatDuration

class NowPlaying(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio
        
    @commands.command(aliases=["np"])
    async def nowplaying(self, ctx):

        if not ctx.author.voice:
            return await ctx.reply("🎵  음성 채널에 들어간 상태에서 명령어를 입력해주세요.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("🎵  음성 채널에 봇이 들어왔는지 확인해주세요.", mention_author=False)

        if not ctx.voice_client.current:
            return await ctx.reply("🎵  노래가 재생되고 있지 않습니다. (노래가 재생되는지 확인해주세요)", mention_author=False)
            
        return await ctx.reply("🎶  {0} (`{1}`)를 지금 재생하고 있습니다..".format(
            ctx.voice_client.current.title, formatDuration(ctx.voice_client.current.duration)), mention_author=False)

def setup(client):
    client.add_cog(NowPlaying(client))