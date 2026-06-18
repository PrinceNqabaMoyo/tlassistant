# Update internal imports in Grade 12 mathematics and accounting files after moving

$basePath = "C:\Users\princ\fundile-tlassistant-vite\src\components\workspace\grade12"

# Grade 12 Mathematics files (3 levels deep) - need ../../../VisualAidsPanel
$g12MathFiles = @(
    "$basePath\mathematics\finance\Grade12FinanceScaffold.jsx",
    "$basePath\mathematics\finance\Grade12FinancePractice.jsx",
    "$basePath\mathematics\functions\Grade12FunctionsScaffold.jsx",
    "$basePath\mathematics\functions\Grade12FunctionsPractice.jsx",
    "$basePath\mathematics\patterns-sequences-series\Grade12PatternsSequencesSeriesScaffold.jsx",
    "$basePath\mathematics\patterns-sequences-series\Grade12PatternsSequencesSeriesPractice.jsx",
    "$basePath\mathematics\trigonometry\Grade12TrigonometryScaffold.jsx",
    "$basePath\mathematics\trigonometry\Grade12TrigonometryPractice.jsx"
)

foreach ($file in $g12MathFiles) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw
        $content = $content -replace "from '\.\./VisualAidsPanel'", "from '../../../VisualAidsPanel'"
        $content = $content -replace "from '\.\./\.\./\.\./utils/renderMathText'", "from '../../../../../utils/renderMathText.jsx'"
        $content = $content -replace "from '\.\./FunctionGraph'", "from '../../../FunctionGraph'"
        Set-Content -Path $file -Value $content -NoNewline
        Write-Host "Updated: $file"
    }
}

# Grade 12 Accounting files (2 levels deep) - need ../../VisualAidsPanel
$g12AcctFiles = @(
    "$basePath\accounting\Grade12AccountingScaffold.jsx",
    "$basePath\accounting\Grade12AccountingPractice.jsx"
)

foreach ($file in $g12AcctFiles) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw
        $content = $content -replace "from '\.\./VisualAidsPanel'", "from '../../VisualAidsPanel'"
        Set-Content -Path $file -Value $content -NoNewline
        Write-Host "Updated: $file"
    }
}

Write-Host "`nAll Grade 12 internal imports updated successfully!"
