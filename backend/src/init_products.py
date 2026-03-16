"""
初始化大量具体产品数据
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
    """初始化产品数据"""
    
    # 美白淡斑产品
    whitening_products = [
        {
            "name": "SK-II 小灯泡精华",
            "brand": "SK-II",
            "category": "精华",
            "price": 1690.0,
            "volume": "30ml",
            "description": "含烟酰胺和维生素C衍生物，有效抑制黑色素生成，提亮肌肤",
            "full_ingredients": "水、烟酰胺、抗坏血酸葡糖苷、甘油、丁二醇、甘草酸二钾、透明质酸钠",
            "purchase_url": "https://www.sk-ii.com.cn",
            "image_url": "https://example.com/sk2-genoptics.jpg"
        },
        {
            "name": "资生堂新透白美肌精华",
            "brand": "资生堂",
            "category": "精华",
            "price": 580.0,
            "volume": "30ml",
            "description": "含传明酸和维生素C，双重美白成分，淡化色斑",
            "full_ingredients": "水、氨甲环酸、3-邻-乙基抗坏血酸、烟酰胺、甘油、透明质酸钠",
            "purchase_url": "https://www.shiseido.com.cn",
            "image_url": "https://example.com/shiseido-haku.jpg",
            "key_ingredients": ["氨甲环酸", "3-邻-乙基抗坏血酸", "烟酰胺"],
            "suitable_skin_types": ["干性肌肤", "混合性肌肤", "敏感性肌肤"]
        },
        {
            "name": "兰蔻小白管精华",
            "brand": "兰蔻",
            "category": "精华",
            "price": 1280.0,
            "volume": "30ml",
            "rating": 4.5,
            "review_count": 12350,
            "description": "含377和维生素C，科学美白配方，温和有效",
            "full_ingredients": "水、苯乙基间苯二酚、维生素C、烟酰胺、甘油、神经酰胺",
            "purchase_url": "https://www.lancome.com.cn",
            "image_url": "https://example.com/lancome-blanc.jpg",
            "key_ingredients": ["苯乙基间苯二酚", "维生素C", "烟酰胺"],
            "suitable_skin_types": ["干性肌肤", "混合性肌肤", "中性肌肤"]
        },
        {
            "name": "OLAY光感小白瓶",
            "brand": "OLAY",
            "category": "精华",
            "price": 269.0,
            "volume": "30ml",
            "rating": 4.3,
            "review_count": 25680,
            "description": "含烟酰胺和α-熊果苷，平价美白精华的经典选择",
            "full_ingredients": "水、烟酰胺、α-熊果苷、甘油、透明质酸钠、甘草提取物",
            "purchase_url": "https://www.olay.com.cn",
            "image_url": "https://example.com/olay-white.jpg",
            "key_ingredients": ["烟酰胺", "α-熊果苷", "甘草提取物"],
            "suitable_skin_types": ["油性肌肤", "混合性肌肤", "中性肌肤"]
        },
        {
            "name": "薇诺娜熊果苷美白精华",
            "brand": "薇诺娜",
            "category": "精华",
            "price": 198.0,
            "volume": "30ml",
            "rating": 4.2,
            "review_count": 18750,
            "description": "含熊果苷和光甘草定，温和美白，敏感肌可用",
            "full_ingredients": "水、α-熊果苷、光甘草定、烟酰胺、甘油、红没药醇",
            "purchase_url": "https://www.winona.com.cn",
            "image_url": "https://example.com/winona-arbutin.jpg",
            "key_ingredients": ["α-熊果苷", "光甘草定", "红没药醇"],
            "suitable_skin_types": ["敏感性肌肤", "干性肌肤", "混合性肌肤"]
        },
        {
            "name": "理肤泉维生素C精华",
            "brand": "理肤泉",
            "category": "精华",
            "price": 298.0,
            "volume": "20ml",
            "rating": 4.4,
            "review_count": 9850,
            "description": "含10%纯维生素C，强效抗氧化美白",
            "full_ingredients": "水、维生素C、阿魏酸、维生素E、甘油、透明质酸钠",
            "purchase_url": "https://www.laroche-posay.cn",
            "image_url": "https://example.com/lrp-vitc.jpg",
            "key_ingredients": ["维生素C", "阿魏酸", "维生素E"],
            "suitable_skin_types": ["油性肌肤", "混合性肌肤", "中性肌肤"]
        }
    ]
    
    # 抗衰老产品
    antiaging_products = [
        {
            "name": "雅诗兰黛小棕瓶精华",
            "brand": "雅诗兰黛",
            "category": "精华",
            "price": 1080.0,
            "volume": "30ml",
            "rating": 4.7,
            "review_count": 32450,
            "description": "含多种多肽和抗氧化成分，全面抗衰老",
            "full_ingredients": "水、棕榈酰五肽-4、乙酰基六肽-8、艾地苯、虾青素、神经酰胺",
            "purchase_url": "https://www.esteelauder.com.cn",
            "image_url": "https://example.com/el-anr.jpg",
            "key_ingredients": ["棕榈酰五肽-4", "乙酰基六肽-8", "艾地苯"],
            "suitable_skin_types": ["干性肌肤", "混合性肌肤", "中性肌肤"]
        },
        {
            "name": "兰蔻小黑瓶精华",
            "brand": "兰蔻",
            "category": "精华",
            "price": 1180.0,
            "volume": "30ml",
            "rating": 4.6,
            "review_count": 28900,
            "description": "含益生菌发酵产物和多肽，修护肌肤屏障",
            "full_ingredients": "水、棕榈酰五肽-4、玻色因、神经酰胺、角鲨烷、积雪草苷",
            "purchase_url": "https://www.lancome.com.cn",
            "image_url": "https://example.com/lancome-genifique.jpg",
            "key_ingredients": ["棕榈酰五肽-4", "玻色因", "神经酰胺"],
            "suitable_skin_types": ["干性肌肤", "混合性肌肤", "敏感性肌肤"]
        },
        {
            "name": "The Ordinary 视黄醇精华",
            "brand": "The Ordinary",
            "category": "精华",
            "price": 68.0,
            "volume": "30ml",
            "rating": 4.2,
            "review_count": 15670,
            "description": "含0.5%视黄醇，平价抗衰老精华",
            "full_ingredients": "水、视黄醇、角鲨烷、甘油、透明质酸钠、维生素E",
            "purchase_url": "https://theordinary.com",
            "image_url": "https://example.com/to-retinol.jpg",
            "key_ingredients": ["视黄醇", "角鲨烷", "维生素E"],
            "suitable_skin_types": ["油性肌肤", "混合性肌肤", "中性肌肤"]
        },
        {
            "name": "修丽可CE精华",
            "brand": "修丽可",
            "category": "精华",
            "price": 1680.0,
            "volume": "30ml",
            "rating": 4.8,
            "review_count": 8920,
            "description": "含15%维生素C、1%维生素E和0.5%阿魏酸的经典抗氧化配方",
            "full_ingredients": "水、维生素C、维生素E、阿魏酸、透明质酸钠、甘油",
            "purchase_url": "https://www.skinceuticals.com.cn",
            "image_url": "https://example.com/skinceuticals-ce.jpg",
            "key_ingredients": ["维生素C", "维生素E", "阿魏酸"],
            "suitable_skin_types": ["油性肌肤", "混合性肌肤", "中性肌肤"]
        },
        {
            "name": "Herbivore Bakuchiol精华",
            "brand": "Herbivore",
            "category": "精华",
            "price": 520.0,
            "volume": "30ml",
            "rating": 4.3,
            "review_count": 6780,
            "description": "含补骨脂酚，天然视黄醇替代品，孕妇可用",
            "full_ingredients": "水、补骨脂酚、角鲨烷、透明质酸钠、甘油、积雪草苷",
            "purchase_url": "https://www.herbivorebotanicals.com",
            "image_url": "https://example.com/herbivore-bakuchiol.jpg",
            "key_ingredients": ["补骨脂酚", "角鲨烷", "积雪草苷"],
            "suitable_skin_types": ["敏感性肌肤", "干性肌肤", "混合性肌肤"]
        }
    ]
    
    # 保湿补水产品
    moisturizing_products = [
        {
            "name": "兰蔻菁纯臻颜面霜",
            "brand": "兰蔻",
            "category": "面霜",
            "price": 1580.0,
            "volume": "50ml",
            "rating": 4.5,
            "review_count": 12450,
            "description": "含透明质酸和神经酰胺，深层保湿修护",
            "full_ingredients": "水、透明质酸钠、神经酰胺、角鲨烷、甘油、泛醇",
            "purchase_url": "https://www.lancome.com.cn",
            "image_url": "https://example.com/lancome-absolue.jpg",
            "key_ingredients": ["透明质酸钠", "神经酰胺", "角鲨烷"],
            "suitable_skin_types": ["干性肌肤", "混合性肌肤", "敏感性肌肤"]
        },
        {
            "name": "CeraVe保湿面霜",
            "brand": "CeraVe",
            "category": "面霜",
            "price": 168.0,
            "volume": "50ml",
            "rating": 4.6,
            "review_count": 28900,
            "description": "含3种神经酰胺和透明质酸，修护肌肤屏障",
            "full_ingredients": "水、神经酰胺、透明质酸钠、甘油、角鲨烷、泛醇",
            "purchase_url": "https://www.cerave.cn",
            "image_url": "https://example.com/cerave-moisturizer.jpg",
            "key_ingredients": ["神经酰胺", "透明质酸钠", "甘油"],
            "suitable_skin_types": ["干性肌肤", "敏感性肌肤", "中性肌肤"]
        },
        {
            "name": "理肤泉特安舒缓保湿面霜",
            "brand": "理肤泉",
            "category": "面霜",
            "price": 198.0,
            "volume": "40ml",
            "rating": 4.4,
            "review_count": 15670,
            "description": "含依克多因和神经酰胺，敏感肌专用",
            "full_ingredients": "水、依克多因、神经酰胺、甘油、角鲨烷、尿囊素",
            "purchase_url": "https://www.laroche-posay.cn",
            "image_url": "https://example.com/lrp-toleriane.jpg",
            "key_ingredients": ["依克多因", "神经酰胺", "尿囊素"],
            "suitable_skin_types": ["敏感性肌肤", "干性肌肤"]
        },
        {
            "name": "润百颜玻尿酸精华",
            "brand": "润百颜",
            "category": "精华",
            "price": 89.0,
            "volume": "30ml",
            "rating": 4.3,
            "review_count": 35680,
            "description": "含高浓度透明质酸，强效补水保湿",
            "full_ingredients": "水、透明质酸钠、甘油、泛醇、依克多因、尿囊素",
            "purchase_url": "https://www.runbainian.com",
            "image_url": "https://example.com/runbainian-ha.jpg",
            "key_ingredients": ["透明质酸钠", "甘油", "依克多因"],
            "suitable_skin_types": ["干性肌肤", "油性肌肤", "混合性肌肤", "敏感性肌肤", "中性肌肤"]
        }
    ]
    
    # 控油祛痘产品
    acne_products = [
        {
            "name": "宝拉珍选2%水杨酸精华",
            "brand": "宝拉珍选",
            "category": "精华",
            "price": 198.0,
            "volume": "30ml",
            "rating": 4.5,
            "review_count": 18920,
            "description": "含2%水杨酸，深入毛孔清洁，改善痘痘",
            "full_ingredients": "水、水杨酸、烟酰胺、甘油、透明质酸钠、绿茶提取物",
            "purchase_url": "https://www.paulaschoice.cn",
            "image_url": "https://example.com/pc-bha.jpg",
            "key_ingredients": ["水杨酸", "烟酰胺", "绿茶提取物"],
            "suitable_skin_types": ["油性肌肤", "混合性肌肤"]
        },
        {
            "name": "The Ordinary 烟酰胺精华",
            "brand": "The Ordinary",
            "category": "精华",
            "price": 48.0,
            "volume": "30ml",
            "rating": 4.2,
            "review_count": 42350,
            "description": "含10%烟酰胺和1%锌，控油收毛孔",
            "full_ingredients": "水、烟酰胺、锌、甘油、透明质酸钠、泛醇",
            "purchase_url": "https://theordinary.com",
            "image_url": "https://example.com/to-niacinamide.jpg",
            "key_ingredients": ["烟酰胺", "锌", "泛醇"],
            "suitable_skin_types": ["油性肌肤", "混合性肌肤", "中性肌肤"]
        },
        {
            "name": "理肤泉K乳",
            "brand": "理肤泉",
            "category": "乳液",
            "price": 168.0,
            "volume": "40ml",
            "rating": 4.3,
            "review_count": 15670,
            "description": "含水杨酸和烟酰胺，温和祛痘",
            "full_ingredients": "水、水杨酸、烟酰胺、甘油、锌、透明质酸钠",
            "purchase_url": "https://www.laroche-posay.cn",
            "image_url": "https://example.com/lrp-effaclar.jpg",
            "key_ingredients": ["水杨酸", "烟酰胺", "锌"],
            "suitable_skin_types": ["油性肌肤", "混合性肌肤", "敏感性肌肤"]
        },
        {
            "name": "茶树精油祛痘凝胶",
            "brand": "The Body Shop",
            "category": "凝胶",
            "price": 89.0,
            "volume": "15ml",
            "rating": 4.1,
            "review_count": 8920,
            "description": "含茶树精油，天然抗菌祛痘",
            "full_ingredients": "水、茶树精油、甘油、尿囊素、红没药醇、积雪草苷",
            "purchase_url": "https://www.thebodyshop.cn",
            "image_url": "https://example.com/tbs-teatree.jpg",
            "key_ingredients": ["茶树精油", "尿囊素", "红没药醇"],
            "suitable_skin_types": ["油性肌肤", "混合性肌肤"]
        }
    ]
    
    # 舒缓修护产品
    soothing_products = [
        {
            "name": "雅漾舒缓特护面霜",
            "brand": "雅漾",
            "category": "面霜",
            "price": 268.0,
            "volume": "50ml",
            "rating": 4.5,
            "review_count": 12450,
            "description": "含红没药醇和积雪草苷，舒缓敏感肌肤",
            "full_ingredients": "水、红没药醇、积雪草苷、甘草酸二钾、神经酰胺、角鲨烷",
            "purchase_url": "https://www.avene.cn",
            "image_url": "https://example.com/avene-tolerance.jpg",
            "key_ingredients": ["红没药醇", "积雪草苷", "甘草酸二钾"],
            "suitable_skin_types": ["敏感性肌肤", "干性肌肤"]
        },
        {
            "name": "薇诺娜舒敏保湿特护霜",
            "brand": "薇诺娜",
            "category": "面霜",
            "price": 168.0,
            "volume": "50ml",
            "rating": 4.4,
            "review_count": 25680,
            "description": "含积雪草苷和尿囊素，专为敏感肌设计",
            "full_ingredients": "水、积雪草苷、尿囊素、红没药醇、甘草酸二钾、神经酰胺",
            "purchase_url": "https://www.winona.com.cn",
            "image_url": "https://example.com/winona-sensitive.jpg",
            "key_ingredients": ["积雪草苷", "尿囊素", "红没药醇"],
            "suitable_skin_types": ["敏感性肌肤", "干性肌肤", "混合性肌肤"]
        }
    ]
    
    # 去角质产品
    exfoliating_products = [
        {
            "name": "宝拉珍选8%果酸精华",
            "brand": "宝拉珍选",
            "category": "精华",
            "price": 268.0,
            "volume": "30ml",
            "rating": 4.4,
            "review_count": 9850,
            "description": "含8%羟基乙酸，温和去角质",
            "full_ingredients": "水、羟基乙酸、甘油、透明质酸钠、尿囊素、甘草提取物",
            "purchase_url": "https://www.paulaschoice.cn",
            "image_url": "https://example.com/pc-aha.jpg",
            "key_ingredients": ["羟基乙酸", "尿囊素", "甘草提取物"],
            "suitable_skin_types": ["油性肌肤", "混合性肌肤", "中性肌肤"]
        },
        {
            "name": "The Ordinary 乳酸精华",
            "brand": "The Ordinary",
            "category": "精华",
            "price": 58.0,
            "volume": "30ml",
            "rating": 4.2,
            "review_count": 15670,
            "description": "含10%乳酸，温和去角质，适合敏感肌",
            "full_ingredients": "水、乳酸、甘油、透明质酸钠、尿囊素、泛醇",
            "purchase_url": "https://theordinary.com",
            "image_url": "https://example.com/to-lactic.jpg",
            "key_ingredients": ["乳酸", "尿囊素", "泛醇"],
            "suitable_skin_types": ["敏感性肌肤", "干性肌肤", "混合性肌肤"]
        }
    ]
    
    # 合并所有产品
    all_products = (whitening_products + antiaging_products + moisturizing_products + 
                   acne_products + soothing_products + exfoliating_products)
    
    # 获取成分和肤质映射
    ingredients = session.query(Ingredient).all()
    skin_types = session.query(SkinType).all()
    
    ingredient_map = {ingredient.name: ingredient.id for ingredient in ingredients}
    skin_type_map = {skin_type.name: skin_type.id for skin_type in skin_types}
    
    for product_data in all_products:
        # 提取关键成分和适合肤质
        key_ingredients = product_data.pop("key_ingredients", [])
        suitable_skin_types = product_data.pop("suitable_skin_types", [])
        
        # 创建产品
        product = Product(**product_data)
        session.add(product)
        session.flush()  # 获取产品ID
        
        # 建立成分关联
        for ingredient_name in key_ingredients:
            if ingredient_name in ingredient_map:
                ingredient_id = ingredient_map[ingredient_name]
                # 模拟成分在成分表中的位置（前几位为主要成分）
                position = key_ingredients.index(ingredient_name) + 1
                
                session.execute(
                    ingredient_product_association.insert().values(
                        ingredient_id=ingredient_id,
                        product_id=product.id,
                        concentration=None,  # 大部分产品不公开具体浓度
                        position_in_list=position,
                        is_active=True
                    )
                )
        
        # 建立肤质关联
        for skin_type_name in suitable_skin_types:
            if skin_type_name in skin_type_map:
                skin_type_id = skin_type_map[skin_type_name]
                session.execute(
                    product_skintype_association.insert().values(
                        product_id=product.id,
                        skintype_id=skin_type_id
                    )
                )
    
    session.commit()
    print(f"产品初始化完成，共添加 {len(all_products)} 个产品")

if __name__ == "__main__":
    print("开始初始化产品数据...")
    
    # 清空现有产品数据
    session.execute(product_skintype_association.delete())
    session.execute(ingredient_product_association.delete())
    session.query(Product).delete()
    session.commit()
    
    # 初始化产品数据
    init_products()
    
    session.close()
    print("产品数据初始化完成！")

