from datetime import datetime

class Result(object):
    def __init__(self, block_id, block_height, block_timestamp, events):
        self.block_id = block_id
        self.block_height = block_height
        self.block_timestamp = block_timestamp
        self.events = events

    def block_id_hex(self): 
        return self.block_id.hex()

    @classmethod
    def from_result_response(cls, result_response):
        block_id = result_response.block_id
        block_height = result_response.block_height
        # TODO process events
        events = result_response.events

        ts = result_response.block_timestamp or {}
        seconds = ts.seconds
        if seconds:
            block_timestamp = datetime.fromtimestamp(seconds)

        new_instance = cls(block_id, block_height, block_timestamp, events)
        return new_instance
