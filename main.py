# vosper: a simple tool to easily get high-quality Automatic Speech Recognition using SOTA models
import vosper, os; vosper = vosper.new()

from pythonosc import osc_message_builder
from pythonosc import udp_client

oscSender = udp_client.UDPClient("127.0.0.1", 8000)

m = osc_message_builder.OscMessageBuilder(address = "/whisper")

while 'listening':
    text = vosper.listen()
    if ('-' in text):
        print(text)
        m.add_arg(text)
        oscSender.send(m.build())
        m = osc_message_builder.OscMessageBuilder(address = "/whisper")
    elif (text != ''):
        os.system('cls')
        print('- '+ text)
        m.add_arg(text)
        oscSender.send(m.build())
        m = osc_message_builder.OscMessageBuilder(address = "/whisper")
