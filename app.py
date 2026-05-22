# main.py（Vercel 要求文件名必须是 main.py）
from openai import OpenAI
import gradio as gr
import os

# 配置
MANUAL_CONTEXT =“根据Atwood房车维修手册、Fogatti热水器维修手册：E1是温控器故障，打不着火检查点火/电磁阀/燃气，漏水检查内胆和接头”
FIX_DICT = {
    "打不着火":"检查点火、电磁阀、燃气压力",
    "E1":"温控器故障，需更换",
    "漏水":"检查进出水管接头、内胆"
}
免费次数 =3
abc = 0

客户端 =OpenAI(
    api_key="ark-b495e756-876a-492c-9ddc-864cdee72534-903b2",
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)

# 拆分函数
def search_manual(question):
    for k,v in FIX_DICT.items():
        if k in question:
            return v
    return None

def call_deepseek(question, context):
    prompt = f"参考以下资料回答问题。资料：{context}。问题:{question}。必须引用手册字样。"
    try:
        res = client.chat.completions.create(
            model="doubao-seed-character-251128",
            messages=[{"role":"user","content":prompt}]
        )
        返回res.
    except:
        return "AI调用出错"

def format_answer(raw):
    返回原始

# 读取手册
 get_pdf_info():
    如果os.path.exists():
文件 =[f对于finos.listdir("手册") 如果f.endswith(".pdf")]
        返回 len(files)}个 " + " "
    返回 "无手册"

# 网页主函数
 web_interface(q):
    全局abc
    abc +=1
    pdf_info = get_pdf_info()
    如果abc>3:
        返回 “免费次数用完，请付款9.9元解锁”, pdf_info
    ans = search_manual(q)
    如果 未答案：
        ans = call_deepseek(q, MANUAL_CONTEXT)
    返回 格式化答案

# 生成网页
demo = gr.界面(
fn=web界面,
输入=“文本”,
输出=["文本","文本"],
title=“赵亮房车热水器维修助手”
)

# Vercel 必须加这一段
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
