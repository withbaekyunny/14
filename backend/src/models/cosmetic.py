"""
化妆品成分筛选系统数据模型
"""
from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# 多对多关系表：功效-成分
effect_ingredient_association = Table(
    'effect_ingredient',
    Base.metadata,
    Column('effect_id', Integer, ForeignKey('effect_categories.id', ondelete="CASCADE"), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id', ondelete="CASCADE"), primary_key=True)
)

# 多对多关系表：成分-产品
ingredient_product_association = Table(
    'ingredient_product',
    Base.metadata,
    Column('ingredient_id', Integer, ForeignKey('ingredients.id', ondelete="CASCADE"), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id', ondelete="CASCADE"), primary_key=True),
    Column('concentration_level', String(50)), # 成分浓度等级（High/Medium/Low）
    Column('position_in_list', Integer),  # 在成分表中的位置
    Column('is_active', Boolean, default=True)  # 是否为活性成分
)

# 多对多关系表：产品-肤质
product_skintype_association = Table(
    'product_skintype',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id', ondelete="CASCADE"), primary_key=True),
    Column('skintype_id', Integer, ForeignKey('skin_types.id', ondelete="CASCADE"), primary_key=True)
)

class EffectCategory(Base):
    """功效类别表"""
    __tablename__ = 'effect_categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    icon = Column(String(50))
    
    ingredients = relationship(
        "Ingredient",
        secondary=effect_ingredient_association,
        back_populates="effects"
    )

class Ingredient(Base):
    """成分表"""
    __tablename__ = 'ingredients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
    english_name = Column(String(200))
    inci_name = Column(String(200))
    efficacy_score = Column(Float)
    evidence_level = Column(String(10))
    mechanism = Column(Text)
    effective_concentration = Column(String(100))
    safety_level = Column(String(20))
    side_effects = Column(Text)
    
    effects = relationship(
        "EffectCategory",
        secondary=effect_ingredient_association,
        back_populates="ingredients"
    )
    products = relationship(
        "Product",
        secondary=ingredient_product_association,
        back_populates="ingredients"
    )

class Product(Base):
    """产品表"""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False, unique=True)
    brand = Column(String(100))
    category = Column(String(50))
    price = Column(Float)
    volume = Column(String(50))
    description = Column(Text)
    full_ingredients = Column(Text)
    purchase_link = Column(String(500))
    image_url = Column(String(500))
    
    ingredients = relationship(
        "Ingredient",
        secondary=ingredient_product_association,
        back_populates="products"
    )
    suitable_skin_types = relationship(
        "SkinType",
        secondary=product_skintype_association,
        back_populates="suitable_products"
    )

class SkinType(Base):
    """肤质类型表"""
    __tablename__ = 'skin_types'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text)
    characteristics = Column(Text)
    care_tips = Column(Text)
    
    suitable_products = relationship(
        "Product",
        secondary=product_skintype_association,
        back_populates="suitable_skin_types"
    )

class IngredientInteraction(Base):
    """成分相互作用表"""
    __tablename__ = 'ingredient_interactions'
    
    id = Column(Integer, primary_key=True)
    ingredient1_id = Column(Integer, ForeignKey('ingredients.id'))
    ingredient2_id = Column(Integer, ForeignKey('ingredients.id'))
    type = Column(String(50))  # 协同/拮抗/禁忌
    description = Column(Text)
    recommendation = Column(Text)

