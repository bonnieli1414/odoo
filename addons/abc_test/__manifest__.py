# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# 參考文件https://github.com/iTranslateX/odoo-cookbook/blob/main/3.md#%E8%BF%90%E8%A1%8C%E5%8E%9F%E7%90%86-1
{
    'name': 'abc_test',
    'summary': '這是一個單行描述的副標題',
    'description': """
    這是一個以普通文本或重構文本（RST）格式編寫的長描述。 通常放在三個引號中，Python中使用三個引號來界定多行文本。
    """,
    'author': '版權作者姓名。本處為一個字串，但可以是逗號分隔的一系列姓名',
    # 標示作者授權模組進行分發的證書。
    # AGPL-3和LGPL-3都是知名的開源選項。通過Odoo應用商店銷售的自有模塊應當使用Odoo自家的證書OPL-1。
    "license": "AGPL-3",
    # 瞭解模組更多資訊的 URL
    # 'website': "http://www.yourcompany.com",
    # 設置模組分類。
    # 清單詳見https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # 如果外掛程式未設置分類，預設使用Uncategorized。 
    # 'category': 'Uncategorized',
    'category': 'Services/Library',
    # 模組的版本號。建議在模組版本號前加上 Odoo 版本，這樣有助於確定模組所針對的Odoo版本。例如，針對Odoo 17.0的1.0.0模組可使用版本號17.0.1.0.0。
    'version': '17.0.1.0.0',
    # 外掛程式模組的依賴清單。安裝模組時會觸發對這些模組的安裝。如果模組沒有具體的依賴，通常會讓其依賴base模組，但這並非強制要求。
    'depends':['base'],
    'application': True,
    'data': [
        'views/views.xml',
    ],
    # 開發環境：開發人員在開發過程中可以使用範例數據進行調試和測試。
    # 測試環境：測試人員可以使用範例數據來編寫測試用例並驗證模組功能。
    # 演示環境：銷售團隊或顧問在向客戶演示模組功能時，可以使用範例數據進行演示。
    'demo': ['demo.xml'],
    
    # 一個布爾型標記，代表模組是否在應用清單中以應用展示。大多數擴展模組是對已有應用添加功能，會將此值設置為False。abc_test模組是一個新應用，因為設置為True。
    'application': False,
    
    # 用於膠水模組。膠水模組的安裝在安裝所有依賴時進行一次觸發。例如，它可用於在實例中同時安裝了兩個應用時，自動為其提供橋接的功能。
    # 'auto_install':True
    
    # installable：表明模組是否可安裝。默認值為True，因而無需顯示設置。如果出於某種原因，希望在外掛程式目錄中保留檔，卻禁用模組可以將其設置為False。
    # "installable": False
}