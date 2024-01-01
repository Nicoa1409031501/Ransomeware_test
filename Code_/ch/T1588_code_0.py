# 方法一
import requests
from bs4 import BeautifulSoup

def obtain_capabilities():
    capabilities = []

    # 爬取T1588的資訊
    url = "https://attack.mitre.org/techniques/T1588/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    technique_description = soup.select_one("#v-defense div div:nth-child(2) div div:nth-child(2)").text.strip()
    capability_list = technique_description.split("，")[:-1]

    # 取得每種capability的描述
    for capability in capability_list:
        capability_name = capability.split("是")[1].strip()
        capabilities.append(capability_name)

    return capabilities

# 呼叫函式
obtain_capabilities()


# 方法二
import requests
from bs4 import BeautifulSoup

def obtain_capabilities():
    capabilities = []

    # 爬取T1588的資訊
    url = "https://attack.mitre.org/techniques/T1588/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    technique_description = soup.find("div", class_="row technique-description").find_all("p")[1].text.strip()
    capability_list = technique_description.split("，")[:-1]

    # 取得每種capability的描述
    for capability in capability_list:
        capability_name = capability.split("是")[1].strip()
        capabilities.append(capability_name)

    return capabilities

# 呼叫函式
obtain_capabilities()


# 方法三
import requests
from bs4 import BeautifulSoup

def obtain_capabilities():
    capabilities = []

    # 爬取T1588的資訊
    url = "https://attack.mitre.org/techniques/T1588/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    technique_description = soup.select("#v-defense > div.expanded-row.expanded-5.row div.row div div div.content:nth-child(2) div p")
    technique_description = "，".join([desc.text.strip() for desc in technique_description])
    capability_list = technique_description.split("，")[:-1]

    # 取得每種capability的描述
    for capability in capability_list:
        capability_name = capability.split("是")[1].strip()
        capabilities.append(capability_name)

    return capabilities

# 呼叫函式
obtain_capabilities()