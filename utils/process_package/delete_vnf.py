# All Rights Reserved.
#
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

from VIMManagement.utils.config_map import ConfigMapClient
from VIMManagement.utils.deployment import DeploymentClient
from VIMManagement.utils.horizontal_pod_autoscaler import HorizontalPodAutoscalerClient
from VIMManagement.utils.persistent_volume import PersistentVolumeClient
from VIMManagement.utils.persistent_volume_claim import PersistentVolumeClaimClient
from VIMManagement.utils.service import ServiceClient
from os_ma_nfvo import settings
from utils.file_manipulation import remove_file
from utils.process_package.process_vnf_instance import ProcessVNFInstance


class DeleteService(ProcessVNFInstance):
    def __init__(self, vnf_package_id, vnf_instance_name):
        super().__init__(vnf_package_id, vnf_instance_name)

    def process_config_map(self, **kwargs):
        client = ConfigMapClient(
            instance_name=self.vnf_instance_name, namespace=kwargs['namespace'],
            config_file_name=kwargs['artifacts_name'])
        client.handle_delete()

    def process_deployment(self, **kwargs):
        data = {'instance_name': self.vnf_instance_name, 'namespace': kwargs['vdu'].namespace}
        client = DeploymentClient(**data)
        client.handle_delete()

    def process_service(self, **kwargs):
        client = ServiceClient(
            instance_name=kwargs['vdu'].name_of_service, namespace=kwargs['vdu'].namespace)
        client.handle_delete()

    def process_persistent_volume_claim(self, **kwargs):
        client = PersistentVolumeClaimClient(
            instance_name=self.vnf_instance_name, namespace=kwargs['vdu'].namespace)
        client.handle_delete()

    def process_persistent_volume(self, **kwargs):
        client = PersistentVolumeClient(instance_name=self.vnf_instance_name)
        client.handle_delete()

    def process_horizontal_pod_autoscaler(self, **kwargs):
        client = HorizontalPodAutoscalerClient(
            instance_name=self.vnf_instance_name, namespace=kwargs['vdu'].namespace)
        client.handle_delete()

    def process_delete(self, **kwargs):
        for vdu in self.vdu:
            self.process_deployment(vdu=vdu)
            for scale in self.scale_policy:
                if scale.node == vdu.node_name:
                    self.process_horizontal_pod_autoscaler(vdu=vdu)
            if vdu.storage_path and vdu.storage_size:
                remove_file("{}{}".format(settings.VOLUME_PATH, self.vnf_instance_name))
