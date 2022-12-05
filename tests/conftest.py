import pytest
from brownie import (
    accounts,
    MarginPool
)
from rich.console import Console

console = Console()

@pytest.fixture(scope="module", autouse=True)
def deployer():
    return accounts[0]

@pytest.fixture(scope="module", autouse=True)
def alice():
    return accounts[1]

@pytest.fixture(scope="module", autouse=True)
def bob():
    return accounts[2]

@pytest.fixture(scope="module", autouse=True)
def bot():
    return accounts[3]

@pytest.fixture(scope="module", autouse=True)
def nitroswap(deployer):

    # get deployment parameters
    badger = '0x3472a5a71965499acd81997a54bba8d852c6e53d'
    usdc = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
    name = 'NitroSwap Margin Pool: Badger-USDC'
    symbol = 'BADGER-USDC-MP'
    decimals = 18

    # deploy
    margin_pool = deploy_margin_pool(badger, usdc, name, symbol, decimals, deployer)

    return (margin_pool)

def deploy_margin_pool(badger, usdc, name, symbol, decimals, dev):
    margin_pool_instance = MarginPool.deploy(badger, usdc, name, symbol, decimals, {"from": dev})
    console.print("[green]Margin Pool was deployed at: [/green]", margin_pool_instance.address)
    return margin_pool_instance

## Forces reset before each test
@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass