// App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./Header";
import ThreadSection from "./ThreadSection";
import QuestionForm from "./QuestionForm";
import AnswerForm from "./AnswerForm";

export default function App() {
  return (
    <Router>
      <div className="w-screen h-screen bg-gray-100 flex flex-col items-center py-6 px-4 overflow-auto">
        <Header />
        <Routes>
          <Route path="/" element={<ThreadSection />} />
          <Route path="/question" element={<QuestionForm />} />
          <Route path="/answer" element={<AnswerForm />} />
        </Routes>
      </div>
    </Router>
  );
}
