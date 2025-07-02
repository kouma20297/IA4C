import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="bg-red-700 text-white w-full max-w-4xl rounded-t-xl px-6 py-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">kacoms 知恵袋</h1>
      <div className="flex items-center gap-4">
        <Link
          to="/question"
          className="bg-blue-500 px-4 py-1 rounded text-sm block text-center no-underline text-white hover:bg-blue-600"
        >
          質問投稿
        </Link>
        <button className="bg-gray-200 text-black px-4 py-1 rounded text-sm flex items-center gap-1">
          <span className="material-icons">lock</span>ログアウト
        </button>
      </div>
    </header>
  );
}
