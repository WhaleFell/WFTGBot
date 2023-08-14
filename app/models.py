# All custom types in pydantic.BaseModel

from pydantic import BaseModel, Field
from typing import List, Union, Dict, Any
from enum import Enum
import os
from pathlib import Path

ROOTPATH = Path(os.getcwd()).absolute()


class PluginConfig(BaseModel):
    # enable:bool = False
    pass


class KeyMonitorConfig(PluginConfig):
    enable: bool = False
    keywords: List[str] = Field(default_factory=lambda: [
                                "做爱"], description="关键词")
    forword_id: List[Union[str, int]] = Field(
        default_factory=lambda: ["me"], description="转发 ID")


class RenameFileConfig(PluginConfig):
    enable: bool = False  # 是否启用
    # 要上传的文件路径,如果填写文件名默认取程序目录下的文件
    file_path: str = str(Path(ROOTPATH, "file.zip"))
    # 文件描述,{update_time}代替文件更新时间
    file_desc: str = "当前毒包更新时间为: {update_time} 请核对好毒包再推毒！"


class CustomCommandConfig(PluginConfig):
    command: str = "/test"
    text: str = "我"
    desc: str = "是大傻逼"


class WebConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 5000
    # 账号密码
    username: str = "admin"
    password: str = "admin"
    # 随机字符串,不懂就不要动
    SECRET_KEY: str = "swepcwiecwpiencwicn"


class Config(BaseModel):
    name: str = Field(default="TGBot", description="名称")
    isUser: bool = Field(default=False, description="是否为用户")
    session_str: str = ''
    bot_token: str = Field(default="", description="机器人token")
    api_id: int = Field(default=11, description="API ID")
    api_hash: str = Field(default="121", description="API Hash")
    log: str = Field(default="DEBUG", description="日志级别")
    bot_desc: str = "机器人描述发送 /start 的时候"

    # web
    Web: WebConfig = WebConfig()

    # plugins config
    KeyMonitor: KeyMonitorConfig = KeyMonitorConfig()

    RenameFile: RenameFileConfig = RenameFileConfig()

    CustomCommands: List[CustomCommandConfig] = [CustomCommandConfig()]
