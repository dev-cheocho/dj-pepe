import discord.ext.commands as commands 

from classes.FormatDuration import formatDuration

class Seek(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    def formatDuration(self, seconds):
        
        seconds = int(seconds)
        minute, second = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)

        return (f"{hour:02}:" if hour else "") + f"{minute:02}:{second:02}"

    @commands.command()
    async def seek(self, ctx, offset: int):

        if not ctx.author.voice:
            return await ctx.reply("🎵  음성 채널에 들어간 상태에서 명령어를 입력해주세요.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("🎵  음성 채널에 봇이 들어왔는지 확인해주세요.", mention_author=False)

        current = await ctx.voice_client.getCurrent()
        if not current:
            return await ctx.reply("🎵  노래가 재생되고 있지 않습니다. (노래가 재생되는지 확인해주세요)", mention_author=False)

        if not 0 < offset < current.duration:
            return await ctx.reply(f"🎵  최소 **0**부터 최대 **{formatDuration(current.duration)}**까지 입력할 수 있습니다.", mention_author=False)

        await ctx.voice_client.seek(offset)
        await ctx.reply(f"🎶  재생 중인 시간을 **{formatDuration(offset)}**로 건너뛰었습니다.", mention_author=False)

def setup(client):
    client.add_cog(Seek(client))