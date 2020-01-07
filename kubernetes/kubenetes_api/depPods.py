from kubernetes import config, config

# from _future_import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IkN0VDcyLXJhSXd1cXBCdXFmQUp2dDBYd01DcU1kS29aRERBai1hRDVzTkkifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tcjc0aHgiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjRhMDdjMDViLWY0OWItNDBlMi1iZmRkLTJiOTY3MTY0YTU4MSIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.GcUiuy8Q6j-f_6PiBXT2rvOY4Q83hxFy96FBRjUL2IoRvkDqaieyQVAKbu3_lte6Pg7LEzW797C_2VwP9xo1us5FDXN6KnmDMdXOU9EjFFrjt1F7IGR_OfnCOmZEG5Diydu2IvzJTq6N_lRMjAZOOq7Rbr8h7AimI2G_W6LJvCxG6-8Ppo-3qjv7vMeFvmG9VUsKcLp-IZyXdTI4OGuuvcOaHiwCzwbI9Uojwi279STsXpnoOj089yeE9sA9QDXpWZqVBonNZpF2Xb9ZPAOYWgrCkx0mT28wLaxWaRWP39ugUmDpct0wxo0eLSwpjOYqqa7HoYpjP20iIyUP5d0OkQ'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Pod() # V1Pod | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

try:
    api_response = api_instance.create_namespaced_pod(namespace, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreV1Api->create_namespaced_pod: %s\n" % e)