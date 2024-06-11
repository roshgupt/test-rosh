def get_login_card():
      card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
          "type": "AdaptiveCard",
          "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
          "version": "1.3",
          "body": [
            {
              "type": "Container",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "Login Late/Logout Early",
                  "size": "Large",
                  "color": "Accent",
                  "weight": "Bolder",
                  "wrap": True
                },
                {
                  "type": "Input.ChoiceSet",
                  "choices": [
                    {
                      "title": "Login Late",
                      "value": "login"
                    },
                    {
                      "title": "Logout Early",
                      "value": "logout"
                    }
                  ],
                  "placeholder": "Login Late / Logout Early",
                  "label": "Select:",
                  "isRequired": True,
                  "style": "expanded",
                  "id": "login_ops",
                  "errorMessage": "Option Missing!!!"
                },
                {
                  "type": "Input.Time",
                  "label": "Enter Time",
                  "isRequired": True,
                  "min": "11:30",
                  "max": "17:30",
                  "errorMessage": "Time Missing / Not in range 11:30-17:30",
                  "id": "time"
                },
                {
                  "type": "Input.Text",
                  "placeholder": "Placeholder text",
                  "label": "Reason:",
                  "isRequired": True,
                  "errorMessage": "Reason Missing!!!",
                  "id": "reason"
                },
                {
                  "type": "ColumnSet",
                  "columns": [
                    {
                      "type": "Column",
                      "width": 50,
                      "items": [
                        {
                          "type": "ActionSet",
                          "actions": [
                            {
                              "type": "Action.Submit",
                              "title": "Submit",
                              "associatedInputs": "auto",
                              "style": "positive",
                              "data": {
                                "callback_keyword": "login_callback"
                              }
                            }
                          ]
                        }
                      ],
                    },
                    {
                      "type": "Column",
                      "spacing":"extraLarge",
                      "width": 50,
                      "items": [
                        {
                          "type": "ActionSet",
                          "actions": [
                            {
                              "type": "Action.Submit",
                              "title": "Exit",
                              "associatedInputs": "None",
                              "style": "destructive",
                              "data": {
                                "callback_keyword": "mistake_callback"
                              }
                            }
                          ],
                          "horizontalAlignment": "right"
                        }
                      ]
                    }
                  ],
                  "spacing": "Medium",
                  "separator": True
                }
              ]
            }
          ]
        }
      }
      return card


class login_late_logout_early(Command):
    def __init__(self):
        super().__init__(
            command_keyword="login"
        )
    
    def execute(self, message, attachment_actions):
        
        response = Response()
        response.text = ' '
        response.attachments = get_login_card()
        return response

class login_callback(Command):
    def __init__(self):
        super().__init__(
            command_keyword="login_callback",
            delete_previous_message=True
        )

    def execute(self, message, attachment_actions):
        login_ops, le_time, reason = attachment_actions['inputs']['login_ops'], attachment_actions['inputs']['time'], attachment_actions['inputs']['reason']
        cecid = get_user_cecid_from_payload(attachment_actions['personId'])
        response = Response()
        response.text = f"{cecid} {login_ops} at {le_time} -> {reason}"
        return response