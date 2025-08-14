import React from 'react';
import { Terminal, Docker, Bot, Wand2, MessageCircle, Brain, ArrowRight, Sparkles } from 'lucide-react';

type PageType = 'home' | 'commands' | 'docker' | 'ai-agents' | 'prompt-tools' | 'chatbot' | 'ml-projects';

interface HomePageProps {
  onNavigate: (page: PageType) => void;
}

const HomePage: React.FC<HomePageProps> = ({ onNavigate }) => {
  const features = [
    {
      id: 'commands' as PageType,
      title: 'Command Launcher',
      description: 'Execute Linux, Windows, and Docker commands with an intuitive interface',
      icon: Terminal,
      gradient: 'from-blue-500 to-cyan-500',
      delay: '0ms'
    },
    {
      id: 'docker' as PageType,
      title: 'Docker Projects',
      description: 'Showcase your Docker containers with beautiful project cards',
      icon: Docker,
      gradient: 'from-indigo-500 to-purple-500',
      delay: '100ms'
    },
    {
      id: 'ai-agents' as PageType,
      title: 'AI Agents',
      description: 'Multi-agent AI interface with smart command understanding',
      icon: Bot,
      gradient: 'from-purple-500 to-pink-500',
      delay: '200ms'
    },
    {
      id: 'prompt-tools' as PageType,
      title: 'Prompt Engineering',
      description: 'Advanced prompt engineering laboratory with templates and testing',
      icon: Wand2,
      gradient: 'from-pink-500 to-rose-500',
      delay: '300ms'
    },
    {
      id: 'chatbot' as PageType,
      title: 'AI Chatbot',
      description: 'Interactive chat assistant powered by advanced language models',
      icon: MessageCircle,
      gradient: 'from-emerald-500 to-teal-500',
      delay: '400ms'
    },
    {
      id: 'ml-projects' as PageType,
      title: 'ML Projects',
      description: 'Machine learning demos with interactive prediction interfaces',
      icon: Brain,
      gradient: 'from-orange-500 to-red-500',
      delay: '500ms'
    }
  ];

  return (
    <div className="p-8 max-w-7xl mx-auto">
      {/* Hero Section */}
      <div className="text-center mb-16">
        <div className="inline-flex items-center space-x-2 bg-gradient-to-r from-purple-500/10 to-pink-500/10 border border-purple-500/20 rounded-full px-4 py-2 mb-6">
          <Sparkles className="w-4 h-4 text-purple-400" />
          <span className="text-sm text-purple-300">Welcome to CommandHub</span>
        </div>
        
        <h1 className="text-6xl font-bold text-white mb-6 bg-gradient-to-r from-white via-purple-200 to-pink-200 bg-clip-text text-transparent">
          Multi-Platform
          <br />
          Command Interface
        </h1>
        
        <p className="text-xl text-gray-300 mb-8 max-w-3xl mx-auto leading-relaxed">
          Your unified dashboard for command execution, Docker management, AI agents, and machine learning projects. 
          Built for developers who need powerful tools in a beautiful interface.
        </p>
        
        <div className="flex items-center justify-center space-x-4">
          <div className="flex items-center space-x-2 text-sm text-gray-400">
            <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
            <span>All systems operational</span>
          </div>
        </div>
      </div>

      {/* Feature Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {features.map((feature) => {
          const Icon = feature.icon;
          return (
            <div
              key={feature.id}
              className="group cursor-pointer animate-fade-in-up"
              style={{ animationDelay: feature.delay }}
              onClick={() => onNavigate(feature.id)}
            >
              <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-white/20 transition-all duration-300 hover:scale-105 hover:shadow-2xl hover:shadow-purple-500/10">
                <div className={`w-12 h-12 bg-gradient-to-r ${feature.gradient} rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300`}>
                  <Icon className="w-6 h-6 text-white" />
                </div>
                
                <h3 className="text-xl font-semibold text-white mb-2 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-purple-300 group-hover:to-pink-300 group-hover:bg-clip-text transition-all duration-300">
                  {feature.title}
                </h3>
                
                <p className="text-gray-400 mb-4 leading-relaxed">
                  {feature.description}
                </p>
                
                <div className="flex items-center space-x-2 text-sm text-purple-400 group-hover:text-purple-300 transition-colors">
                  <span>Explore feature</span>
                  <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform duration-300" />
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Stats Section */}
      <div className="mt-16 grid grid-cols-1 md:grid-cols-4 gap-6">
        {[
          { label: 'Commands Executed', value: '12,847', color: 'text-blue-400' },
          { label: 'Docker Containers', value: '156', color: 'text-purple-400' },
          { label: 'AI Interactions', value: '3,421', color: 'text-pink-400' },
          { label: 'ML Predictions', value: '8,923', color: 'text-emerald-400' },
        ].map((stat, index) => (
          <div key={index} className="text-center p-6 bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl">
            <div className={`text-2xl font-bold ${stat.color} mb-1`}>{stat.value}</div>
            <div className="text-sm text-gray-400">{stat.label}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HomePage;