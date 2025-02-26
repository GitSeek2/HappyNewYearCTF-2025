#!/usr/bin/env python3

"""
脚本用于批量构建指定目录下的镜像

参数:
-u/--username: 必填，Docker Hub用户名或组织名
-p/--path: 项目根目录（默认当前目录）
-t/--tag: 镜像标签（默认latest）

示例:
python3 docker_builder.py -u <username> -p <dir> -t <tag>
python3 docker_builder.py -u cssec -p ../base/web -t gzctf
"""

import os
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor

def build_image(directory, username, tag, path):
    try:
        image_name = f"{username}/{os.path.basename(directory)}:{tag}"
        cmd = [
            "docker", "build",
            "-t", image_name,
            "-f", os.path.join(directory, "Dockerfile"),
            directory
        ]
        
        result = subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        print(f"✅ Successfully built {image_name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to build {image_name}\nError output:\n{e.stdout}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error building {image_name}: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Batch build Docker images")
    parser.add_argument("-p", "--path", default=".",
                        help="Base directory containing Docker projects (default: current directory)")
    parser.add_argument("-t", "--tag", default="latest",
                        help="Docker image tag (default: latest)")
    parser.add_argument("-u", "--username", required=True,
                        help="Docker Hub username or organization name")
    
    args = parser.parse_args()
    
    base_path = os.path.abspath(args.path)
    if not os.path.isdir(base_path):
        print(f"Error: {base_path} is not a valid directory")
        return

    directories = []
    for entry in os.listdir(base_path):
        full_path = os.path.join(base_path, entry)
        if os.path.isdir(full_path):
            dockerfile_path = os.path.join(full_path, "Dockerfile")
            if os.path.exists(dockerfile_path):
                directories.append(full_path)

    if not directories:
        print("No valid Docker projects found")
        return

    print(f"🚀 Found {len(directories)} Docker projects to build:")
    for d in directories:
        print(f" - {os.path.basename(d)}")

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(build_image, d, args.username, args.tag, base_path)
            for d in directories
        ]

    success = 0
    failures = []
    for future, directory in zip(futures, directories):
        if future.result():
            success += 1
        else:
            failures.append(os.path.basename(directory))

    print(f"\nBuild complete: {success} succeeded, {len(failures)} failed")
    if failures:
        print("Failed projects:")
        for name in failures:
            print(f" - {name}")

if __name__ == "__main__":
    main()