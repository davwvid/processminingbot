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
    "richContent": [
      [
        {
          "text": {
            "text": "Please upload your log file"
          }
        },
        {
          "type": "button",
          "icon": {
            "type": "chevron_right",
            "color": "#FF9800"
          },
          "text": "Go to file upload",
          "link": "https://processminingbot.herokuapp.com/upload.html",
          "event": {
            "name": "",
            "languageCode": "",
            "parameters": {}
          }
        }
      ]
    ]
  }