from LLM import GLMFlash_LLM

glm_flash_llm = GLMFlash_LLM(api_key="ffaa63c37c79d11634ac106e80164409.dkDfrKthm4hDoEOi")

while True:
    user_input = input("在命令行中提问（输入'1'退出）: ")
    if user_input == "1":
        print("退出程序。")
        break
    else:
        # 调用假设的LLM库的方法
        result = glm_flash_llm._call(prompt=user_input)
        print(result)