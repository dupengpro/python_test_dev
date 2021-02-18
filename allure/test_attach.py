import allure


# 添加文本信息
def test_attach_text():
    allure.attach("文本信息", name="文本信息文件", attachment_type=allure.attachment_type.TEXT)


# 添加 html
def test_attach_html():
    allure.attach("<h3>html</h3>", name="html 文件", attachment_type=allure.attachment_type.HTML)


# 添加图片
def test_attach_picture():
    allure.attach.file("./test.jpg", name="图片文件", attachment_type=allure.attachment_type.JPG)