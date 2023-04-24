#!/usr/bin/env python
# encoding:utf-8

from loguru import logger


async def send_msg(webhook, message):
    try:
        import requests
    except:
        logger.info("缺少 requests 模块")
        return 2, "缺少 requests 模块"

    res = requests.post(webhook, json={
        "msgtype": "text",
        "text": {
            "content": message
        }
    })

    if res and res.status_code == 200:
        return {"status": 0, "result": "发送企微消息成功"}
    else:
        logger.info("发送失败，错误信息：" + res.text)
        return {"status": 1, "result": "发送失败，错误信息：" + res.text}


if __name__ == '__main__':
    # 导入异步库
    import asyncio

    # 测试函数

    async def test():
        result = await send_msg("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx", "SOAR测试消息")
        print(result)

    # 加入异步队列

    async def main(): await asyncio.gather(test())

    # 启动执行  
    asyncio.run(main())
