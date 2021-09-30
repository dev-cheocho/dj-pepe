import discord.ext.commands as commands 

class Stop(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command()
    async def stop(self, ctx):

        if not ctx.voice_client:
            return await ctx.reply("🎵  음성 채널에 들어간 상태에서 명령어를 입력해주세요.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("🎵  음성 채널에 봇이 들어왔는지 확인해주세요.", mention_author=False)

        await ctx.voice_client.destroy()
        return await ctx.reply("🎶  노래를 종료합니다.. (모든 재생 목록을 초기화했습니다)", mention_author=False)

def setup(client):
    client.add_cog(Stop(client))