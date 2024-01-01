from pywinauto import Application

def modify_office_addins():
    app = Application().start("C:\path\to\office_application.exe")
    window = app.window(title="Microsoft Office Window")
    # 切換到設定頁面
    window[u'工具'].__getattribute__(u'選項(&T)').invoke()
    window[u'選項']['設定'].__getattribute__(u'增益集和外掛程式(&P)...').invoke()
    
    # 在增益集和外掛程式管理員中找到對應的增益集和外掛程式，修改設定並保存
    addin = window[u'增益集和外掛程式管理員'].get_item(u'Add-in Name')
    addin.click_input()
    enable_checkbox = window[u'增益集和外掛程式管理員'][u'啟用']  # 根據介面中的元素名稱修改
    enable_checkbox.set_focus()
    enable_checkbox.toggle_state()
    
    # 確認和保存設定
    window[u'OK'].invoke()
    app.window(title_re=".*-.*").close()