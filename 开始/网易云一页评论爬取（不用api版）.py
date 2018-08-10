import requests
import json


def get_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36",
        "Referer": "https: // music.163.com / song?id = 1297492096"}
    data = {
        "params": "/ikCqD8GzvUt0c2GxliTUKlHWgGnUwsJcWBIcg4noqCXnEXjqaE3nHN39DGclk1MlNKSBFakLC2FpGyIlGH4QsH0+VhxgcD4zdIdsQXr1JiuafhA79XWcOFPPZEJDt2SJrBSlor4sjN4wDK+XqNPrG1dn7x9cXFyTYyCvtTRuKT1uP8e/JdR9D+huA3pA6Af",
        "encSecKey": "7456c7d8dac8c575ce18cc7a631d0be6cd6303538efeefe2a8e5a0b4e7762ca67212e334541f89a4f6e7dd2dd8909da56e077c397a9de994ad886a11debaf6513289e350e1ed7047d55c7e544046b94091b3fe60a9bae76a5b7ce67fa0cddcc22fc5ae9fd87333d290b80b953fab463f5b3c5dd81b72d3d112462214e48074d1"}
    response = requests.post(url, headers=headers, data=data)
    return response


def main():
    # url=input("请输入URL:")
    url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_1297492096?csrf_token="
    html = get_url(url)
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
