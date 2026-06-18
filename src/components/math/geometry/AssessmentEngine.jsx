import React, { useState, useEffect, useCallback, useMemo } from 'react';
import { 
  Play, 
  Pause, 
  RotateCcw, 
  CheckCircle, 
  XCircle, 
  Clock, 
  Target, 
  TrendingUp,
  AlertCircle,
  Lightbulb,
  BookOpen,
  Award
} from 'lucide-react';
import { 
  ASSESSMENT_TYPES, 
  QUESTION_TYPES, 
  DIFFICULTY_LEVELS, 
  TOPIC_AREAS,
  ASSESSMENT_TEMPLATES,
  FEEDBACK_MESSAGES,
  ASSESSMENT_RULES
} from './AssessmentData';

const AssessmentEngine = ({ 
  assessmentType = 'PRACTICE',
  selectedTopics = [],
  difficulty = 'mixed',
  onComplete,
  onProgress
}) => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [timeRemaining, setTimeRemaining] = useState(0);
  const [isActive, setIsActive] = useState(false);
  const [showFeedback, setShowFeedback] = useState(false);
  const [currentFeedback, setCurrentFeedback] = useState(null);
  const [score, setScore] = useState(0);
  const [totalQuestions, setTotalQuestions] = useState(0);
  const [isCompleted, setIsCompleted] = useState(false);
  const [showHint, setShowHint] = useState(false);
  const [attempts, setAttempts] = useState(0);

  // Generate questions based on assessment type and topics
  const generateQuestions = useCallback(() => {
    const questionCount = ASSESSMENT_TYPES[assessmentType].questions;
    const generatedQuestions = [];
    
    // For now, generate sample questions - in real implementation, this would be more sophisticated
    const sampleQuestions = [
      {
        id: 1,
        type: 'CALCULATION',
        difficulty: 'EASY',
        topic: 'SHAPES_2D',
        question: "Calculate the area of a triangle with base 8 cm and height 6 cm.",
        formula: "A = ½ × b × h",
        correctAnswer: 24,
        tolerance: 0.1,
        points: 1,
        timeLimit: 60
      },
      {
        id: 2,
        type: 'MULTIPLE_CHOICE',
        difficulty: 'EASY',
        topic: 'SHAPES_2D',
        question: "Which shape has 4 equal sides and 4 right angles?",
        options: ["Rectangle", "Square", "Rhombus", "Parallelogram"],
        correctAnswer: "Square",
        points: 1,
        timeLimit: 60
      },
      {
        id: 3,
        type: 'CALCULATION',
        difficulty: 'MEDIUM',
        topic: 'SHAPES_3D',
        question: "Find the volume of a cube with side length 4 cm.",
        formula: "V = s³",
        correctAnswer: 64,
        tolerance: 0.1,
        points: 2,
        timeLimit: 120
      },
      {
        id: 4,
        type: 'TRUE_FALSE',
        difficulty: 'MEDIUM',
        topic: 'MEASUREMENTS',
        question: "The area of a circle is always greater than its circumference.",
        correctAnswer: false,
        explanation: "This depends on the radius. For small circles, circumference can be greater than area.",
        points: 2,
        timeLimit: 120
      },
      {
        id: 5,
        type: 'CALCULATION',
        difficulty: 'HARD',
        topic: 'SHAPES_3D',
        question: "Calculate the surface area of a cylinder with radius 3 cm and height 8 cm. Use π = 3.14",
        formula: "SA = 2πr(r + h)",
        correctAnswer: 207.24,
        tolerance: 0.1,
        points: 3,
        timeLimit: 180
      }
    ];

    // Select questions based on assessment type
    const selectedQuestions = sampleQuestions.slice(0, questionCount);
    setQuestions(selectedQuestions);
    setTotalQuestions(selectedQuestions.length);
    
    // Set time limit
    const totalTime = ASSESSMENT_TYPES[assessmentType].duration * 60; // Convert to seconds
    setTimeRemaining(totalTime);
  }, [assessmentType]);

  // Initialize assessment
  useEffect(() => {
    generateQuestions();
  }, [generateQuestions]);

  // Timer effect
  useEffect(() => {
    let interval = null;
    if (isActive && timeRemaining > 0) {
      interval = setInterval(() => {
        setTimeRemaining(time => {
          if (time <= 1) {
            setIsActive(false);
            handleSubmitAssessment();
            return 0;
          }
          return time - 1;
        });
      }, 1000);
    } else if (!isActive && timeRemaining !== 0) {
      clearInterval(interval);
    }
    return () => clearInterval(interval);
  }, [isActive, timeRemaining]);

  // Format time display
  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // Handle answer submission
  const handleAnswerSubmit = (questionId, answer) => {
    const newAnswers = { ...answers, [questionId]: answer };
    setAnswers(newAnswers);
    
    // Validate answer immediately
    const question = questions.find(q => q.id === questionId);
    if (question) {
      const isCorrect = validateAnswer(question, answer);
      const feedback = generateFeedback(question, answer, isCorrect);
      
      setCurrentFeedback(feedback);
      setShowFeedback(true);
      
      if (isCorrect) {
        setScore(prev => prev + question.points);
      }
      
      // Auto-hide feedback after 3 seconds
      setTimeout(() => {
        setShowFeedback(false);
      }, 3000);
    }
  };

  // Validate answer based on question type
  const validateAnswer = (question, answer) => {
    switch (question.type) {
      case 'CALCULATION':
        const tolerance = question.tolerance || 0.1;
        const correctAnswer = question.correctAnswer;
        const userAnswer = parseFloat(answer);
        return Math.abs(userAnswer - correctAnswer) <= tolerance;
      
      case 'MULTIPLE_CHOICE':
        return answer === question.correctAnswer;
      
      case 'TRUE_FALSE':
        return answer === question.correctAnswer;
      
      default:
        return false;
    }
  };

  // Generate feedback based on answer
  const generateFeedback = (question, answer, isCorrect) => {
    const difficulty = question.difficulty.toLowerCase();
    const feedbackMessages = isCorrect ? FEEDBACK_MESSAGES.CORRECT : FEEDBACK_MESSAGES.INCORRECT;
    const randomMessage = feedbackMessages[difficulty][Math.floor(Math.random() * feedbackMessages[difficulty].length)];
    
    return {
      isCorrect,
      message: randomMessage,
      explanation: question.explanation || `The correct answer is ${question.correctAnswer}`,
      hint: FEEDBACK_MESSAGES.HINTS[difficulty][Math.floor(Math.random() * FEEDBACK_MESSAGES.HINTS[difficulty].length)]
    };
  };

  // Handle next question
  const handleNextQuestion = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(prev => prev + 1);
      setShowFeedback(false);
      setShowHint(false);
    } else {
      handleSubmitAssessment();
    }
  };

  // Handle previous question
  const handlePreviousQuestion = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(prev => prev - 1);
      setShowFeedback(false);
      setShowHint(false);
    }
  };

  // Submit assessment
  const handleSubmitAssessment = () => {
    setIsActive(false);
    setIsCompleted(true);
    
    const totalPossiblePoints = questions.reduce((sum, q) => sum + q.points, 0);
    const percentage = Math.round((score / totalPossiblePoints) * 100);
    
    const result = {
      score,
      totalPossiblePoints,
      percentage,
      questionsAnswered: Object.keys(answers).length,
      totalQuestions: questions.length,
      timeSpent: ASSESSMENT_TYPES[assessmentType].duration * 60 - timeRemaining,
      passed: percentage >= ASSESSMENT_RULES.SCORING.passing_percentage
    };
    
    if (onComplete) {
      onComplete(result);
    }
  };

  // Start assessment
  const startAssessment = () => {
    setIsActive(true);
    setCurrentQuestion(0);
    setAnswers({});
    setScore(0);
    setIsCompleted(false);
    setShowFeedback(false);
  };

  // Reset assessment
  const resetAssessment = () => {
    setIsActive(false);
    setCurrentQuestion(0);
    setAnswers({});
    setScore(0);
    setIsCompleted(false);
    setShowFeedback(false);
    setTimeRemaining(ASSESSMENT_TYPES[assessmentType].duration * 60);
  };

  // Get current question
  const currentQuestionData = questions[currentQuestion];

  if (isCompleted) {
    const percentage = Math.round((score / (questions.reduce((sum, q) => sum + q.points, 0))) * 100);
    
    return (
      <div className="bg-white rounded-lg border p-6">
        <div className="text-center">
          <div className="mb-6">
            {percentage >= 70 ? (
              <Award className="w-16 h-16 text-green-500 mx-auto mb-4" />
            ) : (
              <AlertCircle className="w-16 h-16 text-yellow-500 mx-auto mb-4" />
            )}
            <h2 className="text-2xl font-bold text-gray-800 mb-2">
              Assessment Complete!
            </h2>
            <p className="text-gray-600">
              {percentage >= 70 ? "Congratulations! You passed!" : "Keep practicing to improve your score."}
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div className="bg-blue-50 rounded-lg p-4">
              <div className="text-2xl font-bold text-blue-600">{score}</div>
              <div className="text-sm text-blue-800">Points Earned</div>
            </div>
            <div className="bg-green-50 rounded-lg p-4">
              <div className="text-2xl font-bold text-green-600">{percentage}%</div>
              <div className="text-sm text-green-800">Score</div>
            </div>
            <div className="bg-purple-50 rounded-lg p-4">
              <div className="text-2xl font-bold text-purple-600">
                {Object.keys(answers).length}/{questions.length}
              </div>
              <div className="text-sm text-purple-800">Questions Answered</div>
            </div>
          </div>

          <div className="flex justify-center space-x-4">
            <button
              onClick={resetAssessment}
              className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 flex items-center"
            >
              <RotateCcw className="w-4 h-4 mr-2" />
              Try Again
            </button>
            <button
              onClick={() => onComplete && onComplete({ score, percentage, passed: percentage >= 70 })}
              className="px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 flex items-center"
            >
              <CheckCircle className="w-4 h-4 mr-2" />
              Continue
            </button>
          </div>
        </div>
      </div>
    );
  }

  if (!currentQuestionData) {
    return (
      <div className="bg-white rounded-lg border p-6 text-center">
        <BookOpen className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <h3 className="text-lg font-semibold text-gray-600 mb-2">No Questions Available</h3>
        <p className="text-gray-500">Please select topics to generate assessment questions.</p>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg border">
      {/* Header */}
      <div className="p-6 border-b bg-gray-50">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h3 className="text-xl font-semibold text-gray-800">
              {ASSESSMENT_TYPES[assessmentType].name}
            </h3>
            <p className="text-gray-600">{ASSESSMENT_TYPES[assessmentType].description}</p>
          </div>
          
          <div className="flex items-center space-x-4">
            <div className="text-right">
              <div className="text-sm text-gray-600">Time Remaining</div>
              <div className={`text-2xl font-bold ${timeRemaining < 60 ? 'text-red-600' : 'text-gray-800'}`}>
                {formatTime(timeRemaining)}
              </div>
            </div>
            
            <div className="text-right">
              <div className="text-sm text-gray-600">Score</div>
              <div className="text-2xl font-bold text-blue-600">{score}</div>
            </div>
          </div>
        </div>

        {/* Progress Bar */}
        <div className="mb-4">
          <div className="flex justify-between text-sm text-gray-600 mb-2">
            <span>Question {currentQuestion + 1} of {totalQuestions}</span>
            <span>{Math.round(((currentQuestion + 1) / totalQuestions) * 100)}% Complete</span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div 
              className="bg-blue-600 h-2 rounded-full transition-all duration-300"
              style={{ width: `${((currentQuestion + 1) / totalQuestions) * 100}%` }}
            />
          </div>
        </div>

        {/* Controls */}
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            {!isActive ? (
              <button
                onClick={startAssessment}
                className="flex items-center px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700"
              >
                <Play className="w-4 h-4 mr-2" />
                Start Assessment
              </button>
            ) : (
              <button
                onClick={() => setIsActive(!isActive)}
                className="flex items-center px-4 py-2 bg-yellow-600 text-white rounded-md hover:bg-yellow-700"
              >
                <Pause className="w-4 h-4 mr-2" />
                Pause
              </button>
            )}
            
            <button
              onClick={resetAssessment}
              className="flex items-center px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700"
            >
              <RotateCcw className="w-4 h-4 mr-2" />
              Reset
            </button>
          </div>

          <div className="flex items-center space-x-2">
            <button
              onClick={() => setShowHint(!showHint)}
              className="flex items-center px-3 py-2 bg-blue-100 text-blue-700 rounded-md hover:bg-blue-200"
            >
              <Lightbulb className="w-4 h-4 mr-2" />
              Hint
            </button>
          </div>
        </div>
      </div>

      {/* Question Content */}
      <div className="p-6">
        <div className="mb-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center space-x-2">
              <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                currentQuestionData.difficulty === 'EASY' ? 'bg-green-100 text-green-800' :
                currentQuestionData.difficulty === 'MEDIUM' ? 'bg-yellow-100 text-yellow-800' :
                'bg-red-100 text-red-800'
              }`}>
                {currentQuestionData.difficulty}
              </span>
              <span className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-medium">
                {currentQuestionData.points} points
              </span>
            </div>
            
            <div className="text-sm text-gray-600">
              Time Limit: {currentQuestionData.timeLimit}s
            </div>
          </div>

          <h4 className="text-lg font-semibold text-gray-800 mb-4">
            {currentQuestionData.question}
          </h4>

          {currentQuestionData.formula && (
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-3 mb-4">
              <div className="text-sm text-blue-800">
                <strong>Formula:</strong> {currentQuestionData.formula}
              </div>
            </div>
          )}

          {showHint && currentFeedback && (
            <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-4">
              <div className="flex items-start">
                <Lightbulb className="w-5 h-5 text-yellow-600 mt-0.5 mr-3 flex-shrink-0" />
                <div>
                  <h5 className="font-medium text-yellow-800 mb-1">Hint</h5>
                  <p className="text-yellow-700 text-sm">{currentFeedback.hint}</p>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Answer Input */}
        <div className="mb-6">
          {currentQuestionData.type === 'MULTIPLE_CHOICE' && (
            <div className="space-y-2">
              {currentQuestionData.options.map((option, index) => (
                <label key={index} className="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer">
                  <input
                    type="radio"
                    name={`question_${currentQuestionData.id}`}
                    value={option}
                    onChange={(e) => handleAnswerSubmit(currentQuestionData.id, e.target.value)}
                    className="mr-3"
                  />
                  <span className="text-gray-700">{option}</span>
                </label>
              ))}
            </div>
          )}

          {currentQuestionData.type === 'TRUE_FALSE' && (
            <div className="space-y-2">
              <label className="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer">
                <input
                  type="radio"
                  name={`question_${currentQuestionData.id}`}
                  value="true"
                  onChange={(e) => handleAnswerSubmit(currentQuestionData.id, e.target.value)}
                  className="mr-3"
                />
                <span className="text-gray-700">True</span>
              </label>
              <label className="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer">
                <input
                  type="radio"
                  name={`question_${currentQuestionData.id}`}
                  value="false"
                  onChange={(e) => handleAnswerSubmit(currentQuestionData.id, e.target.value)}
                  className="mr-3"
                />
                <span className="text-gray-700">False</span>
              </label>
            </div>
          )}

          {(currentQuestionData.type === 'CALCULATION' || currentQuestionData.type === 'NUMERICAL') && (
            <div>
              <input
                type="number"
                step="0.01"
                placeholder="Enter your answer..."
                onChange={(e) => handleAnswerSubmit(currentQuestionData.id, e.target.value)}
                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
              <p className="text-sm text-gray-500 mt-2">
                Enter your numerical answer. Round to 2 decimal places if needed.
              </p>
            </div>
          )}
        </div>

        {/* Feedback */}
        {showFeedback && currentFeedback && (
          <div className={`mb-6 p-4 rounded-lg border ${
            currentFeedback.isCorrect 
              ? 'bg-green-50 border-green-200' 
              : 'bg-red-50 border-red-200'
          }`}>
            <div className="flex items-start">
              {currentFeedback.isCorrect ? (
                <CheckCircle className="w-5 h-5 text-green-600 mt-0.5 mr-3 flex-shrink-0" />
              ) : (
                <XCircle className="w-5 h-5 text-red-600 mt-0.5 mr-3 flex-shrink-0" />
              )}
              <div>
                <h5 className={`font-medium mb-1 ${
                  currentFeedback.isCorrect ? 'text-green-800' : 'text-red-800'
                }`}>
                  {currentFeedback.isCorrect ? 'Correct!' : 'Incorrect'}
                </h5>
                <p className={`text-sm mb-2 ${
                  currentFeedback.isCorrect ? 'text-green-700' : 'text-red-700'
                }`}>
                  {currentFeedback.message}
                </p>
                <p className={`text-sm ${
                  currentFeedback.isCorrect ? 'text-green-600' : 'text-red-600'
                }`}>
                  {currentFeedback.explanation}
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Navigation */}
        <div className="flex items-center justify-between">
          <button
            onClick={handlePreviousQuestion}
            disabled={currentQuestion === 0}
            className="flex items-center px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Previous
          </button>

          <div className="flex space-x-2">
            {questions.map((_, index) => (
              <button
                key={index}
                onClick={() => setCurrentQuestion(index)}
                className={`w-8 h-8 rounded-full text-sm font-medium ${
                  index === currentQuestion
                    ? 'bg-blue-600 text-white'
                    : answers[questions[index].id]
                    ? 'bg-green-100 text-green-800'
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                }`}
              >
                {answers[questions[index].id] ? <CheckCircle className="w-4 h-4" /> : index + 1}
              </button>
            ))}
          </div>

          <button
            onClick={handleNextQuestion}
            className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
          >
            {currentQuestion === questions.length - 1 ? 'Submit' : 'Next'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default AssessmentEngine;
