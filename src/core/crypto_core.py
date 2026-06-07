class CryptoCore:
    """
    Deterministic cryptographic engine for SeedTools Suite.
    Provides BIP32/39/44/84/86 derivation and Taproot logic.
    """

    def __init__(self):
        from .bip32 import BIP32
        from .bip39 import BIP39
        from .bip44 import BIP44
        from .taproot import TaprootEngine

        self.bip32 = BIP32()
        self.bip39 = BIP39()
        self.bip44 = BIP44()
        self.taproot = TaprootEngine()

    # --- BIP39 ---
    def mnemonic_to_entropy(self, mnemonic: str) -> bytes:
        return self.bip39.mnemonic_to_entropy(mnemonic)

    def entropy_to_mnemonic(self, entropy: bytes) -> str:
        return self.bip39.entropy_to_mnemonic(entropy)

    # --- BIP32 ---
    def derive_bip32(self, seed: bytes, path: str) -> dict:
        return self.bip32.derive(seed, path)

    # --- BIP44/49/84/86 ---
    def derive_account(self, seed: bytes, purpose: int, coin: int, account: int):
        return self.bip44.derive_account(seed, purpose, coin, account)

    # --- Taproot ---
    def taproot_keypath(self, seed: bytes, path: str) -> dict:
        return self.taproot.derive_keypath(seed, path)
