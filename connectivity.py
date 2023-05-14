###########
######---- use pip install azure-storage-blob azure-identity ---- 




from azure.storage.blob import BlobServiceClient
from azure.identity import ClientSecretCredential
from azure.core.exceptions import ResourceNotFoundError

# Replace these with your specific values
tenant_id = "<your-tenant-id>"
client_id = "<your-app-registration-client-id>"
client_secret = "<your-client-secret>"
storage_account_name = "<your-storage-account-name>"
container_name = "<your-container-name>"
blob_name = "<your-blob-name>"

try:
    credential = ClientSecretCredential(tenant_id, client_id, client_secret)

    blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=credential)

    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    print("Attempting to download blob...")

    blob_data = blob_client.download_blob().readall()
    
    print("Blob downloaded successfully.")
    
except ResourceNotFoundError:
    print(f"The specified blob does not exist in the container.")
except Exception as ex:
    print(f"An error occurred: {ex}")
