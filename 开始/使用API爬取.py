import requests
import json
import datetime


def change_datetime(_value):
    time = datetime.datetime.fromtimestamp(_value / 1000)
    return time.strftime('%Y-%m-%d %H:%M:%S')


def comment_get(id, nickname):
    print("开始爬取")
    base_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_"
    offset = 0
    total = json.loads(requests.get(url=base_url + id,
                                    headers={
                                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0"}
                                    ).text)['total']
    with open(str(id) + '的评论.txt', 'a', encoding='utf-8') as file:
        while total + 100 > offset:
            response = requests.get(url=base_url + id + "?limit=100&offset=" + str(offset),
                                    headers={
                                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0"}
                                    )
            comment_json = json.loads(response.text)
            for each in comment_json["comments"]:
                # if(each["user"]["nickname"]==nickname):
                file.write(each["user"]["nickname"] + ":\n\n")
                file.write(each["content"] + '----------' + str(change_datetime(each["time"])) + '\n')
                file.write('----------------------------\n')
            # else:
            #     continue
            print("已爬取{0}条评论".format(offset))
            offset = offset + 100
    print("下载完毕")


def main():
    id = input("请输入歌曲ID:")
    nickname = input("请输入你要查询的用户名：")
    comment_get(id, nickname)


if __name__ == '__main__':
    main()
