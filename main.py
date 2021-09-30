import discodo, os, sys, json
import discord.ext.commands as commands 
import discord

absolute = str(os.path.dirname(os.path.abspath(__file__)))
config = json.load(open('config.json', 'r', encoding='utf-8'))

class Client(commands.Bot):

    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)

        self.Audio = discodo.DPYClient(self)
        self.Audio.registerNode(region="LOCAL", launchOptions={'DEFAULT_AUTOPLAY': False})
        self.ARemoveCommands = [ 'help' ]

    async def on_ready(self) -> True:

        for musicer in filter(lambda x: not x.startswith('_'), os.listdir(str(absolute) + '/commands/')):
            self.load_extension('commands.%s' % (musicer[:-3]))

        if not int(len(self.ARemoveCommands)) <= 0:

            for command in self.ARemoveCommands:
                self.remove_command(command)

        await self.change_presence(activity=discord.Streaming(url="https://twitch.tv/dj.pepe", name="Service Provided. dj-pepe"))

    async def on_command_error(self, ctx, exception):
        
        if exception:
            return await ctx.reply("🚫  의도되지 않은 에러가 발생했습니다. (관리자를 호출해주세요)", mention_author=False)

if __name__ == "__main__" and int(sys.version_info.major) >= 3:
    Client(config.get('command-prefix')).run(config.get('token'))
