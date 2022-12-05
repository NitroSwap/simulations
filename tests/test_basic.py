import pytest
from config import (
    badger,
    usdc,
    name,
    symbol,
    decimals
)

def test_deploy_configuration(nitroswap):
    (margin_pool) = nitroswap

    # assert correct assets
    assert margin_pool.market() ==  badger
    assert margin_pool.base() == usdc
    assert margin_pool.name() == name
    assert margin_pool.symbol() == symbol
    assert margin_pool.decimals() == decimals





