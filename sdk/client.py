import grpc
import flow.access.access_pb2 as access_pb2
import flow.access.access_pb2_grpc as access_pb2_grpc
import models.header 
import models.account 


class AccessServiceClient(object):
    def __init__(self, access_host, access_port):
        self.channel = grpc.insecure_channel(f'{access_host}:{access_port}')
        self.stub = access_pb2_grpc.AccessAPIStub(self.channel)
    
    def ping(self):
        request = access_pb2.PingRequest()
        try:
            self.stub.Ping(request)
        except grpc.RpcError as err:
            print(err.details()) #pylint: disable=no-member
            print('{}, {}'.format(err.code().name, err.code().value)) #pylint: disable=no-member

    def get_latest_block_header(self):
        request = access_pb2.GetLatestBlockHeaderRequest()
        try:
            response = self.stub.GetLatestBlockHeader(request)
            return models.header.BlockHeader.from_blockheader_response(response.block)
        except grpc.RpcError as err:
            print(err.details()) #pylint: disable=no-member
            print('{}, {}'.format(err.code().name, err.code().value)) #pylint: disable=no-member

    def get_block_header_by_id(self, block_id):
        request = access_pb2.GetBlockHeaderByIdRequest()
        request.block_id = block_id
        try:
            response = self.stub.GetBlockHeaderByID(request)
            return models.header.BlockHeader.from_blockheader_response(response.block)
        except grpc.RpcError as err:
            print(err.details()) #pylint: disable=no-member
            print('{}, {}'.format(err.code().name, err.code().value)) #pylint: disable=no-member


    def get_block_header_by_height(self, height):
        request = access_pb2.GetBlockHeaderByHeightRequest()
        request.height = height
        try:
            response = self.stub.GetBlockHeaderByHeight(request)
            return models.header.BlockHeader.from_blockheader_response(response.block)
        except grpc.RpcError as err:
            print(err.details()) #pylint: disable=no-member
            print('{}, {}'.format(err.code().name, err.code().value)) #pylint: disable=no-member

    #### Collection
    def get_collection_by_id(self, collection_id):
        raise NotImplementedError

    ####  Accounts
    def get_account_at_latest_block(self, address):
        request = access_pb2.GetAccountAtLatestBlockRequest()
        request.address = address
        try:
            response = self.stub.GetAccountAtLatestBlock(request)
            return models.account.Account.from_account_response(response.account)
        except grpc.RpcError as err:
            print(err.details())
            print('{}, {}'.format(err.code().name, err.code().value))

    def get_account_at_block_height(self, address, height):
        request = access_pb2.GetAccountAtBlockHeightRequest()
        request.height = height
        request.address = address
        try:
            response = self.stub.GetAccountAtBlockHeight(request)
            return models.account.Account.from_account_response(response.account)
        except grpc.RpcError as err:
            print(err.details())
            print('{}, {}'.format(err.code().name, err.code().value))

    ####  Transactions
    def send_transaction(self, transaction):
        # SendTransaction
        raise NotImplementedError

    def get_transaction(self, tx_id):
        # GetTransaction
        raise NotImplementedError

    def get_transaction_result(self, tx_id):
        # GetTransactionResult
        raise NotImplementedError

    #### Scripts

    def execute_script_at_latest_block(self, script):
        # ExecuteScriptAtLatestBlock
        raise NotImplementedError

    def execute_script_at_block_id(self, script, block_id):
        # ExecuteScriptAtBlockID
        raise NotImplementedError

    def execute_script_at_block_height(self, script, height):
        # ExecuteScriptAtBlockHeight
        raise NotImplementedError

    #### Events

    def get_events_for_height_range(self, type, start_height, end_height):
        # GetEventsForHeightRange
        raise NotImplementedError

    def get_events_for_block_ids(self, type, block_ids):
        # GetEventsForBlockIDs
        raise NotImplementedError

    #### NetworkParameters

    # TODO why do we need chain_id for parameters
    def get_network_parameters(self, chain_id):
        # GetNetworkParameters
        raise NotImplementedError

