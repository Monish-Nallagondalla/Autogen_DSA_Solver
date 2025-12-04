import streamlit as st
import asyncio
from main import get_team_and_docker,run_team
from config.docker_utils import get_docker_executor, start_docker_executor, stop_docker_executor
from config.model_client import get_model_client
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

st.title("DSA Solver")
st.write("This is a simple DSA solver application.")

task = st.text_input("Enter your DSA Question here",value='Can you give me a solution to add 2 numbers?')

async def run(team, task, docker):
    try:
        await start_docker_executor(docker)
        async for message in team.run_stream(task = task):
            print('='*50)
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source}: {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:=f'Task Result: {message.stop_reason}')
                yield msg

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await stop_docker_executor(docker)
