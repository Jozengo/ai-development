import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import ModelClientStreamingChunkEvent, TextMessage, ToolCallExecutionEvent

from examples.llms import model_client


async def get_weather(city: str) -> str:
    """获取指定城市的天气情况"""
    return f"{city} 天气晴朗，23°"


async def web_search(query: str) -> str:
    """通过网络搜索，获取搜索结果"""
    return f"{query}"


# weather_tool = FunctionTool(get_weather, description="获取指定城市的天气情况")


async def main():
    agent = AssistantAgent(
        name="assistant",
        model_client=model_client,
        reflect_on_tool_use=True,  # 对工具调用结果再次发给大模型进行输出
        system_message="""
        你是一个的专业、友好且高效的虚拟淘宝客服助手，你的名字是小慧。
        你的主要目标是帮助用户解决与淘宝购物相关的问题，提供准确的信息，并提升用户满意度。
        首先识别用户的意图，然后调用相应的工具完成。
        """,
        tools=[get_weather, web_search],
        model_client_stream=True
    )
    # 流失调用
    stream = agent.run_stream(task="今天的股市情况如何？")
    # 分解输出的内容，进行监控分析
    async for msg in stream:
        if isinstance(msg, ToolCallExecutionEvent):
            print("工具执行结果：", msg.content[0].content)
        if isinstance(msg, ModelClientStreamingChunkEvent):
            print(msg.content)
        elif isinstance(msg, TaskResult):
            print(msg.messages[-1].content)
            # 获取token消耗情况
            for message in msg.messages:
                if isinstance(message, TextMessage) and message.source == "assistant":
                    print("send token: ", message.models_usage.prompt_tokens)
                    print("receive token: ", message.models_usage.completion_tokens)

    # 非流式调用
    # result = await agent.run(task="新疆支持货到付款吗？")
    # print(result)


asyncio.run(main())
