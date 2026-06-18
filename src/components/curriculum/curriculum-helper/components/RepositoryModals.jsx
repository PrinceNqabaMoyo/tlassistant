import React from 'react';
import { X } from 'lucide-react';
import MathComponentsRepository from '../../../math/MathComponentsRepository';
import ChemistryComponentsRepository from '../../../chemistry/ChemistryComponentsRepository';
import PhysicsComponentsRepository from '../../../physics/PhysicsComponentsRepository';
import CrossDisciplinaryComponentsRepository from '../../../cross-disciplinary/CrossDisciplinaryComponentsRepository';
import MathematicalVisualAids from '../../MathematicalVisualAids';
import ComponentOverlay from '../../../shared/ComponentOverlay';

const RepositoryModals = ({
    selectedSubject,
    selectedGrade,
    setView,
    showMathComponentsRepository,
    setShowMathComponentsRepository,
    showChemistryComponentsRepository,
    setShowChemistryComponentsRepository,
    showPhysicsComponentsRepository,
    setShowPhysicsComponentsRepository,
    showCrossDisciplinaryComponentsRepository,
    setShowCrossDisciplinaryComponentsRepository,
    selectedComponent,
    setSelectedComponent,
    isComponentOverlayVisible,
    setIsComponentOverlayVisible,
    isComponentFullscreen,
    setIsComponentFullscreen,
}) => (
    <>
        <MathComponentsRepository
            isVisible={showMathComponentsRepository}
            onSelectComponent={(component) => {
                setShowMathComponentsRepository(false);
                console.log('Selected math component:', component);
            }}
            selectedSubject={selectedSubject}
            selectedGrade={selectedGrade}
            setView={setView}
        />

        <ChemistryComponentsRepository
            isVisible={showChemistryComponentsRepository}
            onSelectComponent={(component) => {
                setShowChemistryComponentsRepository(false);
                console.log('Selected chemistry component:', component);
            }}
            selectedSubject={selectedSubject}
            selectedGrade={selectedGrade}
        />

        <PhysicsComponentsRepository
            isVisible={showPhysicsComponentsRepository}
            onSelectComponent={(component) => {
                setShowPhysicsComponentsRepository(false);
                console.log('Selected physics component:', component);
            }}
            selectedSubject={selectedSubject}
            selectedGrade={selectedGrade}
        />

        <CrossDisciplinaryComponentsRepository
            isVisible={showCrossDisciplinaryComponentsRepository}
            onSelectComponent={(component) => {
                setShowCrossDisciplinaryComponentsRepository(false);
                console.log('Selected cross-disciplinary component:', component);
            }}
            selectedSubject={selectedSubject}
            selectedGrade={selectedGrade}
        />

        {showMathComponentsRepository && (
            <div className="fixed inset-0 bg-white z-50 flex flex-col">
                <div className="flex items-center justify-between p-6 border-b border-gray-200 bg-white">
                    <h2 className="text-2xl font-bold text-gray-800">Mathematical Visual Aids</h2>
                    <button
                        onClick={() => setShowMathComponentsRepository(false)}
                        className="flex items-center space-x-2 px-4 py-2 text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-lg transition-colors"
                    >
                        <X className="h-5 w-5" />
                        <span>Close</span>
                    </button>
                </div>
                <div className="flex-1 overflow-y-auto p-6">
                    <MathematicalVisualAids
                        onComponentSelect={(component) => {
                            setShowMathComponentsRepository(false);
                            setSelectedComponent(component);
                            setIsComponentOverlayVisible(true);
                        }}
                    />
                </div>
            </div>
        )}

        <ComponentOverlay
            selectedComponent={selectedComponent}
            isVisible={isComponentOverlayVisible}
            isFullscreen={isComponentFullscreen}
            onClose={() => {
                setIsComponentOverlayVisible(false);
                setSelectedComponent(null);
                setIsComponentFullscreen(false);
                setShowMathComponentsRepository(true);
            }}
            onToggleFullscreen={() => setIsComponentFullscreen(!isComponentFullscreen)}
            setView={setView}
        />
    </>
);

export default RepositoryModals;
