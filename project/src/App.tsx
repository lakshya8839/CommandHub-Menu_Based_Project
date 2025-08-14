import React, { useState } from 'react';
import { Terminal, Docker, Bot, Wand2, MessageCircle, Brain, Home, Github, Linkedin } from 'lucide-react';
import HomePage from './components/HomePage';
import CommandsPage from './components/CommandsPage';
import DockerProjectsPage from './components/DockerProjectsPage';
import AIAgentsPage from './components/AIAgentsPage';
import PromptToolsPage from './components/PromptToolsPage';
import ChatbotPage from './components/ChatbotPage';
import MLProjectsPage from './components/MLProjectsPage';

type PageType = 'home' | 'commands' | 'docker' | 'ai-agents' | 'prompt-tools' | 'chatbot' | 'ml-projects';

function App() {
  const [currentPage, setCurrentPage] = useState<PageType>('home');

  const navigationItems = [
    { id: 'home' as PageType, label: 'Dashboard', icon: Home },
    { id: 'commands' as PageType, label: 'Commands', icon: Terminal },
    { id: 'docker' as PageType, label: 'Docker Projects', icon: Docker },
    { id: 'ai-agents' as PageType, label: 'AI Agents', icon: Bot },
    { id: 'prompt-tools' as PageType, label: 'Prompt Tools', icon: Wand2 },
    { id: 'chatbot' as PageType, label: 'Chatbot', icon: MessageCircle },
    { id: 'ml-projects' as PageType, label: 'ML Projects', icon: Brain },
  ];

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <HomePage onNavigate={setCurrentPage} />;
      case 'commands':
        return <CommandsPage onNavigate={setCurrentPage} />;
      case 'docker':
        return <DockerProjectsPage onNavigate={setCurrentPage} />;
      case 'ai-agents':
        return <AIAgentsPage onNavigate={setCurrentPage} />;
      case 'prompt-tools':
        return <PromptToolsPage onNavigate={setCurrentPage} />;
      case 'chatbot':
        return <ChatbotPage onNavigate={setCurrentPage} />;
      case 'ml-projects':
        return <MLProjectsPage onNavigate={setCurrentPage} />;
      default:
        return <HomePage onNavigate={setCurrentPage} />;
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      <div className="flex">
        {/* Sidebar */}
        <div className="w-64 bg-black/20 backdrop-blur-md border-r border-white/10 min-h-screen sticky top-0">
          <div className="p-6">
            <div className="flex items-center space-x-3 mb-8">
              <div className="w-10 h-10 bg-gradient-to-r from-purple-500 to-pink-500 rounded-lg flex items-center justify-center">
                <Terminal className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-white">CommandHub</h1>
                <p className="text-xs text-gray-400">Multi-Platform Interface</p>
              </div>
            </div>
            
            <nav className="space-y-2">
              {navigationItems.map((item) => {
                const Icon = item.icon;
                return (
                  <button
                    key={item.id}
                    onClick={() => setCurrentPage(item.id)}
                    className={`w-full flex items-center space-x-3 px-4 py-3 rounded-lg text-left transition-all duration-200 ${
                      currentPage === item.id
                        ? 'bg-gradient-to-r from-purple-500/20 to-pink-500/20 text-white border border-purple-500/30'
                        : 'text-gray-300 hover:bg-white/5 hover:text-white'
                    }`}
                  >
                    <Icon className="w-5 h-5" />
                    <span className="font-medium">{item.label}</span>
                  </button>
                );
              })}
            </nav>
          </div>
          
          {/* Footer Links */}
          <div className="absolute bottom-6 left-6 right-6">
            <div className="flex items-center justify-center space-x-4 pt-4 border-t border-white/10">
              <a href="https://github.com" target="_blank" rel="noopener noreferrer" 
                 className="text-gray-400 hover:text-white transition-colors">
                <Github className="w-5 h-5" />
              </a>
              <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer"
                 className="text-gray-400 hover:text-white transition-colors">
                <Linkedin className="w-5 h-5" />
              </a>
            </div>
          </div>
        </div>

        {/* Main Content */}
        <div className="flex-1">
          {renderPage()}
        </div>
      </div>
    </div>
  );
}

export default App;