from poium import Page, PageElement

class BaiduPage(Page):
    # 百度 Page 层，百度页面封装操作到的元素
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")

