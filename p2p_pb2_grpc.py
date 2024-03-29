# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import p2p_pb2 as p2p__pb2


class FileServiceStub(object):
    """The gRPC service definition for file operations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DownloadFile = channel.unary_unary(
                '/p2p.FileService/DownloadFile',
                request_serializer=p2p__pb2.DownloadRequest.SerializeToString,
                response_deserializer=p2p__pb2.DownloadResponse.FromString,
                )


class FileServiceServicer(object):
    """The gRPC service definition for file operations.
    """

    def DownloadFile(self, request, context):
        """Sends a request for downloading a file's URL
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DownloadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=p2p__pb2.DownloadRequest.FromString,
                    response_serializer=p2p__pb2.DownloadResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'p2p.FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """The gRPC service definition for file operations.
    """

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/p2p.FileService/DownloadFile',
            p2p__pb2.DownloadRequest.SerializeToString,
            p2p__pb2.DownloadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
