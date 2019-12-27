# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from feast.core import CoreService_pb2 as feast_dot_core_dot_CoreService__pb2


class CoreServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeastCoreVersion = channel.unary_unary(
        '/feast.core.CoreService/GetFeastCoreVersion',
        request_serializer=feast_dot_core_dot_CoreService__pb2.GetFeastCoreVersionRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.GetFeastCoreVersionResponse.FromString,
        )
    self.GetFeatureSet = channel.unary_unary(
        '/feast.core.CoreService/GetFeatureSet',
        request_serializer=feast_dot_core_dot_CoreService__pb2.GetFeatureSetRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.GetFeatureSetResponse.FromString,
        )
    self.ListFeatureSets = channel.unary_unary(
        '/feast.core.CoreService/ListFeatureSets',
        request_serializer=feast_dot_core_dot_CoreService__pb2.ListFeatureSetsRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.ListFeatureSetsResponse.FromString,
        )
    self.ListStores = channel.unary_unary(
        '/feast.core.CoreService/ListStores',
        request_serializer=feast_dot_core_dot_CoreService__pb2.ListStoresRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.ListStoresResponse.FromString,
        )
    self.ApplyFeatureSet = channel.unary_unary(
        '/feast.core.CoreService/ApplyFeatureSet',
        request_serializer=feast_dot_core_dot_CoreService__pb2.ApplyFeatureSetRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.ApplyFeatureSetResponse.FromString,
        )
    self.UpdateStore = channel.unary_unary(
        '/feast.core.CoreService/UpdateStore',
        request_serializer=feast_dot_core_dot_CoreService__pb2.UpdateStoreRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.UpdateStoreResponse.FromString,
        )
    self.CreateProject = channel.unary_unary(
        '/feast.core.CoreService/CreateProject',
        request_serializer=feast_dot_core_dot_CoreService__pb2.CreateProjectRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CreateProjectResponse.FromString,
        )
    self.ArchiveProject = channel.unary_unary(
        '/feast.core.CoreService/ArchiveProject',
        request_serializer=feast_dot_core_dot_CoreService__pb2.ArchiveProjectRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.ArchiveProjectResponse.FromString,
        )
    self.ListProjects = channel.unary_unary(
        '/feast.core.CoreService/ListProjects',
        request_serializer=feast_dot_core_dot_CoreService__pb2.ListProjectsRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.ListProjectsResponse.FromString,
        )


class CoreServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetFeastCoreVersion(self, request, context):
    """Retrieve version information about this Feast deployment
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFeatureSet(self, request, context):
    """Returns a specific feature set
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListFeatureSets(self, request, context):
    """Retrieve feature set details given a filter.

    Returns all feature sets matching that filter. If none are found,
    an empty list will be returned.
    If no filter is provided in the request, the response will contain all the feature
    sets currently stored in the registry.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListStores(self, request, context):
    """Retrieve store details given a filter.

    Returns all stores matching that filter. If none are found, an empty list will be returned.
    If no filter is provided in the request, the response will contain all the stores currently
    stored in the registry.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ApplyFeatureSet(self, request, context):
    """Create or update and existing feature set.

    This function is idempotent - it will not create a new feature set if schema does not change.
    If an existing feature set is updated, core will advance the version number, which will be
    returned in response.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateStore(self, request, context):
    """Updates core with the configuration of the store.

    If the changes are valid, core will return the given store configuration in response, and
    start or update the necessary feature population jobs for the updated store.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateProject(self, request, context):
    """Creates a project. Projects serve as namespaces within which resources like features will be
    created. Both feature set names as well as field names must be unique within a project. Project
    names themselves must be globally unique.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ArchiveProject(self, request, context):
    """Archives a project. Archived projects will continue to exist and function, but won't be visible
    through the Core API. Any existing ingestion or serving requests will continue to function,
    but will result in warning messages being logged. It is not possible to unarchive a project
    through the Core API
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListProjects(self, request, context):
    """Lists all projects active projects.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CoreServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeastCoreVersion': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeastCoreVersion,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.GetFeastCoreVersionRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.GetFeastCoreVersionResponse.SerializeToString,
      ),
      'GetFeatureSet': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeatureSet,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.GetFeatureSetRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.GetFeatureSetResponse.SerializeToString,
      ),
      'ListFeatureSets': grpc.unary_unary_rpc_method_handler(
          servicer.ListFeatureSets,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.ListFeatureSetsRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.ListFeatureSetsResponse.SerializeToString,
      ),
      'ListStores': grpc.unary_unary_rpc_method_handler(
          servicer.ListStores,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.ListStoresRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.ListStoresResponse.SerializeToString,
      ),
      'ApplyFeatureSet': grpc.unary_unary_rpc_method_handler(
          servicer.ApplyFeatureSet,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.ApplyFeatureSetRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.ApplyFeatureSetResponse.SerializeToString,
      ),
      'UpdateStore': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateStore,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.UpdateStoreRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.UpdateStoreResponse.SerializeToString,
      ),
      'CreateProject': grpc.unary_unary_rpc_method_handler(
          servicer.CreateProject,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.CreateProjectRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CreateProjectResponse.SerializeToString,
      ),
      'ArchiveProject': grpc.unary_unary_rpc_method_handler(
          servicer.ArchiveProject,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.ArchiveProjectRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.ArchiveProjectResponse.SerializeToString,
      ),
      'ListProjects': grpc.unary_unary_rpc_method_handler(
          servicer.ListProjects,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.ListProjectsRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.ListProjectsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'feast.core.CoreService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
