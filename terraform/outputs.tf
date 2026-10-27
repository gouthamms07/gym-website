output "control_plane_instance_id" {
  description = "EC2 instance ID of the Kubernetes control-plane node"
  value       = aws_instance.control_plane.id
}

output "control_plane_public_ip" {
  description = "Public IP of the Kubernetes control-plane node"
  value       = aws_instance.control_plane.public_ip
}

output "control_plane_private_ip" {
  description = "Private IP of the Kubernetes control-plane node"
  value       = aws_instance.control_plane.private_ip
}

output "worker_instance_id" {
  description = "EC2 instance ID of the Kubernetes worker node"
  value       = aws_instance.worker.id
}

output "worker_public_ip" {
  description = "Public IP of the Kubernetes worker node"
  value       = aws_instance.worker.public_ip
}

output "worker_private_ip" {
  description = "Private IP of the Kubernetes worker node"
  value       = aws_instance.worker.private_ip
}
