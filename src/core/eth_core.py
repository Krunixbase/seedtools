import hashlib

class ETHCore:
    """
    Deterministic Ethereum address derivation engine.
    """

    def private_key_to_public_key(self, private_key: bytes) -> bytes:
        # secp256k1 uncompressed public key
        raise NotImplementedError

    def public_key_to_address(self, public_key: bytes) -> str:
        # keccak256(public_key[1:]) -> last 20 bytes
        raise NotImplementedError

    def checksum_address(self, address: str) -> str:
        # EIP-55 checksum
        raise NotImplementedError

    def derive_eth_address(self, seed: bytes, path: str) -> dict:
        """
        Full ETH derivation pipeline:
        - BIP32 derive private key
        - secp256k1 public key
        - keccak256 hash
        - EIP-55 checksum
        """
        raise NotImplementedError
