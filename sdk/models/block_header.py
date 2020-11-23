from datetime import datetime

class BlockHeader(object):
    def __init__(self, block_id, parent_block_id, height, timestamp):
        self.height = height
        self.timestamp = timestamp
        self.block_id = block_id
        self.parent_block_id = parent_block_id

    def block_id_hex(self): 
        return self.block_id.hex()

    def parent_block_id_hex(self): 
        return self.parent_block_id.hex()

    def __str__(self):
        return f"""
        Block Header
            id: {self.block_id_hex()}
            height: {self.height}
            parent_block_id: {self.parent_block_id_hex()}
            timestamp: {self.timestamp.isoformat()}  
        """

    @classmethod
    def from_blockheader_response(cls, block_header_response):
        block_id = block_header_response.id
        parent_block_id = block_header_response.parent_id
        height = block_header_response.height
        # TODO take care of nanos 
        ts = block_header_response.timestamp or {}
        seconds = ts.seconds
        if seconds:
            block_timestamp = datetime.fromtimestamp(seconds)

        new_instance = cls(block_id, parent_block_id, height, block_timestamp)
        return new_instance
