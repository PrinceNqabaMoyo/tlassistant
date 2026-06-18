import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function AssessmentUI() {
  const [activeType, setActiveType] = useState("mcq");
  const [mode, setMode] = useState("scaffold");
  const [difficulty, setDifficulty] = useState("medium");
  const [subskill, setSubskill] = useState("format-of-income-statement");
  const [showQuestion, setShowQuestion] = useState(false);

  const modeColors = {
    scaffold: "bg-indigo-50 text-indigo-700 border-indigo-200",
    practice: "bg-emerald-50 text-emerald-700 border-emerald-200",
    marking: "bg-amber-50 text-amber-700 border-amber-200",
  };

  const difficulties = ["easy", "medium", "hard"];

  const subskills = [
    { label: "Format of Income Statement", value: "format-of-income-statement" },
    { label: "Gross Profit Calculation", value: "gross-profit" },
    { label: "Net Profit Calculation", value: "net-profit" },
  ];

  const selectedSubskillLabel =
    subskills.find((s) => s.value === subskill)?.label || "";

  return (
    <div className="min-h-screen bg-slate-50 px-4 py-6 sm:px-6 relative">
      <div className="max-w-5xl mx-auto space-y-6 relative">

        {/* Header */}
        <div>
          <h1 className="text-xl sm:text-2xl font-bold text-slate-800">
            Question Workspace
          </h1>
          <p className="text-slate-500 text-xs sm:text-sm mt-1">
            Grade 11 • Accounting • Income Statements
          </p>
        </div>

        {/* Configuration Panel */}
        {!showQuestion && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
          >
            <Card className="rounded-2xl shadow-sm border border-slate-200 bg-white">
              <CardContent className="p-4 sm:p-6 space-y-6">

                {/* Mode */}
                <div className="space-y-2">
                  <p className="text-xs font-semibold text-slate-500 uppercase tracking-wide">
                    Mode
                  </p>
                  <div className="flex flex-wrap gap-2">
                    {["scaffold", "practice", "marking"].map((m) => (
                      <button
                        key={m}
                        onClick={() => setMode(m)}
                        className={`text-xs px-3 py-2 rounded-full border transition-all capitalize
                          ${mode === m
                            ? modeColors[m]
                            : "bg-white text-slate-500 border-slate-200"}`}
                      >
                        {m}
                      </button>
                    ))}
                  </div>
                </div>

                {/* Controls */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">

                  {/* Difficulty */}
                  <div className="space-y-2">
                    <p className="text-xs font-semibold text-slate-500 uppercase tracking-wide">
                      Difficulty
                    </p>
                    <div className="flex gap-2">
                      {difficulties.map((level) => (
                        <button
                          key={level}
                          onClick={() => setDifficulty(level)}
                          className={`flex-1 px-3 py-2 rounded-xl text-sm capitalize border transition-all
                            ${difficulty === level
                              ? "bg-slate-800 text-white border-slate-800"
                              : "bg-white text-slate-600 border-slate-200"}`}
                        >
                          {level}
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Subskill */}
                  <div className="space-y-2 sm:col-span-2">
                    <p className="text-xs font-semibold text-slate-500 uppercase tracking-wide">
                      Subskill
                    </p>
                    <select
                      value={subskill}
                      onChange={(e) => setSubskill(e.target.value)}
                      className="w-full px-3 py-3 rounded-xl border border-slate-200 text-sm bg-white focus:outline-none focus:ring-2 focus:ring-slate-300"
                    >
                      {subskills.map((skill) => (
                        <option key={skill.value} value={skill.value}>
                          {skill.label}
                        </option>
                      ))}
                    </select>
                  </div>

                  {/* Generate */}
                  <div className="flex items-end">
                    <Button
                      onClick={() => setShowQuestion(true)}
                      className="w-full rounded-xl h-12 text-sm font-semibold"
                    >
                      Generate Question
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          </motion.div>
        )}

        {/* Overlay Background Blur */}
        <AnimatePresence>
          {showQuestion && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="fixed inset-0 bg-slate-900/20 backdrop-blur-sm z-40"
            />
          )}
        </AnimatePresence>

        {/* Question Overlay */}
        <AnimatePresence>
          {showQuestion && (
            <motion.div
              initial={{ opacity: 0, y: 40 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: 20 }}
              transition={{ duration: 0.25 }}
              className="fixed inset-0 z-50 overflow-y-auto px-4 py-10 sm:px-6"
            >
              <div className="max-w-4xl mx-auto space-y-6">
                <QuestionCard
                  type={activeType}
                  mode={mode}
                  difficulty={difficulty}
                  subskillLabel={selectedSubskillLabel}
                  modeColors={modeColors}
                  onEdit={() => setShowQuestion(false)}
                />
                <AnswerCard type={activeType} />
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}

function QuestionCard({
  type,
  mode,
  difficulty,
  subskillLabel,
  modeColors,
  onEdit,
}) {
  const questionText = {
    mcq: "Which account increases on the credit side?",
    matching: "Match the terms with their correct definitions.",
    table: "Complete the Income Statement below using the given figures.",
  };

  return (
    <Card className="rounded-2xl shadow-xl border border-slate-200 bg-white">
      <CardContent className="p-4 sm:p-6 space-y-4">

        {/* Meta Info */}
        <div className="flex flex-wrap items-center justify-between gap-3 text-xs">
          <div className="flex flex-wrap gap-2">
            <button
              onClick={onEdit}
              className={`px-3 py-1 rounded-full border capitalize ${modeColors[mode]}`}
            >
              {mode}
            </button>

            <button
              onClick={onEdit}
              className="px-3 py-1 rounded-full border bg-slate-100 text-slate-700 capitalize"
            >
              {difficulty}
            </button>

            <button
              onClick={onEdit}
              className="px-3 py-1 rounded-full border bg-slate-100 text-slate-700"
            >
              {subskillLabel}
            </button>
          </div>

          {/* Ghost Button */}
          <button
            onClick={onEdit}
            className="text-slate-500 hover:text-slate-700 text-xs underline"
          >
            Change settings
          </button>
        </div>

        {/* Question */}
        <h2 className="text-base sm:text-lg font-semibold text-slate-800 leading-relaxed">
          {questionText[type]}
        </h2>
      </CardContent>
    </Card>
  );
}

function AnswerCard({ type }) {
  return (
    <Card className="rounded-2xl shadow-2xl bg-white">
      <CardContent className="p-4 sm:p-6">
        {type === "mcq" && <MCQAnswer />}
        {type === "matching" && <MatchingAnswer />}
        {type === "table" && <TableAnswer />}
      </CardContent>
    </Card>
  );
}

function MCQAnswer() {
  return (
    <div className="grid gap-3 sm:gap-4">
      {[
        "Assets",
        "Expenses",
        "Income",
        "Drawings",
      ].map((option) => (
        <Button
          key={option}
          variant="outline"
          className="justify-start text-left h-auto py-4 rounded-xl w-full"
        >
          {option}
        </Button>
      ))}
    </div>
  );
}

function MatchingAnswer() {
  const left = ["Gross Profit", "Net Profit", "Assets"];
  const right = [
    "Revenue - Cost of Sales",
    "Revenue - Expenses",
    "Owned resources",
  ];

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
      <div className="space-y-3">
        {left.map((item) => (
          <div key={item} className="p-3 bg-slate-100 rounded-xl">
            {item}
          </div>
        ))}
      </div>
      <div className="space-y-3">
        {right.map((item) => (
          <div
            key={item}
            className="p-3 bg-indigo-50 rounded-xl border border-indigo-200"
          >
            {item}
          </div>
        ))}
      </div>
    </div>
  );
}

function TableAnswer() {
  return (
    <div className="overflow-x-auto">
      <table className="w-full border-collapse text-sm min-w-[320px]">
        <tbody>
          <Row label="Revenue" />
          <Row label="Cost of Sales" />
          <Row label="Gross Profit" bold />
          <Row label="Expenses" />
          <Row label="Net Profit" bold />
        </tbody>
      </table>
    </div>
  );
}

function Row({ label, bold }) {
  return (
    <tr className="border-b last:border-none">
      <td className={`py-3 pr-2 ${bold ? "font-semibold" : ""}`}>
        {label}
      </td>
      <td className="py-3 text-right">
        <Input className="w-24 sm:w-32 ml-auto text-right rounded-lg" />
      </td>
    </tr>
  );
}
