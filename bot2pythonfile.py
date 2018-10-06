from discord.ext.commands import Bot

import random

import re



BOT_PREFIX = (">")
TOKEN = "NDk2MTA0NzM1NzI0Nzk3OTUy.DpLxww.wY7_uByctGNJ3hziF7j1rmNvMhE"



client = Bot(command_prefix=BOT_PREFIX)







@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.__contains__('egg'):
        await client.send_message(message.channel, 'egg indeed')
    await client.process_commands(message)



@client.command(name='8ball',
    description = "Shakes the eight ball.",
    brief = "Shakes the eight ball.",
    pass_context = True)
async def eightball(context):
    possible_responses = [
        'That is a no',
        'It is not looking likely',
        'Too hard to tell',
        'Maybe',
        'Yes',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention + ".")

pass_context = False



@client.command()
async def ping():
    print("Pong!")




    await client.say("Pong!")









@client.command()
async def echo(*args):

    countcheck = 0

    f = open("botfile4.txt", "r")

    with open('botfile4.txt') as f:
        first = f.read(1)
        if not first:
            print('botfile4.txt is empty; starting at 0')
            f = open("botfile4.txt", "w")
            f.write(str(0))

    f = open("botfile4.txt", "r")

    countcheckinteger = f.read()

    ###

    countcheck = int(countcheckinteger)

    count = True

    while count:
        countcheck = countcheck + 1
        print("Command run ",countcheck," times.")

        f = open("botfile4.txt", "w")
        f.write(countcheck.__str__())

        text = "\nThis command has been run " + str(countcheck) + " times.\nGoal: 1,000 runs!"



        f.close()

        count = False



#outputting response \/ \/ \/

    output = ''
    for word in args:
        output += word
        output += ' '

    newline = "\n"


    await client.say(output + "\n")
    await client.say(text)



client.run(TOKEN)

