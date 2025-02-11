import click
import os
import subprocess
import shlex

@click.command()
def cli():
	click.echo("Sensor Lab!")

if __name__ == '__main__':
	cli()