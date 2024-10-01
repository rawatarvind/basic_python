import platform
import subprocess
import os
import distro  # Use distro for detecting Linux distributions

def install_packages_centos(package_list):
    """
    Installs packages on CentOS/RHEL-based systems using yum/dnf.
    """
    try:
        # Attempt to install the packages using yum (for CentOS 7)
        print(f"Installing packages on CentOS 7 using yum...")
        subprocess.run(['sudo', 'yum', 'install', '-y'] + package_list, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing packages on CentOS: {e}")

def install_deb_packages(package_dir):
    """
    Installs .deb packages from a specified directory on Ubuntu/Debian-based systems.
    """
    deb_files = [f for f in os.listdir(package_dir) if f.endswith('.deb')]
    
    for deb_file in deb_files:
        package_path = os.path.join(package_dir, deb_file)
        print(f"Installing {deb_file} on Ubuntu/Debian...")
        try:
            # Install the .deb package
            subprocess.run(['sudo', 'dpkg', '-i', package_path], check=True)
            # Fix any missing dependencies
            subprocess.run(['sudo', 'apt', '-f', 'install', '-y'], check=True)
            print(f"Successfully installed {deb_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {deb_file}: {e}")

def main(package_list, package_dir):
    """
    Main function to detect OS and install packages accordingly.
    - On CentOS, install using yum.
    - On Ubuntu, install local .deb packages.
    """
    os_type = platform.system()
    
    try:
        if os_type == "Linux":
            # Detect Linux distribution
            distro_id = distro.id().lower()
            
            if 'centos' in distro_id or 'rhel' in distro_id:
                print(f"Detected CentOS/RHEL. Installing packages from the package manager...")
                install_packages_centos(package_list)
                
            elif 'ubuntu' in distro_id or 'debian' in distro_id:
                print(f"Detected Ubuntu/Debian. Installing local .deb packages from {package_dir}...")
                install_deb_packages(package_dir)
                
            else:
                print(f"Unsupported Linux distribution: {distro_id}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        
