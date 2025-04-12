import requests
import json

BASE_URL = "http://127.0.0.1:8001"  # 替换为您的实际服务器地址和端口


def get_product_details(product_identifier, query_type="name", user_needs=None):
    """
    获取产品信息接口调用工具

    接口路径: GET /products/{product_identifier}
    功能描述: 根据产品名称、型号或ID查询产品详细信息，并可根据用户需求获取产品推荐。

    Args:
        product_identifier (str): 产品的名称、型号或ID。
        query_type (str, optional): 查询类型，可选值为 "name", "model", "id"，默认为 "name"。
        user_needs (str, optional): 用户对产品的需求或偏好，用于获取推荐，默认为 None。

    Returns:
        dict or None: 包含产品信息的字典，如果请求失败则返回 None。
    """
    url = f"{BASE_URL}/products/{product_identifier}"
    params = {"query_type": query_type, "user_needs": user_needs}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 如果响应状态码不是 200 OK，则抛出 HTTPError 异常
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"获取产品信息失败: {e}")
        return None


def get_current_promotions():
    """
    获取当前促销活动接口调用工具

    接口路径: GET /promotions
    功能描述: 获取当前正在进行的促销活动列表。

    Returns:
        dict or None: 包含促销活动列表的字典，如果请求失败则返回 None。
    """
    url = f"{BASE_URL}/promotions"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"获取促销活动失败: {e}")
        return None


def track_order(order_number):
    """
    追踪订单状态接口调用工具

    接口路径: GET /orders/{order_number}/status
    功能描述: 根据订单号查询订单的当前状态和物流信息。

    Args:
        order_number (str): 要查询的订单号。

    Returns:
        dict or None: 包含订单状态信息的字典，如果请求失败则返回 None。
    """
    url = f"{BASE_URL}/orders/{order_number}/status"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"追踪订单失败: {e}")
        return None


def create_return_exchange(order_item_id, reason, request_type):
    """
    提交退换货申请接口调用工具

    接口路径: POST /returns_exchanges
    功能描述: 提交退货或换货的申请。

    Args:
        order_item_id (int): 需要退换货的订单项ID。
        reason (str): 退换货的原因。
        request_type (str): 请求类型，可选值为 "return" 或 "exchange"。

    Returns:
        dict or None: 包含退换货申请结果的字典，如果请求失败则返回 None。
    """
    url = f"{BASE_URL}/returns_exchanges"
    payload = {"order_item_id": order_item_id, "reason": reason, "request_type": request_type}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"提交退换货申请失败: {e}")
        return None


def submit_feedback(channel, feedback_text, user_identifier=None):
    """
    提交投诉与建议接口调用工具

    接口路径: POST /feedback
    功能描述: 提交用户对产品或服务的投诉或建议。

    Args:
        channel (str): 提交反馈的渠道，例如 "chat", "email"。
        feedback_text (str): 反馈内容。
        user_identifier (str, optional): 用户在特定渠道的标识符，默认为 None。

    Returns:
        dict or None: 包含反馈提交结果的字典，如果请求失败则返回 None。
    """
    url = f"{BASE_URL}/feedback"
    payload = {"channel": channel, "feedback_text": feedback_text, "user_identifier": user_identifier}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"提交反馈失败: {e}")
        return None


def request_human_support(channel, reason=None, user_identifier=None):
    """
    请求人工服务接口调用工具

    接口路径: POST /request_human_support
    功能描述: 请求转接人工客服。

    Args:
        channel (str): 请求人工服务的渠道，例如 "chat", "email"。
        reason (str, optional): 请求人工服务的原因，默认为 None。
        user_identifier (str, optional): 用户在特定渠道的标识符，默认为 None。

    Returns:
        dict or None: 包含请求人工服务结果的字典，如果请求失败则返回 None。
    """
    url = f"{BASE_URL}/request_human_support"
    payload = {"channel": channel, "reason": reason, "user_identifier": user_identifier}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"请求人工服务失败: {e}")
        return None


def main():
    # 示例调用 - 获取产品 "经典T恤" 的详细信息
    product_info = get_product_details("经典T恤")
    if product_info:
        print("产品信息 (获取 '经典T恤'):", json.dumps(product_info, indent=2, ensure_ascii=False))

    # 示例调用 - 获取名称包含 "牛仔裤" 的产品并推荐修身的
    recommended_products = get_product_details("牛仔裤", query_type="name", user_needs="修身的")
    if recommended_products and recommended_products.get("recommendations"):
        print("推荐产品 (名称包含 '牛仔裤'，需求 '修身的'):", json.dumps(recommended_products["recommendations"], indent=2, ensure_ascii=False))

    # 示例调用 - 获取当前促销活动
    promotions = get_current_promotions()
    if promotions:
        print("当前促销活动:", json.dumps(promotions, indent=2, ensure_ascii=False))

    # 示例调用 - 追踪订单状态 (订单号 '20250410001')
    order_status = track_order("20250410001")
    if order_status:
        print("订单状态 (订单号 '20250410001'):", json.dumps(order_status, indent=2, ensure_ascii=False))

    # 示例调用 - 为订单项ID 4 申请退货，原因是 "尺码不合适"
    return_result = create_return_exchange(4, "尺码不合适", "return")
    if return_result:
        print("退换货申请结果:", json.dumps(return_result, indent=2, ensure_ascii=False))

    # 示例调用 - 通过 "chat" 渠道提交了一条投诉
    feedback_result = submit_feedback("chat", "我对你们的服务很不满意！")
    if feedback_result:
        print("提交反馈结果:", json.dumps(feedback_result, indent=2, ensure_ascii=False))

    # 示例调用 - 通过 "chat" 渠道请求人工服务
    support_result = request_human_support("chat")
    if support_result:
        print("请求人工服务结果:", json.dumps(support_result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
