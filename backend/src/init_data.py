"""
初始化化妆品成分筛选系统数据
"""
import sys
import os
# 确保可以导入 src.models.cosmetic
# 这里的路径是基于用户在 backend 目录下运行 python src/init_data.py 的假设
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.cosmetic import Base, EffectCategory, Ingredient, Product, SkinType, IngredientInteraction
from src.models.cosmetic import effect_ingredient_association, ingredient_product_association, product_skintype_association

# 创建数据库连接
# Use a relative path to the current directory for portability
# 确保在运行脚本的目录下创建 cosmetic.db
DATABASE_URL = "sqlite:///cosmetic.db"
engine = create_engine(DATABASE_URL)

# 确保所有表都被创建
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def init_effect_categories():
    """初始化功效类别"""
    effects = [
        {
            "name": "美白淡斑",
            "description": "抑制黑色素生成，淡化色斑，提亮肤色",
            "icon": "brightness"
        },
        {
            "name": "抗衰老",
            "description": "减少皱纹，提升肌肤弹性，延缓衰老",
            "icon": "anti-aging"
        },
        {
            "name": "保湿补水",
            "description": "增强肌肤保湿能力，维持水油平衡",
            "icon": "droplet"
        },
        {
            "name": "控油祛痘",
            "description": "调节油脂分泌，抗炎祛痘，改善肌肤状态",
            "icon": "shield"
        },
        {
            "name": "舒缓修护",
            "description": "舒缓敏感肌肤，修护肌肤屏障",
            "icon": "heart"
        },
        {
            "name": "去角质",
            "description": "温和去除老化角质，促进肌肤更新",
            "icon": "refresh"
        }
    ]
    
    for effect_data in effects:
        effect = EffectCategory(**effect_data)
        session.add(effect)
    
    session.commit()
    print("功效类别初始化完成")

def init_ingredients():
    """初始化成分数据"""
    # 美白淡斑成分 - 化学合成成分
    whitening_chemical = [
        {"name": "氢醌", "english_name": "Hydroquinone", "inci_name": "Hydroquinone", "efficacy_score": 9.5, "evidence_level": "A", "mechanism": "直接抑制酪氨酸酶活性，阻断黑色素生成", "effective_concentration": "2%-4%", "safety_level": "处方药", "side_effects": "可能引起皮肤刺激，长期使用需医生指导"},
        {"name": "间苯二酚", "english_name": "Resorcinol", "inci_name": "Resorcinol", "efficacy_score": 7.0, "evidence_level": "B", "mechanism": "抑制酪氨酸酶活性，具有剥脱作用", "effective_concentration": "0.5%-2%", "safety_level": "中等", "side_effects": "可能引起刺激和过敏"},
        {"name": "苯乙基间苯二酚", "english_name": "Phenylethyl Resorcinol", "inci_name": "Phenylethyl Resorcinol", "efficacy_score": 8.8, "evidence_level": "A", "mechanism": "强效抑制酪氨酸酶，比氢醌温和", "effective_concentration": "0.1%-1%", "safety_level": "较安全", "side_effects": "极少数人可能出现轻微刺激"},
        {"name": "丁基间苯二酚", "english_name": "Butylresorcinol", "inci_name": "Butylresorcinol", "efficacy_score": 8.7, "evidence_level": "A", "mechanism": "抑制酪氨酸酶和TRP-1，减少黑色素生成", "effective_concentration": "0.1%-0.5%", "safety_level": "较安全", "side_effects": "刺激性较低"},
        {"name": "己基间苯二酚", "english_name": "Hexylresorcinol", "inci_name": "Hexylresorcinol", "efficacy_score": 8.5, "evidence_level": "A", "mechanism": "抑制酪氨酸酶，抗糖化", "effective_concentration": "0.5%-1%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "壬二酰二甘氨酸钾", "english_name": "Potassium Azeloyl Diglycinate", "inci_name": "Potassium Azeloyl Diglycinate", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "壬二酸衍生物，控油美白，温和", "effective_concentration": "5%-10%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "4-丁基间苯二酚", "english_name": "4-Butylresorcinol", "inci_name": "4-Butylresorcinol", "efficacy_score": 8.9, "evidence_level": "A", "mechanism": "强效酪氨酸酶抑制剂，美白效果显著", "effective_concentration": "0.1%-0.3%", "safety_level": "较安全", "side_effects": "刺激性较低"},
        {"name": "氨甲环酸", "english_name": "Tranexamic Acid", "inci_name": "Tranexamic Acid", "efficacy_score": 8.5, "evidence_level": "A", "mechanism": "抑制纤溶酶原激活，减少黑色素生成", "effective_concentration": "2%-5%", "safety_level": "安全", "side_effects": "极少副作用"},
        {"name": "烟酰胺", "english_name": "Niacinamide", "inci_name": "Niacinamide", "efficacy_score": 8.5, "evidence_level": "A", "mechanism": "阻断黑色素向角质细胞转移，抗炎", "effective_concentration": "2%-10%", "safety_level": "非常安全", "side_effects": "极少副作用，耐受性好"},
        {"name": "维生素C", "english_name": "L-Ascorbic Acid", "inci_name": "Ascorbic Acid", "efficacy_score": 9.2, "evidence_level": "A", "mechanism": "抑制酪氨酸酶活性，阻断黑色素生成，促进胶原蛋白合成", "effective_concentration": "5%-20%", "safety_level": "安全", "side_effects": "高浓度可能刺激敏感肌肤"},
        {"name": "抗坏血酸葡糖苷", "english_name": "Ascorbyl Glucoside", "inci_name": "Ascorbyl Glucoside", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "稳定的维生素C衍生物，温和美白", "effective_concentration": "1%-5%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "3-邻-乙基抗坏血酸", "english_name": "3-O-Ethyl Ascorbic Acid", "inci_name": "3-O-Ethyl Ascorbic Acid", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "稳定的维生素C衍生物，渗透性好", "effective_concentration": "1%-5%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "抗坏血酸磷酸酯镁", "english_name": "Magnesium Ascorbyl Phosphate", "inci_name": "Magnesium Ascorbyl Phosphate", "efficacy_score": 7.8, "evidence_level": "A", "mechanism": "稳定的维生素C衍生物，抗氧化美白", "effective_concentration": "1%-3%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "抗坏血酸磷酸酯钠", "english_name": "Sodium Ascorbyl Phosphate", "inci_name": "Sodium Ascorbyl Phosphate", "efficacy_score": 7.8, "evidence_level": "A", "mechanism": "稳定的维生素C衍生物，抗氧化美白", "effective_concentration": "1%-3%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "抗坏血酸四异棕榈酸酯", "english_name": "Tetrahexyldecyl Ascorbate", "inci_name": "Tetrahexyldecyl Ascorbate", "efficacy_score": 8.2, "evidence_level": "A", "mechanism": "脂溶性维生素C衍生物，渗透性好，温和", "effective_concentration": "0.5%-2%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "曲酸", "english_name": "Kojic Acid", "inci_name": "Kojic Acid", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "螯合铜离子，抑制酪氨酸酶活性", "effective_concentration": "1%-4%", "safety_level": "中等", "side_effects": "可能引起接触性皮炎"},
        {"name": "曲酸双棕榈酸酯", "english_name": "Kojic Dipalmitate", "inci_name": "Kojic Dipalmitate", "efficacy_score": 7.5, "evidence_level": "B", "mechanism": "曲酸衍生物，稳定性更好，美白", "effective_concentration": "1%-3%", "safety_level": "较安全", "side_effects": "刺激性较低"},
        {"name": "熊果苷", "english_name": "Arbutin", "inci_name": "Arbutin", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "抑制酪氨酸酶活性，美白", "effective_concentration": "1%-7%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "α-熊果苷", "english_name": "Alpha-Arbutin", "inci_name": "Alpha-Arbutin", "efficacy_score": 8.5, "evidence_level": "A", "mechanism": "比β-熊果苷活性更强", "effective_concentration": "0.5%-2%", "safety_level": "安全", "side_effects": "刺激性极低"},
        {"name": "脱氧熊果苷", "english_name": "Deoxyarbutin", "inci_name": "Deoxyarbutin", "efficacy_score": 8.8, "evidence_level": "A", "mechanism": "强效酪氨酸酶抑制剂，美白效果显著", "effective_concentration": "0.1%-0.5%", "safety_level": "较安全", "side_effects": "刺激性较低"},
        {"name": "壬二酸", "english_name": "Azelaic Acid", "inci_name": "Azelaic Acid", "efficacy_score": 8.2, "evidence_level": "A", "mechanism": "抑制酪氨酸酶，具有抗炎作用", "effective_concentration": "10%-20%", "safety_level": "安全", "side_effects": "初期可能有轻微刺激"},
        {"name": "视黄醇", "english_name": "Retinol", "inci_name": "Retinol", "efficacy_score": 9.0, "evidence_level": "A", "mechanism": "促进细胞更新，加速黑色素代谢", "effective_concentration": "0.25%-1%", "safety_level": "需谨慎", "side_effects": "可能引起刺激，需建立耐受"},
        {"name": "羟基乙酸", "english_name": "Glycolic Acid", "inci_name": "Glycolic Acid", "efficacy_score": 7.5, "evidence_level": "A", "mechanism": "剥脱角质，促进黑色素代谢", "effective_concentration": "5%-30%", "safety_level": "需谨慎", "side_effects": "可能引起刺激和光敏"},
        {"name": "乳酸", "english_name": "Lactic Acid", "inci_name": "Lactic Acid", "efficacy_score": 7.2, "evidence_level": "A", "mechanism": "温和剥脱，促进细胞更新", "effective_concentration": "5%-20%", "safety_level": "较安全", "side_effects": "比甘醇酸温和"},
        {"name": "杏仁酸", "english_name": "Mandelic Acid", "inci_name": "Mandelic Acid", "efficacy_score": 7.0, "evidence_level": "B", "mechanism": "温和剥脱，适合敏感肌", "effective_concentration": "5%-25%", "safety_level": "安全", "side_effects": "刺激性最低的果酸"},
        {"name": "水杨酸", "english_name": "Salicylic Acid", "inci_name": "Salicylic Acid", "efficacy_score": 7.8, "evidence_level": "A", "mechanism": "脂溶性，深入毛孔剥脱", "effective_concentration": "0.5%-2%", "safety_level": "较安全", "side_effects": "可能引起干燥"},
        {"name": "辛酰水杨酸", "english_name": "Capryloyl Salicylic Acid", "inci_name": "Capryloyl Salicylic Acid", "efficacy_score": 7.9, "evidence_level": "A", "mechanism": "水杨酸衍生物，更温和，具有抗菌抗炎作用", "effective_concentration": "0.5%-2%", "safety_level": "较安全", "side_effects": "刺激性较低"},
        {"name": "四氢姜黄素", "english_name": "Tetrahydrocurcumin", "inci_name": "Tetrahydrocurcumin", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "强效抗氧化，抑制酪氨酸酶", "effective_concentration": "0.1%-1%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "十一碳烯酰基苯丙氨酸", "english_name": "Undecylenoyl Phenylalanine", "inci_name": "Undecylenoyl Phenylalanine", "efficacy_score": 8.2, "evidence_level": "A", "mechanism": "抑制黑色素细胞活性，减少黑色素生成", "effective_concentration": "0.5%-2%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "甲基葡糖醇聚醚-20", "english_name": "Methyl Gluceth-20", "inci_name": "Methyl Gluceth-20", "efficacy_score": 6.5, "evidence_level": "C", "mechanism": "保湿剂，辅助美白成分渗透", "effective_concentration": "1%-5%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "鞣花酸", "english_name": "Ellagic Acid", "inci_name": "Ellagic Acid", "efficacy_score": 8.3, "evidence_level": "A", "mechanism": "抗氧化，抑制酪氨酸酶，减少黑色素生成", "effective_concentration": "0.5%-1%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "白藜芦醇", "english_name": "Resveratrol", "inci_name": "Resveratrol", "efficacy_score": 8.5, "evidence_level": "A", "mechanism": "强效抗氧化，抑制酪氨酸酶，抗炎", "effective_concentration": "0.5%-1%", "safety_level": "安全", "side_effects": "刺激性较低"},
        {"name": "四肽-30", "english_name": "Tetrapeptide-30", "inci_name": "Tetrapeptide-30", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "抑制黑色素生成，提亮肤色", "effective_concentration": "0.001%-0.01%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "九肽-1", "english_name": "Nonapeptide-1", "inci_name": "Nonapeptide-1", "efficacy_score": 7.8, "evidence_level": "A", "mechanism": "抑制黑色素细胞活性，减少黑色素生成", "effective_concentration": "0.001%-0.01%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "乙酰壳糖胺", "english_name": "Acetyl Glucosamine", "inci_name": "Acetyl Glucosamine", "efficacy_score": 7.5, "evidence_level": "B", "mechanism": "促进角质更新，辅助美白，保湿", "effective_concentration": "2%-5%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "泛酸", "english_name": "Pantothenic Acid", "inci_name": "Pantothenic Acid", "efficacy_score": 6.8, "evidence_level": "C", "mechanism": "维生素B5，保湿修复，辅助美白", "effective_concentration": "1%-5%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "曲酸棕榈酸酯", "english_name": "Kojic Acid Palmitate", "inci_name": "Kojic Acid Palmitate", "efficacy_score": 7.5, "evidence_level": "B", "mechanism": "曲酸衍生物，稳定性好，美白", "effective_concentration": "1%-3%", "safety_level": "较安全", "side_effects": "刺激性较低"},
        {"name": "二甲氧基甲苯基-4-丙基间苯二酚", "english_name": "Dimethoxytolyl Propylresorcinol", "inci_name": "Dimethoxytolyl Propylresorcinol", "efficacy_score": 8.6, "evidence_level": "A", "mechanism": "强效酪氨酸酶抑制剂，美白", "effective_concentration": "0.1%-0.5%", "safety_level": "较安全", "side_effects": "刺激性较低"},
    ]
    
    # 抗衰老成分 - 肽类
    anti_aging_peptides = [
        {"name": "棕榈酰三肽-1", "english_name": "Palmitoyl Tripeptide-1", "inci_name": "Palmitoyl Tripeptide-1", "efficacy_score": 8.5, "evidence_level": "A", "mechanism": "促进胶原蛋白和弹性蛋白生成", "effective_concentration": "0.001%-0.01%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "棕榈酰四肽-7", "english_name": "Palmitoyl Tetrapeptide-7", "inci_name": "Palmitoyl Tetrapeptide-7", "efficacy_score": 8.5, "evidence_level": "A", "mechanism": "抗炎，减少基质金属蛋白酶（MMPs）活性", "effective_concentration": "0.001%-0.01%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "棕榈酰五肽-4", "english_name": "Palmitoyl Pentapeptide-4", "inci_name": "Palmitoyl Pentapeptide-4", "efficacy_score": 9.0, "evidence_level": "A", "mechanism": "促进I型、III型胶原蛋白和纤维连接蛋白生成", "effective_concentration": "0.001%-0.01%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "乙酰基六肽-8", "english_name": "Acetyl Hexapeptide-8", "inci_name": "Acetyl Hexapeptide-8", "efficacy_score": 8.0, "evidence_level": "B", "mechanism": "抑制神经递质释放，减少表情纹", "effective_concentration": "3%-10%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "二肽二氨基丁酰苄基酰胺二乙酸盐", "english_name": "Dipeptide Diaminobutyroyl Benzylamide Diacetate", "inci_name": "Dipeptide Diaminobutyroyl Benzylamide Diacetate", "efficacy_score": 7.8, "evidence_level": "B", "mechanism": "模拟蛇毒血清作用，放松肌肉，减少皱纹", "effective_concentration": "1%-4%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "三氟乙酰三肽-2", "english_name": "Trifluoroacetyl Tripeptide-2", "inci_name": "Trifluoroacetyl Tripeptide-2", "efficacy_score": 8.2, "evidence_level": "A", "mechanism": "抑制早衰蛋白（Progerin）合成，紧致肌肤", "effective_concentration": "0.001%-0.01%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "六肽-9", "english_name": "Hexapeptide-9", "inci_name": "Hexapeptide-9", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "促进胶原蛋白VII型合成，修复真皮-表皮连接处", "effective_concentration": "0.001%-0.01%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "铜肽", "english_name": "Copper Tripeptide-1", "inci_name": "Copper Tripeptide-1", "efficacy_score": 8.8, "evidence_level": "A", "mechanism": "促进胶原蛋白生成，抗氧化，修复", "effective_concentration": "0.001%-0.01%", "safety_level": "安全", "side_effects": "无明显副作用"},
    ]
    
    # 抗衰老成分 - 维生素A类
    anti_aging_retinoids = [
        {"name": "视黄醇", "english_name": "Retinol", "inci_name": "Retinol", "efficacy_score": 9.0, "evidence_level": "A", "mechanism": "促进细胞更新，刺激胶原蛋白生成", "effective_concentration": "0.25%-1%", "safety_level": "需谨慎", "side_effects": "可能引起刺激，需建立耐受"},
        {"name": "视黄醇棕榈酸酯", "english_name": "Retinyl Palmitate", "inci_name": "Retinyl Palmitate", "efficacy_score": 7.5, "evidence_level": "B", "mechanism": "视黄醇衍生物，温和，抗氧化", "effective_concentration": "0.5%-2%", "safety_level": "安全", "side_effects": "刺激性低"},
        {"name": "视黄醇乙酸酯", "english_name": "Retinyl Acetate", "inci_name": "Retinyl Acetate", "efficacy_score": 7.5, "evidence_level": "B", "mechanism": "视黄醇衍生物，温和，抗氧化", "effective_concentration": "0.5%-2%", "safety_level": "安全", "side_effects": "刺激性低"},
        {"name": "视黄醛", "english_name": "Retinaldehyde", "inci_name": "Retinaldehyde", "efficacy_score": 9.2, "evidence_level": "A", "mechanism": "比视黄醇更有效，刺激性低于视黄酸", "effective_concentration": "0.05%-0.1%", "safety_level": "较安全", "side_effects": "初期可能刺激"},
        {"name": "羟基频哪酮视黄酸酯", "english_name": "Hydroxypinacolone Retinoate", "inci_name": "Hydroxypinacolone Retinoate", "efficacy_score": 9.0, "evidence_level": "A", "mechanism": "新型维A酯，直接作用于受体，刺激性低", "effective_concentration": "0.1%-0.5%", "safety_level": "安全", "side_effects": "刺激性极低"},
    ]
    
    # 保湿补水成分
    moisturizing = [
        {"name": "透明质酸钠", "english_name": "Sodium Hyaluronate", "inci_name": "Sodium Hyaluronate", "efficacy_score": 9.5, "evidence_level": "A", "mechanism": "强效吸湿剂，在皮肤表面形成水膜", "effective_concentration": "0.1%-1%", "safety_level": "非常安全", "side_effects": "无明显副作用"},
        {"name": "神经酰胺", "english_name": "Ceramide", "inci_name": "Ceramide", "efficacy_score": 9.8, "evidence_level": "A", "mechanism": "皮肤屏障重要组成部分，修复屏障，锁水", "effective_concentration": "0.1%-1%", "safety_level": "非常安全", "side_effects": "无明显副作用"},
        {"name": "甘油", "english_name": "Glycerin", "inci_name": "Glycerin", "efficacy_score": 9.0, "evidence_level": "A", "mechanism": "经典吸湿剂，从空气中吸收水分", "effective_concentration": "5%-20%", "safety_level": "非常安全", "side_effects": "无明显副作用"},
        {"name": "角鲨烷", "english_name": "Squalane", "inci_name": "Squalane", "efficacy_score": 9.0, "evidence_level": "A", "mechanism": "天然皮脂成分，润肤剂，防止水分流失", "effective_concentration": "1%-10%", "safety_level": "非常安全", "side_effects": "无明显副作用"},
        {"name": "尿素", "english_name": "Urea", "inci_name": "Urea", "efficacy_score": 8.5, "evidence_level": "A", "mechanism": "天然保湿因子（NMF）成分，高浓度可去角质", "effective_concentration": "2%-10%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "泛醇", "english_name": "Panthenol", "inci_name": "Panthenol", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "维生素B5前体，保湿，促进伤口愈合", "effective_concentration": "1%-5%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "聚谷氨酸", "english_name": "Polyglutamic Acid", "inci_name": "Polyglutamic Acid", "efficacy_score": 9.2, "evidence_level": "A", "mechanism": "强效吸湿剂，保湿能力优于透明质酸", "effective_concentration": "0.1%-0.5%", "safety_level": "安全", "side_effects": "无明显副作用"},
    ]
    
    # 控油祛痘成分
    acne_control = [
        {"name": "水杨酸", "english_name": "Salicylic Acid", "inci_name": "Salicylic Acid", "efficacy_score": 8.5, "evidence_level": "A", "mechanism": "脂溶性，深入毛孔溶解油脂，抗炎", "effective_concentration": "0.5%-2%", "safety_level": "较安全", "side_effects": "可能引起干燥"},
        {"name": "壬二酸", "english_name": "Azelaic Acid", "inci_name": "Azelaic Acid", "efficacy_score": 8.8, "evidence_level": "A", "mechanism": "抗菌，抗炎，抑制角质形成细胞增殖", "effective_concentration": "10%-20%", "safety_level": "安全", "side_effects": "初期可能有轻微刺激"},
        {"name": "过氧化苯甲酰", "english_name": "Benzoyl Peroxide", "inci_name": "Benzoyl Peroxide", "efficacy_score": 9.0, "evidence_level": "A", "mechanism": "强效杀菌剂，对痤疮丙酸杆菌有效", "effective_concentration": "2.5%-10%", "safety_level": "需谨慎", "side_effects": "可能引起干燥，脱皮，漂白衣物"},
        {"name": "硫磺", "english_name": "Sulfur", "inci_name": "Sulfur", "efficacy_score": 7.0, "evidence_level": "B", "mechanism": "角质溶解，抗菌", "effective_concentration": "3%-10%", "safety_level": "安全", "side_effects": "气味较大，可能干燥"},
        {"name": "烟酰胺", "english_name": "Niacinamide", "inci_name": "Niacinamide", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "控油，抗炎，减少红肿", "effective_concentration": "2%-10%", "safety_level": "非常安全", "side_effects": "极少副作用"},
        {"name": "茶树油", "english_name": "Tea Tree Oil", "inci_name": "Melaleuca Alternifolia Leaf Oil", "efficacy_score": 7.5, "evidence_level": "B", "mechanism": "天然抗菌剂，抗炎", "effective_concentration": "5%-15%", "safety_level": "较安全", "side_effects": "可能引起接触性皮炎"},
    ]
    
    # 舒缓修护成分
    soothing_repair = [
        {"name": "积雪草提取物", "english_name": "Centella Asiatica Extract", "inci_name": "Centella Asiatica Extract", "efficacy_score": 9.0, "evidence_level": "A", "mechanism": "促进胶原蛋白合成，抗炎，修复屏障", "effective_concentration": "1%-5%", "safety_level": "非常安全", "side_effects": "无明显副作用"},
        {"name": "马齿苋提取物", "english_name": "Portulaca Oleracea Extract", "inci_name": "Portulaca Oleracea Extract", "efficacy_score": 8.5, "evidence_level": "A", "mechanism": "抗炎，抗过敏，舒缓镇静", "effective_concentration": "1%-5%", "safety_level": "非常安全", "side_effects": "无明显副作用"},
        {"name": "红没药醇", "english_name": "Bisabolol", "inci_name": "Bisabolol", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "洋甘菊主要成分，抗炎，舒缓", "effective_concentration": "0.1%-1%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "尿囊素", "english_name": "Allantoin", "inci_name": "Allantoin", "efficacy_score": 7.5, "evidence_level": "A", "mechanism": "促进细胞再生，舒缓，保湿", "effective_concentration": "0.1%-2%", "safety_level": "安全", "side_effects": "无明显副作用"},
        {"name": "神经酰胺", "english_name": "Ceramide", "inci_name": "Ceramide", "efficacy_score": 9.8, "evidence_level": "A", "mechanism": "皮肤屏障重要组成部分，修复屏障，锁水", "effective_concentration": "0.1%-1%", "safety_level": "非常安全", "side_effects": "无明显副作用"},
        {"name": "泛醇", "english_name": "Panthenol", "inci_name": "Panthenol", "efficacy_score": 8.0, "evidence_level": "A", "mechanism": "维生素B5前体，保湿，促进伤口愈合", "effective_concentration": "1%-5%", "safety_level": "安全", "side_effects": "无明显副作用"},
    ]
    
    all_ingredients = (
        whitening_chemical + 
        anti_aging_peptides + 
        anti_aging_retinoids + 
        moisturizing + 
        acne_control + 
        soothing_repair
    )
    
    for ingredient_data in all_ingredients:
        ingredient = Ingredient(**ingredient_data)
        session.add(ingredient)
    
    session.commit()
    print("成分数据初始化完成")

def init_effect_ingredient_association():
    """初始化功效与成分的关联数据"""
    # 功效名称到ID的映射
    effect_map = {e.name: e.id for e in session.query(EffectCategory).all()}
    # 成分名称到ID的映射
    ingredient_map = {i.name: i.id for i in session.query(Ingredient).all()}
    
    associations = [
        # 美白淡斑
        ("美白淡斑", ["氢醌", "间苯二酚", "苯乙基间苯二酚", "丁基间苯二酚", "己基间苯二酚", "壬二酰二甘氨酸钾", "4-丁基间苯二酚", "氨甲环酸", "烟酰胺", "维生素C", "抗坏血酸葡糖苷", "3-邻-乙基抗坏血酸", "抗坏血酸磷酸酯镁", "抗坏血酸磷酸酯钠", "抗坏血酸四异棕榈酸酯", "曲酸", "曲酸双棕榈酸酯", "熊果苷", "α-熊果苷", "脱氧熊果苷", "壬二酸", "视黄醇", "羟基乙酸", "乳酸", "杏仁酸", "水杨酸", "辛酰水杨酸", "四氢姜黄素", "十一碳烯酰基苯丙氨酸", "鞣花酸", "白藜芦醇", "四肽-30", "九肽-1", "乙酰壳糖胺", "泛酸", "曲酸棕榈酸酯", "二甲氧基甲苯基-4-丙基间苯二酚"]),
        # 抗衰老
        ("抗衰老", ["棕榈酰三肽-1", "棕榈酰四肽-7", "棕榈酰五肽-4", "乙酰基六肽-8", "二肽二氨基丁酰苄基酰胺二乙酸盐", "三氟乙酰三肽-2", "六肽-9", "铜肽", "视黄醇", "视黄醇棕榈酸酯", "视黄醇乙酸酯", "视黄醛", "羟基频哪酮视黄酸酯", "白藜芦醇"]),
        # 保湿补水
        ("保湿补水", ["透明质酸钠", "神经酰胺", "甘油", "角鲨烷", "尿素", "泛醇", "聚谷氨酸", "乙酰壳糖胺", "泛酸"]),
        # 控油祛痘
        ("控油祛痘", ["水杨酸", "壬二酸", "过氧化苯甲酰", "硫磺", "烟酰胺", "茶树油"]),
        # 舒缓修护
        ("舒缓修护", ["积雪草提取物", "马齿苋提取物", "红没药醇", "尿囊素", "神经酰胺", "泛醇", "烟酰胺"]),
        # 去角质
        ("去角质", ["羟基乙酸", "乳酸", "杏仁酸", "水杨酸", "辛酰水杨酸", "尿素"]),
    ]
    
    for effect_name, ingredient_names in associations:
        effect_id = effect_map.get(effect_name)
        if effect_id:
            for ingredient_name in ingredient_names:
                ingredient_id = ingredient_map.get(ingredient_name)
                if ingredient_id:
                    # 检查是否已存在
                    exists = session.query(effect_ingredient_association).filter_by(
                        effect_id=effect_id, 
                        ingredient_id=ingredient_id
                    ).first()
                    if not exists:
                        insert_stmt = effect_ingredient_association.insert().values(
                            effect_id=effect_id, 
                            ingredient_id=ingredient_id
                        )
                        session.execute(insert_stmt)
    
    session.commit()
    print("功效与成分关联完成")

def init_skin_types():
    """初始化肤质数据"""
    skin_types = [
        {
            "name": "干性皮肤",
            "description": "皮脂分泌少，皮肤干燥，缺乏光泽，易产生细纹。",
            "characteristics": "紧绷感，易脱皮，对环境变化敏感。",
            "care_tips": "使用高保湿、高滋润度的产品，注重屏障修复。"
        },
        {
            "name": "油性皮肤",
            "description": "皮脂分泌旺盛，皮肤油光，毛孔粗大，易长粉刺和痤疮。",
            "characteristics": "T区油光明显，妆容易脱，不易产生皱纹。",
            "care_tips": "使用清爽、控油、非致粉刺性产品，注重清洁和水油平衡。"
        },
        {
            "name": "混合性皮肤",
            "description": "T区（额头、鼻子、下巴）油腻，U区（脸颊）干燥或正常。",
            "characteristics": "护理难度较大，需分区护理。",
            "care_tips": "T区控油，U区保湿，避免使用过于滋润或过于刺激的产品。"
        },
        {
            "name": "中性皮肤",
            "description": "水油平衡，皮肤光滑细腻，毛孔不明显，是理想的皮肤类型。",
            "characteristics": "无明显皮肤问题，对外界刺激耐受性好。",
            "care_tips": "维持现状，注重基础保湿和防晒。"
        },
        {
            "name": "敏感性皮肤",
            "description": "皮肤屏障受损，易受外界刺激（如温度、化妆品）而产生红肿、刺痛、瘙痒等反应。",
            "characteristics": "皮肤薄，可见红血丝，易过敏。",
            "care_tips": "使用温和、无添加、修复屏障的产品，避免刺激性成分。"
        }
    ]
    
    for skin_type_data in skin_types:
        skin_type = SkinType(**skin_type_data)
        session.add(skin_type)
    
    session.commit()
    print("肤质数据初始化完成")

def init_ingredient_interactions():
    """初始化成分相互作用数据"""
    # 成分名称到ID的映射
    ingredient_map = {i.name: i.id for i in session.query(Ingredient).all()}
    
    interactions = [
        # 协同作用 (Synergy)
        {"ingredient1": "烟酰胺", "ingredient2": "维生素C", "type": "协同", "description": "烟酰胺（B3）和维生素C（抗坏血酸）共同使用可以增强美白和抗氧化效果，但需注意烟酰胺可能影响纯维生素C的稳定性，建议使用稳定的维生素C衍生物或错开使用。", "recommendation": "建议使用稳定的维生素C衍生物（如抗坏血酸葡糖苷）或早C晚A（早晨使用维生素C，晚上使用烟酰胺）。"},
        {"ingredient1": "视黄醇", "ingredient2": "神经酰胺", "type": "协同", "description": "视黄醇（维A醇）具有刺激性，神经酰胺可以修复皮肤屏障，两者搭配使用可以减轻视黄醇带来的刺激和干燥。", "recommendation": "在视黄醇产品后使用含有神经酰胺的保湿霜，或选择含有神经酰胺的视黄醇配方。"},
        {"ingredient1": "水杨酸", "ingredient2": "烟酰胺", "type": "协同", "description": "水杨酸去角质、疏通毛孔，烟酰胺控油、抗炎，两者搭配对控油祛痘有很好的协同作用。", "recommendation": "可以搭配使用，但敏感肌需谨慎，建议先建立耐受。"},
        {"ingredient1": "透明质酸钠", "ingredient2": "甘油", "type": "协同", "description": "两者都是优秀的吸湿剂，共同使用可以提供多层次的保湿效果。", "recommendation": "日常保湿的黄金搭档，可放心使用。"},
        
        # 拮抗作用 (Antagonism) - 实际应用中多为刺激性叠加
        {"ingredient1": "视黄醇", "ingredient2": "羟基乙酸", "type": "拮抗", "description": "视黄醇和羟基乙酸（果酸）都具有较强的刺激性和剥脱性，同时使用会大大增加皮肤刺激、泛红和敏感的风险。", "recommendation": "不建议同时使用，应错开早晚或隔天使用，并严格建立耐受。"},
        {"ingredient1": "水杨酸", "ingredient2": "过氧化苯甲酰", "type": "拮抗", "description": "两者都是强效的祛痘成分，同时使用会过度干燥和刺激皮肤，可能导致皮肤屏障受损。", "recommendation": "不建议同时使用，应错开早晚或隔天使用。"},
        
        # 禁忌 (Contraindication) - 实际应用中极少有绝对禁忌，多为刺激性叠加
        {"ingredient1": "氢醌", "ingredient2": "过氧化苯甲酰", "type": "禁忌", "description": "氢醌与过氧化苯甲酰同时使用会发生化学反应，导致皮肤染色（变黑）。", "recommendation": "绝对禁止同时使用，应完全错开使用。"},
    ]
    
    for interaction_data in interactions:
        ing1_id = ingredient_map.get(interaction_data["ingredient1"])
        ing2_id = ingredient_map.get(interaction_data["ingredient2"])
        
        if ing1_id and ing2_id:
            # 确保 ingredient1_id < ingredient2_id，避免重复添加
            if ing1_id > ing2_id:
                ing1_id, ing2_id = ing2_id, ing1_id
            
            # 检查是否已存在
            exists = session.query(IngredientInteraction).filter(
                IngredientInteraction.ingredient1_id == ing1_id,
                IngredientInteraction.ingredient2_id == ing2_id
            ).first()
            
            if not exists:
                interaction = IngredientInteraction(
                    ingredient1_id=ing1_id,
                    ingredient2_id=ing2_id,
                    type=interaction_data["type"], # 修复后的字段名
                    description=interaction_data["description"],
                    recommendation=interaction_data["recommendation"]
                )
                session.add(interaction)
    
    session.commit()
    print("成分相互作用数据初始化完成")

def main():
    """主函数"""
    try:
        # 1. 确保数据库和表已创建
        # 这一步在文件开头已经执行，但为了确保万无一失，可以再执行一次
        Base.metadata.create_all(engine)
        
        # 2. 初始化基础数据
        init_effect_categories()
        init_ingredients()
        init_effect_ingredient_association()
        init_skin_types()
        init_ingredient_interactions()
        
        # 3. 提示用户运行产品数据初始化脚本
        print("\n--- 提示 ---")
        print("基础数据（功效、成分、肤质、相互作用）初始化成功。")
        print("请手动运行产品数据初始化脚本：")
        print("    python src/init_products.py")
        print("----------------\n")
        
    except Exception as e:
        print(f"数据初始化失败: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == '__main__':
    main()

