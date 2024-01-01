# 安裝套件：pip install pyad

import pyad.adquery
import pyad.aduser

# 方法一：使用pyad套件，修改GPOs

# 定義要修改的GPO的路徑，<DOMAIN>請替換為實際的網域名稱
gpo_path = r"\\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\"

# 修改GPO的設定
# 這裡是一個示範，實際上應根據需要修改對應的GPO設定
def modify_gpo_settings():
    gpo = pyad.adobject.ADObject.from_dn(gpo_path)
    gpo.gpoptions = 1 # 修改GPO設定，這裡將gpoptions改為1
    gpo.update_attribute('gpoptions')

modify_gpo_settings()