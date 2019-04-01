
import threading


class common_keys:
    #第一次执行时间
    FIRST_TIME=6
    #第二次执行时间
    SECOND_TIME=15
    #redis数据库IP
    REDIS_IP = "10.3.1.99"
    #redis端口
    REDIS_PORT = "6379"
    REDIS_DB = "12"

    URL_NAME = "url"
    DATE_NAME = "date"
    TITLE_NEME = "title"
    TEXT_NEME = "text"
    RETRY_NEME = "retry"
    ERR_NAME = "err"
    TITLE_CUT = "cut"
    NAME = "name"
    RESPONSIBLE = "responsible"
    NEED = "need"

    #文件下载路径
    FILE_PATH = "C:/SpiderResultFile"
    #错误文件路径
    ERR_PATH = "C:/temp/err"
    #写日志的文件路径
    LOGGER_PATH = "C:/temp/loger.log"
    #rowkey路径
    ROWKEY_PATH="C:/SpiderResultFile/kettle.properties"
    ROWKEY_HISTORY_PATH="C:/SpiderResultFile/rowkeyhistory.txt"
    jvmPath = 'C:/File/soft/java/jre1.8/bin/server/jvm.dll'
    JAR_PATH = "D:/classifier.jar"
    THULAC_MODEL_PATH = 'C:/File/soft/python36/Lib/site-packages/thulac/models'


    # FILE_PATH = "/home/ntrl"
    # ERR_PATH = "/home/ntrl/temp/err"
    # LOGGER_PATH = "/home/ntrl/temp/loger.log"
    # ROWKEY_PATH = "/root/.kettle/kettle.properties"
    # ROWKEY_HISTORY_PATH=""
    # jvmPath = '/usr/java/jdk1.7.0_67/jre/lib/amd64/server/libjvm.so'
    # JAR_PATH = "/home/classifier.jar"
    # THULAC_MODEL_PATH = '/opt/toolsrc/py/python3/lib/python3.6/site-packages/thulac/models'


    #无数据时，等待时间
    WAIT_TIME=6

    KEY_NUM=0
    KEY_NUM_NAME="key_num"
    KEY_TIME=None
    KEY_TIME_NAME="key_time"
    FIRST_TIME_S="1"
    SECOND_TIME_S="2"
    KEY_TIME_S_NAME="key_time_s"
    ROWKEY_PROFIX=None
    LAST_ROWKEY_PROFIX=None
    ROWKEY_CONDITION=threading.Condition()

    START_ROW="start_row"
    END_ROW="end_row"
    NOTE="# This file was generated by Pentaho Data Integration version 6.0.1.0-386.\n# \n# Here are a few examples of variables to set: \n#\n# PRODUCTION_SERVER = hercules\n# TEST_SERVER = zeus\n# DEVELOPMENT_SERVER = thor\n#\n# Note: lines like these with a # in front of it are comments\n#\n\n"

    CONF_NAME = "conf.cfg"
    FINISH_LIST_NAME = "finish"
    REDIS_ERR_NAME = "err"

    keyword_arr1 = ["文献", "纸质", "纸本", "数据库", "画册", "杂志", "书刊", "报刊", "期刊", "刊物", "期刊订购", "原版图书", "外文图书", "纸质图书", "图书供货",
                    "图书供应", "图书购置", "图书采购", "图书资料", "图书项目", "古籍", "书籍", "电子图书", "电子资源", "全文", "馆配", "馆藏", "订购", "续订",
                    "增订", "查阅", "订阅", "阅览", "编目", "唱片", "平台采购", "数据编制", "数据处理", "数据加工", "数据获取", "数据资源", "数字资源", "网络资源",
                    "资源建设", "资料购买", "软件租赁", "爱思唯尔", "外版", "使用权", "会议录"]
    keyword_arr2 = ["图书", "书", "刊", "库", "报", "软件", "档案", "资料", "材料", "数据", "合集", "电子", "数字化", "图书馆", "索引"]
    keyword_arr3 = ['发电机', '食堂', '垃圾', '设施', '食品', '街道', '电梯', '车辆', '物业', '办公', '小学', '桌椅', '监狱', '棚户区', '办公室', '空调',
                    '网络', '机关', '幼儿园', '卫生院', '行政', '道路', '粮食', '药品', '物资', '住房', '汽车', '危房', '管理处', '教室', '警察', '公寓',
                    '戒毒所', '教学楼', '办公楼', '房屋', '罪犯', '会议室', '锅炉', '会议', '电脑', '路灯', '用房', '计划', '公务', '显示屏', '公路', '劳务',
                    '职工', '国土', '土地', '派出所', '检察院', '操场', '电视台', '海关', '服务器', '营养', '人力', '机组', '综合楼', '围墙', '管道', '窗帘',
                    '宿舍', '机房', '餐饮', '农产品', '高速公路', '水利', '景区', '垃圾桶', '校舍', '后勤', '货物', '能源', '林业', '食用油', '残疾人',
                    '公园', '电力', '财政', '林场', '保护区', '耕地', '原材料', '服装', '垃圾车', '事务所', '办公区', '自行车', '机动车', '污水', '大厦',
                    '福利院', '灯光', '停车场', '厨房', '电器', '广告', '广场', '风情线', '暖气', '屋面', '法庭', '地块', '食材', '副食品', '鸡蛋', '幼儿',
                    '公厕', '核电站', '废标', '救护车', '厕所', '旱厕', '电视', '宿舍楼', '真空', '妇幼', '管线', '燃气', '制服', '轿厢', '河道', '活动室',
                    '政务', '滨海', '课桌', '纪念馆', '运维', '市民', '终端', '篮球场', '保险', '线路', '看守所', '热水', '蔬菜', '轨道', '风雨', '麦积',
                    '用具', '技师', '耗材', '妇女', '绿化带', '治安', '墙面', '电缆', '楼宇', '人防', '太阳能', '打印机', '变压器', '饮食', '保健院',
                    '卫生间', '大米', '停车库', '车库', '武警', '民权', '泵站', '座椅', '特警', '会议桌', '机场', '音响', '餐厨', '厂区', '垃圾箱', '运动场',
                    '地面', '足球场', '土门', '管网', '乐器', '维修费', '摩托车', '施工图', '配电室', '城棚', '电路', '驾驶员', '技能', '运动会', '水库',
                    '米油', '银行', '交换机', '公用楼', '排椅', '伙食', '办案区', '体育馆', '技工', '巡逻车', '茶几', '工作台', '椅子', '公寓楼', '寄宿制',
                    '公椅', '办公桌', '餐桌椅', '阶梯', '含棚户区', '地下室', '准物业', '垃圾袋', '厂房', '公房', '蒸汽', '窗户', '饮水', '门诊楼', '土建',
                    '摄像机', '服务费', '硬件', '体育场', '敬老院', '一体机', '电房', '音视频', '装置', '钢铁', '劳动力', '电源', '客车', '土炕', '场馆',
                    '专网', '车间', '景观', '监测站', '灯箱', '电视机', '烟草', '粮库', '装备', '储备库', '考场', '核电厂', '病房', '机器人', '显微镜',
                    '试卷', '舞蹈', '地震', '台网', '文苑', '运动队', '建材', '雪车', '调料品', '菜品', '阁屏', '办公点', '米线', '卷粉', '面包', '火腿肠',
                    '保健食品', '化妆品', '边防', '屋顶', '潜水泵', '五金类', '立面', '茶水柜', '看台', '升降式课', '实验台', '教具', '文件柜', '地板',
                    '椅威科M', '办公椅', '楼道', '污泥', '基建', '平房', '渣土', '地铁', '填埋场', '度假区', '收集车', '作业', '吊顶', '车棚', '渗滤液',
                    '国道', '危桥', '灭火器', '新风', '跑道', '垦区', '污水泵', '堤防', '绿地', '发生器', '压缩机', '农田水利', '航道', '楼梯', '外立面',
                    '建筑物', '瓷砖', '亚运会', '墨粉', '后院', '门窗', '遮阳棚', '大门', '监舍门', '苗木', '土建工程', '轮胎', '高架', '塑胶', '未成年人',
                    '工程量', '高温', '门锁', '田径场', '演播室', '通道', '餐厅', '低压柜', '车载', '操作台', '接口', '无线网', '防护林', '松树', '航运',
                    '山桥', '无线电', '处理厂', '处理站', '水泵', '灌区', '化粪池', '玩具', '歌剧', '舞剧院', '备件', '罐头', '显示器', '麦积区', '制证',
                    '照明', '审计区', '工程类', '边坡', '光纤', '金属', '试验机', '子系统', '茶叶', '文物', '会计', '房产', '电网', '核桃冲', '开幕式场馆',
                    '炊具', '特警队', '猪肉', '交通线', '炊事车', '麻醉车', '柜存储车', '台车', '托盘架', '车脚', '筐车', '储物架', '仪器车', '内镜', '笔记本',
                    '工伤', '园艺', '恐龙', '防火墙', '承包E', '气象', '网关', '教育馆', '污染源', '校服', '放射科', '书机', '钢木', '农场', '电容', '佛像',
                    '雕塑', '心电图机', '波分', '微镜', '肠镜', '重症', '超声', '试剂', '光纤环圈', '孔镜', '冶金', '工艺', '核磁共振', '草原', '中心站',
                    '无人机', '登记权籍', '海流', '黄芪党', '参种苗', '花椒', '等离子体', '调音台', '水源', '涵养林', '滩羊', '品系', '影像', '电容器', '图像',
                    '手术床', '恒温', '工具', '红外热', '供销', '借阅机', '茶园', '热力', '原煤', '避孕套', '安检机', '轻工业', '推广站', '有机肥', '科技馆',
                    '主题', '激光器', '舞台', 'X射线', '鼎新楼', '高端', '钢制', '协会', '排球场', '中小学校', '招待所', '实验楼', '游泳馆', '控制国', '军人',
                    '消防站', '果壳箱', '先锋', '站台', '餐具', '扫雪机', '船闸', '电站', '拱墅区', '面粉', '主副食品', '老人', '调味品', '良渚', '餐桌',
                    '员工', '水果', '原料', '新址', '白衣窗帘', '裁判员', '食宿', '农贸市场', '荷花', '服务站', '中队', '共产主义', '山丹', '主席台', '桌田丰',
                    '体操', '代表', '财政所', '教舍', '水权', '福民', '政务市民', '妇产科', '目标', '商格式', '床铺', '桌单', '沙发', '楼人', '位置', '桌人',
                    '会议椅', '椅条桌', '海霞', '轮椅类', '闲林', '木质品', '正宇', '剧场', '古浪', '床带', '垫子', '仲裁院', '仲裁椅', '架子', '床储物',
                    '演讲桌', '一体式', '柜椅', '精神', '清泉', '按摩椅', '电脑椅', '田丰Y', '休闲椅', '椅椅套', '藏床', '手椅', '电教室', '护椅', '幼儿课',
                    '二通道', '垃圾堆场', '辖区', '电动车', '砂资源', '槐王', '外包政府', '贵港', '大件', '清运费', '液处理站', '土工', '排水片', '大海',
                    '环卫处', '五星', '班级', '人造台', '面门', '建构室', '梅花碑', '维码', '烟气', '监督性', '废弃物', '环评', '支吊架', '双色桶', '彩钢板',
                    '自卸车', '行政楼', '床用品', '运输车', '压缩箱', '钩臂箱', '天涯区', '土场', '学具', '藤桥', '南田', '水蛟', '收集箱', '微光光', '处理器',
                    '水域', '塑料', '干粉', '逸夫楼', '中心校', '护坡', '双语', '锅炉炉', '检察室', '投影机', '白板', '围栏', '水管网', '人行道', '砼花砖',
                    '旧址管网', '层流', '维修点', '足球', '工资', '活水', '工程泵', '防洪工程', '山水人', '核西物院', '驾校', '岗位', '构筑物', '固体', '废物',
                    '转形站', '路径', '核查类', '电动机', '人脸', '白水', '信用社', '体校', '手球场', '沂沭', '花港', '二环路', '墙体', '崆峒区', '楼水',
                    '装饰', '大城砖', '柴油机', '水厕', '业务楼', '窗纱', '公益性', '展柜', '梯级', '小剧院', '主管道', '钣金', '下水', '将军', '保障性',
                    '道闸', '旅游节', '门厅', '文化墙', '药具', '水暖', '楼顶', '经学院', '党群', '园屋面', '债券', '火门', '事事', '工业区', '牌面',
                    '抢救性', '水土', '层面', '药房', '公卫科', '硒鼓', '服务区', '庆寿堂', '裙楼', '遮阳板', '渠道', '传染病', '法制', '畜牧', '船舶',
                    '干渠', '用车', '植被保护站', '隆务', '电讯楼', '水房', '治沙站', '演播厅', '江堤', '堤塘', '文集', '生态林', '河堤', '宿管', '文科',
                    '光缆沟', '气象站', '秋石', '高架户', '马洼', '水位', '全民', '贤珺宇', '人影', '门洞', '门房', '休屋面', '院楼', '会徽', '楼屋面',
                    '公车', '大滩', '航区', '水电站', '空战', '纪念亭', '渠市', '外科楼', '电控', '监察室', '办案点', '改造箱', '国医馆', '师山洪', '快艇',
                    '趸船', '口A', '过程', '架空层', '卷烟厂', '岩墙', '俞章', '民安视频', '古景区', '潜污泵', '工程路', '案件', '舆情', '海警', '通小站',
                    '实木', '服务点', '亭棚', '院址', '民工程', '辅具', '器具', '闸门井', '阀门', '控制柜', '大道', '彩虹', '越城区', '防撞柱', '运政网',
                    '单元E', '信息网', '液晶', '居住点', '大路', '王棚', '计算机', '计算机房', '空地', '原子能', '轴向', '性能', '回路', '科技园区', '楼墙',
                    '铝合金', '核电', '网球场', '总包', '起重机', '物项', '核燃料', '元件', '控制棒', '控制室', '6电机', '叶轮', '组件', '整体性', '气体',
                    '动力', '山棚', '水箱', '海湾', '山水管', '松材', '线虫病', '中介', '公告号', '配电房', '石头', '住院楼', '金税', '橱柜', '高铁进',
                    '站路', '血透室', '法院', '农牧厅', '工信厅', '通讯', '时分区', '会场', '理学院', 'A座教学', '石工', '高主教', '学楼', '备品', '酒仙桥',
                    '主干', '发射机', '工商所', '电暖', '效林', '广播站', '学士', '分户', '科学技术馆', '剂熨剂', 'A包', '疫苗', '柳浪', '床架', '实事',
                    '驻地', '财物', '饭店', '悦心桥', '浮雕', '酒钢', '史馆', '迎宾路', '农场路', '交叉口', '片棚', '桃园楼', '哨校区', '阳台', '外事',
                    '工程费', '要素', '地瓜', '晨会', '段棚', '胶林', '居民', '水电气', '白银', '高新技术', '农宅', '政府性', '债务', '国际物', '泊位',
                    '地坪', '保健', '公办室', '名称', '用地', '房墙', '电容柜', '大会', '废料', '线路面', '石山', '风貌', '外科', '医用门', '模具', '冷源',
                    '制冷机组', '彩钢房', '高压', '大酒店', '区下水', '病残区', '安居工程', '功能室', '走廊', '农田', '林网', '吸动力', '手术室', '训室', '长廊',
                    '护栏', '音乐厅', '电脑灯', '职能', '制高点', '鼎新馆', '附件', '彩钢棚', '高层次', '加油站', '汽油', '实名', '物探', '信网', '审计厅',
                    '组组', '标牌', '材学院', '化学楼', '总布', '小学录', '课室', '直燃机', '光华', '步行街', '人政府', '主楼', '水管道', '林区', '教楼',
                    '酒店', '文化室', '场区', '体育运动', '大棚', '球场', '加工厂', '天堂', '城校区', '孤残', '滑梯院区', '疫病', '病原学', '兽医', '街道院',
                    '广域', '遗址区', '影像科', '核磁CT室', '人体', '解剖学', '暖房', '试点版', '供暖管网', '保障厅', '卡务', '畜禽', '转播车', '审核费',
                    '排污沟', '水管', '楼门', '马拉松', '建设厅', '提灌站', '路线', '屏幕', '四方', '主二', '动医系', '理工学校', '开水', '青龙业', '楼坡',
                    '大寨', '蒙自市', '路面', '保险费', '机务', '船载', '高层', '精神病', '街区', '新寨', '楼音', '现实', '书山', '垃圾场', '速印机',
                    '牛羊肉', '长效', '消纳场', '存量', '膳食科', '一站式', '证照', '面条', '粗加工区', '栏杆', '医务楼', '检测车', '产业园', '淡水鱼', '许可证',
                    '初中', '用药', '餐食品', '原辅', '检测室', '仓通道', '仓隔热层', '仓库', '成品粮', '充电桩', '邮政', '邮区', '调度室', '农机', '商务教学',
                    '白鹤', '停车场库', '车购税', '红十字', '口岸', '工控机', '车牌', '读写器', '遥感', '自行车队', '变速器', '硬镜', '器械', '干燥台', '转运车',
                    '汽车站', '车底', '监护型', '清运车', '政策', '书I', '能源机', '处理场', '翻斗车', '钩臂车', '工厂', '专用型', '土地权籍', '实物', '机房云',
                    '书棚', '房源', '火车站', '站房', '台式机', '柜台', '理工大学生', '打印纸', '电子屏', '理工学院', '通信车', '地面站', '斗茶赛', '世界',
                    '中国馆', '馆室', '主城', '盛筵', '见证', '农用地', '规划院', '警务', '经验', '历史', '基因组', 'HiC', '卡通', 'pos机', '深度',
                    '放管服', '电刀', '阅览室', '潮位站', '服务类', '宽带', '中心国', '监管平台', '棉服', '鞋子', '书包', '文具', '座席', '回民', '秩序',
                    '图书架', '防盗门', '标签', '云平', '台云', '公楼', '地震波', '知识库', '专线', '硬盘', '山地', '国库', '堡垒机', '耳鸣声', '总台',
                    '政务云', 'IDC机', '柜云', '邮箱', '洗板机', '吊塔', '干化学', '尿液', '排痰机', '红外线', '仪双头', '红外', '喉镜', '肌松', '仪脑',
                    '电波', '注射泵', '胎儿', '母亲', '胎心', '支气管镜', '切片机', '核心路', '离子束', '电镜', '能谱', '离子', '卷宗', '危险品', '储存室',
                    '查询机', '疗椅', '镀膜机', '等离子', '阴道', '阴道镜', '电外科', '能量', '呼吸机', '油气', '原位', '民政厅', '热源', '档案柜', '文头纸',
                    '二氧化碳', '箱孵', '二氧化碳培育箱', '镜子', '宣传牌', '东苑餐厅', '园艺站', '戈壁', '水肥', '公文', '天平质', '音罩', '传电表', '传输网',
                    '主控站', '电动密集柜', '事件', '灾情', '沙盘光伏', '实训', '路域', '桉树', '藏区', '地图', '文传', '编辑', '流域', '湿地', '心脏',
                    '神经', '报印刷费', '整合权籍', '志书', '马蹄', '膀胱镜', '输尿管镜', '电切镜', '液相', '多彩网', '手机', '光调制器', '采矿权', '承包商',
                    '沙盘', '超声波', '机腔镜', '清洗机', '石英砂', '学报', '咽喉科', '辣椒', '火化机', '尾气', '输入式', '数码', '宇窗帘', '平行光', '冷压机',
                    '两翼', '航天', '单室', '本底', '安全阀', '药物', '合成热室', '热室', '现状', '海服', '仪表', '湖泊', '采石场', '分辨率', '活细胞',
                    '飞行包', '印刷费', '陇正骨', '学术', '流派', '首饰', '贵金属', '表面', '浮标', '井录井', '挂药包', '人工费', '黄斑星', '天牛', '精度',
                    '微硬度', '航拍', '台风', '风暴潮', '灾害', '光刻机', '屏障', '监视器', '传播力', '锚系', '温盐', '仪声', '铁氧体', '环形器', '血细胞',
                    '分离机', '机震', '荡器', '标包', '苹果', '品种', '砧木', '种质', '热站', '公羊', '领域', '产权', '湖畔', '聋分子', '过氧化氢', '低温',
                    '指示剂', '阅读器', '棉花', '商品', '交易会', '葡萄酒', '专场', '法官', '助手', '电工', '变流器', '主电路', 'Ku', '波段', '转发器',
                    '容量', '陆地', '周期', '硅酸钇镥', '晶体', '志愿者', '骆驼', '表页', '纸质品', '颅磁', '药学院', '商标', '注册证', '电锅炉', '农药',
                    '化肥', '肉裘', 'X光机', '司法', '径赛类', '细胞', '电信', '释放器', '能见度', '传感器', '购置机', '传真机', '地膜', '集成电路', '扫描量',
                    '仪纯水', '裁判', '签章', '直线', '加速器', '石油', '医药', '研究生', '民歌', '代表性', '传承人', '外观', '新机', '引擎', '乳腺', 'X线',
                    '搏器', '临床药学', '制剂', '血气', '仪1', '盲人', '支气管', '碳硫元素', '核素', '枪弹柜', '戏剧', '导演', '体育房', '净水器', '电话',
                    '电话机', '电磁锁', '翼闸', '阅读机', '眼镜', '套件', '宫腔镜', '椭圆', '铅板', '修剪机', '黄板', '常规', '变速箱', '冲浪', '赛事',
                    '万宁站', '冲浪赛', '文化馆', '题材', '深井', '观测站', '中药', '标本', '宣传栏', '舞剧', '舞蹈诗', '飞秒', '放大器', '全球', '资讯',
                    '螺线管', '极杆液', '谱质谱', '树轮', '干细胞', '阻断器', '字画', '设计院', '手提袋', '主机', '资源池', '代码', '国王', '飞机', '谈话室',
                    '禁闭室', '渭源馆', '分会场', '瓷粉盒', '参数', '差分', '反射式', '质子', '频带', '检测卡', '肥料', '药学', '针灸', '海郡', '电子书',
                    '书法', '秦腔', '冲击波', '敏菌液', '涂布机', '精灵', '水母', '触摸屏', '铸炉', '准分子', '净气型', '药品柜', '马铃薯', '种薯', '殡仪馆',
                    '京剧', '创意', '手套箱', '艺术节', 'D紫外线', '帐篷', '音乐节', '布景', '大学物', '天学院', 'VR', '电感', '刻蚀机', '角膜', '内皮镜',
                    '褥疮垫', '听力', '微量泵', '茶树', '分光光', '消防车', '货运车', '信号机', '遥控器', '河长制', '公示牌', '文学', '艺术界', '荧光', '飞秒钛',
                    '宝石', '加固机', '图集', '草花', '双腔室', '管材', '板卡', '盐湖', '心理', '民航', 'EPR', '丝头', '硫酸钾', '日期', '对联', '热水器',
                    '润滑油', '曲纸', '面胶', '劳保', 'ZG镐铝', '制品', '定位器', '压力', '大讲堂', '柔性', '芯片', '电流体', '动力学', '微滴', '可靠性',
                    '中录播室', '绩效', '核桃功', '能性', '弹性', '法庭庭', '语音', '土木', '火炬', '树木', '槿树', '调查船', '防盗护栏', '龙泉', '读者',
                    '展示室', '音像', '校医院', '校校', '公寓椅', '辅警', '配饰', '警服', 'LDR病区', '织品', '病人', '食盐', '门吊', '假肢', '列车',
                    '楼体', '内科', '透析室', '麻醉科', '关系', '气功', '租班车', '场口', '安全员', '劳务费', 'POS机', '终端机', '图形', '机车', '课程',
                    '教材', '荣誉', '巡诊车', '习艺', '停车位', '原型', '燃油', '降尘车', '班车', '公交车', '单车', '单一性', '公务车', '校车', '非机动车',
                    '士官', '宫物业', '序物业', '物质', '遗产', '故居', '展示厅', '文体', '基础园区', '外包增项', '大礼堂', '净月', '创业园', '聚集园',
                    '金韵华庭', '圩墩', '遗址', '红绿灯', '控制机', '钟楼', '海港', '教育厅', '妇科', '无影灯', '先导区', '都市', '农民', '经理', '特色',
                    '毕节西派', '澜岸', '电梯间', '乘客', '急诊', '科技园', '后勤处', '亮灯', '杂厨', '洗碗机', '租赁车', '网约车', '分院', '资源库', '肉类',
                    '库房', '民兵', '熟食品', '重点段', '门诊', '血透病区', '厨师', '班包', '风景', '名胜区', '晖苑', '节日', '乐清', '教工', '绍剧', '民警',
                    '副食', '物流', '篮球', '联赛', '中心人', '社楼', '餐椅', '超市', '食品园', '骨伤', '风险', '寄生虫', '新贵', '干菜', '糕点', '托管费',
                    '电瓶', '四海', '印刷品', '草坪', '牛奶', '复印机', '粉盒', '集贤楼', '食堂厅', '杂件', '膳食', '大豆', '公开赛', '厨具', '快检箱',
                    '销售厅', '鱼类', '米面油', '微农场', '复印纸', '供应站军', '供分站', '烟管', '耗材供货商', '食堂供货商', '衣柜', '年会', '摊位', '会馆',
                    '炊事员', '劳务包', '东道路', '事故', '风温', '湿度', '种子', '牦牛', '美食', '宗教', '条例', '宣传品', '游泳池', '前沿站', '长街',
                    '体艺馆', '过渡房', '小微', '炼铁厂', '高炉', '洪涝区', '高山', '雪橇', '童装城', '扶梯', '项目师', '财务科', '师垦区', '师师', '师盖',
                    '港区', 'A座B座', '情况', '对策', '木质', '素质', '马克思主义', '封闭式', '观光车', '停车架', '协议供货询', '定点供货商', '屏风', '古水管',
                    '排污口', '马道', '枫园', '精神文明', '军队', '站民', '文化站', '苗圃', '楠苑', '总场', '水务']