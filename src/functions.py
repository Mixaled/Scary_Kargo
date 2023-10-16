import vk_api
import requests
from vk_api.upload import VkUpload
import random
from cursed_text import messages
import vk_captchasolver as vc
import time

def spam_kargo(chat_id, token, anti_spam):
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    vk_upload = VkUpload(vk_session)
    for i in range(60):
        random_id = random.getrandbits(31)
        pic = f"pics/scary{random.randint(0,10)}.jpg"
        upload_url = vk.photos.getMessagesUploadServer()['upload_url']
        with open(pic, 'rb') as f:
            response = requests.post(upload_url, files={'photo': f}).json()
        photo_info = vk.photos.saveMessagesPhoto(**response)
        attachment_id = f"photo{photo_info[0]['owner_id']}_{photo_info[0]['id']}"
        try:
            vk.messages.send(chat_id=chat_id, message=messages[random.randint(0, 10)], random_id=random_id, attachment=attachment_id)
        except vk_api.Captcha as captcha:
            print("Captcha needed. Solving...")
            sid = captcha.sid
            print(f"Captcha data {sid}")
            solved_captcha_code = vc.solve(sid=sid, s=1)
            print(f"Solved code {solved_captcha_code}")
            try:
                vk.messages.send(chat_id=chat_id, message=messages[random.randint(0, 10)], random_id=random_id,
                                 attachment=attachment_id, captcha_sid=sid, captcha_key=solved_captcha_code)
            except vk_api.exceptions.ApiError as error:
                if error.code == 9:
                    print(f"Flood control error encountered. Retrying in 5 seconds...")
                    time.sleep(5)
                    continue
                else:
                    raise error # raise other errors
        except vk_api.exceptions.ApiError as error:
            if error.code == 9:
                print(f"Flood control error encountered. Retrying in 5 seconds...")
                time.sleep(5)
                continue
            else:
                raise error  # raise other errors
        print(f"Message sent with attachment: {attachment_id}")


def spam_kargo2(user_id, token):
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    vk_upload = VkUpload(vk_session)
    for i in range(60):
         random_id = random.getrandbits(31)
         pic = f"pics/scary{random.randint(0,10)}.jpg"
         upload_url = vk.photos.getMessagesUploadServer()['upload_url']
         with open(pic, 'rb') as f:
             response = requests.post(upload_url, files={'photo': f}).json()
         photo_info = vk.photos.saveMessagesPhoto(**response)
         attachment_id = f"photo{photo_info[0]['owner_id']}_{photo_info[0]['id']}"
         try:
            vk.messages.send(user_id=user_id, message=messages[random.randint(0,10)], random_id=random_id, attachment=attachment_id)
         except vk_api.Captcha as captcha:
             print("Captcha needed. Solving...")
             sid = captcha.sid
             print(f"Captcha data {sid}")
             solved_captcha_code = vc.solve(sid=sid, s=1)
             print(f"Solved code {solved_captcha_code}")
             try:
                vk.messages.send(user_id=user_id, message=messages[random.randint(0, 10)], random_id=random_id,
                                 attachment=attachment_id, captcha_sid=sid, captcha_key=solved_captcha_code)
             except vk_api.exceptions.ApiError as error:
                if error.code == 9:
                    print(f"Flood control error encountered. Retrying in 5 seconds...")
                    time.sleep(5)
                    continue
                else:
                    raise error # raise other errors
         print(f"Message sent with attachment: {attachment_id}")