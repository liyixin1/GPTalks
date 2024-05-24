import json

import nls
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

import config


class SpeechRecognition:
    def __init__(self, tid):
        # 设置HTTP头部
        self.client = AcsClient(
            config.aliyun.access_key_id,
            config.aliyun.access_key_secret,
            "cn-shanghai"
        )
        # 创建request，并设置参数。
        self.request = CommonRequest()
        self.request.set_method('POST')
        self.request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
        self.request.set_version('2019-02-28')
        self.request.set_action_name('CreateToken')

        self.url = 'wss://nls-gateway-cn-shanghai.aliyuncs.com/ws/v1'
        self.__id = tid
        self.sr = None  # 用于在__test_run中初始化NlsSpeechTranscriber的实例
        self.speech_text_end = ""
        self.speech_text_chg = ""

    def get_token(self):
        response = self.client.do_action_with_exception(self.request)
        # 第一步：解码bytes对象成字符串
        str_obj = response.decode('utf-8')
        # 第二步：使用json模块解析字符串成字典
        dict_obj = json.loads(str_obj)
        print(dict_obj['Token'])
        return dict_obj['Token']['Id']

    def start(self):
        self.run()

    def send_audio_data(self, data):
        # 检查是否sr实例已经创建
        if self.sr:
            self.sr.send_audio(bytes(data))
        else:
            print("尚未创建NlsSpeechTranscriber对象")

    def on_sentence_begin(self, message, *args):
        print("test_on_sentence_begin:{}".format(message))

    def on_sentence_end(self, message, *args):
        print("test_on_sentence_end:{}".format(message))
        message_json = json.loads(message)
        self.speech_text_end = (message_json['payload']['result'])
        # print(message_json['payload']['result'])

    def on_start(self, message, *args):
        print("test_on_start:{}".format(message))

    def on_error(self, message, *args):
        print("on_error args=>{}".format(args))

    def on_close(self, *args):
        print("on_close: args=>{}".format(args))

    def on_result_chg(self, message, *args):
        print("test_on_chg:{}".format(message))
        message_json = json.loads(message)
        self.speech_text_chg = message_json['payload']['result']
        print(message_json['payload']['result'])

    def on_completed(self, message, *args):
        print("on_completed:args=>{} message=>{}".format(args, message))

    def run(self):
        print("thread:{} start..".format(self.__id))
        self.sr = nls.NlsSpeechTranscriber(
            url=self.url,
            token=self.get_token(),
            appkey="FbTDstRfLf1b1HMx",
            on_sentence_begin=self.on_sentence_begin,
            on_sentence_end=self.on_sentence_end,
            on_start=self.on_start,
            on_result_changed=self.on_result_chg,
            on_completed=self.on_completed,
            on_error=self.on_error,
            on_close=self.on_close,
            callback_args=[self.__id]
        )

        print("{}: session start".format(self.__id))
        self.sr.start(aformat="pcm",
                      enable_intermediate_result=True,
                      enable_punctuation_prediction=True,
                      enable_inverse_text_normalization=True)


nls.enableTrace(True)
