Set the following environment variables in your terminal using the values from your Azure account:

Copy code
export AZURE_SUBSCRIPTION_ID=f269d616-d6dd-4823-993e-578f5f04bee0
export AZURE_TENANT_ID=15c26471-ca6a-4799-8bc9-45cc581a7644
export AZURE_CLIENT_ID=9bcce004-12da-4bf6-aaac-01719c5db6fd
export AZURE_CLIENT_SECRET=JaE8Q~Q0B2y0_B10S8Z9S~.JUL.ooZim1eTIGcK9

subscription_id - ID of your Azure subscription
tenant_id - ID of your Azure Active Directory tenant
client_id - ID of the registered application in Azure Active Directory
client_secret - client secret generated for the registered application

Once environment variables are set, run the following command to deploy the project to Azure:
sls deploy
Wait for the deployment to complete and verify that the project is running on Azure
