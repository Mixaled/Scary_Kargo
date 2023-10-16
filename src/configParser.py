with open('config.txt', 'r') as file:
    bots = []
    for line in file:
        line = line.strip()
        if line:
            bots.append(line)
print("Bots ready: ", len(bots))
x = input("Target human or chat(H/C)? ")
if x == 'H' or x == 'h':
    while True:
        chat_id = input("Enter chat ID: ")
        try:
            chat_id = int(chat_id)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    for i in range(len(bots)):
        with open(f'bots/main{i}.py', 'w') as file:
            file.write('import sys\n')
            file.write('import vk_api\n')
            file.write('import random\n')
            file.write('import os\n')
            file.write(f'parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))\n')
            file.write('sys.path.append(parent_dir)\n')
            file.write('from functions import spam_kargo, spam_kargo2\n')
            file.write('from cursed_text import messages\n')
            file.write('import vk_captchasolver as vc\n\n')

            file.write(f'token{i} = "{bots[i]}"\n')
            file.write(f'vk_session = vk_api.VkApi(token=token{i})\n')
            file.write('vk = vk_session.get_api()\n')
            file.write(f'chat_id = {chat_id}\n\n')

            file.write(f'spam_kargo2(chat_id, token{i})\n')

    with open('bots/start.sh', 'w') as script:
        script.write('#!/bin/bash\n')
        for i in range(len(bots)):
            script.write(f'/usr/bin/python3 main{i}.py &\n')
    print("Ready")
elif x == 'C' or x == 'c':
    anti_spam = input("Are there any anti-spam systems(Iris, Kay etc.)(Y/n)? ")
    if anti_spam == 'Y' or 'y':
        print("Anti-spam destroyer enabled")
        anti_spam = True
    else:
        print("Anti-spam destroyer disabled")
        anti_spam = False
    link = input("Enter join link: ")
    for i in range(len(bots)):
        with open(f'bots/main{i}.py', 'w') as file:
            file.write('import sys\n')
            file.write('import vk_api\n')
            file.write('import random\n')
            file.write('import os\n')
            file.write(f'parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))\n')
            file.write('sys.path.append(parent_dir)\n')
            file.write('from functions import spam_kargo, spam_kargo2\n')
            file.write('from cursed_text import messages\n')
            file.write('import vk_captchasolver as vc\n\n')

            file.write(f'token{i} = "{bots[i]}"\n')
            file.write(f'vk_session = vk_api.VkApi(token=token{i})\n')
            file.write('vk = vk_session.get_api()\n')
            file.write(f'invite_link = "{link}"\n\n')
            file.write(f'chat_id = vk.messages.joinChatByInviteLink(link=invite_link)["chat_id"]\n')

            file.write(f'spam_kargo(chat_id, token{i}, {anti_spam})\n')
    with open('bots/start.sh', 'w') as script:
        script.write('#!/bin/bash\n')
        for i in range(len(bots)):
            script.write(f'/usr/bin/python3 main{i}.py &\n')
    print("Ready")






