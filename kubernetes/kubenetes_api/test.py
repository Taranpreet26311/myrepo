
from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


# from kubernetes import client, config, watch
# # Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()
# v1 = client.CoreV1Api()
# count = 10
# w = watch.Watch()
# for event in w.stream(v1.list_namespace, _request_timeout=60):
#     print("Event: %s %s" % (event['type'], event['object'].metadata.name))
#     count -= 1
#     if not count:
#         w.stop()
#         print("Ended.")
