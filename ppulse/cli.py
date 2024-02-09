import click
from ppulse import client


@click.group()
def ppulse():
    pass

@ppulse.command()
def server_status():
    client.cli_server_status()

@ppulse.command()
@click.option("--channel", "-ch", required=True, type=int, help="Number of channel (1-16)")
@click.option("--at_ser", "-s", required=True, type=float, help="Serial attenuator bit value (0-255)")
@click.option("--at_par", "-p", required=True, type=float, help="Parallel attenuator bit value (0-255)")
def set_channel(channel, at_ser, at_par):
    client.set_channel(channel, at_ser, at_par)

@ppulse.command()
@click.option("--filename", "-f", required=True, type=str, help="Config file (see template)")
def set_channels_file(filename):
    client.set_channels_file(filename)

@ppulse.command()
@click.option("--period", "-p", required=True, type=int, help="Trigger period in ms (3-1000)")
def set_trigger(period):
    client.set_trig(period)

@ppulse.command()
@click.option("--duration", "-d", required=True, type=int, help="Trigger duration in seconds (1-600)")
def run_trigger(duration):
    client.run_trig(duration)