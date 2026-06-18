import React, { useState, useEffect, useCallback } from 'react';
import { 
  BookOpen, 
  Target, 
  TrendingUp, 
  Award, 
  Clock, 
  CheckCircle, 
  AlertCircle,
  Lightbulb,
  Users,
  BarChart3,
  Settings
} from 'lucide-react';

const LearningModeSystem = ({ 
  studentLevel = 'beginner',
  onModeChange,
  onProgressUpdate
}) => {
  const [currentMode, setCurrentMode] = useState('guided');
  const [learningProgress, setLearningProgress] = useState({
    beginner: { completed: 0, total: 10, percentage: 0 },
    intermediate: { completed: 0, total: 15, percentage: 0 },
    advanced: { completed: 0, total: 20, percentage: 0 }
  });
  const [currentTopic, setCurrentTopic] = useState(null);
  const [showSettings, setShowSettings] = useState(false);

  const LEARNING_MODES = {
    guided: {
      name: "Guided Learning",
      description: "Step-by-step guided learning with hints and explanations",
      icon: BookOpen,
      color: "blue",
      features: [
        "Step-by-step instructions",
        "Built-in hints and tips",
        "Progress tracking",
        "Adaptive difficulty"
      ],
      suitableFor: ["beginner", "intermediate"]
    },
    practice: {
      name: "Practice Mode",
      description: "Self-paced practice with immediate feedback",
      icon: Target,
      color: "green",
      features: [
        "Unlimited practice",
        "Immediate feedback",
        "Mistake analysis",
        "Performance tracking"
      ],
      suitableFor: ["intermediate", "advanced"]
    },
    challenge: {
      name: "Challenge Mode",
      description: "Advanced problems and time-based challenges",
      icon: Award,
      color: "purple",
      features: [
        "Time-based challenges",
        "Advanced problems",
        "Leaderboards",
        "Achievement system"
      ],
      suitableFor: ["advanced"]
    },
    exploration: {
      name: "Exploration Mode",
      description: "Free exploration and experimentation",
      icon: Lightbulb,
      color: "yellow",
      features: [
        "Free-form exploration",
        "Creative problem solving",
        "No time pressure",
        "Discovery learning"
      ],
      suitableFor: ["beginner", "intermediate", "advanced"]
    }
  };

  const TOPICS = {
    shapes_2d: {
      name: "2D Shapes",
      description: "Triangles, quadrilaterals, circles, and polygons",
      difficulty: "beginner",
      estimatedTime: "2 hours",
      prerequisites: [],
      learningObjectives: [
        "Identify different 2D shapes",
        "Calculate area and perimeter",
        "Understand shape properties",
        "Solve shape-related problems"
      ]
    },
    shapes_3d: {
      name: "3D Shapes",
      description: "Cubes, prisms, cylinders, and spheres",
      difficulty: "intermediate",
      estimatedTime: "3 hours",
      prerequisites: ["shapes_2d"],
      learningObjectives: [
        "Visualize 3D shapes",
        "Calculate volume and surface area",
        "Understand 3D properties",
        "Work with 3D measurements"
      ]
    },
    measurements: {
      name: "Measurements",
      description: "Area, perimeter, volume, and unit conversions",
      difficulty: "intermediate",
      estimatedTime: "2.5 hours",
      prerequisites: ["shapes_2d"],
      learningObjectives: [
        "Master measurement formulas",
        "Convert between units",
        "Solve measurement problems",
        "Apply measurements in real contexts"
      ]
    },
    constructions: {
      name: "Geometric Constructions",
      description: "Drawing shapes using compass and ruler",
      difficulty: "advanced",
      estimatedTime: "4 hours",
      prerequisites: ["shapes_2d", "measurements"],
      learningObjectives: [
        "Use construction tools",
        "Follow construction steps",
        "Verify constructions",
        "Solve construction problems"
      ]
    }
  };

  // Update progress when mode changes
  const handleModeChange = (mode) => {
    setCurrentMode(mode);
    if (onModeChange) {
      onModeChange(mode);
    }
  };

  // Update learning progress
  const updateProgress = useCallback((topic, completed) => {
    setLearningProgress(prev => {
      const newProgress = { ...prev };
      const level = TOPICS[topic]?.difficulty || 'beginner';
      newProgress[level] = {
        ...newProgress[level],
        completed: newProgress[level].completed + (completed ? 1 : 0),
        percentage: Math.round(((newProgress[level].completed + (completed ? 1 : 0)) / newProgress[level].total) * 100)
      };
      
      if (onProgressUpdate) {
        onProgressUpdate(newProgress);
      }
      
      return newProgress;
    });
  }, [onProgressUpdate]);

  // Get recommended mode based on student level
  const getRecommendedMode = (level) => {
    switch (level) {
      case 'beginner':
        return 'guided';
      case 'intermediate':
        return 'practice';
      case 'advanced':
        return 'challenge';
      default:
        return 'guided';
    }
  };

  // Get available topics for current level
  const getAvailableTopics = (level) => {
    return Object.entries(TOPICS).filter(([key, topic]) => {
      if (level === 'beginner') return topic.difficulty === 'beginner';
      if (level === 'intermediate') return ['beginner', 'intermediate'].includes(topic.difficulty);
      return true; // Advanced students can access all topics
    });
  };

  const availableTopics = getAvailableTopics(studentLevel);
  const recommendedMode = getRecommendedMode(studentLevel);

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-white rounded-lg border p-6">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h3 className="text-xl font-semibold text-gray-800 flex items-center">
              <BookOpen className="w-6 h-6 mr-2" />
              Learning Mode System
            </h3>
            <p className="text-gray-600">Choose your learning approach and track your progress</p>
          </div>
          
          <button
            onClick={() => setShowSettings(!showSettings)}
            className="p-2 text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-md"
          >
            <Settings className="w-5 h-5" />
          </button>
        </div>

        {/* Student Level Indicator */}
        <div className="mb-6">
          <div className="flex items-center space-x-4">
            <div className={`px-4 py-2 rounded-lg ${
              studentLevel === 'beginner' ? 'bg-green-100 text-green-800' :
              studentLevel === 'intermediate' ? 'bg-yellow-100 text-yellow-800' :
              'bg-purple-100 text-purple-800'
            }`}>
              <span className="font-medium">Current Level: {studentLevel.charAt(0).toUpperCase() + studentLevel.slice(1)}</span>
            </div>
            
            <div className="text-sm text-gray-600">
              Recommended Mode: <span className="font-medium">{LEARNING_MODES[recommendedMode].name}</span>
            </div>
          </div>
        </div>

        {/* Progress Overview */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          {Object.entries(learningProgress).map(([level, progress]) => (
            <div key={level} className="bg-gray-50 rounded-lg p-4">
              <div className="flex items-center justify-between mb-2">
                <span className="text-sm font-medium text-gray-700 capitalize">{level}</span>
                <span className="text-sm text-gray-500">{progress.completed}/{progress.total}</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2 mb-2">
                <div 
                  className={`h-2 rounded-full ${
                    level === 'beginner' ? 'bg-green-500' :
                    level === 'intermediate' ? 'bg-yellow-500' :
                    'bg-purple-500'
                  }`}
                  style={{ width: `${progress.percentage}%` }}
                />
              </div>
              <div className="text-xs text-gray-600">{progress.percentage}% Complete</div>
            </div>
          ))}
        </div>
      </div>

      {/* Learning Modes */}
      <div className="bg-white rounded-lg border p-6">
        <h4 className="text-lg font-semibold text-gray-800 mb-4">Choose Learning Mode</h4>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {Object.entries(LEARNING_MODES).map(([modeKey, mode]) => {
            const Icon = mode.icon;
            const isRecommended = modeKey === recommendedMode;
            const isSuitable = mode.suitableFor.includes(studentLevel);
            
            return (
              <div
                key={modeKey}
                onClick={() => isSuitable && handleModeChange(modeKey)}
                className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                  currentMode === modeKey
                    ? `border-${mode.color}-500 bg-${mode.color}-50`
                    : isSuitable
                    ? 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
                    : 'border-gray-100 bg-gray-50 cursor-not-allowed opacity-50'
                }`}
              >
                <div className="flex items-center mb-3">
                  <Icon className={`w-6 h-6 mr-2 ${
                    currentMode === modeKey ? `text-${mode.color}-600` : 'text-gray-600'
                  }`} />
                  <h5 className={`font-medium ${
                    currentMode === modeKey ? `text-${mode.color}-800` : 'text-gray-800'
                  }`}>
                    {mode.name}
                  </h5>
                  {isRecommended && (
                    <span className="ml-2 px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full">
                      Recommended
                    </span>
                  )}
                </div>
                
                <p className="text-sm text-gray-600 mb-3">{mode.description}</p>
                
                <div className="space-y-1">
                  {mode.features.map((feature, index) => (
                    <div key={index} className="flex items-center text-xs text-gray-500">
                      <CheckCircle className="w-3 h-3 mr-2 text-green-500" />
                      {feature}
                    </div>
                  ))}
                </div>
                
                {!isSuitable && (
                  <div className="mt-3 text-xs text-gray-400">
                    Requires {mode.suitableFor.join(' or ')} level
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* Topic Selection */}
      <div className="bg-white rounded-lg border p-6">
        <h4 className="text-lg font-semibold text-gray-800 mb-4">Available Topics</h4>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {availableTopics.map(([topicKey, topic]) => (
            <div
              key={topicKey}
              onClick={() => setCurrentTopic(topicKey)}
              className={`p-4 rounded-lg border cursor-pointer transition-all ${
                currentTopic === topicKey
                  ? 'border-blue-500 bg-blue-50'
                  : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <h5 className="font-medium text-gray-800">{topic.name}</h5>
                <span className={`px-2 py-1 rounded-full text-xs ${
                  topic.difficulty === 'beginner' ? 'bg-green-100 text-green-800' :
                  topic.difficulty === 'intermediate' ? 'bg-yellow-100 text-yellow-800' :
                  'bg-purple-100 text-purple-800'
                }`}>
                  {topic.difficulty}
                </span>
              </div>
              
              <p className="text-sm text-gray-600 mb-3">{topic.description}</p>
              
              <div className="flex items-center justify-between text-xs text-gray-500">
                <span>⏱️ {topic.estimatedTime}</span>
                <span>📚 {topic.learningObjectives.length} objectives</span>
              </div>
              
              {topic.prerequisites.length > 0 && (
                <div className="mt-2 text-xs text-gray-500">
                  <span className="font-medium">Prerequisites:</span> {topic.prerequisites.join(', ')}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Current Topic Details */}
      {currentTopic && TOPICS[currentTopic] && (
        <div className="bg-white rounded-lg border p-6">
          <h4 className="text-lg font-semibold text-gray-800 mb-4">
            {TOPICS[currentTopic].name} - Learning Objectives
          </h4>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h5 className="font-medium text-gray-700 mb-3">Learning Objectives</h5>
              <ul className="space-y-2">
                {TOPICS[currentTopic].learningObjectives.map((objective, index) => (
                  <li key={index} className="flex items-start text-sm text-gray-600">
                    <CheckCircle className="w-4 h-4 mr-2 text-green-500 mt-0.5 flex-shrink-0" />
                    {objective}
                  </li>
                ))}
              </ul>
            </div>
            
            <div>
              <h5 className="font-medium text-gray-700 mb-3">Topic Information</h5>
              <div className="space-y-2 text-sm text-gray-600">
                <div className="flex justify-between">
                  <span>Difficulty:</span>
                  <span className="font-medium capitalize">{TOPICS[currentTopic].difficulty}</span>
                </div>
                <div className="flex justify-between">
                  <span>Estimated Time:</span>
                  <span className="font-medium">{TOPICS[currentTopic].estimatedTime}</span>
                </div>
                <div className="flex justify-between">
                  <span>Objectives:</span>
                  <span className="font-medium">{TOPICS[currentTopic].learningObjectives.length}</span>
                </div>
              </div>
              
              <div className="mt-4">
                <button
                  onClick={() => updateProgress(currentTopic, true)}
                  className="w-full px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
                >
                  Start Learning This Topic
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Settings Panel */}
      {showSettings && (
        <div className="bg-white rounded-lg border p-6">
          <h4 className="text-lg font-semibold text-gray-800 mb-4">Learning Settings</h4>
          
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Learning Speed
              </label>
              <select className="w-full p-2 border border-gray-300 rounded-md">
                <option value="slow">Slow - More explanations</option>
                <option value="normal" selected>Normal - Balanced pace</option>
                <option value="fast">Fast - Quick progression</option>
              </select>
            </div>
            
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Feedback Level
              </label>
              <select className="w-full p-2 border border-gray-300 rounded-md">
                <option value="minimal">Minimal - Basic feedback</option>
                <option value="standard" selected>Standard - Detailed feedback</option>
                <option value="extensive">Extensive - Comprehensive feedback</option>
              </select>
            </div>
            
            <div>
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" defaultChecked />
                <span className="text-sm text-gray-700">Enable hints and tips</span>
              </label>
            </div>
            
            <div>
              <label className="flex items-center">
                <input type="checkbox" className="mr-2" defaultChecked />
                <span className="text-sm text-gray-700">Show progress indicators</span>
              </label>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default LearningModeSystem;
