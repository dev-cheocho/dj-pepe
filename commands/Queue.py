import discord.ext.commands as commands 
import math

from classes.FormatDuration import formatDuration

class Queue(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command(aliases=['q'])
    async def queue(self, ctx, page: int = 1):

        if not ctx.author.voice:
            return await ctx.reply("🎵  음성 채널에 들어간 상태에서 명령어를 입력해주세요.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("🎵  음성 채널에 봇이 들어왔는지 확인해주세요.", mention_author=False)

        queues = ctx.voice_client.Queue
        maxpages = math.ceil(len(queues) / 10)

        if int(len(queues)) <= 0:
            return await ctx.reply("🎵  대기 중인 재생 목록이 비어있습니다.", mention_author=False)

        if int(page) > int(maxpages) or int(page) <= 0:
            return await ctx.reply("🎵  **0**페이지보다 작거나 또는 **{}**페이지보다 큰지 확인해주세요.".format(maxpages), mention_author=False)

        execute = (page - 1) * 10
        maxexecute = execute + 9

        queue_titles = ""
        for number in range(execute, maxexecute + 1):
            if int(number) < int(len(queues)):
                queue_titles += "**#{0}** {1} (`{2}`)\n".format(number + 1, queues[number].title, formatDuration(queues[number].duration))
                
        return await ctx.reply("`💿 다음 노래에서 재생될 목록을 불러왔습니다. ({0}페이지 중 {1}페이지를 로드함)`\n{2}".format(maxpages, page, queue_titles), mention_author=False)

def setup(client):
    client.add_cog(Queue(client))