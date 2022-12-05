import pytest
from brownie import (
    accounts,
    MarginPool
)
from config import (
    badger,
    usdc,
    name,
    symbol,
    decimals
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