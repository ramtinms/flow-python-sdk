class BlockSeal(object):
    def __init__(self, block_id, execution_receipt_id, execution_receipt_signatures, result_approval_signatures):
    	self.block_id = block_id
    	self.execution_receipt_id = execution_receipt_id
        self.execution_receipt_signatures = execution_receipt_signatures
        self.result_approval_signatures = result_approval_signatures

    def block_id_hex(self): 
        return self.block_id.hex()

    def __str__(self):
    	# TODO iterate over other values
        return f"""
        Block Seal
            block_id: {self.block_id_hex()}
        """