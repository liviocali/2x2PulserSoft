import click
#from ppulse import client
from ppulseserver import server


@click.group()
def ppulseserver():
    pass

@ppulseserver.command()
def run_server():
    server.start_server()