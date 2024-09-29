import requests
from bs4 import BeautifulSoup

# chapter = 1
with open(f"novel.md", "a+", encoding="utf-8") as file:
    for chapter in range(0,343):
        # 添加headers，模拟浏览器请求
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        # 请求页面
        url = f"https://www.lightnovelworld.co/novel/the-main-heroines-are-trying-to-kill-me-1407/chapter-{chapter}"
        response = requests.get(url, headers=headers)

        # 解析页面内容
        soup = BeautifulSoup(response.content, "html.parser")

        # 获取标题
        title = soup.find("span", class_="chapter-title").text

        # 获取正文
        chapter_container = soup.find("div", id="chapter-container")
        paragraphs = chapter_container.find_all("p")
        content = "\n\n".join([p.text for p in paragraphs])

        # 写入txt文件
        if chapter == 0:
            file.write(f"# {title}\n")
        else:
            file.write(f"\n\n# {title}\n")
        file.write(content)
        # file.write("<div style=\"page-break-after: always;\"></div> ")

        print(f"第{chapter}章已成功保存")
