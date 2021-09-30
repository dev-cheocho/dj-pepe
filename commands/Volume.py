import discord.ext.commands as commands 

class Volume(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command(aliases=['vol', 'v'])
    async def volume(self, ctx, volume : int):

        if not ctx.author.voice:
            return await ctx.reply("🎵  음성 채널에 들어간 상태에서 명령어를 입력해주세요.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("🎵  음성 채널에 봇이 들어왔는지 확인해주세요.", mention_author=False)

        if not 0 < volume < 101:
            return await ctx.reply("🎵  최소 **1** 부터 최대 **100**까지만 불륨을 설정할 수 있습니다.", mention_author=False)

        await ctx.voice_client.setVolume(volume / 100)
        return await ctx.reply(f"🔊  불륨을 **{volume}%**로 설정했습니다.", mention_author=False)

def setup(client):
    client.add_cog(Volume(client))