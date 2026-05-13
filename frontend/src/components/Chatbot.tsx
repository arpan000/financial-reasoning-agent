"use client";

import { useState } from "react";

export default function Chatbot() {

    const [message, setMessage] = useState("");

    const [chatHistory, setChatHistory] = useState<any[]>([]);

    const [loading, setLoading] = useState(false);

    const sessionId = "user001";

    async function sendMessage() {

        if (!message.trim()) return;

        const userMessage = {
            role: "user",
            content: message
        };

        setChatHistory((prev) => [
            ...prev,
            userMessage
        ]);

        setLoading(true);

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/financial-chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({

                        session_id: sessionId,

                        message: message
                    })
                }
            );

            const data = await response.json();

            const aiMessage = {

                role: "assistant",

                content: data.response
            };

            setChatHistory((prev) => [
                ...prev,
                aiMessage
            ]);

        } catch (error) {

            console.error(error);
        }

        setMessage("");

        setLoading(false);
    }

    return (

        <div className="max-w-4xl mx-auto p-6">

            <h1 className="text-5xl font-bold mb-8">
                AI Financial Advisor
            </h1>

            <div className="border rounded-xl p-4 h-[500px] overflow-y-auto bg-white">

                {chatHistory.map((chat, index) => (

                    <div
                        key={index}
                        className={`mb-4 flex ${
                            chat.role === "user"
                                ? "justify-end"
                                : "justify-start"
                        }`}
                    >

                        <div
                            className={`max-w-[75%] p-4 rounded-xl ${
                                chat.role === "user"
                                    ? "bg-black text-white"
                                    : "bg-gray-200 text-black"
                            }`}
                        >

                            {chat.content}

                        </div>

                    </div>
                ))}

                {loading && (

                    <div className="text-gray-500">
                        AI is thinking...
                    </div>
                )}

            </div>

            <div className="flex gap-4 mt-6">

                <textarea
                    value={message}
                    onChange={(e) =>
                        setMessage(e.target.value)
                    }

                    placeholder="Ask financial questions..."

                    className="flex-1 border rounded-xl p-4 h-24"
                />

                <button
                    onClick={sendMessage}

                    className="bg-black text-white px-6 py-4 rounded-xl"
                >
                    Send
                </button>

            </div>

        </div>
    );
}