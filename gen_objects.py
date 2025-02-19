import http.client
import json
import os

#--------------------------------------------------------------------------
# define some utility functions

def exec_rest(payload):
   # Convert dictionary to JSON string
   payload = json.dumps(payload)
   # Execute REST call
   conn = http.client.HTTPSConnection(server)
   conn.request("POST", endpoint, payload, headers=header)
   response = conn.getresponse()
   print("Status: {}\nReason: {}\n".format(response.status, response.reason))
   if response.status == 201:
      data = response.read().decode("utf-8")
      # Retrieve the ID of the new object
      my_dict = json.loads(data)
      object_id = my_dict["id"]
      print( "ID of the new object: {}\n\n".format( object_id))
      # Now we print the entire result in JSON format
      print( json.dumps(json.loads(data), indent=4))
      return object_id
   else: 
      print( "Error!\n")
      exit()


def payload_org_entity( name, description, parent_id):
   payload = {
        'name': name,
        'description': description,
        "creator": "admin",
        'type_definition_id': '5',
        'primary_parent_id': parent_id
   }
   return payload


def payload_use_case(name,description,purpose,parent_id):
   payload = {
        'name': name,
        'description': description,
        'type_definition_id': '74',
        'creator': 'admin',
        'primary_parent_id': parent_id,
        'title': name,
    'fields': [
               {
            'id': '1860',
            'data_type': 'STRING_TYPE',
            'name': 'MRG-AIFacts-ModelUseCase:Purpose',
            'value': purpose
        }
    ]
   }
   return payload


def payload_model(name,description,parent_id):
   payload = {
        'name': name,
        'description': description,
        'type_definition_id': '58',
        'primary_parent_id': parent_id,
        'title': name,
        'fields': [
        {
            'id': '1275',
            'data_type': 'STRING_TYPE',
            'name': 'MRG-Model:Model Owner',
            'value': 'admin'
        },
        {
            'id': '1286',
            'data_type': 'ENUM_TYPE',
            'name': 'MRG-Model:Model Non Model',
             'value': {
                'id': '3696',
                'name': 'Model',
                'localized_label': 'Model',
                'index': 1
             }
        },
    {
            'id': '1279',
            'data_type': 'ENUM_TYPE',
            'name': 'MRG-Model:Machine Learning Model',
             'value': {
                'id': '3694',
                'name': 'Yes',
                'localized_label': 'Yes',
                'index': 1
              }
        }
    ]
   }
   return payload

#--------------------------------------------------------------------------
# read environment variables

if 'SERVER' not in os.environ:
    print("Environment variable $SERVER needs to be defined!")
    exit()
else:
    server = os.environ.get('SERVER')
    print("Environment variable SERVER: ", server)

if 'TOKEN' not in os.environ:
    print("Environment variable $TOKEN needs to be defined!")
    exit()
else:
    token = os.environ.get('TOKEN')
    print("Environment variable TOKEN: ", token)

#--------------------------------------------------------------------------
# define HTTP request header and request endpoint

token = "ZenApiKey" + " " + token
header = {
    'Authorization': token,
    "content-type": "application/json",
    'accept': "application/json"
    }

endpoint= "/openpages-openpagesinstance-cr-opgrc/api/v2/contents"

#--------------------------------------------------------------------------
# define objects of type "Business Entity"

name = 'My_Enterprise'
payload = payload_org_entity( name, name, None)
my_enterprise_id = exec_rest(payload)

name = 'Credit_Department'
payload = payload_org_entity( name, name, my_enterprise_id)
credit_department_id = exec_rest(payload)

name = 'HR_Department'
payload = payload_org_entity( name, name, my_enterprise_id)
hr_department_id = exec_rest(payload)

name = 'Marketing_Department'
payload = payload_org_entity( name, name, my_enterprise_id)
marketing_department_id = exec_rest(payload)

#--------------------------------------------------------------------------
# define objects of type 'Use Case'

name = 'Claims_Processing_Automation'
description = 'Analyze and classify claims data, identify relevant policy coverage, and automate responses for initial claims assessments.'
purpose = 'To streamline the claims process, reduce manual workload, and improve processing speed and accuracy.'
payload = payload_use_case( name, description, purpose, my_enterprise_id)
use_case_id = exec_rest(payload)

name = 'Fraud_Detection'
description = 'Analyze historical claims, detect inconsistencies or patterns that suggest fraud, and flag suspicious claims for further investigation.'
purpose = 'To improve the accuracy of fraud detection and reduce the likelihood of fraudulent claims being paid out.'
payload = payload_use_case( name, description, purpose, my_enterprise_id)
use_case_id = exec_rest(payload)

name = 'Customer_Support_Chatbots'
description = 'Chatbots can assist customers with policy inquiries, claims status, and other general questions, providing instant responses 24/7.'
purpose = 'To enhance customer service, improve response time, and reduce the strain on human agents.'
payload = payload_use_case( name, description, purpose, my_enterprise_id)
use_case_id = exec_rest(payload)

name = 'Policy_Document_Analysis'
description = 'Extract key information from policy documents, terms, and conditions, making it easier to generate summaries or compare policies.'
purpose = 'To assist in policy analysis, improve efficiency, and ensure customers fully understand policy terms.'
payload = payload_use_case( name, description, purpose, my_enterprise_id)
use_case_id = exec_rest(payload)

name = 'Risk_Assessment'
description = 'Analyze data, including historical claims, market conditions, and customer information, to predict potential risks and trends.'
purpose = 'To provide insurers with better insights into risk exposure, helping to inform pricing and underwriting.'
payload = payload_use_case( name, description, purpose, my_enterprise_id)
use_case_id = exec_rest(payload)

name = 'Applicant_Screening'
description = 'Find the right candidates for a job.'
purpose = 'Accelerate your hiring process'
payload = payload_use_case( name, description, purpose, hr_department_id)
use_case_id = exec_rest(payload)

#--------------------------------------------------------------------------
# define objects of type 'Model'

name = 'Applicant_Classification'
description = 'Cluster candidates in high, medium and low profile candidates.'
payload = payload_model( name, description, use_case_id)
object_id = exec_rest(payload)

name = 'Credit_Risk_Classification'
description = 'Cluster customer credits into risk categories.'
payload = payload_model( name, description, credit_department_id)
object_id = exec_rest(payload)

name = 'Customer_Churn_Prediction'
description = 'Customer churn prediction.'
payload = payload_model( name, description, marketing_department_id)
object_id = exec_rest(payload)
