import discord.ext.commands as commands 

class Shuffle(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command(aliases=['sh', 'shuff'])
    async def shuffle(self, ctx):

        if not ctx.author.voice:
            return await ctx.reply("🎵  음성 채널에 들어간 상태에서 명령어를 입력해주세요.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("🎵  음성 채널에 봇이 들어왔는지 확인해주세요.", mention_author=False)

        queues = ctx.voice_client.Queue
        if int(len(queues)) <= 0:
            return await ctx.reply("🎵  뒤섞을 재생 목록이 비어있습니다. (추가한 후 다시 입력해주세요)", mention_author=False)

        await ctx.voice_client.shuffle()
        return await ctx.reply("🎶  대기 중인 모든 재생 목록을 랜덤으로 뒤섞었습니다.", mention_author=False)

def setup(client):
    client.add_cog(Shuffle(client))