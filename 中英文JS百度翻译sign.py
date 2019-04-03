import js2py
import requests
import re

'''中英文互换
判断输入语言为中/英
翻译
终端交互sys
'''


class Translation():
    def __init__(self, content, headers):
        self.content = content
        self.headers = headers
        self.session = requests.Session()

    def judge(self):
        url_lang = 'https://fanyi.baidu.com/langdetect'
        data = {'query': self.content}
        response = requests.post(url_lang, data=data)
        print(response.text)
        assert response.status_code == 200
        from_ = response.json()['lan']
        return from_

    def translate(self, from_, to_):
        url = 'https://fanyi.baidu.com/v2transapi'
        data = {'query': self.content,
                'from': from_,
                'to': to_,
                'simple_means_flag': '3',
                'sign': self.get_sign(),
                'token': 'af6a73dd6ce133869a0dcefec3b4426d'}
        response = requests.post(url, data=data, headers=self.headers)
        print(response.text)
        result = response.json()['trans_result']['data'][0]['dst']
        return result

    def run(self):
        from_ = self.judge()
        to_ = 'en' if from_ == 'zh' else 'zh'
        translation = self.translate(from_, to_)
        print(translation)

    def get_sign(self):
        session = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
        session.headers = headers
        response = session.get("http://fanyi.baidu.com/")

        gtk = re.findall(";window.gtk = ('.*?');", response.content.decode())[0]
        word = self.content
        context = js2py.EvalJs()
        js = r'''
    function a(r) {
            if (Array.isArray(r)) {
                for (var o = 0, t = Array(r.length); o < r.length; o++)
                    t[o] = r[o];
                return t
            }
            return Array.from(r)
        }
        function n(r, o) {
            for (var t = 0; t < o.length - 2; t += 3) {
                var a = o.charAt(t + 2);
                a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                    a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                    r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
            }
            return r
        }
        function e(r) {
            var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
            if (null === o) {
                var t = r.length;
                t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
            } else {
                for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                    "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                    C !== h - 1 && f.push(o[C]);
                var g = f.length;
                g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
            }
            var u = void 0
                , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
            u = 'null !== i ? i : (i = window[l] || "") || ""';
            for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
                var A = r.charCodeAt(v);
                128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
                    S[c++] = A >> 18 | 240,
                    S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                    S[c++] = A >> 6 & 63 | 128),
                    S[c++] = 63 & A | 128)
            }
            for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
                p += S[b],
                    p = n(p, F);
            return p = n(p, D),
                p ^= s,
            0 > p && (p = (2147483647 & p) + 2147483648),
                p %= 1e6,
            p.toString() + "." + (p ^ m)
        }
    '''
        # js中添加一行gtk
        js = js.replace('\'null !== i ? i : (i = window[l] || "") || ""\'', gtk)
        # 执行js
        context.execute(js)
        # 调用函数得到sign
        sign = context.e(word)
        return sign


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
        'Host': 'fanyi.baidu.com',
        'Origin': 'https://fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'BAIDUID=2375D07CD9605ED866C7A60A38E656BF:FG=1; BIDUPSID=2375D07CD9605ED866C7A60A38E656BF; PSTM=1554020560; H_PS_PSSID=; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1554298807; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1554298807; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_2c2888b2fe22cba4fac6b948cd7e7834=1554298807; Hm_lpvt_2c2888b2fe22cba4fac6b948cd7e7834=1554298807; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D'
    }
    i = 0
    while i < 6:
        content = input('输入要翻译的中文或英文：')
        # content = 'hello'
        trans = Translation(content, headers)
        trans.run()
        i += 1
