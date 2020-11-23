class Event(object):
    def __init__(self, type, transaction_id, transaction_index, event_index, payload):
        self.type = type
        self.transaction_id = transaction_id
        self.transaction_index = transaction_index
        self.event_index = event_index
        # TODO parse payload
        self.payload = payload
