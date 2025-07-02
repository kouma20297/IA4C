import React, { useState } from "react";

export default function QuestionForm() {
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`タイトル: ${title}\n本文: ${body}`);
    // 本番ではここでAPI送信など
  };

  return (
    <div className="max-w-4xl w-full bg-white rounded-xl p-6 shadow-md mt-4 mx-auto">
      <h2 className="text-2xl text-black font-bold mb-4">質問投稿フォーム</h2>

      <form onSubmit={handleSubmit}>
        <label className="block mb-2 font-semibold" htmlFor="title">
          タイトル
        </label>
        <input
          id="title"
          type="text"
          className="w-full bg-gray-100 text-black border border-gray-300 rounded px-3 py-2 mb-4"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="質問のタイトルを入力してください"
          required
        />

        <label className="block mb-2 font-semibold" htmlFor="body">
          本文
        </label>
        <textarea
          id="body"
          className="w-full bg-gray-100 text-black border border-gray-300 rounded px-3 py-2 mb-4"
          rows={6}
          value={body}
          onChange={(e) => setBody(e.target.value)}
          placeholder="質問の詳細を入力してください"
          required
        />

        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          投稿する
        </button>
      </form>
    </div>
  );
}
