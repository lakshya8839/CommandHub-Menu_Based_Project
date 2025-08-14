import paramiko
import subprocess
import sys
from typing import Dict, Any, Optional

class SSHRunner:
    """Handle SSH-based command execution for remote Linux systems"""
    
    def __init__(self, hostname: str = None, username: str = None, password: str = None, key_path: str = None):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.key_path = key_path
        self.client = None
    
    def connect(self) -> bool:
        """Establish SSH connection"""
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            if self.key_path:
                # Use SSH key authentication
                self.client.connect(
                    hostname=self.hostname,
                    username=self.username,
                    key_filename=self.key_path,
                    timeout=10
                )
            else:
                # Use password authentication
                self.client.connect(
                    hostname=self.hostname,
                    username=self.username,
                    password=self.password,
                    timeout=10
                )
            
            return True
        except Exception as e:
            print(f"SSH connection failed: {str(e)}")
            return False
    
    def execute_command(self, command: str, timeout: int = 30) -> Dict[str, Any]:
        """Execute command via SSH"""
        if not self.client:
            return {
                "success": False,
                "output": "",
                "error": "No SSH connection established",
                "exit_code": -1
            }
        
        try:
            stdin, stdout, stderr = self.client.exec_command(command, timeout=timeout)
            
            output = stdout.read().decode('utf-8', errors='replace')
            error = stderr.read().decode('utf-8', errors='replace')
            exit_code = stdout.channel.recv_exit_status()
            
            return {
                "success": exit_code == 0,
                "output": output,
                "error": error,
                "exit_code": exit_code
            }
        
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": f"Command execution failed: {str(e)}",
                "exit_code": -1
            }
    
    def execute_local_command(self, command: str, timeout: int = 30) -> Dict[str, Any]:
        """Execute command on local Linux system"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr,
                "exit_code": result.returncode
            }
        
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "",
                "error": f"Command timed out after {timeout} seconds",
                "exit_code": -1
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": f"Command execution failed: {str(e)}",
                "exit_code": -1
            }
    
    def get_system_info(self) -> Dict[str, str]:
        """Get basic system information"""
        commands = {
            "hostname": "hostname",
            "uptime": "uptime",
            "kernel": "uname -r",
            "distro": "lsb_release -d 2>/dev/null || cat /etc/os-release | head -1",
            "memory": "free -h",
            "disk": "df -h /",
            "load": "cat /proc/loadavg"
        }
        
        info = {}
        for key, cmd in commands.items():
            if self.client:
                result = self.execute_command(cmd)
            else:
                result = self.execute_local_command(cmd)
            
            info[key] = result["output"].strip() if result["success"] else "N/A"
        
        return info
    
    def disconnect(self):
        """Close SSH connection"""
        if self.client:
            self.client.close()
            self.client = None

# Common Linux commands with descriptions
COMMON_LINUX_COMMANDS = {
    "System Information": {
        "uname -a": "Display system information",
        "whoami": "Display current username",
        "id": "Display user and group IDs",
        "uptime": "Show system uptime and load",
        "hostname": "Display system hostname",
        "date": "Display current date and time"
    },
    "File Operations": {
        "ls -la": "List all files with details",
        "pwd": "Print working directory",
        "find /path -name '*.txt'": "Find files by name",
        "du -sh *": "Show directory sizes",
        "stat filename": "Display file statistics",
        "file filename": "Determine file type"
    },
    "Process Management": {
        "ps aux": "List all running processes",
        "top": "Display running processes (interactive)",
        "htop": "Enhanced process viewer",
        "kill -9 PID": "Force kill process by PID",
        "killall processname": "Kill all processes by name",
        "nohup command &": "Run command in background"
    },
    "System Monitoring": {
        "free -h": "Display memory usage",
        "df -h": "Display disk usage",
        "iostat": "Display I/O statistics",
        "netstat -tlnp": "Display network connections",
        "ss -tlnp": "Modern netstat alternative",
        "iftop": "Display network bandwidth usage"
    },
    "Network": {
        "ping -c 4 google.com": "Ping a host 4 times",
        "wget URL": "Download file from URL",
        "curl -I URL": "Get HTTP headers",
        "nslookup domain.com": "DNS lookup",
        "dig domain.com": "Advanced DNS lookup",
        "traceroute google.com": "Trace network path"
    }
}

def get_command_help(command: str) -> str:
    """Get help text for a command"""
    for category, commands in COMMON_LINUX_COMMANDS.items():
        if command in commands:
            return f"{category}: {commands[command]}"
    return "Command not found in help database"

# Safe command validation
SAFE_COMMANDS = [
    'ls', 'pwd', 'whoami', 'date', 'uptime', 'hostname', 'id', 'uname',
    'cat', 'head', 'tail', 'grep', 'find', 'which', 'whereis',
    'ps', 'top', 'free', 'df', 'du', 'stat', 'file',
    'ping', 'curl', 'wget', 'nslookup', 'dig',
    'history', 'env', 'printenv'
]

def is_safe_command(command: str) -> bool:
    """Check if command is safe to execute"""
    # Extract the base command (first word)
    base_cmd = command.strip().split()[0]
    
    # Check against safe command list
    if base_cmd in SAFE_COMMANDS:
        return True
    
    # Check for dangerous patterns
    dangerous_patterns = [
        'rm', 'del', 'format', 'mkfs', 'dd',
        'shutdown', 'reboot', 'halt', 'poweroff',
        'passwd', 'su', 'sudo', 'chmod 777',
        '>', '>>', 'mv', 'cp /dev'
    ]
    
    for pattern in dangerous_patterns:
        if pattern in command.lower():
            return False
    
    return True