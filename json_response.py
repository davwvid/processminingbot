def text_response(text):
  return {
    "fulfillmentMessages": [
      {
        "text": {
          "text": [text]
        }
      }
    ]
  }

def fileupload_response():
  return {
    "fulfillment_messages": [
      {
        "payload": {
          "richContent": [
            [
              {
                "type": "button",
                "icon": {},
                "text": "Upload",
                "link": "https://processminingbot.herokuapp.com/upload",
                "event": {
                  "name": "",
                  "languageCode": "",
                  "parameters": {}
                }
              }
            ]
          ]
        }
      }
    ]
  }