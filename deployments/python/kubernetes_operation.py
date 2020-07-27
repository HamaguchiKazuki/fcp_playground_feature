from kubernetes import client, config, watch

search_metadata_name = input()

config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_service_for_all_namespaces(watch=False)
# for i in ret.items:
    # print(f"{i.status.pod_ip} : {i.metadata.namespace} : {i.metadata.name}")
