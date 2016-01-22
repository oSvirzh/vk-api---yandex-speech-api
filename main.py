#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import vk
import os
import logging
import asyncio
import uuid
import sys

from ysc.asr import asr
from ysc.audio import record
from time import sleep

os.environ["OLEG_VK_TOKEN"]='asdasd'

def getUserId(link):
    id = link
    if 'vk.com/' in link:
        id = link.split('/')[-1]
    if not id.replace('id', '').isdigit():
        id = vkapi.utils.resolveScreenName(screen_name=id)['object_id']
    else:
        id = id.replace('id', '')
    return int(id)
	
def speechGet(topic):
    params = {}		
    params["uuid"] = uuid.uuid4().hex
    params["topic"] = topic
    params["key"] = 'ad58fe15-7d80-4f36-9e53-0db6ea0ab082'	
    inputstream=record()
    loop = asyncio.get_event_loop()
    res=loop.run_until_complete(asr(loop, inputstream, params))
    loop.close()
    return res  
    
session = vk.Session(access_token=os.environ["OLEG_VK_TOKEN"])
vkapi = vk.API(session, v='5.44', lang='ru')
        
if __name__ == '__main__':
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s: %(levelname)s: %(name)s: %(message)s")


text=speechGet('notes')
	
i=0
for child in text:
    i = i + 1
    print("{}: {}\n".format(i, child.text))
	


#vkapi.messages.send(user_id=user_to_send, message=text)
