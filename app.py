from openai import OpenAI
导入gradio作为gr
导入os

MANUAL_CONTEXT =“根据Atwood房车维修手册、Fogatti热水器维修手册：E1是温控器故障，打不着火检查点火/电磁阀/燃气，漏水检查内胆和接头”
FIX_DICT = {
    "打不着火":"检查点火、电磁阀、燃气压力",
    "E1":"温控器故障，需更换",
    "漏水":"检查进出水管接头、内胆"
}
FREE_TIMES = 3
abc = 0

# 你的亚马逊联盟短链接
AMAZON_LINK =“https://amzn.to/3RWIAI5”

client = OpenAI(
    api_key="ark-b495e756-876a-492c-9ddc-864cdee72534-903b2",
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)

# ① 查字典
def search_manual(question):
    for k,v in FIX_DICT.items():
        if k in question:
            return v
    返回 无

# ② 调用AI
 call_deepseek(问题，上下文):
    prompt = f"参考：{context}，问题：{question}，必须引用手册字样"
    尝试:
        res = client.chat.completions.create(
            model="doubao-seed-character-251128",
            messages=[{"role":"user","content":prompt}]
        )
        return res.choices[0].message.content
       except:
        返回 “AI调用出错”

# ③ 格式化回答 + 挂上亚马逊联盟链接
def format_answer(raw):
    return f"{raw}\n\n👉 购买配件：<a href='{AMAZON_LINK}' target='_blank'>RV热水器点火器（亚马逊正品）</a>"

# 读取手册
def get_pdf_info():
    if os.path.exists("manuals"):
文件 =[fforinos.listdir("手册")如果f.以".pdf"结尾]
        返回 len(files)}个 " + " "
    return "无手册"

# 主交互
def web_interface(q):
    global abc
    abc +=1
    pdf_info = get_pdf_info()
    if abc>3:
        返回 “免费次数用完，请付款9.9元解锁”
    ans = search_manual(q)
    if not ans:
        ans = call_deepseek(q, MANUAL_CONTEXT)
    返回 格式化答案(答案), pdf_info

demo = gr.Interface(
    fn=web_interface,
输入=“文本”,
输出=["文本","文本"],
    title="房车热水器维修助手"
)

如果__name__ =="__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT",7860)))
