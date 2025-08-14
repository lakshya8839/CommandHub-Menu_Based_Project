import json
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
import random

# Mock AI agents for demonstration
# In a real implementation, you would integrate with:
# - OpenAI API
# - Google Gemini API
# - Anthropic Claude API
# - Local models via Ollama/LMStudio
# - LangChain for agent orchestration

class BaseAgent:
    """Base class for all AI agents"""
    
    def __init__(self, name: str, description: str, specialties: List[str]):
        self.name = name
        self.description = description
        self.specialties = specialties
        self.conversation_history = []
    
    def process_request(self, request: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process user request and return response"""
        raise NotImplementedError("Subclasses must implement process_request")
    
    def add_to_history(self, request: str, response: str):
        """Add interaction to conversation history"""
        self.conversation_history.append({
            "timestamp": datetime.now(),
            "request": request,
            "response": response
        })
    
    def get_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent conversation history"""
        return self.conversation_history[-limit:]
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []

class CommandRunnerAgent(BaseAgent):
    """Agent specialized in command execution and explanation"""
    
    def __init__(self):
        super().__init__(
            name="CommandRunner",
            description="Executes and explains system commands across platforms",
            specialties=["Linux commands", "Windows commands", "Command explanation", "System administration"]
        )
    
    def process_request(self, request: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process command-related requests"""
        request_lower = request.lower()
        
        # Detect command execution requests
        if any(word in request_lower for word in ["run", "execute", "command"]):
            return self._handle_command_execution(request, context)
        
        # Detect command explanation requests
        elif any(word in request_lower for word in ["explain", "what does", "how to"]):
            return self._handle_command_explanation(request, context)
        
        # General command help
        else:
            return self._handle_general_help(request, context)
    
    def _handle_command_execution(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle command execution requests"""
        # Extract command from request (simplified)
        commands_mentioned = ["ls", "pwd", "whoami", "date", "ps", "top", "df", "free"]
        
        detected_command = None
        for cmd in commands_mentioned:
            if cmd in request.lower():
                detected_command = cmd
                break
        
        if detected_command:
            # Mock command execution
            mock_outputs = {
                "ls": "total 24\ndrwxr-xr-x 5 user user 4096 Dec  1 10:30 .\ndrwxr-xr-x 3 user user 4096 Dec  1 10:25 ..\n-rw-r--r-- 1 user user  156 Dec  1 10:30 app.py",
                "pwd": "/home/user/commandhub",
                "whoami": "commandhub-user",
                "date": "Mon Dec  1 10:35:42 UTC 2025",
                "ps": "PID TTY          TIME CMD\n1234 pts/0    00:00:01 bash\n5678 pts/0    00:00:00 python3",
                "df": "Filesystem     1K-blocks    Used Available Use% Mounted on\n/dev/sda1       20971520 8388608  11534336  42% /",
                "free": "              total        used        free      shared\nMem:        8147160     2097152     6050008      256000"
            }
            
            output = mock_outputs.get(detected_command, f"Mock output for {detected_command}")
            
            response = f"I'll execute the `{detected_command}` command for you:\n\n```\n{output}\n```\n\nThis command {self._explain_command(detected_command)}"
            
            self.add_to_history(request, response)
            
            return {
                "success": True,
                "response": response,
                "command_executed": detected_command,
                "agent": self.name
            }
        
        else:
            response = "I can help you execute commands! Please specify which command you'd like me to run. For example: 'run ls command' or 'execute pwd'."
            self.add_to_history(request, response)
            
            return {
                "success": True,
                "response": response,
                "agent": self.name
            }
    
    def _handle_command_explanation(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle command explanation requests"""
        explanations = {
            "ls": "lists directory contents. The -l flag shows detailed information including permissions, ownership, size, and timestamps.",
            "pwd": "prints the current working directory path.",
            "whoami": "displays the current username.",
            "date": "shows the current system date and time.",
            "ps": "displays information about running processes.",
            "top": "shows real-time information about running processes, sorted by resource usage.",
            "df": "displays filesystem disk space usage.",
            "free": "shows memory usage information including total, used, and available memory."
        }
        
        # Find command in request
        for cmd, explanation in explanations.items():
            if cmd in request.lower():
                response = f"The `{cmd}` command {explanation}\n\nExample usage: `{cmd}`"
                self.add_to_history(request, response)
                return {
                    "success": True,
                    "response": response,
                    "agent": self.name
                }
        
        response = "I can explain various commands! Try asking about specific commands like 'ls', 'pwd', 'whoami', 'date', 'ps', 'top', 'df', or 'free'."
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_general_help(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle general command help requests"""
        response = """I'm the CommandRunner agent! I can help you with:

🔧 **Command Execution:**
- Run Linux/Unix commands safely
- Execute Windows commands
- Explain command output

📚 **Command Explanation:**
- Explain what commands do
- Show command syntax and options
- Provide usage examples

🛠️ **System Administration:**
- System monitoring commands
- File operations
- Process management

Ask me things like:
- "Run the ls command"
- "Explain what pwd does"
- "How do I check system memory?"
- "Execute whoami command"

What would you like help with?"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _explain_command(self, command: str) -> str:
        """Get brief explanation of command"""
        explanations = {
            "ls": "lists the contents of the current directory",
            "pwd": "shows your current location in the filesystem",
            "whoami": "displays your current username",
            "date": "shows the current system date and time",
            "ps": "shows currently running processes",
            "df": "displays disk space usage",
            "free": "shows memory usage statistics"
        }
        return explanations.get(command, "performs system operations")

class DockerAssistantAgent(BaseAgent):
    """Agent specialized in Docker operations"""
    
    def __init__(self):
        super().__init__(
            name="DockerAssistant",
            description="Manages Docker containers and images",
            specialties=["Container management", "Docker Compose", "Image building", "Docker networking"]
        )
    
    def process_request(self, request: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process Docker-related requests"""
        request_lower = request.lower()
        
        if any(word in request_lower for word in ["container", "ps", "running"]):
            return self._handle_container_info(request, context)
        
        elif any(word in request_lower for word in ["image", "images", "pull", "build"]):
            return self._handle_image_info(request, context)
        
        elif any(word in request_lower for word in ["compose", "docker-compose"]):
            return self._handle_compose_info(request, context)
        
        else:
            return self._handle_general_docker_help(request, context)
    
    def _handle_container_info(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle container-related requests"""
        # Mock container data
        containers = [
            {"name": "web-server", "image": "nginx:latest", "status": "running", "ports": "80:80"},
            {"name": "database", "image": "postgres:13", "status": "running", "ports": "5432:5432"},
            {"name": "cache", "image": "redis:alpine", "status": "running", "ports": "6379:6379"}
        ]
        
        response = "Here are the currently running Docker containers:\n\n"
        response += "```\n"
        response += "CONTAINER    IMAGE           STATUS     PORTS\n"
        response += "-" * 45 + "\n"
        
        for container in containers:
            response += f"{container['name']:<12} {container['image']:<15} {container['status']:<10} {container['ports']}\n"
        
        response += "```\n\nAll containers are running healthy. Would you like me to check logs or perform any operations?"
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_image_info(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle image-related requests"""
        # Mock image data
        images = [
            {"repository": "nginx", "tag": "latest", "size": "133MB"},
            {"repository": "postgres", "tag": "13", "size": "314MB"},
            {"repository": "redis", "tag": "alpine", "size": "32.4MB"},
            {"repository": "python", "tag": "3.9-slim", "size": "115MB"}
        ]
        
        response = "Here are the available Docker images:\n\n"
        response += "```\n"
        response += "REPOSITORY    TAG        SIZE\n"
        response += "-" * 30 + "\n"
        
        for image in images:
            response += f"{image['repository']:<12} {image['tag']:<10} {image['size']}\n"
        
        response += "```\n\nWould you like me to help you pull a new image or build one from a Dockerfile?"
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_compose_info(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle Docker Compose requests"""
        response = """I can help you with Docker Compose! Here's a sample docker-compose.yml structure:

```yaml
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    depends_on:
      - api
  
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/app
    depends_on:
      - db
  
  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=app
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Common Compose Commands:**
- `docker-compose up -d` - Start services in background
- `docker-compose down` - Stop and remove services
- `docker-compose logs` - View service logs
- `docker-compose ps` - List services

Need help with a specific Compose setup?"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_general_docker_help(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle general Docker help"""
        response = """I'm the DockerAssistant! I can help you with:

🐳 **Container Management:**
- List running containers
- Start/stop containers
- View container logs
- Execute commands in containers

📦 **Image Operations:**
- List available images
- Pull images from registries
- Build images from Dockerfiles
- Tag and push images

🔧 **Docker Compose:**
- Multi-container applications
- Service orchestration
- Environment management
- Volume and network configuration

🛠️ **Docker System:**
- System information
- Cleanup unused resources
- Monitor resource usage
- Network management

What Docker task can I help you with?"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }

class CodeExplainerAgent(BaseAgent):
    """Agent specialized in code analysis and explanation"""
    
    def __init__(self):
        super().__init__(
            name="CodeExplainer",
            description="Analyzes and explains code across various programming languages",
            specialties=["Python", "JavaScript", "Code review", "Best practices", "Debugging"]
        )
    
    def process_request(self, request: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process code-related requests"""
        request_lower = request.lower()
        
        if any(word in request_lower for word in ["python", "function", "def", "import"]):
            return self._handle_python_code(request, context)
        
        elif any(word in request_lower for word in ["javascript", "js", "function(", "const", "let"]):
            return self._handle_javascript_code(request, context)
        
        elif any(word in request_lower for word in ["review", "optimize", "improve"]):
            return self._handle_code_review(request, context)
        
        else:
            return self._handle_general_code_help(request, context)
    
    def _handle_python_code(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle Python code explanation"""
        response = """I can analyze Python code for you! Here's an example of what I can explain:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Optimized version with memoization
def fibonacci_optimized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_optimized(n-1, memo) + fibonacci_optimized(n-2, memo)
    return memo[n]
```

**Explanation:**
1. **Basic version**: Recursive Fibonacci with exponential time complexity O(2^n)
2. **Optimized version**: Uses memoization to cache results, reducing time complexity to O(n)

**Code Quality Tips:**
- Add type hints: `def fibonacci(n: int) -> int:`
- Add docstrings for documentation
- Handle edge cases (negative numbers)
- Use iterative approach for better performance

Share your Python code and I'll provide detailed analysis!"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_javascript_code(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle JavaScript code explanation"""
        response = """I can help with JavaScript code analysis! Here's an example:

```javascript
// Array methods demonstration
const users = [
    { name: 'Alice', age: 25, active: true },
    { name: 'Bob', age: 30, active: false },
    { name: 'Charlie', age: 35, active: true }
];

// Filter active users
const activeUsers = users.filter(user => user.active);

// Map to get names only
const userNames = users.map(user => user.name);

// Find user by name
const findUser = (name) => users.find(user => user.name === name);

// Reduce to calculate average age
const averageAge = users.reduce((sum, user) => sum + user.age, 0) / users.length;
```

**Code Analysis:**
1. **filter()**: Creates new array with elements that pass the test
2. **map()**: Transforms each element and returns new array
3. **find()**: Returns first element that matches condition
4. **reduce()**: Accumulates array values into single result

**Best Practices:**
- Use const/let instead of var
- Arrow functions for cleaner syntax
- Method chaining for readability
- Destructuring for cleaner code

Share your JavaScript code for detailed review!"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_code_review(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle code review requests"""
        response = """I provide comprehensive code reviews focusing on:

🔍 **Code Quality Assessment:**
- Readability and maintainability
- Naming conventions
- Code structure and organization
- Documentation quality

⚡ **Performance Analysis:**
- Time and space complexity
- Optimization opportunities
- Bottleneck identification
- Best practice recommendations

🔒 **Security Review:**
- Input validation
- SQL injection prevention
- XSS protection
- Authentication/authorization

🐛 **Bug Detection:**
- Logic errors
- Edge case handling
- Error handling patterns
- Testing recommendations

**Review Process:**
1. Share your code snippet or file
2. I'll analyze structure and logic
3. Provide specific improvement suggestions
4. Explain reasoning behind recommendations
5. Suggest refactored version if needed

Ready to review your code! Please share the code you'd like me to analyze."""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_general_code_help(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle general code help"""
        response = """I'm the CodeExplainer agent! I specialize in:

💻 **Code Analysis:**
- Explain how code works line by line
- Identify patterns and algorithms
- Suggest improvements and optimizations

🔧 **Programming Languages:**
- Python (data structures, algorithms, frameworks)
- JavaScript (ES6+, Node.js, React)
- SQL (queries, optimization, design)
- Bash scripting

🎯 **Code Quality:**
- Best practices and conventions
- Code reviews and refactoring
- Performance optimization
- Security considerations

🐛 **Debugging Help:**
- Error analysis and solutions
- Logic error identification
- Testing strategies

**How to use me:**
- Share code snippets for explanation
- Ask about specific programming concepts
- Request code reviews and improvements
- Get help with debugging issues

What code would you like me to help you with?"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }

class LinuxExpertAgent(BaseAgent):
    """Agent specialized in Linux system administration"""
    
    def __init__(self):
        super().__init__(
            name="LinuxExpert",
            description="Linux system administration and troubleshooting specialist",
            specialties=["System administration", "Shell scripting", "Performance tuning", "Troubleshooting"]
        )
    
    def process_request(self, request: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process Linux-related requests"""
        request_lower = request.lower()
        
        if any(word in request_lower for word in ["memory", "ram", "free"]):
            return self._handle_memory_info(request, context)
        
        elif any(word in request_lower for word in ["process", "cpu", "ps", "top"]):
            return self._handle_process_info(request, context)
        
        elif any(word in request_lower for word in ["disk", "storage", "df"]):
            return self._handle_disk_info(request, context)
        
        elif any(word in request_lower for word in ["network", "connection", "netstat"]):
            return self._handle_network_info(request, context)
        
        else:
            return self._handle_general_linux_help(request, context)
    
    def _handle_memory_info(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle memory-related requests"""
        response = """Here's the current memory usage analysis:

```bash
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           8.0Gi       2.1Gi       4.2Gi       256Mi       1.7Gi       5.5Gi
Swap:          2.0Gi          0B       2.0Gi
```

**Memory Analysis:**
- **Total RAM**: 8GB installed
- **Used**: 2.1GB (26% utilization)
- **Available**: 5.5GB (69% available for applications)
- **Buffer/Cache**: 1.7GB (used for filesystem caching)
- **Swap**: 2GB configured, currently unused

**Memory Status**: ✅ **Healthy** - Memory usage is normal

**Optimization Tips:**
- Current usage is optimal for system performance
- Swap is available but not needed (good sign)
- Buffer/cache is working efficiently
- Consider monitoring if usage approaches 80%

**Monitoring Commands:**
```bash
free -h              # Human-readable memory info
watch -n 1 free -h   # Real-time memory monitoring
cat /proc/meminfo    # Detailed memory statistics
vmstat 1 5           # Memory and CPU statistics
```

Need help with memory optimization or troubleshooting?"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_process_info(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle process-related requests"""
        response = """Here are the top processes by resource usage:

```bash
$ ps aux --sort=-%cpu | head -10
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      1234 12.5  3.2 123456 65536 ?       S    10:00   0:05 python3 app.py
www-data  5678  8.1  2.1  98765 43210 ?       S    09:30   0:12 nginx: worker
postgres  9012  4.3  1.8  87654 32109 ?       S    09:00   0:08 postgres: server
user      3456  2.1  0.8  45678 16384 pts/0   S+   10:15   0:02 bash
systemd      1  0.1  0.3  12345  6789 ?       S    08:00   0:01 /sbin/init
```

**Process Analysis:**
1. **python3 app.py** (PID 1234) - High CPU usage (12.5%)
2. **nginx worker** (PID 5678) - Moderate CPU usage (8.1%)
3. **postgres server** (PID 9012) - Database activity (4.3%)

**System Health**: ✅ **Normal** - CPU usage distributed appropriately

**Process Management Commands:**
```bash
top                    # Interactive process viewer
htop                   # Enhanced process viewer
ps aux                 # All running processes
pgrep -f "python"      # Find processes by name
kill -15 PID           # Graceful process termination
kill -9 PID            # Force kill process
killall processname    # Kill all instances
nohup command &        # Run process in background
```

**Performance Tips:**
- Monitor processes consuming >50% CPU consistently
- Check for zombie processes with `ps aux | grep defunct`
- Use `nice` and `ionice` to adjust process priorities

Need help with specific process management tasks?"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_disk_info(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle disk-related requests"""
        response = """Here's the current disk usage analysis:

```bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G  8.5G   11G  44% /
/dev/sda2       100G   45G   50G  48% /home
tmpfs           4.0G     0  4.0G   0% /dev/shm
/dev/sdb1       500G  200G  275G  42% /var/lib/docker
```

**Disk Analysis:**
- **Root (/)**: 8.5GB used of 20GB (44% - Good)
- **Home (/home)**: 45GB used of 100GB (48% - Good)  
- **Docker (/var/lib/docker)**: 200GB used of 500GB (42% - Good)

**Disk Health**: ✅ **Healthy** - All partitions have adequate free space

**Large Directory Analysis:**
```bash
$ du -sh /var/log/*
1.2G  /var/log/apache2
856M  /var/log/docker
234M  /var/log/syslog
```

**Disk Management Commands:**
```bash
df -h                    # Disk space usage
du -sh /path/*          # Directory sizes
find /path -size +100M  # Find large files
ncdu /                  # Interactive disk usage
lsblk                   # List block devices
iostat -x 1 5           # I/O statistics
```

**Maintenance Tips:**
- Set up alerts when usage exceeds 80%
- Regular log rotation and cleanup
- Monitor `/tmp` and `/var/tmp` directories
- Use `logrotate` for automatic log management

Need help with disk cleanup or optimization?"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_network_info(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle network-related requests"""
        response = """Here's the current network configuration and status:

```bash
$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536
    inet 127.0.0.1/8 scope host lo
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0

$ ss -tlnp
State    Recv-Q Send-Q Local Address:Port  Peer Address:Port
LISTEN   0      128          0.0.0.0:22            0.0.0.0:*     users:(("sshd",pid=1234,fd=3))
LISTEN   0      128          0.0.0.0:80            0.0.0.0:*     users:(("nginx",pid=5678,fd=6))
LISTEN   0      128    192.168.1.100:5432          0.0.0.0:*     users:(("postgres",pid=9012,fd=4))
```

**Network Analysis:**
- **Interface eth0**: IP 192.168.1.100/24 (Active)
- **SSH**: Listening on port 22 (Secure access)
- **HTTP**: Nginx on port 80 (Web server)
- **PostgreSQL**: Database on port 5432 (Local only)

**Network Health**: ✅ **Operational** - All services accessible

**Network Monitoring Commands:**
```bash
ss -tlnp              # Active network connections
netstat -tlnp         # Network connections (older)
iftop                 # Real-time network usage
nload                 # Network load monitor
ping -c 4 google.com  # Connectivity test
traceroute google.com # Network path trace
curl -I website.com   # HTTP connectivity test
```

**Security Check:**
```bash
$ nmap -p 1-1000 localhost
22/tcp   open  ssh
80/tcp   open  http
5432/tcp open  postgresql
```

**Network Troubleshooting:**
- Check firewall rules: `iptables -L`
- Verify DNS resolution: `nslookup domain.com`
- Test port connectivity: `telnet host port`
- Monitor bandwidth: `iftop` or `nethogs`

Need help with network configuration or troubleshooting?"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }
    
    def _handle_general_linux_help(self, request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle general Linux help"""
        response = """I'm the LinuxExpert! I specialize in comprehensive Linux system administration:

🖥️ **System Monitoring:**
- Memory and CPU analysis
- Disk usage optimization
- Process management
- Performance tuning

🔧 **System Administration:**
- User and permission management
- Service configuration
- Log analysis and troubleshooting
- Security hardening

🌐 **Network Management:**
- Network configuration
- Firewall setup (iptables/ufw)
- Service monitoring
- Connection troubleshooting

📜 **Shell Scripting:**
- Bash automation scripts
- System maintenance tasks
- Backup and recovery
- Monitoring solutions

🔒 **Security:**
- Access control and permissions
- Security auditing
- Intrusion detection
- System hardening

**Common Tasks I Help With:**
- System performance analysis
- Troubleshooting boot issues
- Service management (systemd)
- Log file analysis
- Automated backup solutions
- User management
- Network configuration

**Example Commands:**
```bash
# System info
uname -a && lsb_release -a

# Resource usage
top -bn1 | head -20

# Service status
systemctl status --no-pager

# Log analysis
journalctl -f --no-pager
```

What Linux system task can I help you with today?"""
        
        self.add_to_history(request, response)
        
        return {
            "success": True,
            "response": response,
            "agent": self.name
        }

class AgentRouter:
    """Routes requests to appropriate AI agents"""
    
    def __init__(self):
        self.agents = {
            "CommandRunner": CommandRunnerAgent(),
            "DockerAssistant": DockerAssistantAgent(),
            "CodeExplainer": CodeExplainerAgent(),
            "LinuxExpert": LinuxExpertAgent()
        }
    
    def route_request(self, request: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Route request to most appropriate agent"""
        agent_name = self._select_agent(request)
        agent = self.agents[agent_name]
        
        return agent.process_request(request, context)
    
    def _select_agent(self, request: str) -> str:
        """Select most appropriate agent based on request content"""
        request_lower = request.lower()
        
        # Docker-related keywords
        if any(word in request_lower for word in ["docker", "container", "image", "compose"]):
            return "DockerAssistant"
        
        # Code-related keywords
        elif any(word in request_lower for word in ["code", "python", "javascript", "function", "programming", "debug"]):
            return "CodeExplainer"
        
        # Linux system keywords
        elif any(word in request_lower for word in ["linux", "system", "memory", "process", "network", "admin"]):
            return "LinuxExpert"
        
        # Default to CommandRunner
        else:
            return "CommandRunner"
    
    def get_agent_info(self, agent_name: str) -> Dict[str, Any]:
        """Get information about specific agent"""
        if agent_name in self.agents:
            agent = self.agents[agent_name]
            return {
                "name": agent.name,
                "description": agent.description,
                "specialties": agent.specialties,
                "history_count": len(agent.conversation_history)
            }
        return None
    
    def list_agents(self) -> List[Dict[str, Any]]:
        """List all available agents"""
        return [self.get_agent_info(name) for name in self.agents.keys()]
    
    def clear_agent_history(self, agent_name: str):
        """Clear conversation history for specific agent"""
        if agent_name in self.agents:
            self.agents[agent_name].clear_history()

# Example usage and testing
if __name__ == "__main__":
    router = AgentRouter()
    
    # Test requests
    test_requests = [
        "Can you run the ls command?",
        "Show me running Docker containers",
        "Explain this Python function",
        "Check system memory usage",
        "How do I build a Docker image?",
        "What does the ps command do?"
    ]
    
    for request in test_requests:
        print(f"\nRequest: {request}")
        response = router.route_request(request)
        print(f"Agent: {response['agent']}")
        print(f"Response: {response['response'][:100]}...")