import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('API_TOKEN')

# Load excel sheets
# materials_df = pd.read_excel(
#     './data/raw_data-SA Exercise.xlsx', sheet_name='Materials')
# transportation_df = pd.read_excel(
#     './data/raw_data-SA Exercise.xlsx', sheet_name='Transportation')
# waste_df = pd.read_excel(
#     './data/raw_data-SA Exercise.xlsx', sheet_name='Waste')
#
# # Display the first few rows of the DataFrame
# print(materials_df.head())
# print(transportation_df.head())
# print(waste_df.head())


# # Countries
# response = requests.get("https://sa-exercise.co2ai.com/api/0.1/matching/countries",
#                         headers={"Authorization": f"Bearer {token}"})
#
# print(response.json())
#
#
# payload = {"efIds": "1"}
#
# ef_id_response = requests.post("https://sa-exercise.co2ai.com/api/0.1/matching/look-up-efs",
#                                headers={"Authorization": f"Bearer {token}"}, json=payload)
#
# print(ef_id_response.json())
#
# # Units
# response = requests.get("https://sa-exercise.co2ai.com/api/0.1/matching/units",
#                         headers={"Authorization": f"Bearer {token}"})
#
# print(response.json())


payload = {"query": {"ghg_category": "Purchased goods and services"},
           "impact_type": "co2"}
query_response = requests.post("https://sa-exercise.co2ai.com/api/0.1/matching/search",
                               headers={"Authorization": f"Bearer {token}"}, json=payload)

print(query_response.json())
