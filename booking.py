# -*- coding:utf-8 -*-
from time import sleep
from bs4 import BeautifulSoup
"""
def login(session, base_url, username, password):
    postData = {
        'username': username,
        'password': password,
        'rememberMe': 'false'
    }
    session.post(base_url, postData)
"""

def booking(session, base_url,ID):
    headers = {
        'Host':'172.18.249.153:6080',
        "Origin":'http://172.18.249.153:6080',
        "Referer": 'http://172.18.249.153:6080/seatSubscribeServer/index.do',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    postData = {
        'userId': '4106',
        'seatSectionId': ID,
        'r':'0.8172563019924376'
    }
    book_data = session.post(base_url, data=postData,headers=headers)
    return book_data.text

def getinfo(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    dicts = soup.find("map")
    trs = dicts.find_all("area")
    i=1
    lists = []
    for tr in trs:
        info = {}
        name = tr.attrs["alt"]
        id = tr.attrs['id']
        info["序号"] = i
        info["座位"] = name
        info["id"] = id
        i = i + 1
        lists.append(info)
    return lists

def mune(date):
    url3east = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.8155444803447855&imageUrl=/images/seatResult/5e8f6722-07a4-43b6-bfea-05220e47f1be' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=62'
    url3west = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.08844843221934706&imageUrl=/images/seatResult/eb833dbb-8526-45f1-a739-4f7f7983cc41' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=63'
    url4east = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.1666412330077942&imageUrl=/images/seatResult/440c6978-95cc-4785-8900-db529f57d836' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=64'
    url4west = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.9316103269779259&imageUrl=/images/seatResult/805eede7-535b-4029-87cd-8fb79a861b3e' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=65'
    url5east = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.8034358995400162&imageUrl=/images/seatResult/3a283fe1-ae63-4c74-b451-5c9cace38f46' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=66'
    url5mid = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.7633520922774231&imageUrl=/images/seatResult/71934688-351a-4660-977d-8a42e2563b07' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=67'
    url5west = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.5842258553794377&imageUrl=/images/seatResult/2051ee9b-61e5-4f76-9b15-322fba9995c5' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=68'
    url6east = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.9023130104776556&imageUrl=/images/seatResult/120785ef-82d4-423a-91d8-ef886d1b1cda' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=69'
    url6west = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.2518309024951757&imageUrl=/images/seatResult/359178c5-3bdb-49de-8112-5374502df900' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=70'
    url7east = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.09738120287771856&imageUrl=/images/seatResult/f2ebd071-3195-4622-aaa9-5e3f3817f6c0' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=71'
    url7west = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.41158631476384966&imageUrl=/images/seatResult/35158d63-557f-421c-94a4-4a9f12159b07' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=72'
    url8east = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.4601234287444893&imageUrl=/images/seatResult/8d6d964a-75c7-486d-b6ae-9b2dce3927ab' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=73'
    url8mid = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.9046385651100175&imageUrl=/images/seatResult/9af655d1-647e-4777-a5d5-d10441d6dba5' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=74'
    url8west = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.7982274150140556&imageUrl=/images/seatResult/bf0201ad-8962-4c7e-94cf-08cdc1d3c5c4' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=75'
    url9east = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.8878320187842057&imageUrl=/images/seatResult/839ead6a-e63b-4db9-bf12-ff5433201da4' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=76'
    url9mid = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.6548179044318811&imageUrl=/images/seatResult/3744f2d6-2862-4abc-8af8-34a538f3128b' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=77'
    url9west = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.5664931577582566&imageUrl=/images/seatResult/50d65f3a-3c48-4e62-937f-580909a0e2f3' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=78'
    url10east = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.3710558413349221&imageUrl=/images/seatResult/82a5fa63-cc0b-413b-a802-aef59a06d3bc' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=60'
    url10west = 'http://172.18.249.153:6080/seatSubscribeServer/seat/intoSeatPage.do?r=0.12820610952269318&imageUrl=/images/seatResult/c83ad992-4b10-44ef-8744-e6212d78f638' + date + '.png&seatAppointmentDate=' + date + '&seatAppointmentHall=61'

    urls = [url3east, url3west, url4east, url4west, url5east, url5mid, url5west, url6east, url6west, url7east,url7west, url8east, url8mid, url8west, url9east, url9mid, url9west, url10east, url10west]
    print("请选择预约书库: ")
    print("1.三楼东书库\n"
          "2.三楼西书库\n"
          "3.四楼东书库\n"
          "4.四楼西书库\n"
          "5.五楼东书库\n"
          "6.五楼中书库\n"
          "7.五楼西书库\n"
          "8.六楼东书库\n"
          "9.六楼西书库\n"
          "10.七楼东书库\n"
          "11.七楼西书库\n"
          "12.八楼东书库\n"
          "13.八楼中书库\n"
          "14.八楼西书库\n"
          "15.九楼东书库\n"
          "16.九楼中书库\n"
          "17.九楼西书库\n"
          "18.十楼东特藏书库\n"
          "19.十楼西报刊阅览室\n")

    choice = input("请选择预约书库: ").strip()

    if (int(choice) < 20 and int(choice) > 0):
        url = urls[int(choice)-1]
    else:
        print("您的输入有误！")
        exit(0)

    infos = getinfo(url)

    for i in infos:
        print(i["序号"],i["座位"])
    num = input("请输入座位序号: ").strip()

    for info in infos:
        if (int(info["序号"]) == int(num)):
            return info
    return info

if __name__ == '__main__':
    import requests
    """
    name = input("请输入学号: ").strip()
    passwd = input("请输入密码: ").strip()
    login(session=requests.session(),
        base_url='http://172.18.249.153:6080/seatSubscribeServer/login',
          username=name,
          password=passwd
          )
    """
    date = input("请输入预约时期: ").strip()
    info = mune(date)
    locateId = info["id"]
    locateName = info["座位"]
    if(locateId == None):
        print("您的选择有误!")
        exit(0)
    book = booking(session=requests.session(),
                 base_url='http://172.18.249.153:6080/seatSubscribeServer/seat/appointmentSeat.do',
                 ID=locateId)
    soup = BeautifulSoup(book,'lxml')
    isSucc = eval(soup.find("p").get_text())['result']
    if(isSucc == 'success'):
        print("你已成功预约" + locateName)
    else:
        print(eval(soup.find("p").get_text())['errorMsg'])
