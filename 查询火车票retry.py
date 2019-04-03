import requests, json
import pygame, time
from retrying import retry


class Train():
    @retry(stop_max_attempt_number=3)
    def parse(self, url):
        print('1')
        response = requests.get(url, timeout=5)
        return json.loads(response.content.decode())

    def get_result(self, response):
        res = response['data']['result'][0]
        return res

    def sing(self, music):
        pygame.mixer.init()
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        time.sleep(20)

    def run(self, url, music):
        try:
            response = self.parse(url)
        except:
            pass
        result = self.get_result(response)
        ret = result.count('无')
        if ('有' in result) or (ret != 4):
            self.sing(music)


if __name__ == "__main__":
    while True:
        pathM = 'E:\QQ音乐下载\莫文蔚 - 盛夏的果实 (Live).mp3'
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-04-05&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=JYK&purpose_codes=ADULT'
        train = Train()
        train.run(url, pathM)
        time.sleep(10)
