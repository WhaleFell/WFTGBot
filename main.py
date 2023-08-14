# from pyrogram import Client as c

# API_ID = input("\nEnter Your API_ID:\n > ")
# API_HASH = input("\nEnter Your API_HASH:\n > ")

# print("\n\n Enter Phone number when asked.\n\n")

# i = c("wbb", api_id=API_ID, api_hash=API_HASH, in_memory=True)

# with i:
#     ss = i.export_session_string()
#     print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
#     print(f"\n{ss}\n")

import click
import subprocess
from web.mian import server
from app import CONF


@click.group()
def cli():
    pass


@click.command(help="启动机器人")
@click.option('--without-web', is_flag=True, help="不带web后台管理")
def start(without_web):
    if without_web:
        return subprocess.Popen("python -m app", shell=True)
    else:
        subprocess.Popen("python -m app", shell=True)
        server.run(
            host=CONF.Web.host,
            port=CONF.Web.port,
        )


@click.command(help="登录并生成字符串 token")
def token():
    from pyrogram import Client as c
    API_ID = input(
        f"\nEnter Your API_ID:[{CONF.api_id}]\n > ").strip() or CONF.api_id
    API_HASH = input(
        f"\nEnter Your API_HASH[{CONF.api_hash}]:\n > ").strip() or CONF.api_hash

    i = c("tempSession", api_id=API_ID, api_hash=API_HASH, in_memory=True)

    with i:
        ss = i.export_session_string()
        print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
        print(f"\n{ss}\n")


cli.add_command(start)
cli.add_command(token)

if __name__ == "__main__":
    cli()
