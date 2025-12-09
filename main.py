import asyncio
from team.dsa_solver_team import get_team
from agents.problem_solver_agent import get_problem_solver_expert
from agents.code_executor_agent import get_code_executor_agent
from config.docker_utils import get_docker_executor, start_docker_executor, stop_docker_executor
from config.model_client import get_model_client
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


async def get_team_and_docker():

    docker = get_docker_executor()
    model_client = get_model_client()
    problem_solver_agent = get_problem_solver_expert(model_client)
    code_executor_agent = get_code_executor_agent(docker)

    team = get_team(problem_solver_agent, code_executor_agent)
    return team, docker
