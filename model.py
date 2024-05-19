import requests
API_URL = "https://api-inference.huggingface.co/models/Riftkey/NER-Disease"
API_TOKEN ="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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
# data = query("influenza cancer tumor ")


# sample text = "terdapat gejala bersin dan batuk, kemungkinan paseins sedang mengalami flu. selain itu terdapat cairan di dalam paru-paru kemungkinan pneumonia"
def diagnosis(text):

  """
  Performs NER analysis on the provided text and returns a list of potential diagnoses.

  Args:
      text: The text to be analyzed for named entities (potential diagnoses).

  Returns:
      A list of potential diagnoses extracted from the text using NER.
  """
  
  result = query(text)
  print(result)
  diagnoses = set() 
  for entity in result:
    # if entity['word'][0] == "#":  # Exclude special tokens
    # Extract only the disease name after removing hashtag and following characters
    if entity['word'].startswith("##"):
        # print(entity['word'])
        disease_name = entity['word'].split()[1]  # Get the word after the space
        # print(disease_name)
    else:
        disease_name = entity['word']
    diagnoses.add(disease_name)

  if not diagnoses:  # Handle no diagnoses found
    return "Tidak ada kemungkinan diagnosis ditemukan."

  # Join diagnoses with commas and capitalize the first letter
  formatted_diagnosis = "Kemungkinan Diagnosis: " + ", ".join(diagnoses)
  return formatted_diagnosis.capitalize()



