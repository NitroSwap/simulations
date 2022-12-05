from brownie import (
    accounts,
    network,
    interface,
    MarginPool
)

import click
from rich.console import Console

console = Console()

def main():
    """
    FOR DEV
    Deploys an instance of the MarginPool.sol contract and wires up .
    Note that the deployer must be provided via brownie. This script
    is testing the MarginPool deployment and can be used in the conftest. 
    """


    # get deployer account from local keystore
    dev = connect_account()

    # get deployment parameters
    badger = '0x3472a5a71965499acd81997a54bba8d852c6e53d'
    usdc = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
    name = 'NitroSwap Margin Pool: Badger-USDC'
    symbol = 'BADGER-USDC-MP'
    decimals = 18

    # deploy
    margin_pool = deploy_margin_pool(badger, usdc, name, symbol, decimals, dev)

def deploy_margin_pool(badger, usdc, name, symbol, decimals, dev):
    margin_pool_instance = MarginPool.deploy(badger, usdc, name, symbol, decimals, {"from": dev})
    console.print("[green]Margin Pool was deployed at: [/green]", margin_pool_instance.address)
    return margin_pool_instance



def connect_account():
    click.echo(f"You are using the '{network.show_active()}' network")
    dev = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    click.echo(f"You are using: 'dev' [{dev.address}]")
    return dev