import discord.ext.commands as commands 

class Pause(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command()
    async def pause(self, ctx):

        if not ctx.author.voice:
            return await ctx.reply("🎵  음성 채널에 들어간 상태에서 명령어를 입력해주세요.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("🎵  음성 채널에 봇이 들어왔는지 확인해주세요.", mention_author=False)

        client_source = await ctx.voice_client.fetchState()
        current = await ctx.voice_client.getCurrent()

        if not current:
            return await ctx.reply("🎵  노래가 재생되고 있지 않습니다. (노래가 재생되는지 확인해주세요)", mention_author=False)
        
        if int(client_source['state']) != 3:
            await ctx.voice_client.resume()
            return await ctx.reply("🎶  노래 일시 정지를 해제했습니다.", mention_author=False)
        else:
            await ctx.voice_client.pause()
            return await ctx.reply("🎶  노래를 일시 정지했습니다. (명령어를 한번 더 입력하면 해제됩니다)", mention_author=False)

def setup(client):
    client.add_cog(Pause(client))