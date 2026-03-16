import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import { ArrowLeft, Star, StarHalf, ChevronDown, ChevronUp, Search, Filter, ShoppingCart, ExternalLink, AlertTriangle, CheckCircle } from 'lucide-react';
import './App.css';

// The base URL for the backend API
const API_BASE_URL = 'http://localhost:5000';

// Utility function for efficacy score display (simple text format, as per user's request to revert to first version style)
const EfficacyScoreDisplay = ({ score, className = "" }) => {
  const normalizedScore = Math.max(0, Math.min(10, score || 0));
  return (
    <div className={`flex items-center ${className}`}>
      <span className="text-lg font-bold text-slate-800">{normalizedScore.toFixed(1)}</span>
      <span className="ml-1 text-xs text-slate-500">/10</span>
    </div>
  );
};

// Component for displaying ingredient details with expandable sections
const IngredientDetailsCard = ({ ingredient, onClick, onShowEvidenceInfo }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  // Helper to render mechanism/clinical data with line breaks
  const renderTextWithBreaks = (text) => {
    return text.split('\n').map((line, index) => (
      <React.Fragment key={index}>
        {line}
        <br />
      </React.Fragment>
    ));
  };

  return (
    <div className="bg-white border border-gray-200 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 p-6 flex flex-col space-y-4">
      <div className="flex justify-between items-start">
        <div className="flex-1 min-w-0">
          <h3 className="text-xl font-bold text-gray-900 truncate">{ingredient.name}</h3>
          {(ingredient.english_name || ingredient.inci_name) && (
            <p className="text-sm text-gray-500 mt-1 truncate">
              {ingredient.english_name} / {ingredient.inci_name}
            </p>
          )}
        </div>
        <div className="flex-shrink-0 ml-4 flex flex-col items-end space-y-1">
          <EfficacyScoreDisplay score={ingredient.efficacy_score} className="text-lg" />
          <span onClick={onShowEvidenceInfo} className="cursor-pointer text-xs font-semibold text-sky-600 bg-sky-100 px-2 py-0.5 rounded-full hover:bg-sky-200 transition-colors">
            证据等级: {ingredient.evidence_level}
          </span>
        </div>
      </div>
      
      <div className="flex items-center space-x-4 text-sm">
        <span className={`px-3 py-1 rounded-full font-medium ${
          ingredient.safety_level_score === 1 ? 'bg-green-100 text-green-800' : 
          ingredient.safety_level_score === 2 ? 'bg-blue-100 text-blue-800' : 
          ingredient.safety_level_score === 3 ? 'bg-yellow-100 text-yellow-800' : 
          'bg-red-100 text-red-800'
        }`}>
          {ingredient.safety_level}
        </span>
        {ingredient.is_banned && (
          <span className="flex items-center text-red-600 font-semibold">
            <AlertTriangle className="w-4 h-4 mr-1" /> 已禁用/限用
          </span>
        )}
      </div>

      <div className="border-t border-gray-100 pt-4">
        <button 
          onClick={() => setIsExpanded(!isExpanded)}
          className="w-full flex justify-between items-center text-base font-medium text-blue-600 hover:text-blue-800 transition-colors"
        >
          <span>{isExpanded ? '收起详情' : '展开详情'}</span>
          {isExpanded ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
        </button>

        {isExpanded && (
          <div className="mt-4 text-sm text-gray-700 space-y-4">
            <div>
              <p className="font-semibold text-gray-900 mb-1">作用机制 (Mechanism of Action):</p>
              <div className="bg-gray-50 p-3 rounded-lg whitespace-pre-wrap">
                {renderTextWithBreaks(ingredient.mechanism || '暂无详细机制描述。')}
              </div>
            </div>
            <div>
              <p className="font-semibold text-gray-900 mb-1">临床数据/研究 (Clinical Data):</p>
              <div className="bg-gray-50 p-3 rounded-lg whitespace-pre-wrap">
                {renderTextWithBreaks(ingredient.clinical_data || '暂无详细临床数据。')}
              </div>
            </div>
            
            {/* "小巧思" - 成分相互作用警告 */}
            {ingredient.interactions && ingredient.interactions.length > 0 && (
              <div>
                <p className="font-semibold text-gray-900 mb-1 flex items-center">
                  <AlertTriangle className="w-4 h-4 mr-1 text-orange-500" /> 成分相互作用提示:
                </p>
                <div className="bg-yellow-50 p-3 rounded-lg space-y-2">
                  {ingredient.interactions.map((interaction, index) => (
                    <div key={index} className="border-l-4 border-yellow-500 pl-3">
                      <p className={`font-bold ${interaction.interaction_type === '冲突' ? 'text-red-600' : interaction.interaction_type === '协同' ? 'text-green-600' : 'text-gray-600'}`}>
                        {interaction.interaction_type}: {interaction.target_ingredient}
                      </p>
                      <p className="text-sm text-gray-700 mt-1">
                        {interaction.description}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
      
<button 
		        onClick={() => onClick(ingredient.id)}
		        className="mt-4 w-full py-2 px-4 bg-slate-800 text-white font-semibold rounded-lg shadow-md hover:bg-slate-900 transition-colors duration-200"
		      >
	        查看包含此成分的产品 ({ingredient.product_count || '...'})
	      </button>
    </div>
  );
};

// Component for displaying product cards
const ProductCard = ({ product }) => {
  return (
    <div className="bg-white border border-gray-200 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 p-6 flex flex-col space-y-3">
      <div className="flex justify-between items-start">
        <h3 className="text-xl font-bold text-gray-900">{product.name}</h3>
        <span className="text-lg font-semibold text-slate-800">${product.price ? product.price.toFixed(2) : '0.00'}</span>
      </div>
      <p className="text-sm text-gray-500">{product.brand}</p>
      
      <div className="flex items-center space-x-2 text-sm">
        <span className={`px-3 py-1 rounded-full font-medium ${
          product.concentration_level === 'High' ? 'bg-orange-100 text-orange-700' : 
          product.concentration_level === 'Medium' ? 'bg-yellow-100 text-yellow-700' : 
          'bg-green-100 text-green-700'
        }`}>
          有效成分含量: {product.concentration_level === 'High' ? '高浓度' : product.concentration_level === 'Medium' ? '中浓度' : '低浓度'}
        </span>
        <span className="text-gray-600">适用肤质: {product.suitable_skin_types && product.suitable_skin_types.length > 0 ? product.suitable_skin_types.join(' / ') : '所有肤质'}</span>
      </div>

      {/* No product ratings/reviews displayed as per requirement */}
      
{product.url && 
        <a href={product.url} target="_blank" rel="noopener noreferrer" 
           className="flex items-center text-slate-500 hover:text-slate-700 text-sm font-medium transition-colors mt-2">
          <ExternalLink className="w-4 h-4 mr-1" /> 查看产品官网
        </a>
      }
    </div>
  );
};

// Component for the main application header
const AppHeader = ({ title, onBack, showBackButton = true }) => (
  <header className="sticky top-0 z-10 bg-white shadow-md p-4 flex items-center">
    {showBackButton && onBack && (
      <button onClick={onBack} className="p-2 mr-4 text-gray-600 hover:text-gray-900 transition-colors rounded-full hover:bg-gray-100">
        <ArrowLeft className="w-6 h-6" />
      </button>
    )}
    <h1 className="text-2xl font-extrabold text-gray-900">{title}</h1>
  </header>
);

// Main Application Component
const App = () => {
  const [efficacies, setEfficacies] = useState([]);
  const [ingredients, setIngredients] = useState([]);
  const [products, setProducts] = useState([]);
  const [skinTypes, setSkinTypes] = useState([]);
  const [evidenceExplanation, setEvidenceExplanation] = useState(null);
  const [selectedEfficacy, setSelectedEfficacy] = useState(null);
  const [selectedIngredient, setSelectedIngredient] = useState(null);
  const [selectedSkinType, setSelectedSkinType] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // --- API Fetching ---

  const fetchEfficacies = useCallback(async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_BASE_URL}/api/effect-categories`);
      setEfficacies(response.data);
      setError(null);
    } catch (err) {
      console.error("Error fetching efficacies:", err);
      setError("无法加载功效列表，请检查后端服务是否运行正常。");
    } finally {
      setLoading(false);
    }
  }, []);

  const fetchIngredients = useCallback(async (efficacyId) => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_BASE_URL}/api/ingredients/by-effect/${efficacyId}`);
      setIngredients(response.data);
      setError(null);
    } catch (err) {
      console.error(`Error fetching ingredients for ${efficacyId}:`, err);
      setError("无法加载成分列表。");
    } finally {
      setLoading(false);
    }
  }, []);

  const fetchProducts = useCallback(async (ingredientName, skinTypeNames = []) => {
    setLoading(true);
    try {
      let response;
      
      if (skinTypeNames.length > 0) {
        // Use the POST filter endpoint for skin type filtering
        response = await axios.post(`${API_BASE_URL}/api/products/filter`, {
          ingredient_name: ingredientName,
          skin_type_names: skinTypeNames
        });
      } else {
        // Use the GET endpoint for initial product list
        response = await axios.get(`${API_BASE_URL}/api/products/by-ingredient/${ingredientName}`);
      }
      // The Neo4j backend returns the product list directly
      console.log("返回的产品数据（第一个）:", response.data[0]);   // ★★ 加这里

      // The Neo4j backend returns the product list directly
      setProducts(response.data);
      setError(null);
    } catch (err) {
      console.error(`Error fetching products for ${ingredientName}:`, err);
      setError("无法加载产品列表。");
    } finally {
      setLoading(false);
    }
  }, []);
  
    const fetchEvidenceExplanation = useCallback(async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/evidence-explanation`);
      setEvidenceExplanation(response.data);
    } catch (err) {
      console.error("Error fetching evidence explanation:", err);
    }
  }, []);

  const fetchSkinTypes = useCallback(async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/skin-types`);
      setSkinTypes(response.data);
    } catch (err) {
      console.error("Error fetching skin types:", err);
    }
  }, []);

  // --- Navigation/State Management ---

    useEffect(() => {
    fetchEfficacies();
    fetchSkinTypes();
    fetchEvidenceExplanation();
  }, [fetchEfficacies, fetchSkinTypes, fetchEvidenceExplanation]);

  const handleSelectEfficacy = (efficacy) => {
    setSelectedEfficacy(efficacy);
    setSelectedIngredient(null);
    setSelectedSkinType(null);
    setProducts([]);
    fetchIngredients(efficacy.id);
  };

    const handleShowEvidenceInfo = () => {
    if (evidenceExplanation) {
      const info = `证据等级说明:\n\nA级: ${evidenceExplanation.A}\n\nB级: ${evidenceExplanation.B}\n\nC级: ${evidenceExplanation.C}`;
      alert(info);
    }
  };

  const handleSelectIngredient = (ingredientId) => {
    const ingredient = ingredients.find(ing => ing.id === ingredientId);
    setSelectedIngredient(ingredient);
    setSelectedSkinType(null);
    // Neo4j backend uses ingredient name for product lookup
    fetchProducts(ingredient.name);
  };

  const handleFilterBySkinType = (skinTypeId) => {
    const skinType = skinTypes.find(st => st.id === skinTypeId);
    setSelectedSkinType(skinTypeId);
    
    if (selectedIngredient && skinType) {
      // Use the new fetchProducts logic with ingredient name and skin type name
      fetchProducts(selectedIngredient.name, [skinType.name]);
    } else if (selectedIngredient) {
      // If skin type is deselected, fetch all products for the ingredient
      fetchProducts(selectedIngredient.name, []);
    }
  };
  
  // --- Back Button Handlers ---
  
  const handleBack = () => {
    if (selectedIngredient) {
      // Back from Products to Ingredients
      setSelectedIngredient(null);
      setProducts([]);
      setSelectedSkinType(null);
    } else if (selectedEfficacy) {
      // Back from Ingredients to Efficacies
      setSelectedEfficacy(null);
      setIngredients([]);
    }
  };

  // --- Rendering Logic ---

  let content;
  let headerTitle = "成分党产品筛选平台";
  let showBackButton = true;

  if (loading) {
    content = <div className="text-center p-12 text-gray-500">加载中...</div>;
  } else if (error) {
    content = <div className="text-center p-12 text-red-500 font-semibold">{error}</div>;
  } else if (selectedIngredient) {
    // 3. Product List View
    headerTitle = `产品列表: ${selectedIngredient.name}`;
    content = (
      <div className="p-6">
        <div className="mb-6 flex justify-between items-center">
          <h2 className="text-2xl font-bold text-gray-800">
            包含 "{selectedIngredient.name}" 的产品 ({products.length})
          </h2>
          {/* Skin Type Filter */}
          <div className="flex items-center space-x-2">
            <Filter className="w-5 h-5 text-gray-500" />
            <select
              value={selectedSkinType || ''}
              onChange={(e) => handleFilterBySkinType(e.target.value ? parseInt(e.target.value) : null)}
              className="p-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="">所有肤质</option>
              {skinTypes.map(st => (
                <option key={st.id} value={st.id}>{st.name}</option>
              ))}
            </select>
          </div>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {products.length > 0 ? (
            products.map(product => (
              <ProductCard key={product.id} product={product} />
            ))
          ) : (
            <p className="col-span-full text-center text-gray-500">暂无符合筛选条件的产品。</p>
          )}
        </div>
      </div>
    );
  } else if (selectedEfficacy) {
    // 2. Ingredient List View
    headerTitle = `成分列表: ${selectedEfficacy.name}`;
    content = (
      <div className="p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">
          {selectedEfficacy.name} 功效成分 ({ingredients.length})
        </h2>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {ingredients.length > 0 ? (
            ingredients.map(ingredient => (
<IngredientDetailsCard 
                key={ingredient.id} 
                ingredient={ingredient} 
                onClick={handleSelectIngredient} 
                onShowEvidenceInfo={handleShowEvidenceInfo}
              />
            ))
          ) : (
            <p className="col-span-full text-center text-gray-500">暂无成分数据。</p>
          )}
        </div>
      </div>
    );
  } else {
    // 1. Efficacy Selection View
    headerTitle = "功效选择";
    showBackButton = false;
    content = (
      <div className="p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">请选择您关注的功效类别:</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {efficacies.map(efficacy => (
            <div 
              key={efficacy.id} 
              onClick={() => handleSelectEfficacy(efficacy)}
              className="bg-white border border-blue-200 rounded-xl shadow-lg p-6 cursor-pointer hover:shadow-xl hover:border-blue-500 transition-all duration-300 transform hover:scale-[1.02]"
            >
              <h3 className="text-xl font-bold text-blue-700 mb-2">{efficacy.name}</h3>
              <p className="text-gray-600 text-sm line-clamp-3">{efficacy.description}</p>
            </div>
          ))}
        </div>
        <div className="mt-12 p-4 bg-gray-50 border-l-4 border-blue-500 text-gray-700">
          <p className="font-semibold">提示 :</p>
          <p className="text-sm">本平台旨在提供客观、科学的成分信息和产品筛选。所有成分均根据其作用机制和临床数据进行评分和排序，产品列表按有效成分浓度排序，不含任何主观评价或评分。</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <AppHeader 
        title={headerTitle} 
        onBack={handleBack} 
        showBackButton={selectedEfficacy !== null} // Show back button only if an efficacy is selected
      />
      <main className="max-w-7xl mx-auto">
        {content}
      </main>
    </div>
  );
};

export default App;
