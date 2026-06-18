import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\src\components\workspace\Workspace.jsx'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if line.startswith("import FreeformWorkspaceLanding from './shared/FreeformWorkspaceLanding';"):
        continue
    
    if "const showFreeformLanding = workspaceMode === 'freeform'" in line:
        skip = True
        
    if skip:
        if line.strip() == "{/* --- Practice Mode (Visible when workspaceMode is 'practice') --- */}":
            skip = False
            new_lines.append('''    const showFreeformLanding = false;

    return (
        <div className="bg-gray-50 min-h-screen">

            {workspaceMode === 'freeform' && (
                <div className="flex h-screen items-center justify-center bg-gray-50 p-6">
                    <div className="bg-white p-8 rounded-xl shadow-lg text-center max-w-md w-full border border-gray-100">
                        <div className="mb-6 flex justify-center">
                            <div className="bg-blue-50 p-4 rounded-full text-blue-500">
                                <FileText size={48} />
                            </div>
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800 mb-4">No Workspace Selected</h2>
                        <p className="text-gray-600 mb-8 leading-relaxed">
                            Please select a topic and mode from the Curriculum section to begin your learning session.
                        </p>
                        <button
                            onClick={() => {
                                if (typeof setView === 'function') {
                                    setView('curriculum_helper');
                                }
                            }}
                            className="w-full bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors font-semibold shadow-sm hover:shadow-md"
                        >
                            Go to Curriculum
                        </button>
                    </div>
                </div>
            )}

''')
            new_lines.append(line)
        continue
        
    new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Workspace.jsx patched.')
