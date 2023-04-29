import requests, uuid
import json

with open('Config.json', 'r' , encoding='utf-8') as f:
    ke = json.load(f)

def tradict(text,list_lang):
    key = ke["key_tre"]
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = ke["location_tre"]

    path = '/translate'
    constructed_url = endpoint + path

    list_lang.sort()

    params = {
        'api-version': '3.0',
        'from': 'fr',
        'to': list_lang
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    try:
        response = response[0]["translations"]
    except:
        return response
    
    res = {}
    for i in response:
        #print(i["to"], ":" , i["text"])
        res[i["to"]] = i["text"]
    #print(res)

    return res

if __name__ == "__main__":
    print(tradict("I would really like to drive your car around the block a few times!"))