import React from 'react'
import Image from "next/image";
import ChatDrawer from "@/components/ChatDrawer";
import LogInOut from "@/components/LogInOut";

const Nav = () => {
    return (
        <nav className="fixed top-0 left-0 w-full bg-old-gold text-gt-white shadow-lg z-50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex items-center justify-between h-16">
                    <div className="flex items-center">
                        <Image
                            width={244}
                            height={42}
                            alt="GT"
                            src="/gt.svg"
                        />
                    </div>
                    <div className="flex space-x-4">
                        <ChatDrawer chatType='Settings' />
                        <ChatDrawer chatType='NLI' />
                        <ChatDrawer chatType='Documentation' />
                        <LogInOut />
                    </div>
                </div>
            </div>
        </nav>
    );
};

export default Nav;
