#废了，没有正确的data
import requests
import json


def get_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36",
        "Referer": "https: // music.163.com / song?id = 513360721"}
    data = {
        "params": "7Nc6CR0/Jq1kCZ/QGvleW9YSJTFmnIDveB9Ukii3OXHz0qH9BAQIjtMaUkzQ/J8hUmGO5YFUjwaXrzFc4WwQittZgteYHCRoMiPPoJD9j3U4jxlZmvFUyrGDRqxuV35O+0fz4HK+H8XOqsrA4RAw7fAsC3lkmABeHl1ALPEGIikXF6kYbFVJCFzYujPMt43U",
        "encSecKey": "cadf5642760f3d2bbb93c35eedeaafad91e509e508f800b17c34cae0af1d0e5c5fedd181c70fb496537853ef8c9273d2d271a4a2d3ea3a47e8d80d7dc9bd5399966a89bc35ce165557bac5bd57fee94df17c678ec16dee07965f464272db62979199c80dcbf4097ef9c5146256c3a3fc1a7d25f2a2018f0897d5f1deff212290"}
    response = requests.post(url, headers=headers, data=data)
    return response


def main():
    # url=input("请输入URL:")
    url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_513360721?csrf_token="
    html = get_url(url)
    print(html)
    comment_json=json.loads(html.text)
    # print(html.text)
    # print(comment_json)
    # with open("comment.txt","w",encoding="utf-8") as f:
    #     f.write(comment_json["comments"][0]["user"]["nickname"])
    with open('网易云评论.txt','w',encoding='utf-8') as file:
        for each in comment_json["comments"]:
            file.write(each["user"]["nickname"]+":\n\n")
            file.write(each["content"]+'\n')
            file.write('----------------------------\n')


if __name__ == '__main__':
    main()
