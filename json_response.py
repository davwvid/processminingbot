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
