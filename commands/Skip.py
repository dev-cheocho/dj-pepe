import discord.ext.commands as commands 

class Skip(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command(aliases=['s'])
    async def skip(self, ctx):

        if not ctx.author.voice:
            return await ctx.reply("🎵  음성 채널에 들어간 상태에서 명령어를 입력해주세요.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("🎵  음성 채널에 봇이 들어왔는지 확인해주세요.", mention_author=False)

        current = await ctx.voice_client.getCurrent()
        if not current:
            return await ctx.reply("🎵  노래가 재생되고 있지 않습니다. (노래가 재생되는지 확인해주세요)", mention_author=False)

        await ctx.voice_client.skip()
        return await ctx.reply("🎶  노래를 강제로 종료했습니다.", mention_author=False)

def setup(client):
    client.add_cog(Skip(client))