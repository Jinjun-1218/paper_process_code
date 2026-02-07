from openai import OpenAI
import os

# ================= 配置区域 =================
# 在此处填入你的 DeepSeek API Key (sk-开头)
DEEPSEEK_API_KEY = "sk-2d46d29e85164996906978c4321daea1"
# ===========================================

# 初始化客户端
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.Deepseek.com"  # DeepSeek 官方接口地址
)

print("📡 正在连接 DeepSeek 服务器查询可用模型...")

try:
    # 获取模型列表
    response = client.models.list()

    print(f"✅ 连接成功！你的账号可以使用以下 {len(response.data)} 个模型：")
    print("-" * 40)

    for model in response.data:
        print(f"🔹 模型 ID: {model.id}")
        # 简单的模型说明
        if "chat" in model.id:
            print(f"   (说明: 这是 DeepSeek V3，最适合处理文本、代码和论文分析，速度快)")
        elif "reasoner" in model.id:
            print(f"   (说明: 这是 DeepSeek R1，推理能力强，适合做数学题，但较慢)")
        print("-" * 40)

except Exception as e:
    print(f"❌ 连接失败，请检查 API Key 是否正确。")
    print(f"报错信息: {e}")