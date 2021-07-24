# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import requests

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):

        """
        call api
        """
        input_data = {}
        # print(turn_context.activity.conversation.id)
        input_data['message'] = turn_context.activity.text
        input_data['state_tracker_id'] = str(turn_context.activity.conversation.id)

        try:

            converse_api_url = 'https://api-bkbot.herokuapp.com/api/convers-manager'
            response_object = requests.post(url=converse_api_url, json=input_data)
            response_object_json = response_object.json()
            
            if response_object_json['message']:
                list_mess_response = [item.replace('\n', r'').replace(r'"',r'') for item in response_object_json['message']]

                first_mess_response = list_mess_response[0]
                await turn_context.send_activity(first_mess_response)
        except:
            await turn_context.send_activity("Xin lỗi mình không hiểu ý bạn lắm!")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Xin chào, mình là trợ lý ảo có thể cung cấp cho bạn các thông tin liên quan đến tuyển sinh đại học như: điểm chuẩn, mã ngành, cách thức đăng ký,... cũng như cơ hội nghề nghiệp về các ngành/ nhóm ngành đang được đào tạo tại trường Đại học Bách Khoa Tp.HCM. Vậy mình có thể giúp được gì cho bạn ?")
