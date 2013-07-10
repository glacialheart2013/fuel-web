# -*- coding: utf-8 -*-

#    Copyright 2013 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nailgun.api.handlers.cluster import ClusterHandler
from nailgun.api.handlers.cluster import ClusterCollectionHandler
from nailgun.api.handlers.cluster import ClusterChangesHandler
from nailgun.api.handlers.cluster import ClusterAttributesHandler
from nailgun.api.handlers.cluster import ClusterAttributesDefaultsHandler

from nailgun.api.handlers.network_configuration \
    import NetworkConfigurationHandler
from nailgun.api.handlers.network_configuration \
    import NetworkConfigurationVerifyHandler

from nailgun.api.handlers.redhat import RedHatAccountHandler
from nailgun.api.handlers.release import ReleaseHandler
from nailgun.api.handlers.release import ReleaseCollectionHandler

from nailgun.api.handlers.node import NodesAllocationStatsHandler
from nailgun.api.handlers.node import NodeHandler
from nailgun.api.handlers.node import NodeCollectionHandler

from nailgun.api.handlers.disks import NodeDisksHandler
from nailgun.api.handlers.disks import NodeDefaultsDisksHandler
from nailgun.api.handlers.disks import NodeVolumesInformationHandler

from nailgun.api.handlers.node import NodeNICsHandler
from nailgun.api.handlers.node import NodeNICsDefaultHandler
from nailgun.api.handlers.node import NodeCollectionNICsHandler
from nailgun.api.handlers.node import NodeCollectionNICsDefaultHandler
from nailgun.api.handlers.node import NodeNICsVerifyHandler

from nailgun.api.handlers.tasks import TaskHandler
from nailgun.api.handlers.tasks import TaskCollectionHandler

from nailgun.api.handlers.notifications import NotificationHandler
from nailgun.api.handlers.notifications import NotificationCollectionHandler

from nailgun.api.handlers.logs import LogEntryCollectionHandler
from nailgun.api.handlers.logs import LogPackageHandler
from nailgun.api.handlers.logs import LogSourceCollectionHandler
from nailgun.api.handlers.logs import LogSourceByNodeCollectionHandler

from nailgun.api.handlers.version import VersionHandler

from nailgun.api.handlers.plugin import PluginCollectionHandler
from nailgun.api.handlers.plugin import PluginHandler

from nailgun.api.handlers.ostf import OSTFHandler

urls = (
    (
        '/api/releases/',
        ReleaseCollectionHandler,
    ),
    (
        '/api/releases/<int:release_id>/',
        ReleaseHandler,
    ),
    (
        '/api/clusters/',
        ClusterCollectionHandler
    ),
    (
        '/api/clusters/<int:cluster_id>/',
        ClusterHandler
    ),
    (
        '/api/clusters/<int:cluster_id>/changes/',
        ClusterChangesHandler
    ),
    (
        '/api/clusters/<int:cluster_id>/attributes/',
        ClusterAttributesHandler
    ),
    (
        '/api/clusters/<int:cluster_id>/attributes/defaults/',
        ClusterAttributesDefaultsHandler
    ),
    (
        '/api/nodes/',
        NodeCollectionHandler
    ),
    (
        '/api/nodes/<int:node_id>/',
        NodeHandler
    ),
    (
        '/api/nodes/<int:node_id>/disks/',
        NodeDisksHandler
    ),
    (
        '/api/nodes/<int:node_id>/disks/defaults/',
        NodeDefaultsDisksHandler
    ),
    (
        '/api/nodes/<int:node_id>/volumes/',
        NodeVolumesInformationHandler
    ),
    (
        '/api/clusters/<int:cluster_id>/network_configuration/',
        NetworkConfigurationHandler
    ),
    (
        '/api/clusters/<int:cluster_id>/network_configuration/verify/',
        NetworkConfigurationVerifyHandler
    ),
    (
        '/api/nodes/<int:node_id>/attributes/',
        NodeAttributesHandler
    ),
    (
        '/api/nodes/<int:node_id>/attributes/defaults/',
        NodeAttributesDefaultsHandler
    ),
    (
        '/api/nodes/<int:node_id>/attributes/<attr_name>/',
        NodeAttributesByNameHandler
    ),
    (
        '/api/nodes/<int:node_id>/attributes/<attr_name>/defaults/',
        NodeAttributesByNameDefaultsHandler
    ),
    (
        '/api/nodes/interfaces/',
        NodeCollectionNICsHandler
    ),
    (
        '/api/nodes/interfaces/default_assignment',
        NodeCollectionNICsDefaultHandler
    ),
    (
        '/api/nodes/<int:node_id>/interfaces/',
        NodeNICsHandler
    ),
    (
        '/api/nodes/<int:node_id>/interfaces/default_assignment/',
        NodeNICsDefaultHandler
    ),
    (
        '/api/nodes/interfaces_verify/',
        NodeNICsVerifyHandler
    ),
    (
        '/api/tasks',
        TaskCollectionHandler
    ),
    (
        '/api/tasks/<int:task_id>',
        TaskHandler
    ),
    (
        '/api/notifications',
        NotificationCollectionHandler
    ),
    (
        '/api/notifications/<int:notification_id>',
        NotificationHandler
    ),
    (
        '/api/version',
        VersionHandler
    )
)
"""
    r'/logs/?$',
    'LogEntryCollectionHandler',
    r'/logs/package/?$',
    'LogPackageHandler',
    r'/logs/sources/?$',
    'LogSourceCollectionHandler',
    r'/logs/sources/nodes/(?P<node_id>\d+)/?$',
    'LogSourceByNodeCollectionHandler',

    r'/version/?$',
    'VersionHandler',

    r'/plugins/?$',
    'PluginCollectionHandler',
    r'/plugins/(?P<plugin_id>\d+)/?$',
    'PluginHandler',
    r'/redhat/account/?$',
    'RedHatAccountHandler',
    # Handlers for openstack testing framework
    r'/ostf/(?P<cluster_id>\d+)/?$',
    'OSTFHandler',
)

"""
