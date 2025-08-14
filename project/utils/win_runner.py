import subprocess
import sys
import os
import platform
from typing import Dict, Any, List

class WindowsRunner:
    """Handle Windows command execution"""
    
    def __init__(self):
        self.is_windows = platform.system().lower() == 'windows'
    
    def execute_command(self, command: str, timeout: int = 30) -> Dict[str, Any]:
        """Execute Windows command"""
        if not self.is_windows:
            return {
                "success": False,
                "output": "",
                "error": "Not running on Windows system",
                "exit_code": -1
            }
        
        try:
            # Use cmd /c to execute the command
            if not command.startswith('cmd /c'):
                command = f'cmd /c {command}'
            
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'
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
    
    def execute_powershell(self, command: str, timeout: int = 30) -> Dict[str, Any]:
        """Execute PowerShell command"""
        try:
            ps_command = f'powershell -Command "{command}"'
            
            result = subprocess.run(
                ps_command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'
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
                "error": f"PowerShell command timed out after {timeout} seconds",
                "exit_code": -1
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": f"PowerShell command failed: {str(e)}",
                "exit_code": -1
            }
    
    def get_system_info(self) -> Dict[str, str]:
        """Get Windows system information"""
        commands = {
            "os_version": "ver",
            "computer_name": "echo %COMPUTERNAME%",
            "username": "echo %USERNAME%",
            "processor": "wmic cpu get name /value",
            "memory": "wmic computersystem get TotalPhysicalMemory /value",
            "disk_space": "wmic logicaldisk get size,freespace,caption /value",
            "uptime": "wmic os get lastbootuptime /value",
            "ip_config": "ipconfig /all"
        }
        
        info = {}
        for key, cmd in commands.items():
            result = self.execute_command(cmd)
            info[key] = result["output"].strip() if result["success"] else "N/A"
        
        return info
    
    def get_running_processes(self) -> List[Dict[str, str]]:
        """Get list of running processes"""
        result = self.execute_command("tasklist /fo csv")
        
        if not result["success"]:
            return []
        
        processes = []
        lines = result["output"].strip().split('\n')
        
        # Skip header line
        for line in lines[1:]:
            if line.strip():
                parts = [part.strip('"') for part in line.split('","')]
                if len(parts) >= 5:
                    processes.append({
                        "name": parts[0],
                        "pid": parts[1],
                        "session": parts[2],
                        "session_num": parts[3],
                        "memory": parts[4]
                    })
        
        return processes
    
    def get_installed_software(self) -> List[str]:
        """Get list of installed software"""
        result = self.execute_command('wmic product get name /value')
        
        if not result["success"]:
            return []
        
        software = []
        for line in result["output"].split('\n'):
            if line.startswith('Name=') and line.strip() != 'Name=':
                software.append(line.replace('Name=', '').strip())
        
        return sorted(software)
    
    def get_network_info(self) -> Dict[str, Any]:
        """Get network configuration"""
        ipconfig_result = self.execute_command("ipconfig /all")
        netstat_result = self.execute_command("netstat -an")
        
        return {
            "ip_configuration": ipconfig_result["output"] if ipconfig_result["success"] else "N/A",
            "network_connections": netstat_result["output"] if netstat_result["success"] else "N/A"
        }

# Common Windows commands with descriptions
COMMON_WINDOWS_COMMANDS = {
    "System Information": {
        "systeminfo": "Display detailed system information",
        "ver": "Display Windows version",
        "hostname": "Display computer name",
        "whoami": "Display current user",
        "date /t": "Display current date",
        "time /t": "Display current time"
    },
    "File Operations": {
        "dir": "List directory contents",
        "cd": "Change directory",
        "md foldername": "Create directory",
        "rd foldername": "Remove directory",
        "copy source dest": "Copy files",
        "move source dest": "Move files",
        "del filename": "Delete file",
        "attrib filename": "Display/modify file attributes"
    },
    "Process Management": {
        "tasklist": "List running processes",
        "taskkill /pid PID": "Kill process by PID",
        "taskkill /im processname": "Kill process by name",
        "start program": "Start a program",
        "wmic process list": "Detailed process list"
    },
    "Network": {
        "ipconfig": "Display IP configuration",
        "ipconfig /all": "Display detailed IP configuration",
        "ping hostname": "Ping a host",
        "nslookup hostname": "DNS lookup",
        "netstat -an": "Display network connections",
        "tracert hostname": "Trace route to host"
    },
    "System Management": {
        "services.msc": "Open Services manager",
        "msconfig": "System configuration",
        "regedit": "Registry editor",
        "control": "Control Panel",
        "msinfo32": "System Information tool",
        "dxdiag": "DirectX diagnostics"
    },
    "Disk Management": {
        "chkdsk C:": "Check disk for errors",
        "sfc /scannow": "System file checker",
        "defrag C:": "Defragment drive",
        "diskpart": "Disk partitioning tool",
        "fsutil": "File system utilities"
    }
}

def get_command_help(command: str) -> str:
    """Get help text for a Windows command"""
    for category, commands in COMMON_WINDOWS_COMMANDS.items():
        if command in commands:
            return f"{category}: {commands[command]}"
    return "Command not found in help database"

# Safe Windows commands
SAFE_WINDOWS_COMMANDS = [
    'dir', 'cd', 'pwd', 'echo', 'type', 'find', 'findstr',
    'systeminfo', 'ver', 'hostname', 'whoami', 'date', 'time',
    'ipconfig', 'ping', 'nslookup', 'tracert', 'netstat',
    'tasklist', 'wmic', 'help', 'cls',
    'tree', 'attrib', 'where'
]

def is_safe_command(command: str) -> bool:
    """Check if Windows command is safe to execute"""
    # Extract the base command (first word)
    base_cmd = command.strip().split()[0].lower()
    
    # Remove cmd /c prefix if present
    if command.lower().startswith('cmd /c'):
        base_cmd = command[6:].strip().split()[0].lower()
    
    # Check against safe command list
    if base_cmd in SAFE_WINDOWS_COMMANDS:
        return True
    
    # Check for dangerous patterns
    dangerous_patterns = [
        'del', 'erase', 'rd', 'rmdir', 'format',
        'shutdown', 'restart', 'taskkill',
        'reg delete', 'regedit', 'diskpart',
        'fdisk', 'bcdedit', 'sfc'
    ]
    
    for pattern in dangerous_patterns:
        if pattern in command.lower():
            return False
    
    return True

def get_windows_version() -> str:
    """Get Windows version information"""
    try:
        version = platform.version()
        release = platform.release()
        return f"Windows {release} (Version {version})"
    except Exception:
        return "Windows (Version Unknown)"

def get_environment_variables() -> Dict[str, str]:
    """Get Windows environment variables"""
    return dict(os.environ)

def get_cpu_info() -> Dict[str, str]:
    """Get CPU information"""
    try:
        import cpuinfo
        info = cpuinfo.get_cpu_info()
        return {
            "name": info.get("brand_raw", "Unknown"),
            "arch": info.get("arch", "Unknown"),
            "bits": str(info.get("bits", "Unknown")),
            "count": str(info.get("count", "Unknown"))
        }
    except ImportError:
        # Fallback to wmic
        runner = WindowsRunner()
        result = runner.execute_command("wmic cpu get name,architecture,numberofcores /format:csv")
        
        if result["success"]:
            return {"info": result["output"]}
        else:
            return {"info": "CPU information not available"}