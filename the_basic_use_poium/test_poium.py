from poium import Page, PageElement


class SomePage(Page):
    elem_id = PageElement(id_='id')
    elem_name = PageElement(name='name')
    elem_class = PageElement(class_naem='class')
    elem_tag = PageElement(tag='input')
    elem_link_text = PageElement(link_text='this_is_link')
    elem_partial_link_text = PageElement(partial_link_text='is_link')
    elem_xpath = PageElement(xpath='//*[@id="kw"]')
    elem_css = PageElement(id_='id')
    elem_id = PageElement(css='#id')


class BaiduPage(Page):
    search_input = PageElement(id_="kw", timeout=5)
    search_button = PageElement(id_="su", timeout=30)

class LoginPage(Page):
    """
    登录 Page 表
    """
    usernaem = PageElement(css='#loginAccount', describe="用户名")
    password = PageElement(css='loginPwd', describe='密码')



from poium import PageElements

class ResultPage(Page):
    search_result = PageElements(xpath='//div/hs/a')
