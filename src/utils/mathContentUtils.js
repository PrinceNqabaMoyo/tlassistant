/**
 * Math and text content processing utilities extracted from App.jsx
 */

export const getPlainTextFromHtml = (htmlString) => {
  if (!htmlString) return "";
  const parser = new DOMParser();
  const doc = parser.parseFromString(
    htmlString
      .replace(/<br\s*\/?>/gi, ", ")
      .replace(/<p>|<\/p>|<div>|<\/div>/g, ", ")
      .replace(/&nbsp;/g, ' '),
    'text/html'
  );
  let text = doc.body.textContent || "";
  return text.replace(/\s+/g, ' ').trim();
};

export const detectMathStructure = (content) => {
  if (typeof content !== 'string') return false;

  const mathPatterns = [
    /[=+\-*/^√∫∑∏]/g,
    /[a-zA-Z]\d+/g,
    /\([^)]*\)/g,
    /\d+\.\d+/g,
    /[≤≥≠≈]/g,
    /\b\d+\b/g,
    /[a-zA-Z]\s*[=]\s*[a-zA-Z0-9]/g,
    /\b(sin|cos|tan|log|ln|exp)\b/gi,
    /\b(area|perimeter|volume|surface area|circumference)\b/gi,
    /\b(percentage|ratio|proportion|fraction)\b/gi,
    /\b(profit|loss|cost|price|discount|tax)\b/gi,
    /\b(velocity|acceleration|force|mass|energy)\b/gi,
    /\b(concentration|molarity|density|pressure)\b/gi,
    /\b(cell|organism|population|growth rate)\b/gi,
    /\b(historical|period|century|decade|era)\b/gi,
    /\b(latitude|longitude|distance|scale|map)\b/gi,
    /\b(economic|GDP|inflation|interest rate|exchange rate)\b/gi
  ];

  const mathScore = mathPatterns.reduce((score, pattern) => {
    return score + (content.match(pattern) || []).length;
  }, 0);

  return mathScore > 1;
};

export const formatMathematicalContent = (content) => {
  if (!detectMathStructure(content)) {
    return content;
  }

  let formatted = content
    .replace(/([=+\-*/^])/g, '\n$1 ')
    .replace(/([a-zA-Z]\d+)/g, '\n$1')
    .replace(/(\d+\.\d+)/g, '\n$1')
    .replace(/(\([^)]*\))/g, '\n$1')
    .replace(/(\b\d+\b)/g, '\n$1')
    .replace(/\b(sin|cos|tan|log|ln|exp)\b/gi, '\n$1')
    .replace(/\b(area|perimeter|volume|surface area|circumference)\b/gi, '\n$1')
    .replace(/\b(percentage|ratio|proportion|fraction)\b/gi, '\n$1')
    .replace(/\b(profit|loss|cost|price|discount|tax)\b/gi, '\n$1')
    .replace(/\b(GDP|inflation|interest rate|exchange rate)\b/gi, '\n$1')
    .replace(/\b(velocity|acceleration|force|mass|energy)\b/gi, '\n$1')
    .replace(/\b(concentration|molarity|density|pressure)\b/gi, '\n$1')
    .replace(/\b(cell|organism|population|growth rate)\b/gi, '\n$1')
    .replace(/\b(historical|period|century|decade|era)\b/gi, '\n$1')
    .replace(/\b(latitude|longitude|distance|scale|map)\b/gi, '\n$1')
    .replace(/, /g, '\n')
    .replace(/;\s*/g, '\n')
    .replace(/\.\s+/g, '.\n')
    .replace(/\n+/g, '\n')
    .replace(/\n\s*\n\s*\n/g, '\n\n')
    .trim();

  return formatted;
};

export const shouldUseMathStructure = (subject, content) => {
  return detectMathStructure(content);
};

export const formatMathematicalExpressions = (text) => {
  if (!text || typeof text !== 'string') return text;

  return text
    .replace(/(\w+)\s*=\s*(\w+)/g, '$1 = $2')
    .replace(/(\d+)\s*\+\s*(\d+)/g, '$1 + $2')
    .replace(/(\d+)\s*-\s*(\d+)/g, '$1 - $2')
    .replace(/(\d+)\s*\*\s*(\d+)/g, '$1 × $2')
    .replace(/(\d+)\s*\/\s*(\d+)/g, '$1 ÷ $2')
    .replace(/(\w+)\^(\d+)/g, '$1^$2')
    .replace(/\b(sin|cos|tan|log|ln)\b/gi, '$1')
    .replace(/(\d+)\s*(cm|m|km|mm)/g, '$1 $2')
    .replace(/(\d+)\s*(g|kg|mg)/g, '$1 $2')
    .replace(/(\d+)\s*(ml|l|cl)/g, '$1 $2')
    .replace(/(\d+)\s*(°C|°F|K)/g, '$1 $2')
    .replace(/(\d+)\s*%/g, '$1%')
    .replace(/R\s*(\d+)/g, 'R$1')
    .replace(/\$(\d+)/g, '$$1')
    .replace(/\s+/g, ' ')
    .trim();
};

export const processMathematicalContent = (content, subject) => {
  if (!content || typeof content !== 'string') return content;

  const needsMathStructure = detectMathStructure(content);
  if (!needsMathStructure) {
    return content;
  }

  let formatted = content;
  if (subject?.name === 'Mathematics' || subject?.name === 'Mathematical Literacy' || subject?.name === 'Technical Mathematics') {
    formatted = formatMathematicalContent(content);
  } else if (subject?.name === 'Physical Sciences' || subject?.name === 'Chemistry' || subject?.name === 'Biology') {
    formatted = formatMathematicalContent(content)
      .replace(/(\d+\.\d+e[+-]\d+)/g, '\n$1')
      .replace(/(\d+)\s*(mol|g\/mol|L\/mol)/g, '\n$1 $2');
  } else if (subject?.name === 'Accounting' || subject?.name === 'Business Studies' || subject?.name === 'Economic and Management Sciences') {
    formatted = formatMathematicalContent(content)
      .replace(/(\d+)\s*(profit|loss|cost|price)/gi, '\n$1 $2')
      .replace(/(\d+)\s*%/g, '\n$1%');
  } else {
    formatted = formatMathematicalContent(content);
  }

  return formatted;
};
