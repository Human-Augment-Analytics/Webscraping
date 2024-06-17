'use client';
import React, { useState } from "react";
import axios from "axios";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer";

interface ChatDrawer {
  chatType: 'Settings' | 'NLI' | 'Documentation';
}

const ChatDrawer: React.FC<ChatDrawer> = ({ chatType }) => {
  const [messages, setMessages] = useState([
    { role: 'system', content: 'Hello! How can I assist you today?' }
  ]);
  const [inputValue, setInputValue] = useState('');

  const handleSend = async () => {
    if (inputValue.trim() === '') return;

    const newMessage = { role: 'user', content: inputValue };
    const updatedMessages = [...messages, newMessage];

    setMessages(updatedMessages);
    setInputValue('');

    const token = localStorage.getItem('token');

    try {
      const response = await axios.post('https://haaggtbe-production.up.railway.app/ask', {
      // const response = await axios.post('http://localhost:8000/ask', {
        conversation: updatedMessages,
      }, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });

      const systemMessage = response.data.conversation.slice(-1)[0];
      setMessages((prevMessages) => [...prevMessages, systemMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = { role: 'system', content: 'An error occurred while processing your request.' };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
  };

  return (
    <Drawer>
      <DrawerTrigger asChild>
        <Button variant="outline">{chatType}</Button>
      </DrawerTrigger>
      <DrawerContent className="max-h-screen">
        <div className="mx-auto min-w-[600px] w-full max-w-sm">
          <DrawerHeader>
            <DrawerTitle>{chatType}</DrawerTitle>
            <DrawerDescription>{chatType}</DrawerDescription>
          </DrawerHeader>
          <div className="flex flex-col space-y-4 overflow-y-auto max-h-[500px]">
            {messages.map((message, index) => (
              <div
                key={index}
                className={`p-2 rounded-md ${
                  message.role === 'user' ? 'border-2 border-primary text-black self-end' : 'bg-primary self-start'
                }`}
              >
                {message.content}
              </div>
            ))}
          </div>
          <DrawerFooter>
            <div className="flex items-center space-x-2">
              <Input
                placeholder="Type your message here..."
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
              />
              <Button onClick={handleSend}>Submit</Button>
            </div>
            <DrawerClose asChild>
              <Button variant="outline">Close</Button>
            </DrawerClose>
          </DrawerFooter>
        </div>
      </DrawerContent>
    </Drawer>
  );
};

export default ChatDrawer;
