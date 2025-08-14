import React from 'react';
import { Home, Github, Linkedin, ExternalLink, Play, Star, GitBranch } from 'lucide-react';

type PageType = 'home' | 'commands' | 'docker' | 'ai-agents' | 'prompt-tools' | 'chatbot' | 'ml-projects';

interface DockerProjectsPageProps {
  onNavigate: (page: PageType) => void;
}

const DockerProjectsPage: React.FC<DockerProjectsPageProps> = ({ onNavigate }) => {
  const projects = [
    {
      id: 1,
      name: 'CommandHub API',
      description: 'RESTful API backend for CommandHub with authentication and command execution',
      image: 'commandhub/api',
      tags: ['Python', 'FastAPI', 'PostgreSQL'],
      github: 'https://github.com/user/commandhub-api',
      linkedin: 'https://linkedin.com/in/user',
      stars: 234,
      status: 'running',
      ports: ['8000:8000'],
      gradient: 'from-blue-500 to-cyan-500'
    },
    {
      id: 2,
      name: 'ML Model Trainer',
      description: 'Containerized machine learning training pipeline with GPU support',
      image: 'ml-trainer/latest',
      tags: ['Python', 'TensorFlow', 'CUDA'],
      github: 'https://github.com/user/ml-trainer',
      linkedin: 'https://linkedin.com/in/user',
      stars: 189,
      status: 'stopped',
      ports: ['8080:8080'],
      gradient: 'from-purple-500 to-pink-500'
    },
    {
      id: 3,
      name: 'Redis Cache',
      description: 'High-performance in-memory data structure store for caching',
      image: 'redis:alpine',
      tags: ['Redis', 'Cache', 'NoSQL'],
      github: 'https://github.com/user/redis-config',
      linkedin: 'https://linkedin.com/in/user',
      stars: 67,
      status: 'running',
      ports: ['6379:6379'],
      gradient: 'from-emerald-500 to-teal-500'
    },
    {
      id: 4,
      name: 'Web Scraper',
      description: 'Scalable web scraping service with proxy rotation and data processing',
      image: 'webscraper/v2',
      tags: ['Node.js', 'Puppeteer', 'MongoDB'],
      github: 'https://github.com/user/web-scraper',
      linkedin: 'https://linkedin.com/in/user',
      stars: 156,
      status: 'running',
      ports: ['3000:3000'],
      gradient: 'from-orange-500 to-red-500'
    },
    {
      id: 5,
      name: 'Analytics Dashboard',
      description: 'Real-time analytics dashboard with data visualization and reporting',
      image: 'analytics/dashboard',
      tags: ['React', 'D3.js', 'InfluxDB'],
      github: 'https://github.com/user/analytics-dashboard',
      linkedin: 'https://linkedin.com/in/user',
      stars: 298,
      status: 'running',
      ports: ['4000:4000'],
      gradient: 'from-indigo-500 to-purple-500'
    },
    {
      id: 6,
      name: 'Message Queue',
      description: 'Distributed message queue system for handling asynchronous tasks',
      image: 'rabbitmq:management',
      tags: ['RabbitMQ', 'AMQP', 'Messaging'],
      github: 'https://github.com/user/message-queue',
      linkedin: 'https://linkedin.com/in/user',
      stars: 87,
      status: 'stopped',
      ports: ['5672:5672', '15672:15672'],
      gradient: 'from-pink-500 to-rose-500'
    }
  ];

  const getStatusColor = (status: string) => {
    return status === 'running' ? 'text-green-400' : 'text-gray-400';
  };

  const getStatusDot = (status: string) => {
    return status === 'running' ? 'bg-green-400 animate-pulse' : 'bg-gray-400';
  };

  return (
    <div className="p-8 max-w-7xl mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-4xl font-bold text-white mb-2">Docker Projects</h1>
          <p className="text-gray-400">Showcase of containerized applications and services</p>
        </div>
        <button
          onClick={() => onNavigate('home')}
          className="flex items-center space-x-2 px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white hover:bg-white/20 transition-colors"
        >
          <Home className="w-4 h-4" />
          <span>Back to Dashboard</span>
        </button>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-4">
          <div className="text-2xl font-bold text-green-400">4</div>
          <div className="text-sm text-gray-400">Running</div>
        </div>
        <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-4">
          <div className="text-2xl font-bold text-gray-400">2</div>
          <div className="text-sm text-gray-400">Stopped</div>
        </div>
        <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-4">
          <div className="text-2xl font-bold text-purple-400">6</div>
          <div className="text-sm text-gray-400">Total Projects</div>
        </div>
        <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-4">
          <div className="text-2xl font-bold text-blue-400">1,031</div>
          <div className="text-sm text-gray-400">Total Stars</div>
        </div>
      </div>

      {/* Project Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {projects.map((project, index) => (
          <div
            key={project.id}
            className="group bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-6 hover:bg-white/10 hover:border-white/20 transition-all duration-300 hover:scale-105 hover:shadow-2xl hover:shadow-purple-500/10 animate-fade-in-up"
            style={{ animationDelay: `${index * 100}ms` }}
          >
            {/* Header */}
            <div className="flex items-start justify-between mb-4">
              <div className={`w-12 h-12 bg-gradient-to-r ${project.gradient} rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300`}>
                <Play className="w-6 h-6 text-white" />
              </div>
              <div className="flex items-center space-x-2">
                <div className="flex items-center space-x-1">
                  <Star className="w-4 h-4 text-yellow-400" />
                  <span className="text-sm text-gray-300">{project.stars}</span>
                </div>
                <div className={`w-2 h-2 rounded-full ${getStatusDot(project.status)}`}></div>
              </div>
            </div>

            {/* Content */}
            <h3 className="text-xl font-semibold text-white mb-2 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-purple-300 group-hover:to-pink-300 group-hover:bg-clip-text transition-all duration-300">
              {project.name}
            </h3>
            
            <p className="text-gray-400 text-sm mb-4 leading-relaxed">
              {project.description}
            </p>

            {/* Image info */}
            <div className="bg-black/30 border border-white/10 rounded-lg p-3 mb-4">
              <div className="flex items-center space-x-2 text-sm">
                <span className="text-gray-400">Image:</span>
                <code className="text-purple-300 font-mono">{project.image}</code>
              </div>
              <div className="flex items-center space-x-2 text-sm mt-1">
                <span className="text-gray-400">Status:</span>
                <span className={`font-medium ${getStatusColor(project.status)} capitalize`}>
                  {project.status}
                </span>
              </div>
              {project.ports.length > 0 && (
                <div className="flex items-center space-x-2 text-sm mt-1">
                  <span className="text-gray-400">Ports:</span>
                  <span className="text-cyan-300 font-mono text-xs">
                    {project.ports.join(', ')}
                  </span>
                </div>
              )}
            </div>

            {/* Tags */}
            <div className="flex flex-wrap gap-2 mb-4">
              {project.tags.map((tag, tagIndex) => (
                <span
                  key={tagIndex}
                  className="px-2 py-1 bg-white/10 border border-white/20 rounded-full text-xs text-gray-300"
                >
                  {tag}
                </span>
              ))}
            </div>

            {/* Actions */}
            <div className="flex items-center space-x-3">
              <a
                href={project.github}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center space-x-2 px-3 py-2 bg-black/30 border border-white/20 rounded-lg text-sm text-gray-300 hover:text-white hover:bg-black/50 hover:border-purple-500/30 transition-all duration-200"
              >
                <Github className="w-4 h-4" />
                <span>Code</span>
              </a>
              
              <a
                href={project.linkedin}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center space-x-2 px-3 py-2 bg-blue-500/20 border border-blue-500/30 rounded-lg text-sm text-blue-300 hover:text-blue-200 hover:bg-blue-500/30 transition-all duration-200"
              >
                <Linkedin className="w-4 h-4" />
                <span>Profile</span>
              </a>
              
              <button className="flex items-center space-x-2 px-3 py-2 bg-gradient-to-r from-purple-500/20 to-pink-500/20 border border-purple-500/30 rounded-lg text-sm text-purple-300 hover:text-purple-200 hover:from-purple-500/30 hover:to-pink-500/30 transition-all duration-200">
                <ExternalLink className="w-4 h-4" />
                <span>Demo</span>
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default DockerProjectsPage;