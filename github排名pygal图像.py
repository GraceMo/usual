import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

'''获取数据'''
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # 使用api调用请求数据
r = requests.get(url)
response_dict = r.json()  # 数据1
'''筛选数据'''
repo_dicts = response_dict['items']  # 数据2
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])  # x 姓名
    repo_dict_desc = 'empty' if not repo_dict['description'] else repo_dict['description']
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict_desc,  # 添加工具提示(鼠标指向条形显示的信息)
    }
    plot_dicts.append(plot_dict)
'''数据可视化'''
my_style = LS('#CD661D', base_style=LCS)  # 设置图表样式
# chart = pygal.Bar(style = my_style,x_label_rotation=45,show_legend=False)   # x标签绕x轴旋转45度,隐藏图例
'''设置图表配置文件'''
my_config = pygal.Config()  # 创建一个实例
my_config.x_label_rotation = 45
my_config.show_legend = False  # 隐藏图例
my_config.title_font_size = 24  # 标题字体大小
my_config.label_font_size = 14  # 副标签字体大小
my_config.major_label_font_size = 18  # 主标签
my_config.truncate_label = 10  # 将项目名(副标签)缩短为10个字符
my_config.show_y_guides = False  # 隐藏水平线
my_config.width = 1000  # 标签宽度
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)  # 不需要添加标签,所以为'',
chart.render_to_file('python_r.svg')
