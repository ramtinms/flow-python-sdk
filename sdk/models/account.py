from enum import Enum


class SigningAlgorithm(Enum):
    # Unknown Signing Algorithm 
    UnknownSigningAlgorithm = 0
    # BLS on BLS 12-381 curve
    BLSBLS12381 = 1
    # ECDSA on NIST P-256 curve
    ECDSAP256 = 2
    # ECDSA on secp256k1 curve
    ECDSASecp256k1 = 3


class HashingAlgorithm(Enum):
    # Unkown Hashing Algorithm
    UnknownHashingAlgorithm = 0
    # SHA2 hashing algorithm(256 bits)
    SHA2_256 = 1
    # SHA2 hashing algorithm(384 bits)
    SHA2_384 = 2
    # SHA3 hashing algorithm(256 bits)
    SHA3_256 = 3
    # SHA3 hashing algorithm(384 bits)
    SHA3_384 = 4
    # SHA3 ShakeHash hashing algorithm(128 bits)
    KMAC128 = 5


class AccountKey(object):
    def __init__(self, index, public_key, sign_algo, hash_algo, weight, sequence_number, revoked):
        self.index = index or 0
        self.public_key = public_key
        self.sign_algo = SigningAlgorithm(sign_algo)
        self.hash_algo = HashingAlgorithm(hash_algo)
        self.weight = weight
        self.sequence_number = sequence_number
        self.revoked = revoked


class Account(object):
    def __init__(self, address, code, keys):
        self.address = address
        self.code = code
        self.keys = keys

    def address_hex(self): 
        return self.block_id.hex()

    def parent_block_id_hex(self): 
        return self.parent_block_id.hex()

    @classmethod
    def from_account_response(cls, account_response):
        address = account_response.address
        code = account_response.code
        keys = []
        for key in account_response.keys:
            keys += [AccountKey(key.index, key.public_key, key.sign_algo, key.hash_algo, key.weight, key.sequence_number, key.revoked)]
        new_instance = cls(address, code, keys)
        return new_instance
