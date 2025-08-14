import React, { useState } from 'react';
import { Home, Terminal, Monitor, Package, Play, Loader2, Copy, CheckCircle } from 'lucide-react';

type PageType = 'home' | 'commands' | 'docker' | 'ai-agents' | 'prompt-tools' | 'chatbot' | 'ml-projects';

interface CommandsPageProps {
  onNavigate: (page: PageType) => void;
}

const CommandsPage: React.FC<CommandsPageProps> = ({ onNavigate }) => {
  const [activeTab, setActiveTab] = useState<'linux' | 'windows' | 'docker'>('linux');
  const [command, setCommand] = useState('');
  const [output, setOutput] = useState('');
  const [isExecuting, setIsExecuting] = useState(false);
  const [copied, setCopied] = useState(false);

  const tabs = [
    { id: 'linux' as const, label: 'Linux Commands', icon: Terminal },
    { id: 'windows' as const, label: 'Windows Commands', icon: Monitor },
    { id: 'docker' as const, label: 'Docker Commands', icon: Package },
  ];

  const commonCommands = {
    linux: [
      'ls -la',
      'pwd',
      'whoami',
      'df -h',
      'free -m',
      'ps aux',
      'netstat -tlnp',
      'systemctl status'
    ],
    windows: [
      'dir',
      'ipconfig',
      'systeminfo',
      'tasklist',
      'netstat -an',
      'whoami',
      'echo %PATH%',
      'wmic os get caption'
    ],
    docker: [
      'docker ps',
      'docker images',
      'docker logs',
      'docker exec -it',
      'docker build -t',
      'docker run -d',
      'docker compose up',
      'docker system prune'
    ]
  };

  const executeCommand = async () => {
    if (!command.trim()) return;
    
    setIsExecuting(true);
    setOutput('');
    
    // Simulate command execution
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    // Mock different outputs based on command type
    let mockOutput = '';
    if (activeTab === 'linux') {
      if (command.includes('ls')) {
        mockOutput = `total 12
drwxr-xr-x 3 user user 4096 Dec  1 10:30 .
drwxr-xr-x 5 user user 4096 Dec  1 10:25 ..
-rw-r--r-- 1 user user  156 Dec  1 10:30 app.py
-rw-r--r-- 1 user user  89 Dec  1 10:29 requirements.txt
drwxr-xr-x 2 user user 4096 Dec  1 10:30 utils`;
      } else if (command.includes('pwd')) {
        mockOutput = '/home/user/commandhub';
      } else {
        mockOutput = `Command executed successfully: ${command}\nOutput would appear here in a real implementation.`;
      }
    } else if (activeTab === 'windows') {
      mockOutput = `Microsoft Windows [Version 10.0.19044.2006]\n(c) Microsoft Corporation. All rights reserved.\n\nC:\\Users\\User>${command}\nCommand executed successfully.`;
    } else {
      mockOutput = `CONTAINER ID   IMAGE     COMMAND                  CREATED       STATUS       PORTS                    NAMES
a1b2c3d4e5f6   nginx     "/docker-entrypoint.…"   2 hours ago   Up 2 hours   0.0.0.0:80->80/tcp      web-server
f6e5d4c3b2a1   redis     "docker-entrypoint.s…"   3 hours ago   Up 3 hours   0.0.0.0:6379->6379/tcp  cache`;
    }
    
    setOutput(mockOutput);
    setIsExecuting(false);
  };

  const copyOutput = () => {
    navigator.clipboard.writeText(output);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="p-8 max-w-6xl mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-4xl font-bold text-white mb-2">Command Launcher</h1>
          <p className="text-gray-400">Execute commands across different platforms</p>
        </div>
        <button
          onClick={() => onNavigate('home')}
          className="flex items-center space-x-2 px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white hover:bg-white/20 transition-colors"
        >
          <Home className="w-4 h-4" />
          <span>Back to Dashboard</span>
        </button>
      </div>

      {/* Tabs */}
      <div className="flex space-x-1 mb-8 bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-1">
        {tabs.map((tab) => {
          const Icon = tab.icon;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center space-x-2 px-4 py-3 rounded-lg transition-all duration-200 ${
                activeTab === tab.id
                  ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white'
                  : 'text-gray-300 hover:text-white hover:bg-white/10'
              }`}
            >
              <Icon className="w-4 h-4" />
              <span>{tab.label}</span>
            </button>
          );
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Command Input */}
        <div className="lg:col-span-2 space-y-6">
          <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-6">
            <h3 className="text-lg font-semibold text-white mb-4">Command Input</h3>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Enter {activeTab} command:
                </label>
                <input
                  type="text"
                  value={command}
                  onChange={(e) => setCommand(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && executeCommand()}
                  placeholder={`e.g., ${commonCommands[activeTab][0]}`}
                  className="w-full px-4 py-3 bg-black/30 border border-white/20 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/20"
                />
              </div>
              <button
                onClick={executeCommand}
                disabled={!command.trim() || isExecuting}
                className="flex items-center space-x-2 px-6 py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-lg hover:from-purple-600 hover:to-pink-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200"
              >
                {isExecuting ? (
                  <Loader2 className="w-4 h-4 animate-spin" />
                ) : (
                  <Play className="w-4 h-4" />
                )}
                <span>{isExecuting ? 'Executing...' : 'Execute Command'}</span>
              </button>
            </div>
          </div>

          {/* Output */}
          <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold text-white">Output</h3>
              {output && (
                <button
                  onClick={copyOutput}
                  className="flex items-center space-x-2 px-3 py-1 bg-white/10 border border-white/20 rounded-lg text-sm text-gray-300 hover:text-white hover:bg-white/20 transition-colors"
                >
                  {copied ? (
                    <>
                      <CheckCircle className="w-3 h-3" />
                      <span>Copied!</span>
                    </>
                  ) : (
                    <>
                      <Copy className="w-3 h-3" />
                      <span>Copy</span>
                    </>
                  )}
                </button>
              )}
            </div>
            <div className="bg-black/50 border border-white/10 rounded-lg p-4 min-h-48">
              {isExecuting ? (
                <div className="flex items-center space-x-2 text-gray-400">
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>Executing command...</span>
                </div>
              ) : output ? (
                <pre className="text-green-400 text-sm font-mono whitespace-pre-wrap">{output}</pre>
              ) : (
                <div className="text-gray-500 text-sm">Command output will appear here...</div>
              )}
            </div>
          </div>
        </div>

        {/* Common Commands */}
        <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-6">
          <h3 className="text-lg font-semibold text-white mb-4">Common Commands</h3>
          <div className="space-y-2">
            {commonCommands[activeTab].map((cmd, index) => (
              <button
                key={index}
                onClick={() => setCommand(cmd)}
                className="w-full text-left px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-gray-300 hover:text-white hover:bg-white/10 hover:border-purple-500/30 transition-all duration-200"
              >
                <code className="font-mono">{cmd}</code>
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default CommandsPage;