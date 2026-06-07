from src.core.crypto_core import CryptoCore

def test_crypto_core_interface():
    core = CryptoCore()
    assert hasattr(core, "derive_bip32")
    assert hasattr(core, "mnemonic_to_entropy")
