import pytest
from eip681_python.eip681 import EIP681

test_address = "0x0000000000000000000000000000000000000000"

@pytest.fixture(scope="module")
def eip681_instance():
    return EIP681()

def test_make_url(eip681_instance: EIP681):
    url = eip681_instance.build_tx_url(test_address, amount=10)
    assert url == f'ethereum:{test_address}@1?value=10e18'

def test_make_url_payment(eip681_instance: EIP681):
    url = eip681_instance.build_tx_url(test_address, amount=10, payment=True)
    assert url == f'pay-{test_address}@1?value=10e18'