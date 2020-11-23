class Collection(object):
    def __init__(self, collection_id, transaction_ids):
        self.collection_id = collection_id
        self.transaction_ids = transaction_ids

    def collection_id_hex(self): 
        return self.collection_id.hex()

    def __str__(self):
    	# TODO iterate over transaction IDs
        return f"""
        Collection
            id: {self.block_id_hex()}
        """

    @classmethod
    def from_collection_response(cls, collection_response):
        collection_id = collection_response.id
        transaction_ids = collection_response.transaction_ids
        return cls(collection_id, transaction_ids)


class CollectionGuarantee(object):
    def __init__(self, collection_id, signatures):
        self.collection_id = collection_id
        self.signatures = signatures

    def collection_id_hex(self): 
        return self.collection_id.hex()

    def __str__(self):
    	# TODO iterate over signatures
        return f"""
        Collection Guarantee
            id: {self.block_id_hex()}
        """
