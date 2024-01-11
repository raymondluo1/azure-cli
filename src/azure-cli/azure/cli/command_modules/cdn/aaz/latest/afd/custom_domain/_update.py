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
    "afd custom-domain update",
)
class Update(AAZCommand):
    """Update a new domain within the specified profile.

    :example: Update the custom domain's supported minimum TLS version.
        az afd custom-domain update -g group --custom-domain-name customDomain --profile-name profile --minimum-tls-version TLS12

    :example: Update the custom domain's certificate type to AFD managed certificate.
        az afd custom-domain update -g group --custom-domain-name customDomain --profile-name profile --certificate-type ManagedCertificate
    """

    _aaz_info = {
        "version": "2023-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cdn/profiles/{}/customdomains/{}", "2023-05-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.custom_domain_name = AAZStrArg(
            options=["-n", "--name", "--custom-domain-name"],
            help="Name of the domain under the profile which is unique globally.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "AzureDnsZone"

        _args_schema = cls._args_schema
        _args_schema.azure_dns_zone = AAZStrArg(
            options=["--azure-dns-zone"],
            arg_group="AzureDnsZone",
            help="ID of the Azure DNS zone.",
            nullable=True,
        )

        # define Arg Group "Properties"

        # define Arg Group "Secret"

        _args_schema = cls._args_schema
        _args_schema.secret = AAZStrArg(
            options=["--secret"],
            arg_group="Secret",
            help="Resource reference to the secret. ie. subs/rg/profile/secret",
            nullable=True,
        )

        # define Arg Group "TlsSettings"

        _args_schema = cls._args_schema
        _args_schema.certificate_type = AAZStrArg(
            options=["--certificate-type"],
            arg_group="TlsSettings",
            help="Defines the source of the SSL certificate.",
            enum={"AzureFirstPartyManagedCertificate": "AzureFirstPartyManagedCertificate", "CustomerCertificate": "CustomerCertificate", "ManagedCertificate": "ManagedCertificate"},
        )
        _args_schema.minimum_tls_version = AAZStrArg(
            options=["--minimum-tls-version"],
            arg_group="TlsSettings",
            help="TLS protocol version that will be used for Https",
            nullable=True,
            enum={"TLS10": "TLS10", "TLS12": "TLS12"},
        )
        return cls._args_schema

    _args_resource_reference_update = None

    @classmethod
    def _build_args_resource_reference_update(cls, _schema):
        if cls._args_resource_reference_update is not None:
            _schema.id = cls._args_resource_reference_update.id
            return

        cls._args_resource_reference_update = AAZObjectArg(
            nullable=True,
        )

        resource_reference_update = cls._args_resource_reference_update
        resource_reference_update.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
            nullable=True,
        )

        _schema.id = cls._args_resource_reference_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.AFDCustomDomainsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.AFDCustomDomainsCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AFDCustomDomainsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/customDomains/{customDomainName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "customDomainName", self.ctx.args.custom_domain_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
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
                    "api-version", "2023-05-01",
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
            _UpdateHelper._build_schema_afd_domain_read(cls._schema_on_200)

            return cls._schema_on_200

    class AFDCustomDomainsCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/customDomains/{customDomainName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "customDomainName", self.ctx.args.custom_domain_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
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
                    "api-version", "2023-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_afd_domain_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("azureDnsZone", AAZObjectType)
                properties.set_prop("tlsSettings", AAZObjectType)

            azure_dns_zone = _builder.get(".properties.azureDnsZone")
            if azure_dns_zone is not None:
                azure_dns_zone.set_prop("id", AAZStrType, ".azure_dns_zone")

            tls_settings = _builder.get(".properties.tlsSettings")
            if tls_settings is not None:
                tls_settings.set_prop("certificateType", AAZStrType, ".certificate_type", typ_kwargs={"flags": {"required": True}})
                tls_settings.set_prop("minimumTlsVersion", AAZStrType, ".minimum_tls_version")
                tls_settings.set_prop("secret", AAZObjectType)

            secret = _builder.get(".properties.tlsSettings.secret")
            if secret is not None:
                secret.set_prop("id", AAZStrType, ".secret")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_resource_reference_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_afd_domain_read = None

    @classmethod
    def _build_schema_afd_domain_read(cls, _schema):
        if cls._schema_afd_domain_read is not None:
            _schema.id = cls._schema_afd_domain_read.id
            _schema.name = cls._schema_afd_domain_read.name
            _schema.properties = cls._schema_afd_domain_read.properties
            _schema.system_data = cls._schema_afd_domain_read.system_data
            _schema.type = cls._schema_afd_domain_read.type
            return

        cls._schema_afd_domain_read = _schema_afd_domain_read = AAZObjectType()

        afd_domain_read = _schema_afd_domain_read
        afd_domain_read.id = AAZStrType(
            flags={"read_only": True},
        )
        afd_domain_read.name = AAZStrType(
            flags={"read_only": True},
        )
        afd_domain_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        afd_domain_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        afd_domain_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_afd_domain_read.properties
        properties.azure_dns_zone = AAZObjectType(
            serialized_name="azureDnsZone",
        )
        cls._build_schema_resource_reference_read(properties.azure_dns_zone)
        properties.deployment_status = AAZStrType(
            serialized_name="deploymentStatus",
            flags={"read_only": True},
        )
        properties.domain_validation_state = AAZStrType(
            serialized_name="domainValidationState",
            flags={"read_only": True},
        )
        properties.extended_properties = AAZDictType(
            serialized_name="extendedProperties",
        )
        properties.host_name = AAZStrType(
            serialized_name="hostName",
            flags={"required": True},
        )
        properties.pre_validated_custom_domain_resource_id = AAZObjectType(
            serialized_name="preValidatedCustomDomainResourceId",
        )
        cls._build_schema_resource_reference_read(properties.pre_validated_custom_domain_resource_id)
        properties.profile_name = AAZStrType(
            serialized_name="profileName",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.tls_settings = AAZObjectType(
            serialized_name="tlsSettings",
        )
        properties.validation_properties = AAZObjectType(
            serialized_name="validationProperties",
        )

        extended_properties = _schema_afd_domain_read.properties.extended_properties
        extended_properties.Element = AAZStrType()

        tls_settings = _schema_afd_domain_read.properties.tls_settings
        tls_settings.certificate_type = AAZStrType(
            serialized_name="certificateType",
            flags={"required": True},
        )
        tls_settings.minimum_tls_version = AAZStrType(
            serialized_name="minimumTlsVersion",
        )
        tls_settings.secret = AAZObjectType()
        cls._build_schema_resource_reference_read(tls_settings.secret)

        validation_properties = _schema_afd_domain_read.properties.validation_properties
        validation_properties.expiration_date = AAZStrType(
            serialized_name="expirationDate",
            flags={"read_only": True},
        )
        validation_properties.validation_token = AAZStrType(
            serialized_name="validationToken",
            flags={"read_only": True},
        )

        system_data = _schema_afd_domain_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_afd_domain_read.id
        _schema.name = cls._schema_afd_domain_read.name
        _schema.properties = cls._schema_afd_domain_read.properties
        _schema.system_data = cls._schema_afd_domain_read.system_data
        _schema.type = cls._schema_afd_domain_read.type

    _schema_resource_reference_read = None

    @classmethod
    def _build_schema_resource_reference_read(cls, _schema):
        if cls._schema_resource_reference_read is not None:
            _schema.id = cls._schema_resource_reference_read.id
            return

        cls._schema_resource_reference_read = _schema_resource_reference_read = AAZObjectType()

        resource_reference_read = _schema_resource_reference_read
        resource_reference_read.id = AAZStrType()

        _schema.id = cls._schema_resource_reference_read.id


__all__ = ["Update"]
