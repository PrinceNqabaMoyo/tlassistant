import { useState } from "react";

/**
 * CAPS-style General Ledger UI (T-Account Layout)
 * - Proper Debit | Spine | Credit structure
 * - Period auto-repeat (grey but editable)
 * - Add + Delete row support
 * - Optional underlined totals row (manual entry ONLY — no auto-summing)
 */

const makeEmptySide = (period = "Feb 2026") => ({
  period,
  day: "",
  details: "",
  folio: "",
  amount: "",
});

const makeRow = (period = "Feb 2026") => ({
  left: makeEmptySide(period),
  right: makeEmptySide(period),
});

export default function Ledger() {
  const [rows, setRows] = useState(
    Array.from({ length: 8 }, () => makeRow("Feb 2026"))
  );

  const [showTotals, setShowTotals] = useState(false);
  const [manualTotals, setManualTotals] = useState({ debit: "", credit: "" });

  const addRow = () => {
    const lastPeriod = rows[rows.length - 1]?.left.period || "";
    setRows([...rows, makeRow(lastPeriod)]);
  };

  const deleteRow = (index) => {
    const updated = rows.filter((_, i) => i !== index);
    setRows(updated.length > 0 ? updated : [makeRow("")]);
  };

  const updateCell = (rowIndex, side, field, value) => {
    setRows((prev) => {
      const updated = prev.map((r, i) => {
        if (i !== rowIndex) return r;
        return {
          ...r,
          [side]: {
            ...r[side],
            [field]: value,
          },
        };
      });

      // Auto-repeat period downward
      if (field === "period") {
        for (let i = rowIndex + 1; i < updated.length; i++) {
          if (updated[i][side].period === prev[rowIndex][side].period) {
            updated[i] = {
              ...updated[i],
              [side]: {
                ...updated[i][side],
                period: value,
              },
            };
          } else {
            break;
          }
        }
      }

      return updated;
    });
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>📘 General Ledger (CAPS Format)</h2>

      <table style={styles.table}>
        <thead>
          <tr>
            <th colSpan={5} style={styles.header}>Debit (Dr)</th>
            <th style={styles.spine}></th>
            <th colSpan={5} style={styles.header}>Credit (Cr)</th>
            <th style={styles.header}>Del</th>
          </tr>
          <tr>
            <th style={styles.header}>Period</th>
            <th style={styles.header}>Day</th>
            <th style={styles.header}>Details</th>
            <th style={styles.header}>Folio</th>
            <th style={styles.header}>Amount</th>
            <th style={styles.spine}></th>
            <th style={styles.header}>Period</th>
            <th style={styles.header}>Day</th>
            <th style={styles.header}>Details</th>
            <th style={styles.header}>Folio</th>
            <th style={styles.header}>Amount</th>
            <th style={styles.header}></th>
          </tr>
        </thead>

        <tbody>
          {rows.map((row, index) => (
            <tr key={index}>
              {/* Debit Side */}
              <td style={styles.td}>
                <input
                  style={{ ...styles.input, ...styles.period }}
                  value={row.left.period}
                  onChange={(e) =>
                    updateCell(index, "left", "period", e.target.value)
                  }
                />
              </td>
              <td style={styles.td}>
                <input
                  style={styles.input}
                  value={row.left.day}
                  onChange={(e) =>
                    updateCell(index, "left", "day", e.target.value)
                  }
                />
              </td>
              <td style={styles.td}>
                <input
                  style={styles.input}
                  value={row.left.details}
                  onChange={(e) =>
                    updateCell(index, "left", "details", e.target.value)
                  }
                />
              </td>
              <td style={styles.td}>
                <input
                  style={styles.input}
                  value={row.left.folio}
                  onChange={(e) =>
                    updateCell(index, "left", "folio", e.target.value)
                  }
                />
              </td>
              <td style={styles.td}>
                <input
                  style={{ ...styles.input, ...styles.numeric }}
                  value={row.left.amount}
                  onChange={(e) =>
                    updateCell(index, "left", "amount", e.target.value)
                  }
                />
              </td>

              {/* Spine */}
              <td style={styles.spine}></td>

              {/* Credit Side */}
              <td style={styles.td}>
                <input
                  style={{ ...styles.input, ...styles.period }}
                  value={row.right.period}
                  onChange={(e) =>
                    updateCell(index, "right", "period", e.target.value)
                  }
                />
              </td>
              <td style={styles.td}>
                <input
                  style={styles.input}
                  value={row.right.day}
                  onChange={(e) =>
                    updateCell(index, "right", "day", e.target.value)
                  }
                />
              </td>
              <td style={styles.td}>
                <input
                  style={styles.input}
                  value={row.right.details}
                  onChange={(e) =>
                    updateCell(index, "right", "details", e.target.value)
                  }
                />
              </td>
              <td style={styles.td}>
                <input
                  style={styles.input}
                  value={row.right.folio}
                  onChange={(e) =>
                    updateCell(index, "right", "folio", e.target.value)
                  }
                />
              </td>
              <td style={styles.td}>
                <input
                  style={{ ...styles.input, ...styles.numeric }}
                  value={row.right.amount}
                  onChange={(e) =>
                    updateCell(index, "right", "amount", e.target.value)
                  }
                />
              </td>

              {/* Delete */}
              <td style={styles.td}>
                <button
                  style={styles.deleteButton}
                  onClick={() => deleteRow(index)}
                >
                  ✕
                </button>
              </td>
            </tr>
          ))}

          {showTotals && (
            <tr>
              <td colSpan={4} style={styles.totalsLabel}>Totals</td>
              <td style={styles.totalsValue}>
                <input
                  style={{ ...styles.input, ...styles.numeric }}
                  value={manualTotals.debit}
                  onChange={(e) =>
                    setManualTotals((t) => ({ ...t, debit: e.target.value }))
                  }
                />
              </td>

              <td style={styles.spine}></td>

              <td colSpan={4} style={styles.totalsLabel}></td>
              <td style={styles.totalsValue}>
                <input
                  style={{ ...styles.input, ...styles.numeric }}
                  value={manualTotals.credit}
                  onChange={(e) =>
                    setManualTotals((t) => ({ ...t, credit: e.target.value }))
                  }
                />
              </td>
              <td style={styles.td}></td>
            </tr>
          )}
        </tbody>
      </table>

      <div style={styles.controls}>
        <button onClick={addRow} style={styles.button}>+ Add Row</button>
        <button onClick={() => setShowTotals((s) => !s)} style={styles.button}>
          {showTotals ? "Hide totals" : "Add totals"}
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "1300px",
    margin: "auto",
    padding: "12px",
    fontFamily: "Inter, system-ui, sans-serif",
  },
  title: {
    marginBottom: "8px",
  },
  table: {
    width: "100%",
    borderCollapse: "collapse",
    tableLayout: "fixed",
  },
  header: {
    border: "1px solid #000",
    padding: "6px",
    background: "#e5e7eb",
    fontWeight: "600",
    textAlign: "center",
  },
  td: {
    border: "1px solid #000",
    padding: 0,
  },
  input: {
    width: "100%",
    padding: "6px",
    border: "none",
    outline: "none",
    boxSizing: "border-box",
    textAlign: "center",
  },
  period: {
    color: "#6b7280",
  },
  numeric: {
    fontFamily: "ui-monospace, monospace",
    textAlign: "right",
    paddingRight: "6px",
  },
  spine: {
    width: "10px",
    borderLeft: "3px solid #000",
    borderRight: "3px solid #000",
    background: "#fff",
  },
  totalsLabel: {
    borderTop: "2px solid #000",
    padding: "6px",
    textAlign: "right",
    fontWeight: 600,
    textDecoration: "underline",
  },
  totalsValue: {
    borderTop: "2px solid #000",
    padding: "6px",
    textAlign: "right",
    fontWeight: 600,
    textDecoration: "underline",
  },
  controls: {
    marginTop: "8px",
    display: "flex",
    gap: "8px",
  },
  button: {
    padding: "6px 12px",
    border: "1px solid #000",
    background: "white",
    cursor: "pointer",
  },
  deleteButton: {
    width: "100%",
    height: "100%",
    border: "none",
    background: "#f3f4f6",
    cursor: "pointer",
    fontWeight: "bold",
  },
};
