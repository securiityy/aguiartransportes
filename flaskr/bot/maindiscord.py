senhaaa = input('DIGITE O TOKEN: ')


#import subprocess
#import signal
#import time
#import threading
#def execute():
#    # Execute o arquivo Python
#    process = subprocess.Popen(["python", "mainflask.py"])
#    # Aguarde um pouco, ou faça qualquer outra coisa
#    time.sleep(15)
#    # Mate o processo
#    os.kill(process.pid, signal.SIGTERM)
#    print('processo finalizado!!!')
#@client.event
#async def on_ready():
#    print(f'We have logged in as {client.user}')
#
#@client.event
#async def on_message(message):
#
#    if message.content.startswith('aa'):
#        #threading.Thread(target=execute).start()
#        await message.channel.send(Questionnaire())
#@bot.command()
#async def b(ctx):
#    embed = discord.Embed()
#    embed.add_field(name="LINK DA SESSAO", value="https//:oioi", inline=False)
#    embed.add_field(name="ID", value="83291038640510983756129", inline=False)
#    await ctx.send(embed=embed)
import discord
from discord import app_commands
import traceback
import json
import os
from datetime import datetime
from re import match

#TEST_GUILD = discord.Object(1247537783971778600)
TEST_GUILD = discord.Object(1259888680085098537)



class MessageTypes():
    def sucess(self):
        hora_inicial = datetime.strptime(str(self.horainicio), "%H:%M")
        hora_final = datetime.strptime(str(self.horafinal), "%H:%M")
        diferenca = hora_final - hora_inicial
        total_horas = diferenca.seconds // 3600
        total_minutos = (diferenca.seconds % 3600) // 60

        myembed = discord.Embed(title='SUCESS :white_check_mark:', colour=discord.Colour.green())
        myembed.add_field(name='KM INICIAL', value=f'{self.kminicial.value}')
        myembed.add_field(name='KM FINAL', value=f'{self.kmfinal.value}')
        myembed.add_field(name='KM RODADO', value=f'{int(self.kmfinal.value) - int(self.kminicial.value)}')
        myembed.add_field(name='HORA INICIAL', value=f'{self.horainicio}')
        myembed.add_field(name='HORA FINAL', value=f'{self.horafinal}')
        myembed.add_field(name='HORA GASTA', value=f'{total_horas}:{total_minutos}')
        myembed.add_field(name='ID', value=f'{self.kmfinal.value}')
        return myembed

    def failed(self):
        myembed = discord.Embed(title='Mensagem de Erro', colour=discord.Colour.red())
        myembed.add_field(name='HORA FINAL', value=f'''
        Por favor, verifique sua entrada:


        Quilômetros: Deve ser um número inteiro. Certifique-se de inserir apenas dígitos numéricos para a distância percorrida.


        Hora: Deve estar no formato HH
        , onde HH é a hora (00 a 23) e MM são os minutos (00 a 59). Exemplos válidos são 08:45, 15:30, etc.


        Certifique-se de seguir essas diretrizes para garantir que sua entrada seja processada corretamente.
        ''')
        return myembed


class MyClient(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def setup_hook(self) -> None:
        # Sync the application command with Discord.
        await self.tree.sync(guild=TEST_GUILD)


class Feedback(discord.ui.Modal, title='Feedback'):
    kminicial = discord.ui.TextInput(
        label='KM INICIAL:',
        placeholder='KM INICIAL',
        required=True,
    )
    kmfinal = discord.ui.TextInput(
        label='KM FINAL:',
        placeholder='KM FINAL',
        required=True,
    )
    horainicio = discord.ui.TextInput(
        label='HORA INICIAL: Exenplo 13:15',
        placeholder='Digite a hora inicial..',
        # time
        default='00:00',
        required=True,
    )
    horafinal = discord.ui.TextInput(
        label='HORA FINAL: Exenplo 04:50',
        placeholder='Digite a hora final..',
        # time
        default='00:00',
        required=True,
    )
    idsection = discord.ui.TextInput(
        label='ID:',
        placeholder='Id section',
        required=True,
    )

    async def on_submit(self, interaction: discord.Interaction):
        existfile = self.idsection.value in os.listdir('./aguiartransportes/flaskr/proc/')

        def isnumber(s):
            for char in s:
                if not char.isdigit():
                    return False
            return True

        def stringisvalid(s):
            return bool(match(r'^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]|60)$', s))

        if (existfile
            and isnumber(self.kminicial.value) == True
            and isnumber(self.kmfinal.value) == True
            and stringisvalid(self.horainicio.value) == True
            and stringisvalid(self.horafinal.value) == True
            and isnumber(self.idsection.value) == True
            and len(self.idsection.value) == 15):

            hora_inicial = datetime.strptime(str(self.horainicio), "%H:%M")
            hora_final = datetime.strptime(str(self.horafinal), "%H:%M")
            diferenca = hora_final - hora_inicial
            total_horas = diferenca.seconds // 3600
            total_minutos = (diferenca.seconds % 3600) // 60

            with open(f'./aguiartransportes/flaskr/proc/{self.idsection.value}','r') as file:
                casa = json.load(file)
                casa['kminicial'] = self.kminicial.value
                casa['kmfinal'] = self.kmfinal.value
                casa['kmrodado'] = int(self.kmfinal.value) - int(self.kminicial.value)
                casa['horainicio'] = self.horainicio.value
                casa['horafinal'] = self.horafinal.value
                casa['horatotal'] = f'{total_horas}:{total_minutos}' 
                casa['statusmotorista'] = 'on' 

            with open(f'./aguiartransportes/flaskr/proc/{self.idsection.value}','w') as file:
                file.write('')
                json.dump(casa,file,indent=4)

            await interaction.response.send_message(
                embed=MessageTypes.sucess(self)
            ) 
        else:
            await interaction.response.send_message(
                embed=MessageTypes.failed(self),
                ephemeral=True
            ) 


    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Você digitou alguma coisa errada!!!.', ephemeral=True)
        traceback.print_exception(type(error), error, error.__traceback__)


client = MyClient()


@client.tree.command(guild=TEST_GUILD, description="Submit feedback")
async def feedback(interaction: discord.Interaction):
    await interaction.response.send_modal(Feedback())

@client.tree.command(guild=TEST_GUILD, description="embedsection")
async def embedsection(interaction: discord.Interaction):
    embed = discord.Embed()
    embed.add_field(name='KM INICIAL', value='{self.kminicial.value}')
    embed.insert_field_at(1,name='KM INICIAL', value='{self.kminicial.value}')
    await interaction.response.send_message(embed=embed)


# Roda o bot com o token fornecido
client.run(senhaaa)





