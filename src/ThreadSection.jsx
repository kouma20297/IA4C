import React, { useState } from "react";

const dummyQuestions = [
  {
    id: 1,
    title: "Reactでフォームのバリデーションをどうやる？",
    body: "React Hook Formを使うのがおすすめです。具体的な例は〜",
    createdAt: "2025-07-01 10:00",
    answered: false,
  },
  {
    id: 2,
    title: "JavaScriptの非同期処理のコツは？",
    body: "Promiseやasync/awaitを理解すると便利です。例を示します...",
    createdAt: "2025-06-28 15:30",
    answered: true,
  },
  // 他の質問があれば追加してください
];

export default function ThreadSection() {
  const [tab, setTab] = useState("open"); // "open"か"past"
  const [selectedId, setSelectedId] = useState(null);

  const filteredQuestions = dummyQuestions.filter((q) =>
    tab === "open" ? !q.answered : q.answered
  );
  const selectedQuestion = dummyQuestions.find((q) => q.id === selectedId);

  return (
    <div className="max-w-4xl w-full bg-white rounded-xl p-6 shadow-md mt-4 mx-auto">
      {/* タブ切り替え */}
      <div className="flex justify-center border-b mb-4 w-full max-w-md mx-auto">
        <button
          className={`flex-1 text-center px-6 py-2 ${
            tab === "open"
              ? "border-b-2 border-blue-600 font-bold"
              : "text-gray-500"
          }`}
          onClick={() => {
            setTab("open");
            setSelectedId(null);
          }}
        >
          回答募集中
        </button>
        <button
          className={`flex-1 text-center px-6 py-2 ${
            tab === "past"
              ? "border-b-2 border-blue-600 font-bold"
              : "text-gray-500"
          }`}
          onClick={() => {
            setTab("past");
            setSelectedId(null);
          }}
        >
          過去の回答
        </button>
      </div>

      {/* 詳細 or 一覧 */}
      {selectedQuestion ? (
        <div>
          <h3 className="text-xl font-bold mb-2">{selectedQuestion.title}</h3>
          <p className="text-gray-600 mb-4">{selectedQuestion.createdAt}</p>
          <p className="whitespace-pre-wrap">{selectedQuestion.body}</p>

          <button
            className="mt-4 text-blue-600 hover:underline"
            onClick={() => setSelectedId(null)}
          >
            一覧に戻る
          </button>
        </div>
      ) : (
        <ul>
          {filteredQuestions.length === 0 ? (
            <p className="text-gray-500">表示する質問がありません。</p>
          ) : (
            filteredQuestions.map((q) => (
              <li
                key={q.id}
                className="border-b py-2 cursor-pointer hover:bg-gray-100 rounded"
                onClick={() => setSelectedId(q.id)}
              >
                <div className="text-blue-600 hover:underline">{q.title}</div>
                <div className="text-gray-500 text-sm">{q.createdAt}</div>
              </li>
            ))
          )}
        </ul>
      )}
    </div>
  );
}
