Set the following environment variables in your terminal using the values from your Azure account:

Copy code
export AZURE_SUBSCRIPTION_ID=f269d616-d6dd-4823-993e-578f5f04bee0
export AZURE_TENANT_ID=15c26471-ca6a-4799-8bc9-45cc581a7644
export AZURE_CLIENT_ID=378e9f91-4bcd-437d-88a5-f2a2893ebf1b
export AZURE_CLIENT_SECRET=rDu8Q~EKZCZkxfq1g6qeD.rMBUa~TChq.wtKndrP

subscription_id - ID of your Azure subscription
tenant_id - ID of your Azure Active Directory tenant
client_id - ID of the registered application in Azure Active Directory
client_secret - client secret generated for the registered application
Once environment variables are set, run the following command to deploy the project to Azure:
Copy code
sis deploy
Wait for the deployment to complete and verify that the project is running on Azure
If you have any issues with the deployment process or setting up the environment variables, please refer to the Azure documentation or contact the Azure support team.