import React from "react";
import { useNavigate } from "react-router-dom";

export default function QuestionForm() {
  const navigate = useNavigate();

  const handleCancel = () => {
    navigate("/"); // トップページに戻る
  };

  return (
    <div className="max-w-4xl w-full bg-white rounded-xl p-6 shadow-md">
      <h2 className="text-2xl font-bold mb-4">質問投稿フォーム</h2>
      {/* フォーム内容ここに */}
      
      {/* キャンセルボタン */}
      <button
        type="button"
        onClick={handleCancel}
        className="bg-gray-300 px-4 py-2 rounded mr-2 hover:bg-gray-400"
      >
        キャンセル
      </button>

      {/* 送信ボタンなど他のボタン */}
      <button
        type="submit"
        className="bg-blue-500 px-4 py-2 rounded text-white hover:bg-blue-600"
      >
        送信
      </button>
    </div>
  );
}
