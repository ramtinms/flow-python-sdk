from datetime import datetime

class Block(object):
    def __init__(self, 
                 block_id, 
                 parent_block_id, 
                 height, 
                 timestamp, 
                 collection_guarantees,
                 block_seals,
                 signatures):
        self.block_id = block_id
        self.parent_block_id = parent_block_id
        self.height = height
        self.timestamp = timestamp
        self.collection_guarantees = collection_guarantees
        self.block_seals = block_seals
        self.signatures = signatures

    def block_id_hex(self): 
        return self.block_id.hex()

    def parent_block_id_hex(self): 
        return self.parent_block_id.hex()

    def __str__(self):
        # TODO iterate over block seals and collections
        return f"""
        Block 
            id: {self.block_id_hex()}
            height: {self.height}
            parent_block_id: {self.parent_block_id_hex()}
            timestamp: {self.timestamp.isoformat()}
        """

    @classmethod
    def from_block_response(cls, block_response):
        block_id = block_response.id
        parent_block_id = block_response.parent_id
        height = block_response.height
        # TODO take care of nanos 
        ts = block_response.timestamp or {}
        seconds = ts.seconds
        if seconds:
            block_timestamp = datetime.fromtimestamp(seconds)

        # TODO populate other fields
        new_instance = cls(block_id, parent_block_id, height, block_timestamp)
        return new_instance
