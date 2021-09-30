import discord.ext.commands as commands 
import discodo, asyncio, re 

from classes.FormatDuration import formatDuration

class Play(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio
        self.youtube_matcher_url = re.compile(r'https?://(?:www\.)?.+')

    @commands.command()
    async def join(self, ctx):

        try:
            VC = await self.audio.connect(ctx.author.voice.channel)
        except discodo.NodeNotConnected:
            return await ctx.send("There is no available node.")
        except asyncio.TimeoutError:
            return await ctx.send("The connection is not established in 10 seconds.")

        await VC.setContext({"text_channel": ctx.channel.id})

    @commands.command(aliases=['p'])
    async def play(self, ctx, *, query: str):

        if not ctx.author.voice:
            return await ctx.reply("🎵  음성 채널에 들어간 상태에서 명령어를 입력해주세요.", mention_author=False)

        if not ctx.voice_client:
            await ctx.invoke(self.join)

        if self.youtube_matcher_url.match(query):

            source = await ctx.voice_client.loadSource(query)
            current = await ctx.voice_client.getCurrent()

            if isinstance(source, list):
                source = source[0]

            if not current:
                return await ctx.reply("🎶  **{0}**(을)를 재생합니다..".format(source.title), mention_author=False)
            else:
                return await ctx.reply("🎶  **{0}**(이)가 재생 목록에 추가되었습니다".format(source.title), mention_author=False)

        sources = await ctx.voice_client.searchSources(query)
        if not sources:
            return await ctx.reply("🔎  **{0}**와 관련된 노래를 찾을 수 없습니다..", mention_author=False)

        search_titles = ""
        check_numbers = []

        for number in range(0, int(len(sources))):

            if int(number + 1) <= 5:
                check_numbers.append(str(number + 1))
                search_titles += "**#{0}**. {1} ({2})\n".format(number + 1, sources[number].title, formatDuration(sources[number].duration))

        message = await ctx.send("`📀 아래의 트랙 중 하나를 선택해 재생할 수 있습니다.`\n{0}".format(search_titles))
        
        def check(message) -> True:
            return message.author.id == message.author.id and message.channel == ctx.channel and message.content in check_numbers

        try:

            user = await self.client.wait_for('message', check=check, timeout=30)
            if user.channel == ctx.channel and user.content in check_numbers:

                await user.delete()
                await sources[int(user.content) - 1].put()

                current = await ctx.voice_client.getCurrent()
                if not current:
                    return await message.edit(content="🎶  **{0}**(을)를 재생합니다..".format(sources[int(user.content) - 1].title), mention_author=False)
                else:
                    return await message.edit(content="🎶  **{0}**(이)가 재생 목록에 추가되었습니다".format(sources[int(user.content) - 1].title), mention_author=False)

        except asyncio.TimeoutError:
            return await message.edit(content="⏱  시간이 초과되어 자동으로 트랙 선택이 취소되었습니다.", mention_author=False)

def setup(client):
    client.add_cog(Play(client))