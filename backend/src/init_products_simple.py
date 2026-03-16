"""
初始化大量产品数据 - 简化版
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.cosmetic import Base, EffectCategory, Ingredient, Product, SkinType
from src.models.cosmetic import ingredient_product_association, product_skintype_association

# 创建数据库连接
DATABASE_URL = "sqlite:///src/database/app.db"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

def init_products():
    """初始化大量产品数据"""
    
    products_data = [
        # 美白淡斑产品
        {
            "name": "SK-II 小灯泡精华",
            "brand": "SK-II",
            "category": "精华",
            "price": 1380.0,
            "volume": "30ml",
            "description": "含有烟酰胺和多种美白成分，有效淡化色斑，提亮肤色",
            "full_ingredients": "水、烟酰胺、甘油、透明质酸钠、光甘草定、维生素C衍生物",
            "purchase_url": "https://www.sk-ii.com.cn",
            "image_url": "https://example.com/sk2-genoptics.jpg"
        },
        {
            "name": "资生堂 新透白美肌精华",
            "brand": "资生堂",
            "category": "精华",
            "price": 680.0,
            "volume": "30ml",
            "description": "含有4-丁基间苯二酚，强效美白，温和不刺激",
            "full_ingredients": "水、4-丁基间苯二酚、甘油、透明质酸钠、维生素E",
            "purchase_url": "https://www.shiseido.com.cn",
            "image_url": "https://example.com/shiseido-white.jpg"
        },
        {
            "name": "兰蔻 小白管美白精华",
            "brand": "兰蔻",
            "category": "精华",
            "price": 890.0,
            "volume": "30ml",
            "description": "含有维生素C和阿魏酸，抗氧化美白双重功效",
            "full_ingredients": "水、维生素C、阿魏酸、甘油、透明质酸钠、烟酰胺",
            "purchase_url": "https://www.lancome.com.cn",
            "image_url": "https://example.com/lancome-white.jpg"
        },
        {
            "name": "雅诗兰黛 小棕瓶美白精华",
            "brand": "雅诗兰黛",
            "category": "精华",
            "price": 1280.0,
            "volume": "30ml",
            "description": "含有氨甲环酸和烟酰胺，有效阻断黑色素生成",
            "full_ingredients": "水、氨甲环酸、烟酰胺、甘油、透明质酸钠、维生素E",
            "purchase_url": "https://www.esteelauder.com.cn",
            "image_url": "https://example.com/estee-white.jpg"
        },
        {
            "name": "OLAY 光感小白瓶",
            "brand": "OLAY",
            "category": "精华",
            "price": 299.0,
            "volume": "30ml",
            "description": "含有烟酰胺和维生素C，平价美白精华",
            "full_ingredients": "水、烟酰胺、3-邻-乙基抗坏血酸、甘油、透明质酸钠",
            "purchase_url": "https://www.olay.com.cn",
            "image_url": "https://example.com/olay-white.jpg"
        },
        {
            "name": "理肤泉 维生素C精华",
            "brand": "理肤泉",
            "category": "精华",
            "price": 398.0,
            "volume": "20ml",
            "description": "含有纯维生素C，温泉水配方，敏感肌可用",
            "full_ingredients": "理肤泉温泉水、维生素C、甘油、透明质酸钠、维生素E",
            "purchase_url": "https://www.laroche-posay.com.cn",
            "image_url": "https://example.com/lrp-vitc.jpg"
        },
        {
            "name": "修丽可 CE精华",
            "brand": "修丽可",
            "category": "精华",
            "price": 1680.0,
            "volume": "30ml",
            "description": "含有15%维生素C、1%维生素E和0.5%阿魏酸的经典抗氧化精华",
            "full_ingredients": "水、维生素C、维生素E、阿魏酸、甘油",
            "purchase_url": "https://www.skinceuticals.com.cn",
            "image_url": "https://example.com/skinceuticals-ce.jpg"
        },
        {
            "name": "城野医生 VC精华",
            "brand": "城野医生",
            "category": "精华",
            "price": 168.0,
            "volume": "18ml",
            "description": "含有维生素C衍生物，温和美白，适合日常使用",
            "full_ingredients": "水、抗坏血酸磷酸酯镁、甘油、透明质酸钠、烟酰胺",
            "purchase_url": "https://www.drci-labo.com",
            "image_url": "https://example.com/drci-vitc.jpg"
        },
        {
            "name": "薇诺娜 熊果苷美白精华",
            "brand": "薇诺娜",
            "category": "精华",
            "price": 198.0,
            "volume": "30ml",
            "description": "含有α-熊果苷和甘草提取物，温和美白，敏感肌友好",
            "full_ingredients": "水、α-熊果苷、甘草提取物、甘油、透明质酸钠、红没药醇",
            "purchase_url": "https://www.winona.com.cn",
            "image_url": "https://example.com/winona-arbutin.jpg"
        },
        {
            "name": "珂润 美白精华",
            "brand": "珂润",
            "category": "精华",
            "price": 258.0,
            "volume": "30ml",
            "description": "含有氨甲环酸和神经酰胺，美白同时修护屏障",
            "full_ingredients": "水、氨甲环酸、神经酰胺、甘油、透明质酸钠、尿囊素",
            "purchase_url": "https://www.curel.com.cn",
            "image_url": "https://example.com/curel-white.jpg"
        },
        {
            "name": "宝拉珍选 2%水杨酸精华",
            "brand": "宝拉珍选",
            "category": "精华",
            "price": 228.0,
            "volume": "30ml",
            "description": "含有2%水杨酸，去角质美白，改善肤色不均",
            "full_ingredients": "水、水杨酸、甘油、烟酰胺、透明质酸钠、绿茶提取物",
            "purchase_url": "https://www.paulaschoice.com.cn",
            "image_url": "https://example.com/pc-bha.jpg"
        },
        {
            "name": "The Ordinary 熊果苷精华",
            "brand": "The Ordinary",
            "category": "精华",
            "price": 68.0,
            "volume": "30ml",
            "description": "含有2%熊果苷和透明质酸，平价美白精华",
            "full_ingredients": "水、熊果苷、透明质酸钠、甘油、卡波姆",
            "purchase_url": "https://theordinary.com",
            "image_url": "https://example.com/to-arbutin.jpg"
        },
        {
            "name": "Melano CC 美白精华",
            "brand": "Melano CC",
            "category": "精华",
            "price": 89.0,
            "volume": "20ml",
            "description": "含有活性维生素C和维生素E，日本平价美白精华",
            "full_ingredients": "维生素C、维生素E、异丙基甲基酚、甘油、透明质酸钠",
            "purchase_url": "https://www.rohto.com",
            "image_url": "https://example.com/melano-cc.jpg"
        },
        {
            "name": "HABA 鲨烷美白精华",
            "brand": "HABA",
            "category": "精华",
            "price": 298.0,
            "volume": "30ml",
            "description": "含有维生素C衍生物和角鲨烷，美白滋润双重功效",
            "full_ingredients": "角鲨烷、抗坏血酸磷酸酯镁、甘油、透明质酸钠、维生素E",
            "purchase_url": "https://www.haba.co.jp",
            "image_url": "https://example.com/haba-white.jpg"
        },
        {
            "name": "FANCL 美白精华",
            "brand": "FANCL",
            "category": "精华",
            "price": 368.0,
            "volume": "18ml",
            "description": "含有维生素C和甘草提取物，无添加配方",
            "full_ingredients": "水、维生素C、甘草提取物、甘油、透明质酸钠、神经酰胺",
            "purchase_url": "https://www.fancl.com.cn",
            "image_url": "https://example.com/fancl-white.jpg"
        },
        
        # 抗衰老产品
        {
            "name": "兰蔻 小黑瓶精华",
            "brand": "兰蔻",
            "category": "精华",
            "price": 1080.0,
            "volume": "30ml",
            "description": "含有多种多肽和益生菌发酵产物，全面抗衰老",
            "full_ingredients": "水、棕榈酰五肽-4、乙酰基六肽-8、发酵产物、甘油、透明质酸钠",
            "purchase_url": "https://www.lancome.com.cn",
            "image_url": "https://example.com/lancome-genifique.jpg"
        },
        {
            "name": "雅诗兰黛 小棕瓶精华",
            "brand": "雅诗兰黛",
            "category": "精华",
            "price": 1380.0,
            "volume": "30ml",
            "description": "含有多种抗氧化成分和修护因子，经典抗衰精华",
            "full_ingredients": "水、棕榈酰五肽-4、艾地苯、维生素E、甘油、透明质酸钠",
            "purchase_url": "https://www.esteelauder.com.cn",
            "image_url": "https://example.com/estee-anr.jpg"
        },
        {
            "name": "SK-II 大红瓶面霜",
            "brand": "SK-II",
            "category": "面霜",
            "price": 1680.0,
            "volume": "50g",
            "description": "含有Pitera和多种抗衰成分，深层滋养抗衰",
            "full_ingredients": "水、Pitera、棕榈酰五肽-4、神经酰胺、角鲨烷、甘油",
            "purchase_url": "https://www.sk-ii.com.cn",
            "image_url": "https://example.com/sk2-rna.jpg"
        },
        {
            "name": "资生堂 红腰子精华",
            "brand": "资生堂",
            "category": "精华",
            "price": 1280.0,
            "volume": "30ml",
            "description": "含有视黄醇和多种植物提取物，温和抗衰",
            "full_ingredients": "水、视黄醇、补骨脂酚、甘油、透明质酸钠、神经酰胺",
            "purchase_url": "https://www.shiseido.com.cn",
            "image_url": "https://example.com/shiseido-ultimune.jpg"
        },
        {
            "name": "欧莱雅 小蜜罐面霜",
            "brand": "欧莱雅",
            "category": "面霜",
            "price": 398.0,
            "volume": "50ml",
            "description": "含有玻色因和多种抗衰成分，平价抗衰面霜",
            "full_ingredients": "水、玻色因、甘油、神经酰胺、角鲨烷、透明质酸钠",
            "purchase_url": "https://www.loreal-paris.com.cn",
            "image_url": "https://example.com/loreal-revitalift.jpg"
        },
        {
            "name": "OLAY 大红瓶面霜",
            "brand": "OLAY",
            "category": "面霜",
            "price": 299.0,
            "volume": "50g",
            "description": "含有烟酰胺和多肽，平价抗衰面霜",
            "full_ingredients": "水、烟酰胺、棕榈酰五肽-4、甘油、神经酰胺、角鲨烷",
            "purchase_url": "https://www.olay.com.cn",
            "image_url": "https://example.com/olay-regenerist.jpg"
        },
        {
            "name": "The Ordinary 视黄醇精华",
            "brand": "The Ordinary",
            "category": "精华",
            "price": 58.0,
            "volume": "30ml",
            "description": "含有1%视黄醇，平价抗衰精华",
            "full_ingredients": "角鲨烷、视黄醇、维生素E、BHT",
            "purchase_url": "https://theordinary.com",
            "image_url": "https://example.com/to-retinol.jpg"
        },
        {
            "name": "Paula's Choice 视黄醇精华",
            "brand": "宝拉珍选",
            "category": "精华",
            "price": 328.0,
            "volume": "30ml",
            "description": "含有0.5%视黄醇和多种抗氧化成分",
            "full_ingredients": "水、视黄醇、维生素E、甘油、透明质酸钠、神经酰胺",
            "purchase_url": "https://www.paulaschoice.com.cn",
            "image_url": "https://example.com/pc-retinol.jpg"
        },
        {
            "name": "修丽可 B5精华",
            "brand": "修丽可",
            "category": "精华",
            "price": 980.0,
            "volume": "30ml",
            "description": "含有维生素B5和透明质酸，修护抗衰",
            "full_ingredients": "水、泛醇、透明质酸钠、甘油、维生素E",
            "purchase_url": "https://www.skinceuticals.com.cn",
            "image_url": "https://example.com/skinceuticals-b5.jpg"
        },
        {
            "name": "Drunk Elephant A醇精华",
            "brand": "Drunk Elephant",
            "category": "精华",
            "price": 680.0,
            "volume": "30ml",
            "description": "含有1%视黄醇和多种舒缓成分",
            "full_ingredients": "水、视黄醇、甘油、透明质酸钠、神经酰胺、尿囊素",
            "purchase_url": "https://www.drunkelephant.com",
            "image_url": "https://example.com/de-apassioni.jpg"
        },
        
        # 保湿补水产品
        {
            "name": "兰蔻 水分缘舒缓保湿面霜",
            "brand": "兰蔻",
            "category": "面霜",
            "price": 680.0,
            "volume": "50ml",
            "description": "含有透明质酸和神经酰胺，深层保湿",
            "full_ingredients": "水、透明质酸钠、神经酰胺、甘油、角鲨烷、泛醇",
            "purchase_url": "https://www.lancome.com.cn",
            "image_url": "https://example.com/lancome-hydra.jpg"
        },
        {
            "name": "雅诗兰黛 红石榴面霜",
            "brand": "雅诗兰黛",
            "category": "面霜",
            "price": 580.0,
            "volume": "50ml",
            "description": "含有透明质酸和多种植物提取物，保湿抗氧化",
            "full_ingredients": "水、透明质酸钠、甘油、神经酰胺、维生素E、红石榴提取物",
            "purchase_url": "https://www.esteelauder.com.cn",
            "image_url": "https://example.com/estee-nutritious.jpg"
        },
        {
            "name": "理肤泉 特安面霜",
            "brand": "理肤泉",
            "category": "面霜",
            "price": 198.0,
            "volume": "40ml",
            "description": "含有神经酰胺和温泉水，敏感肌专用保湿面霜",
            "full_ingredients": "理肤泉温泉水、神经酰胺、甘油、角鲨烷、尿囊素",
            "purchase_url": "https://www.laroche-posay.com.cn",
            "image_url": "https://example.com/lrp-toleriane.jpg"
        },
        {
            "name": "珂润 面霜",
            "brand": "珂润",
            "category": "面霜",
            "price": 158.0,
            "volume": "40g",
            "description": "含有神经酰胺和透明质酸，干燥敏感肌专用",
            "full_ingredients": "水、神经酰胺、透明质酸钠、甘油、角鲨烷、尿囊素",
            "purchase_url": "https://www.curel.com.cn",
            "image_url": "https://example.com/curel-cream.jpg"
        },
        {
            "name": "CeraVe 保湿面霜",
            "brand": "CeraVe",
            "category": "面霜",
            "price": 168.0,
            "volume": "52g",
            "description": "含有3种神经酰胺和透明质酸，24小时保湿",
            "full_ingredients": "水、神经酰胺、透明质酸钠、甘油、胆甾醇、脂肪酸",
            "purchase_url": "https://www.cerave.com",
            "image_url": "https://example.com/cerave-moisturizer.jpg"
        },
        {
            "name": "薇诺娜 舒敏保湿面霜",
            "brand": "薇诺娜",
            "category": "面霜",
            "price": 128.0,
            "volume": "50g",
            "description": "含有透明质酸和马齿苋提取物，敏感肌保湿",
            "full_ingredients": "水、透明质酸钠、甘油、神经酰胺、马齿苋提取物、红没药醇",
            "purchase_url": "https://www.winona.com.cn",
            "image_url": "https://example.com/winona-moisturizer.jpg"
        },
        {
            "name": "HADA LABO 肌研极润面霜",
            "brand": "HADA LABO",
            "category": "面霜",
            "price": 89.0,
            "volume": "50g",
            "description": "含有5种透明质酸，深层保湿",
            "full_ingredients": "水、透明质酸钠、甘油、角鲨烷、神经酰胺",
            "purchase_url": "https://www.rohto.com",
            "image_url": "https://example.com/hadalabo-cream.jpg"
        },
        {
            "name": "Neutrogena 水活保湿面霜",
            "brand": "Neutrogena",
            "category": "面霜",
            "price": 98.0,
            "volume": "50ml",
            "description": "含有透明质酸和甘油，轻盈保湿",
            "full_ingredients": "水、透明质酸钠、甘油、二甲硅油、泛醇",
            "purchase_url": "https://www.neutrogena.com",
            "image_url": "https://example.com/neutrogena-hydro.jpg"
        },
        {
            "name": "The Ordinary 透明质酸精华",
            "brand": "The Ordinary",
            "category": "精华",
            "price": 48.0,
            "volume": "30ml",
            "description": "含有2%透明质酸和维生素B5，平价保湿精华",
            "full_ingredients": "水、透明质酸钠、泛醇、甘油、卡波姆",
            "purchase_url": "https://theordinary.com",
            "image_url": "https://example.com/to-hyaluronic.jpg"
        },
        {
            "name": "Fresh 玫瑰保湿面霜",
            "brand": "Fresh",
            "category": "面霜",
            "price": 580.0,
            "volume": "50ml",
            "description": "含有透明质酸和玫瑰精油，保湿舒缓",
            "full_ingredients": "水、透明质酸钠、甘油、玫瑰精油、神经酰胺、角鲨烷",
            "purchase_url": "https://www.fresh.com",
            "image_url": "https://example.com/fresh-rose.jpg"
        },
        
        # 控油祛痘产品
        {
            "name": "理肤泉 K乳",
            "brand": "理肤泉",
            "category": "乳液",
            "price": 198.0,
            "volume": "40ml",
            "description": "含有水杨酸和烟酰胺，控油祛痘，敏感肌可用",
            "full_ingredients": "理肤泉温泉水、水杨酸、烟酰胺、甘油、锌",
            "purchase_url": "https://www.laroche-posay.com.cn",
            "image_url": "https://example.com/lrp-effaclar.jpg"
        },
        {
            "name": "薇诺娜 控油祛痘精华",
            "brand": "薇诺娜",
            "category": "精华",
            "price": 168.0,
            "volume": "30ml",
            "description": "含有水杨酸和马齿苋提取物，温和控油祛痘",
            "full_ingredients": "水、水杨酸、马齿苋提取物、烟酰胺、甘油、锌",
            "purchase_url": "https://www.winona.com.cn",
            "image_url": "https://example.com/winona-acne.jpg"
        },
        {
            "name": "The Ordinary 烟酰胺精华",
            "brand": "The Ordinary",
            "category": "精华",
            "price": 48.0,
            "volume": "30ml",
            "description": "含有10%烟酰胺和1%锌，控油收毛孔",
            "full_ingredients": "水、烟酰胺、锌、透明质酸钠、卡波姆",
            "purchase_url": "https://theordinary.com",
            "image_url": "https://example.com/to-niacinamide.jpg"
        },
        {
            "name": "FANCL 祛痘精华",
            "brand": "FANCL",
            "category": "精华",
            "price": 268.0,
            "volume": "8ml",
            "description": "含有甘草酸和维生素B6，无添加祛痘精华",
            "full_ingredients": "水、甘草酸二钾、维生素B6、甘油、透明质酸钠",
            "purchase_url": "https://www.fancl.com.cn",
            "image_url": "https://example.com/fancl-acne.jpg"
        },
        {
            "name": "城野医生 毛孔收敛水",
            "brand": "城野医生",
            "category": "爽肤水",
            "price": 128.0,
            "volume": "100ml",
            "description": "含有乳酸和苹果酸，温和去角质，收敛毛孔",
            "full_ingredients": "水、乳酸、苹果酸、甘油、透明质酸钠、烟酰胺",
            "purchase_url": "https://www.drci-labo.com",
            "image_url": "https://example.com/drci-pore.jpg"
        },
        {
            "name": "MUJI 敏感肌用乳液",
            "brand": "MUJI",
            "category": "乳液",
            "price": 89.0,
            "volume": "200ml",
            "description": "含有透明质酸和甘油，温和保湿，痘痘肌可用",
            "full_ingredients": "水、甘油、透明质酸钠、角鲨烷、尿囊素",
            "purchase_url": "https://www.muji.com.cn",
            "image_url": "https://example.com/muji-sensitive.jpg"
        },
        {
            "name": "Cetaphil 控油洁面乳",
            "brand": "Cetaphil",
            "category": "洁面",
            "price": 68.0,
            "volume": "125ml",
            "description": "含有水杨酸，温和控油清洁",
            "full_ingredients": "水、水杨酸、甘油、椰油酰胺丙基甜菜碱、烟酰胺",
            "purchase_url": "https://www.cetaphil.com",
            "image_url": "https://example.com/cetaphil-oily.jpg"
        },
        {
            "name": "Differin 阿达帕林凝胶",
            "brand": "Differin",
            "category": "凝胶",
            "price": 158.0,
            "volume": "15g",
            "description": "含有0.1%阿达帕林，处方级祛痘产品",
            "full_ingredients": "阿达帕林、甘油、卡波姆、氢氧化钠",
            "purchase_url": "https://www.differin.com",
            "image_url": "https://example.com/differin-gel.jpg"
        },
        {
            "name": "Stridex 水杨酸棉片",
            "brand": "Stridex",
            "category": "棉片",
            "price": 58.0,
            "volume": "55片",
            "description": "含有2%水杨酸，便携祛痘棉片",
            "full_ingredients": "水、水杨酸、柠檬酸、薄荷醇、芦荟提取物",
            "purchase_url": "https://www.stridex.com",
            "image_url": "https://example.com/stridex-pads.jpg"
        },
        
        # 舒缓修护产品
        {
            "name": "理肤泉 B5修复霜",
            "brand": "理肤泉",
            "category": "面霜",
            "price": 158.0,
            "volume": "40ml",
            "description": "含有5%泛醇和透明质酸，舒缓修护",
            "full_ingredients": "理肤泉温泉水、泛醇、透明质酸钠、甘油、尿囊素",
            "purchase_url": "https://www.laroche-posay.com.cn",
            "image_url": "https://example.com/lrp-cicaplast.jpg"
        },
        {
            "name": "薇诺娜 舒敏保湿特护霜",
            "brand": "薇诺娜",
            "category": "面霜",
            "price": 168.0,
            "volume": "50g",
            "description": "含有马齿苋提取物和神经酰胺，敏感肌专用",
            "full_ingredients": "水、马齿苋提取物、神经酰胺、甘油、红没药醇、尿囊素",
            "purchase_url": "https://www.winona.com.cn",
            "image_url": "https://example.com/winona-soothing.jpg"
        },
        {
            "name": "雅漾 舒护活泉喷雾",
            "brand": "雅漾",
            "category": "喷雾",
            "price": 68.0,
            "volume": "150ml",
            "description": "含有雅漾活泉水，舒缓敏感肌肤",
            "full_ingredients": "雅漾活泉水",
            "purchase_url": "https://www.avene.com.cn",
            "image_url": "https://example.com/avene-spray.jpg"
        },
        {
            "name": "珂润 润浸保湿面霜",
            "brand": "珂润",
            "category": "面霜",
            "price": 158.0,
            "volume": "40g",
            "description": "含有神经酰胺和尿囊素，修护敏感肌屏障",
            "full_ingredients": "水、神经酰胺、尿囊素、甘油、角鲨烷、透明质酸钠",
            "purchase_url": "https://www.curel.com.cn",
            "image_url": "https://example.com/curel-intensive.jpg"
        },
        {
            "name": "AVEENO 燕麦舒缓面霜",
            "brand": "AVEENO",
            "category": "面霜",
            "price": 98.0,
            "volume": "50ml",
            "description": "含有胶体燕麦和甘油，舒缓干燥敏感肌",
            "full_ingredients": "水、胶体燕麦、甘油、透明质酸钠、神经酰胺",
            "purchase_url": "https://www.aveeno.com",
            "image_url": "https://example.com/aveeno-oat.jpg"
        },
        {
            "name": "修丽可 B5修护凝胶",
            "brand": "修丽可",
            "category": "凝胶",
            "price": 680.0,
            "volume": "30ml",
            "description": "含有维生素B5和透明质酸，医美术后修护",
            "full_ingredients": "水、泛醇、透明质酸钠、甘油、尿囊素",
            "purchase_url": "https://www.skinceuticals.com.cn",
            "image_url": "https://example.com/skinceuticals-phyto.jpg"
        },
        {
            "name": "CeraVe 修护乳液",
            "brand": "CeraVe",
            "category": "乳液",
            "price": 128.0,
            "volume": "236ml",
            "description": "含有3种神经酰胺和烟酰胺，修护肌肤屏障",
            "full_ingredients": "水、神经酰胺、烟酰胺、甘油、透明质酸钠、胆甾醇",
            "purchase_url": "https://www.cerave.com",
            "image_url": "https://example.com/cerave-pm.jpg"
        },
        {
            "name": "Eucerin 5%尿素修护霜",
            "brand": "Eucerin",
            "category": "面霜",
            "price": 158.0,
            "volume": "50ml",
            "description": "含有5%尿素和乳酸，修护干燥粗糙肌肤",
            "full_ingredients": "水、尿素、乳酸、甘油、神经酰胺、角鲨烷",
            "purchase_url": "https://www.eucerin.com",
            "image_url": "https://example.com/eucerin-urea.jpg"
        },
        {
            "name": "First Aid Beauty 急救面霜",
            "brand": "First Aid Beauty",
            "category": "面霜",
            "price": 268.0,
            "volume": "56.7g",
            "description": "含有胶体燕麦和神经酰胺，舒缓敏感肌",
            "full_ingredients": "水、胶体燕麦、神经酰胺、甘油、尿囊素、透明质酸钠",
            "purchase_url": "https://www.firstaidbeauty.com",
            "image_url": "https://example.com/fab-ultra.jpg"
        },
        {
            "name": "Vanicream 温和面霜",
            "brand": "Vanicream",
            "category": "面霜",
            "price": 88.0,
            "volume": "113g",
            "description": "无香料无防腐剂，极度敏感肌专用",
            "full_ingredients": "水、甘油、角鲨烷、神经酰胺、透明质酸钠",
            "purchase_url": "https://www.vanicream.com",
            "image_url": "https://example.com/vanicream-moisturizer.jpg"
        },
        
        # 去角质产品
        {
            "name": "宝拉珍选 8%果酸精华",
            "brand": "宝拉珍选",
            "category": "精华",
            "price": 268.0,
            "volume": "30ml",
            "description": "含有8%羟基乙酸，深层去角质，改善肤质",
            "full_ingredients": "水、羟基乙酸、甘油、透明质酸钠、绿茶提取物",
            "purchase_url": "https://www.paulaschoice.com.cn",
            "image_url": "https://example.com/pc-aha.jpg"
        },
        {
            "name": "The Ordinary 30%果酸面膜",
            "brand": "The Ordinary",
            "category": "面膜",
            "price": 58.0,
            "volume": "30ml",
            "description": "含有30%AHA和2%BHA，强效去角质面膜",
            "full_ingredients": "水、羟基乙酸、水杨酸、透明质酸钠、芦荟提取物",
            "purchase_url": "https://theordinary.com",
            "image_url": "https://example.com/to-peeling.jpg"
        },
        {
            "name": "Drunk Elephant 婴儿面部去角质",
            "brand": "Drunk Elephant",
            "category": "精华",
            "price": 580.0,
            "volume": "30ml",
            "description": "含有25%AHA和2%BHA，温和去角质",
            "full_ingredients": "水、羟基乙酸、乳酸、水杨酸、甘油、透明质酸钠",
            "purchase_url": "https://www.drunkelephant.com",
            "image_url": "https://example.com/de-babyfacial.jpg"
        },
        {
            "name": "城野医生 去角质凝胶",
            "brand": "城野医生",
            "category": "凝胶",
            "price": 168.0,
            "volume": "250g",
            "description": "含有木瓜蛋白酶，温和去角质",
            "full_ingredients": "水、木瓜蛋白酶、甘油、透明质酸钠、芦荟提取物",
            "purchase_url": "https://www.drci-labo.com",
            "image_url": "https://example.com/drci-peeling.jpg"
        },
        {
            "name": "COSRX AHA精华",
            "brand": "COSRX",
            "category": "精华",
            "price": 128.0,
            "volume": "100ml",
            "description": "含有7%羟基乙酸，温和去角质",
            "full_ingredients": "水、羟基乙酸、甘油、透明质酸钠、烟酰胺",
            "purchase_url": "https://www.cosrx.com",
            "image_url": "https://example.com/cosrx-aha.jpg"
        },
        {
            "name": "Pixi 5%果酸爽肤水",
            "brand": "Pixi",
            "category": "爽肤水",
            "price": 168.0,
            "volume": "100ml",
            "description": "含有5%羟基乙酸和芦荟，温和去角质",
            "full_ingredients": "水、羟基乙酸、芦荟提取物、甘油、透明质酸钠",
            "purchase_url": "https://www.pixibeauty.com",
            "image_url": "https://example.com/pixi-glow.jpg"
        },
        {
            "name": "Good Molecules 乳酸精华",
            "brand": "Good Molecules",
            "category": "精华",
            "price": 68.0,
            "volume": "30ml",
            "description": "含有5%乳酸，温和去角质，敏感肌友好",
            "full_ingredients": "水、乳酸、甘油、透明质酸钠、尿囊素",
            "purchase_url": "https://www.goodmolecules.com",
            "image_url": "https://example.com/gm-lactic.jpg"
        },
        {
            "name": "Alpha-H 液体黄金",
            "brand": "Alpha-H",
            "category": "精华",
            "price": 298.0,
            "volume": "50ml",
            "description": "含有5%羟基乙酸，澳洲经典去角质产品",
            "full_ingredients": "水、羟基乙酸、甘油、透明质酸钠、甘草提取物",
            "purchase_url": "https://www.alpha-h.com",
            "image_url": "https://example.com/alphah-liquid.jpg"
        },
        {
            "name": "Neostrata 果酸面霜",
            "brand": "Neostrata",
            "category": "面霜",
            "price": 368.0,
            "volume": "40g",
            "description": "含有10%羟基乙酸，医美级去角质面霜",
            "full_ingredients": "水、羟基乙酸、甘油、神经酰胺、透明质酸钠",
            "purchase_url": "https://www.neostrata.com",
            "image_url": "https://example.com/neostrata-aha.jpg"
        },
        {
            "name": "Ren 完美去角质面膜",
            "brand": "Ren",
            "category": "面膜",
            "price": 268.0,
            "volume": "50ml",
            "description": "含有乳酸和木瓜蛋白酶，温和去角质面膜",
            "full_ingredients": "水、乳酸、木瓜蛋白酶、甘油、透明质酸钠、芦荟提取物",
            "purchase_url": "https://www.renskincare.com",
            "image_url": "https://example.com/ren-perfect.jpg"
        }
    ]
    
    for product_data in products_data:
        product = Product(**product_data)
        session.add(product)
    
    session.commit()
    print(f"产品初始化完成，共添加 {len(products_data)} 个产品")

if __name__ == "__main__":
    print("开始初始化产品数据...")
    
    init_products()
    
    session.close()
    print("产品数据初始化完成！")

