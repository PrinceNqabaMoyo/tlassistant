import React, { useState, useEffect } from 'react';
import { 
  Play, 
  Pause, 
  RotateCcw, 
  ChevronLeft, 
  ChevronRight, 
  CheckCircle, 
  AlertCircle,
  Wrench,
  Clock,
  Target
} from 'lucide-react';
import { CONSTRUCTION_GUIDES, CONSTRUCTION_TOOLS, DIFFICULTY_LEVELS } from './ConstructionGuideData';

const ConstructionGuide = ({ 
  shapeType, 
  dimensions, 
  onStepComplete,
  autoPlay = false,
  speed = 1 
}) => {
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(autoPlay);
  const [completedSteps, setCompletedSteps] = useState(new Set());
  const [showTips, setShowTips] = useState(true);
  const [animationSpeed, setAnimationSpeed] = useState(speed);

  const guide = CONSTRUCTION_GUIDES[shapeType];
  
  if (!guide) {
    return (
      <div className="bg-white rounded-lg border p-6 text-center">
        <AlertCircle className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <h3 className="text-lg font-semibold text-gray-600 mb-2">No Guide Available</h3>
        <p className="text-gray-500">Construction guide not available for this shape type.</p>
      </div>
    );
  }

  const totalSteps = guide.steps.length;
  const isLastStep = currentStep === totalSteps - 1;
  const isFirstStep = currentStep === 0;

  // Auto-play functionality
  useEffect(() => {
    let interval;
    if (isPlaying && !isLastStep) {
      interval = setInterval(() => {
        setCurrentStep(prev => prev + 1);
      }, 3000 / animationSpeed); // 3 seconds per step, adjusted by speed
    }
    return () => clearInterval(interval);
  }, [isPlaying, isLastStep, animationSpeed]);

  // Mark step as completed
  const markStepCompleted = (stepId) => {
    setCompletedSteps(prev => new Set([...prev, stepId]));
    if (onStepComplete) {
      onStepComplete(stepId, guide.steps[stepId]);
    }
  };

  // Navigation functions
  const goToNextStep = () => {
    if (!isLastStep) {
      markStepCompleted(currentStep);
      setCurrentStep(prev => prev + 1);
    }
  };

  const goToPreviousStep = () => {
    if (!isFirstStep) {
      setCurrentStep(prev => prev - 1);
    }
  };

  const goToStep = (stepIndex) => {
    setCurrentStep(stepIndex);
  };

  const resetGuide = () => {
    setCurrentStep(0);
    setCompletedSteps(new Set());
    setIsPlaying(false);
  };

  const togglePlayPause = () => {
    setIsPlaying(!isPlaying);
  };

  const currentStepData = guide.steps[currentStep];

  return (
    <div className="bg-white rounded-lg border">
      {/* Header */}
      <div className="p-6 border-b bg-gray-50">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h3 className="text-xl font-semibold text-gray-800">{guide.title}</h3>
            <p className="text-gray-600 mt-1">{guide.description}</p>
          </div>
          
          <div className="flex items-center space-x-2">
            <span className={`px-3 py-1 rounded-full text-sm font-medium ${
              DIFFICULTY_LEVELS[guide.difficulty].color === 'green' ? 'bg-green-100 text-green-800' :
              DIFFICULTY_LEVELS[guide.difficulty].color === 'yellow' ? 'bg-yellow-100 text-yellow-800' :
              'bg-red-100 text-red-800'
            }`}>
              {DIFFICULTY_LEVELS[guide.difficulty].name}
            </span>
          </div>
        </div>

        {/* Progress Bar */}
        <div className="mb-4">
          <div className="flex justify-between text-sm text-gray-600 mb-2">
            <span>Step {currentStep + 1} of {totalSteps}</span>
            <span>{Math.round(((currentStep + 1) / totalSteps) * 100)}% Complete</span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div 
              className="bg-blue-600 h-2 rounded-full transition-all duration-300"
              style={{ width: `${((currentStep + 1) / totalSteps) * 100}%` }}
            />
          </div>
        </div>

        {/* Controls */}
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <button
              onClick={togglePlayPause}
              className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
            >
              {isPlaying ? <Pause className="w-4 h-4 mr-2" /> : <Play className="w-4 h-4 mr-2" />}
              {isPlaying ? 'Pause' : 'Play'}
            </button>
            
            <button
              onClick={resetGuide}
              className="flex items-center px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700"
            >
              <RotateCcw className="w-4 h-4 mr-2" />
              Reset
            </button>
          </div>

          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-2">
              <label className="text-sm text-gray-600">Speed:</label>
              <input
                type="range"
                min="0.5"
                max="3"
                step="0.5"
                value={animationSpeed}
                onChange={(e) => setAnimationSpeed(parseFloat(e.target.value))}
                className="w-20"
              />
              <span className="text-sm text-gray-600">{animationSpeed}x</span>
            </div>

            <button
              onClick={() => setShowTips(!showTips)}
              className={`px-3 py-2 rounded-md text-sm ${
                showTips ? 'bg-yellow-100 text-yellow-700' : 'bg-gray-100 text-gray-600'
              }`}
            >
              <Target className="w-4 h-4 mr-1" />
              Tips
            </button>
          </div>
        </div>
      </div>

      {/* Step Navigation */}
      <div className="p-4 border-b bg-gray-50">
        <div className="flex items-center justify-between">
          <button
            onClick={goToPreviousStep}
            disabled={isFirstStep}
            className="flex items-center px-3 py-2 bg-white border rounded-md hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <ChevronLeft className="w-4 h-4 mr-1" />
            Previous
          </button>

          <div className="flex space-x-2">
            {guide.steps.map((_, index) => (
              <button
                key={index}
                onClick={() => goToStep(index)}
                className={`w-8 h-8 rounded-full text-sm font-medium ${
                  index === currentStep
                    ? 'bg-blue-600 text-white'
                    : completedSteps.has(index)
                    ? 'bg-green-100 text-green-800'
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                }`}
              >
                {completedSteps.has(index) ? <CheckCircle className="w-4 h-4" /> : index + 1}
              </button>
            ))}
          </div>

          <button
            onClick={goToNextStep}
            disabled={isLastStep}
            className="flex items-center px-3 py-2 bg-white border rounded-md hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Next
            <ChevronRight className="w-4 h-4 ml-1" />
          </button>
        </div>
      </div>

      {/* Current Step Content */}
      <div className="p-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Step Information */}
          <div className="space-y-4">
            <div>
              <h4 className="text-lg font-semibold text-gray-800 mb-2">
                Step {currentStep + 1}: {currentStepData.title}
              </h4>
              <p className="text-gray-600 mb-4">{currentStepData.description}</p>
              
              <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
                <h5 className="font-medium text-blue-800 mb-2">Instruction:</h5>
                <p className="text-blue-700">{currentStepData.instruction}</p>
              </div>
            </div>

            {/* Tools Required */}
            <div>
              <h5 className="font-medium text-gray-800 mb-2 flex items-center">
                <Wrench className="w-4 h-4 mr-2" />
                Tools Required:
              </h5>
              <div className="flex flex-wrap gap-2">
                {currentStepData.tools.map((tool, index) => (
                  <span
                    key={index}
                    className="flex items-center px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm"
                  >
                    <span className="mr-1">{CONSTRUCTION_TOOLS[tool]?.icon}</span>
                    {CONSTRUCTION_TOOLS[tool]?.name || tool}
                  </span>
                ))}
              </div>
            </div>

            {/* Tips */}
            {showTips && currentStepData.tips && (
              <div>
                <h5 className="font-medium text-gray-800 mb-2 flex items-center">
                  <Target className="w-4 h-4 mr-2" />
                  Tips:
                </h5>
                <ul className="space-y-1">
                  {currentStepData.tips.map((tip, index) => (
                    <li key={index} className="flex items-start text-sm text-gray-600">
                      <span className="w-2 h-2 bg-blue-500 rounded-full mt-2 mr-3 flex-shrink-0" />
                      {tip}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          {/* Visual Area */}
          <div className="bg-gray-50 rounded-lg p-4 min-h-[300px] flex items-center justify-center">
            <div className="text-center">
              <div className="w-32 h-32 bg-white border-2 border-dashed border-gray-300 rounded-lg flex items-center justify-center mb-4">
                <span className="text-gray-400 text-sm">
                  {currentStepData.visual}
                </span>
              </div>
              <p className="text-sm text-gray-500">
                Visual representation for: {currentStepData.title}
              </p>
            </div>
          </div>
        </div>

        {/* Step Actions */}
        <div className="mt-6 pt-4 border-t">
          <div className="flex items-center justify-between">
            <div className="text-sm text-gray-600">
              {isLastStep ? (
                <span className="flex items-center text-green-600">
                  <CheckCircle className="w-4 h-4 mr-2" />
                  Construction Complete!
                </span>
              ) : (
                <span className="flex items-center">
                  <Clock className="w-4 h-4 mr-2" />
                  Next: {guide.steps[currentStep + 1]?.title}
                </span>
              )}
            </div>

            <div className="flex space-x-2">
              <button
                onClick={() => markStepCompleted(currentStep)}
                disabled={completedSteps.has(currentStep)}
                className={`px-4 py-2 rounded-md text-sm font-medium ${
                  completedSteps.has(currentStep)
                    ? 'bg-green-100 text-green-700 cursor-not-allowed'
                    : 'bg-green-600 text-white hover:bg-green-700'
                }`}
              >
                {completedSteps.has(currentStep) ? (
                  <>
                    <CheckCircle className="w-4 h-4 mr-2" />
                    Completed
                  </>
                ) : (
                  'Mark Complete'
                )}
              </button>

              {!isLastStep && (
                <button
                  onClick={goToNextStep}
                  className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
                >
                  Next Step
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ConstructionGuide;
