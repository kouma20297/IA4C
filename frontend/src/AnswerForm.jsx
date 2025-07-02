import React from "react";

export default function AnswerForm() {
  return (
    <section className="bg-white w-full max-w-4xl px-6 py-6 shadow-md mt-4 rounded">
      <h2 className="text-lg font-semibold mb-2">質問内容</h2>
      <p className="text-sm text-gray-700 mb-4">
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      </p>
      <h3 className="text-md font-medium mb-2">回答投稿</h3>
      <textarea
        className="w-full h-32 border border-gray-300 p-2 rounded resize-none"
        placeholder="回答を入力してください"
      />
      <div className="flex justify-end mt-4 gap-4">
        <button className="px-4 py-2 bg-gray-300 rounded">キャンセル</button>
        <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
          送信
        </button>
      </div>
    </section>
  );
}
