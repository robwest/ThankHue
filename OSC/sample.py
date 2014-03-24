import argparse
import random
import time
import __builtin__

from pythonosc import osc_message_builder
from pythonosc import udp_client

host = "localhost"
incomingPort = 2331
outgoingPort = 9031

client = udp_client.UDPClient(host, incomingPort)

msg = osc_message_builder.OscMessageBuilder(address = "/hue/cmd")
msg.add_arg("all off")
msg = msg.build()

client.send(msg)

msg = osc_message_builder.OscMessageBuilder(address = "/hue/cmd")
msg.add_arg("all on")
msg = msg.build()

client.send(msg)
