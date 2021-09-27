import discord
from discord.ext import commands

class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx : commands.Context, error : commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"Command masih dalam cooldown. Silahkan coba lagi setelah {round(error.retry_after, 1)} detik"
        elif isinstance(error, commands.MissingPermissions):
            message = "Kamu tidak mempunyai izin untuk menjalankan command ini!"
        elif isinstance(error, commands.UserInputError):
            message = "Input salah!"
        elif isinstance(error, commands.MissingAnyRole):
            message = f"Kamu tidak memiliki role Admin atau Moderator!"
        else:
            message = "Ada sesuatu yang salah perintah ini! Code Perintah: 000201001200120010201020102090939129031010210200120012010x"
        await ctx.send(message, delete_after=5)
        await ctx.message.delete(delay=5)


def setup(bot):
    bot.add_cog(ErrorHandling(bot))