# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network express-route peering show",
)
class Show(AAZCommand):
    """Get the details of an express route peering.

    :example: Get private peering details of an ExpressRoute circuit.
        az network express-route peering show -g MyResourceGroup --circuit-name MyCircuit -n AzurePrivatePeering
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressroutecircuits/{}/peerings/{}", "2022-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.circuit_name = AAZStrArg(
            options=["--circuit-name"],
            help="ExpressRoute circuit name.",
            required=True,
            id_part="name",
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the peering.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ExpressRouteCircuitPeeringsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ExpressRouteCircuitPeeringsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "circuitName", self.ctx.args.circuit_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "peeringName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType()
            _schema_on_200.name = AAZStrType()
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.azure_asn = AAZIntType(
                serialized_name="azureASN",
            )
            properties.connections = AAZListType()
            properties.express_route_connection = AAZObjectType(
                serialized_name="expressRouteConnection",
            )
            properties.gateway_manager_etag = AAZStrType(
                serialized_name="gatewayManagerEtag",
            )
            properties.ipv6_peering_config = AAZObjectType(
                serialized_name="ipv6PeeringConfig",
            )
            properties.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            properties.microsoft_peering_config = AAZObjectType(
                serialized_name="microsoftPeeringConfig",
            )
            _build_schema_express_route_circuit_peering_config_read(properties.microsoft_peering_config)
            properties.peer_asn = AAZIntType(
                serialized_name="peerASN",
            )
            properties.peered_connections = AAZListType(
                serialized_name="peeredConnections",
                flags={"read_only": True},
            )
            properties.peering_type = AAZStrType(
                serialized_name="peeringType",
            )
            properties.primary_azure_port = AAZStrType(
                serialized_name="primaryAzurePort",
            )
            properties.primary_peer_address_prefix = AAZStrType(
                serialized_name="primaryPeerAddressPrefix",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.route_filter = AAZObjectType(
                serialized_name="routeFilter",
            )
            _build_schema_sub_resource_read(properties.route_filter)
            properties.secondary_azure_port = AAZStrType(
                serialized_name="secondaryAzurePort",
            )
            properties.secondary_peer_address_prefix = AAZStrType(
                serialized_name="secondaryPeerAddressPrefix",
            )
            properties.shared_key = AAZStrType(
                serialized_name="sharedKey",
            )
            properties.state = AAZStrType()
            properties.stats = AAZObjectType()
            properties.vlan_id = AAZIntType(
                serialized_name="vlanId",
            )

            connections = cls._schema_on_200.properties.connections
            connections.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.connections.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties.connections.Element.properties
            properties.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            properties.authorization_key = AAZStrType(
                serialized_name="authorizationKey",
            )
            properties.circuit_connection_status = AAZStrType(
                serialized_name="circuitConnectionStatus",
                flags={"read_only": True},
            )
            properties.express_route_circuit_peering = AAZObjectType(
                serialized_name="expressRouteCircuitPeering",
            )
            _build_schema_sub_resource_read(properties.express_route_circuit_peering)
            properties.ipv6_circuit_connection_config = AAZObjectType(
                serialized_name="ipv6CircuitConnectionConfig",
            )
            properties.peer_express_route_circuit_peering = AAZObjectType(
                serialized_name="peerExpressRouteCircuitPeering",
            )
            _build_schema_sub_resource_read(properties.peer_express_route_circuit_peering)
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            ipv6_circuit_connection_config = cls._schema_on_200.properties.connections.Element.properties.ipv6_circuit_connection_config
            ipv6_circuit_connection_config.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            ipv6_circuit_connection_config.circuit_connection_status = AAZStrType(
                serialized_name="circuitConnectionStatus",
                flags={"read_only": True},
            )

            express_route_connection = cls._schema_on_200.properties.express_route_connection
            express_route_connection.id = AAZStrType(
                flags={"read_only": True},
            )

            ipv6_peering_config = cls._schema_on_200.properties.ipv6_peering_config
            ipv6_peering_config.microsoft_peering_config = AAZObjectType(
                serialized_name="microsoftPeeringConfig",
            )
            _build_schema_express_route_circuit_peering_config_read(ipv6_peering_config.microsoft_peering_config)
            ipv6_peering_config.primary_peer_address_prefix = AAZStrType(
                serialized_name="primaryPeerAddressPrefix",
            )
            ipv6_peering_config.route_filter = AAZObjectType(
                serialized_name="routeFilter",
            )
            _build_schema_sub_resource_read(ipv6_peering_config.route_filter)
            ipv6_peering_config.secondary_peer_address_prefix = AAZStrType(
                serialized_name="secondaryPeerAddressPrefix",
            )
            ipv6_peering_config.state = AAZStrType()

            peered_connections = cls._schema_on_200.properties.peered_connections
            peered_connections.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.peered_connections.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties.peered_connections.Element.properties
            properties.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            properties.auth_resource_guid = AAZStrType(
                serialized_name="authResourceGuid",
            )
            properties.circuit_connection_status = AAZStrType(
                serialized_name="circuitConnectionStatus",
                flags={"read_only": True},
            )
            properties.connection_name = AAZStrType(
                serialized_name="connectionName",
            )
            properties.express_route_circuit_peering = AAZObjectType(
                serialized_name="expressRouteCircuitPeering",
            )
            _build_schema_sub_resource_read(properties.express_route_circuit_peering)
            properties.peer_express_route_circuit_peering = AAZObjectType(
                serialized_name="peerExpressRouteCircuitPeering",
            )
            _build_schema_sub_resource_read(properties.peer_express_route_circuit_peering)
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            stats = cls._schema_on_200.properties.stats
            stats.primarybytes_in = AAZIntType(
                serialized_name="primarybytesIn",
            )
            stats.primarybytes_out = AAZIntType(
                serialized_name="primarybytesOut",
            )
            stats.secondarybytes_in = AAZIntType(
                serialized_name="secondarybytesIn",
            )
            stats.secondarybytes_out = AAZIntType(
                serialized_name="secondarybytesOut",
            )

            return cls._schema_on_200


_schema_express_route_circuit_peering_config_read = None


def _build_schema_express_route_circuit_peering_config_read(_schema):
    global _schema_express_route_circuit_peering_config_read
    if _schema_express_route_circuit_peering_config_read is not None:
        _schema.advertised_communities = _schema_express_route_circuit_peering_config_read.advertised_communities
        _schema.advertised_public_prefixes = _schema_express_route_circuit_peering_config_read.advertised_public_prefixes
        _schema.advertised_public_prefixes_state = _schema_express_route_circuit_peering_config_read.advertised_public_prefixes_state
        _schema.customer_asn = _schema_express_route_circuit_peering_config_read.customer_asn
        _schema.legacy_mode = _schema_express_route_circuit_peering_config_read.legacy_mode
        _schema.routing_registry_name = _schema_express_route_circuit_peering_config_read.routing_registry_name
        return

    _schema_express_route_circuit_peering_config_read = AAZObjectType()

    express_route_circuit_peering_config_read = _schema_express_route_circuit_peering_config_read
    express_route_circuit_peering_config_read.advertised_communities = AAZListType(
        serialized_name="advertisedCommunities",
    )
    express_route_circuit_peering_config_read.advertised_public_prefixes = AAZListType(
        serialized_name="advertisedPublicPrefixes",
    )
    express_route_circuit_peering_config_read.advertised_public_prefixes_state = AAZStrType(
        serialized_name="advertisedPublicPrefixesState",
        flags={"read_only": True},
    )
    express_route_circuit_peering_config_read.customer_asn = AAZIntType(
        serialized_name="customerASN",
    )
    express_route_circuit_peering_config_read.legacy_mode = AAZIntType(
        serialized_name="legacyMode",
    )
    express_route_circuit_peering_config_read.routing_registry_name = AAZStrType(
        serialized_name="routingRegistryName",
    )

    advertised_communities = _schema_express_route_circuit_peering_config_read.advertised_communities
    advertised_communities.Element = AAZStrType()

    advertised_public_prefixes = _schema_express_route_circuit_peering_config_read.advertised_public_prefixes
    advertised_public_prefixes.Element = AAZStrType()

    _schema.advertised_communities = _schema_express_route_circuit_peering_config_read.advertised_communities
    _schema.advertised_public_prefixes = _schema_express_route_circuit_peering_config_read.advertised_public_prefixes
    _schema.advertised_public_prefixes_state = _schema_express_route_circuit_peering_config_read.advertised_public_prefixes_state
    _schema.customer_asn = _schema_express_route_circuit_peering_config_read.customer_asn
    _schema.legacy_mode = _schema_express_route_circuit_peering_config_read.legacy_mode
    _schema.routing_registry_name = _schema_express_route_circuit_peering_config_read.routing_registry_name


_schema_sub_resource_read = None


def _build_schema_sub_resource_read(_schema):
    global _schema_sub_resource_read
    if _schema_sub_resource_read is not None:
        _schema.id = _schema_sub_resource_read.id
        return

    _schema_sub_resource_read = AAZObjectType()

    sub_resource_read = _schema_sub_resource_read
    sub_resource_read.id = AAZStrType()

    _schema.id = _schema_sub_resource_read.id


__all__ = ["Show"]
