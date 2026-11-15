// Book: Node.js for DevOps Engineers — Example 182
// examples/azure-vms.js
import { DefaultAzureCredential } from '@azure/identity';
import {
  ComputeManagementClient,
} from '@azure/arm-compute';

const client = new ComputeManagementClient(
  new DefaultAzureCredential(),
  process.env.AZURE_SUBSCRIPTION_ID,
);
for await (const vm of client.virtualMachines.listAll()) {
  console.log(vm.location, vm.name);
}
