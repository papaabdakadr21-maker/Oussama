name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo6 cmake libffi-dev libssl-dev
        pip install --upgrade pip
        pip install cython==0.29.33 buildozer

    - name: Accept Android SDK licenses explicitly
      run: |
        mkdir -p /home/runner/.android
        # إنشاء ملفات التراخيص يدويًا لتجاوز أي توقف إجباري
        sdkmanager --version
        yes | sdkmanager --licenses || true
        # قبول تراخيص إضافية إن وجدت
        export ANDROID_HOME=/usr/local/lib/android/sdk
        yes | $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --licenses || true

    - name: Build with Buildozer
      run: |
        buildozer -v android debug
