
export const normalizeText = (value) => {
    if (value === null || value === undefined) return '';
    return String(value).trim().replace(/\s+/g, ' ').toLowerCase();
};

export const toNumber = (value) => {
    if (value === null || value === undefined) return null;
    let s = String(value).trim();
    if (!s) return null;

    s = s.replace(/\s+/g, '');
    s = s.replace(/[Rr]/g, '');

    const lastDot = s.lastIndexOf('.');
    const lastComma = s.lastIndexOf(',');

    if (lastDot >= 0 && lastComma >= 0) {
        const decSep = lastDot > lastComma ? '.' : ',';
        const thouSep = decSep === '.' ? ',' : '.';
        s = s.split(thouSep).join('');
        if (decSep === ',') s = s.replace(',', '.');
    } else if (lastComma >= 0) {
        s = s.split('.').join('');
        s = s.replace(',', '.');
    } else {
        s = s.split(',').join('');
    }

    s = s.replace(/[^0-9.\-]/g, '');
    const n = Number(s);
    return Number.isFinite(n) ? n : null;
};

export const buildEmptyJournalAnswer = (question) => {
    const journals = Array.isArray(question?.journals)
        ? question.journals
        : (question?.journal ? [question.journal] : []);
    const out = {};
    journals.forEach((j) => {
        const rows = Array.isArray(j?.rows) ? j.rows : [];
        const titleFields = Array.isArray(j?.title_fields) ? j.title_fields : [];
        titleFields.forEach((tf) => {
            const id = tf?.cell_id;
            if (!id) return;
            out[String(id)] = '';
        });
        rows.forEach((row) => {
            (Array.isArray(row) ? row : []).forEach((cell) => {
                if (!cell?.cell_id) return;
                out[String(cell.cell_id)] = cell?.value || '';
            });
        });
    });
    return { cells: out, extra_rows_by_table: {} };
};

export const getExpectedByCellId = (question) => (question?.correct_map && typeof question.correct_map === 'object') ? question.correct_map : {};

export const isNumericExpected = (expected) => {
    if (expected === null || expected === undefined) return false;
    if (typeof expected === 'number') return true;
    const s = String(expected).trim();
    if (!s) return false;
    return /^-?\d+(?:\.\d+)?$/.test(s);
};

export const journalTypeLabel = (journalTypeRaw) => {
    const jt = String(journalTypeRaw || '').trim().toLowerCase();
    if (!jt) return 'Table';
    return jt.replace(/_/g, ' ');
};

export const getWordBank = (question) => Array.isArray(question?.word_bank) ? question.word_bank : [];

export const getCorrectMap = (question) => (question?.correct_map && typeof question.correct_map === 'object') ? question.correct_map : {};

export const buildEmptyWordbankAnswer = (question) => {
    const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
    const selections = {};
    for (let i = 0; i < rows.length; i += 1) {
        selections[String(i)] = { '2': null };
    }
    return { selections, activeTokenId: null };
};

export const getUsedTokenIds = (ans) => {
    const selections = ans?.selections && typeof ans.selections === 'object' ? ans.selections : {};
    const used = new Set();
    Object.values(selections).forEach((row) => {
        if (!row) return;
        const v = row['2'];
        if (v) used.add(String(v));
    });
    return used;
};

export const buildEmptyBundleAnswer = (question) => {
    const parts = Array.isArray(question?.parts) ? question.parts : [];
    return parts.map((p) => {
        if (p?.question_type === 'table_wordbank') return buildEmptyWordbankAnswer(p);
        if (p?.question_type === 'journal' || p?.question_type === 'ledger') return buildEmptyJournalAnswer(p);
        return '';
    });
};
