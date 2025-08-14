import docker
import subprocess
import json
from typing import Dict, Any, List, Optional
import logging

class DockerRunner:
    """Handle Docker command execution and container management"""
    
    def __init__(self):
        self.client = None
        self.connected = False
        self._connect()
    
    def _connect(self):
        """Connect to Docker daemon"""
        try:
            self.client = docker.from_env()
            # Test connection
            self.client.ping()
            self.connected = True
            logging.info("Connected to Docker daemon")
        except Exception as e:
            logging.error(f"Failed to connect to Docker: {str(e)}")
            self.connected = False
    
    def execute_docker_command(self, command: str, timeout: int = 30) -> Dict[str, Any]:
        """Execute Docker command using subprocess (fallback)"""
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
                "error": f"Docker command timed out after {timeout} seconds",
                "exit_code": -1
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": f"Docker command failed: {str(e)}",
                "exit_code": -1
            }
    
    def list_containers(self, all_containers: bool = False) -> List[Dict[str, Any]]:
        """List Docker containers"""
        if not self.connected:
            return []
        
        try:
            containers = self.client.containers.list(all=all_containers)
            container_list = []
            
            for container in containers:
                container_info = {
                    "id": container.short_id,
                    "name": container.name,
                    "image": container.image.tags[0] if container.image.tags else "unknown",
                    "status": container.status,
                    "ports": self._format_ports(container.ports),
                    "created": container.attrs["Created"],
                    "command": container.attrs["Config"]["Cmd"]
                }
                container_list.append(container_info)
            
            return container_list
        
        except Exception as e:
            logging.error(f"Failed to list containers: {str(e)}")
            return []
    
    def list_images(self) -> List[Dict[str, Any]]:
        """List Docker images"""
        if not self.connected:
            return []
        
        try:
            images = self.client.images.list()
            image_list = []
            
            for image in images:
                image_info = {
                    "id": image.short_id,
                    "tags": image.tags,
                    "size": self._format_size(image.attrs["Size"]),
                    "created": image.attrs["Created"]
                }
                image_list.append(image_info)
            
            return image_list
        
        except Exception as e:
            logging.error(f"Failed to list images: {str(e)}")
            return []
    
    def get_container_logs(self, container_name: str, lines: int = 100) -> str:
        """Get container logs"""
        if not self.connected:
            return "Docker not connected"
        
        try:
            container = self.client.containers.get(container_name)
            logs = container.logs(tail=lines, timestamps=True)
            return logs.decode('utf-8', errors='replace')
        
        except Exception as e:
            return f"Failed to get logs: {str(e)}"
    
    def start_container(self, container_name: str) -> Dict[str, Any]:
        """Start a Docker container"""
        if not self.connected:
            return {"success": False, "error": "Docker not connected"}
        
        try:
            container = self.client.containers.get(container_name)
            container.start()
            return {"success": True, "message": f"Container {container_name} started"}
        
        except Exception as e:
            return {"success": False, "error": f"Failed to start container: {str(e)}"}
    
    def stop_container(self, container_name: str) -> Dict[str, Any]:
        """Stop a Docker container"""
        if not self.connected:
            return {"success": False, "error": "Docker not connected"}
        
        try:
            container = self.client.containers.get(container_name)
            container.stop()
            return {"success": True, "message": f"Container {container_name} stopped"}
        
        except Exception as e:
            return {"success": False, "error": f"Failed to stop container: {str(e)}"}
    
    def restart_container(self, container_name: str) -> Dict[str, Any]:
        """Restart a Docker container"""
        if not self.connected:
            return {"success": False, "error": "Docker not connected"}
        
        try:
            container = self.client.containers.get(container_name)
            container.restart()
            return {"success": True, "message": f"Container {container_name} restarted"}
        
        except Exception as e:
            return {"success": False, "error": f"Failed to restart container: {str(e)}"}
    
    def remove_container(self, container_name: str, force: bool = False) -> Dict[str, Any]:
        """Remove a Docker container"""
        if not self.connected:
            return {"success": False, "error": "Docker not connected"}
        
        try:
            container = self.client.containers.get(container_name)
            container.remove(force=force)
            return {"success": True, "message": f"Container {container_name} removed"}
        
        except Exception as e:
            return {"success": False, "error": f"Failed to remove container: {str(e)}"}
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get Docker system information"""
        if not self.connected:
            return {"error": "Docker not connected"}
        
        try:
            info = self.client.info()
            return {
                "containers": info.get("Containers", 0),
                "containers_running": info.get("ContainersRunning", 0),
                "containers_paused": info.get("ContainersPaused", 0),
                "containers_stopped": info.get("ContainersStopped", 0),
                "images": info.get("Images", 0),
                "server_version": info.get("ServerVersion", "Unknown"),
                "kernel_version": info.get("KernelVersion", "Unknown"),
                "operating_system": info.get("OperatingSystem", "Unknown"),
                "total_memory": self._format_size(info.get("MemTotal", 0)),
                "cpu_cores": info.get("NCPU", 0)
            }
        
        except Exception as e:
            return {"error": f"Failed to get system info: {str(e)}"}
    
    def build_image(self, dockerfile_path: str, tag: str) -> Dict[str, Any]:
        """Build Docker image from Dockerfile"""
        if not self.connected:
            return {"success": False, "error": "Docker not connected"}
        
        try:
            image, logs = self.client.images.build(
                path=dockerfile_path,
                tag=tag,
                rm=True
            )
            
            log_output = "\n".join([log.get("stream", "").strip() for log in logs if "stream" in log])
            
            return {
                "success": True,
                "image_id": image.short_id,
                "logs": log_output
            }
        
        except Exception as e:
            return {"success": False, "error": f"Failed to build image: {str(e)}"}
    
    def pull_image(self, image_name: str, tag: str = "latest") -> Dict[str, Any]:
        """Pull Docker image from registry"""
        if not self.connected:
            return {"success": False, "error": "Docker not connected"}
        
        try:
            image = self.client.images.pull(image_name, tag=tag)
            return {
                "success": True,
                "image_id": image.short_id,
                "image_tags": image.tags
            }
        
        except Exception as e:
            return {"success": False, "error": f"Failed to pull image: {str(e)}"}
    
    def run_container(self, image: str, name: str = None, ports: Dict = None, 
                     environment: Dict = None, volumes: Dict = None, 
                     detach: bool = True) -> Dict[str, Any]:
        """Run a new Docker container"""
        if not self.connected:
            return {"success": False, "error": "Docker not connected"}
        
        try:
            container = self.client.containers.run(
                image=image,
                name=name,
                ports=ports or {},
                environment=environment or {},
                volumes=volumes or {},
                detach=detach
            )
            
            return {
                "success": True,
                "container_id": container.short_id,
                "container_name": container.name
            }
        
        except Exception as e:
            return {"success": False, "error": f"Failed to run container: {str(e)}"}
    
    def _format_ports(self, ports: Dict) -> List[str]:
        """Format container ports for display"""
        if not ports:
            return []
        
        port_list = []
        for container_port, host_configs in ports.items():
            if host_configs:
                for host_config in host_configs:
                    host_port = host_config.get("HostPort", "")
                    port_list.append(f"{host_port}:{container_port}")
            else:
                port_list.append(container_port)
        
        return port_list
    
    def _format_size(self, size_bytes: int) -> str:
        """Format size in bytes to human readable format"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024
            i += 1
        
        return f"{size_bytes:.1f} {size_names[i]}"

# Common Docker commands with descriptions
COMMON_DOCKER_COMMANDS = {
    "Container Management": {
        "docker ps": "List running containers",
        "docker ps -a": "List all containers",
        "docker start CONTAINER": "Start a container",
        "docker stop CONTAINER": "Stop a container",
        "docker restart CONTAINER": "Restart a container",
        "docker rm CONTAINER": "Remove a container",
        "docker logs CONTAINER": "View container logs",
        "docker exec -it CONTAINER bash": "Execute command in container"
    },
    "Image Management": {
        "docker images": "List local images",
        "docker pull IMAGE": "Pull image from registry",
        "docker build -t TAG .": "Build image from Dockerfile",
        "docker rmi IMAGE": "Remove an image",
        "docker tag SOURCE TARGET": "Tag an image",
        "docker push IMAGE": "Push image to registry"
    },
    "System Commands": {
        "docker info": "Display system information",
        "docker version": "Show Docker version",
        "docker system df": "Show disk usage",
        "docker system prune": "Remove unused data",
        "docker stats": "Display container resource usage",
        "docker network ls": "List networks"
    },
    "Docker Compose": {
        "docker-compose up": "Start services",
        "docker-compose up -d": "Start services in background",
        "docker-compose down": "Stop and remove services",
        "docker-compose ps": "List services",
        "docker-compose logs": "View service logs",
        "docker-compose build": "Build services"
    }
}

def get_command_help(command: str) -> str:
    """Get help text for a Docker command"""
    for category, commands in COMMON_DOCKER_COMMANDS.items():
        if command in commands:
            return f"{category}: {commands[command]}"
    return "Command not found in help database"

# Docker command safety check
def is_safe_docker_command(command: str) -> bool:
    """Check if Docker command is safe to execute"""
    # Allow most Docker commands, but be cautious with destructive ones
    dangerous_patterns = [
        'docker system prune -a',  # Removes all unused images
        'docker rm $(docker ps -aq)',  # Removes all containers
        'docker rmi $(docker images -q)',  # Removes all images
        'docker network prune -f',  # Force remove networks
        'docker volume prune -f'  # Force remove volumes
    ]
    
    for pattern in dangerous_patterns:
        if pattern in command.lower():
            return False
    
    return True

def parse_dockerfile(dockerfile_content: str) -> Dict[str, Any]:
    """Parse Dockerfile content and extract information"""
    instructions = []
    base_image = None
    exposed_ports = []
    
    for line in dockerfile_content.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        parts = line.split(None, 1)
        if len(parts) < 2:
            continue
        
        instruction = parts[0].upper()
        value = parts[1]
        
        instructions.append({"instruction": instruction, "value": value})
        
        if instruction == "FROM":
            base_image = value
        elif instruction == "EXPOSE":
            exposed_ports.extend(value.split())
    
    return {
        "base_image": base_image,
        "exposed_ports": exposed_ports,
        "instructions": instructions,
        "instruction_count": len(instructions)
    }