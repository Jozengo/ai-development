# Initialize user memory
import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core.memory import ListMemory, MemoryContent, MemoryMimeType
from autogen_ext.models.openai import OpenAIChatCompletionClient

from backends.examples.llms import model_client


async def get_weather(city: str, units: str = "imperial") -> str:
    if units == "imperial":
        return f"The weather in {city} is 73 °F and Sunny."
    elif units == "metric":
        return f"The weather in {city} is 23 °C and Sunny."
    else:
        return f"Sorry, I don't know the weather in {city}."


user_memory = ListMemory()


async def main():
    # Add user preferences to memory
    await user_memory.add(MemoryContent(content="A:支持的支付方式； Q: 支持的支付方式有支付宝，银联，Paypal", mime_type=MemoryMimeType.TEXT))
    await user_memory.add(MemoryContent(content="Meal recipe must be vegan", mime_type=MemoryMimeType.TEXT))

    assistant_agent = AssistantAgent(
        name="assistant_agent",
        model_client=model_client,
        tools=[get_weather],
        memory=[user_memory],
    )

    # Run the agent with a task.
    stream = assistant_agent.run_stream(task="支持微信支付吗?")
    await Console(stream)


asyncio.run(main())
