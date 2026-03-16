
"""
化妆品成分筛选系统API路由 (Neo4j Version)
"""
from flask import Blueprint, jsonify, request
from src.neo4j_db import neo4j_db

cosmetic_bp = Blueprint('cosmetic', __name__)

@cosmetic_bp.route('/api/effect-categories', methods=['GET'])
def get_effect_categories():
    """获取所有功效类别"""
    try:
        categories = neo4j_db.get_efficacies()
        return jsonify(categories)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cosmetic_bp.route('/api/ingredients/by-effect/<int:effect_id>', methods=['GET'])
def get_ingredients_by_effect(effect_id):
    """根据功效获取成分列表，按功效评分排序"""
    try:
        ingredients = neo4j_db.get_ingredients_by_efficacy(effect_id)
        result = []
        for ingredient in ingredients:
            # The '小巧思' (ingredient interactions) are fetched here
            interactions = neo4j_db.get_ingredient_interactions(ingredient['name'])
            ingredient['interactions'] = interactions
            result.append(ingredient)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cosmetic_bp.route('/api/products/by-ingredient/<string:ingredient_name>', methods=['GET'])
def get_products_by_ingredient(ingredient_name):
    """根据成分获取产品列表，按成分浓度等级排序"""
    try:
        # Note: The frontend must be updated to pass the ingredient name, not the ID.
        products = neo4j_db.get_products_by_ingredient(ingredient_name)
        return jsonify(products)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cosmetic_bp.route('/api/skin-types', methods=['GET'])
def get_skin_types():
    """获取所有肤质类型"""
    try:
        skin_types = neo4j_db.get_skin_types()
        return jsonify(skin_types)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cosmetic_bp.route('/api/products/filter', methods=['POST'])
def filter_products():
    """根据成分和肤质筛选产品 (Neo4j version)"""
    data = request.get_json()
    ingredient_name = data.get('ingredient_name')
    skin_type_names = data.get('skin_type_names', [])

    if not ingredient_name:
        return jsonify({"error": "Missing ingredient_name"}), 400

    try:
        # This is a placeholder for Phase 7 (intelligent recommendation)
        # For now, it filters by ingredient and will be expanded to use skin types
        if skin_type_names:
             # This function will be implemented in neo4j_db.py later
            products = neo4j_db.get_products_by_ingredient_and_skintypes(ingredient_name, skin_type_names)
        else:
            products = neo4j_db.get_products_by_ingredient(ingredient_name)
        
        return jsonify(products)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cosmetic_bp.route('/api/stats/overview', methods=['GET'])
def get_overview_stats():
    """获取系统概览统计"""
    try:
        stats = neo4j_db.get_overview_stats()
        return jsonify(stats)
    except Exception as e:
        # Fallback to static data if query fails
        return jsonify({
            'total_effects': 6,
            'total_ingredients': 156, # Master ingredients
            'total_products': 1138,
            'total_skin_types': 4
        })

