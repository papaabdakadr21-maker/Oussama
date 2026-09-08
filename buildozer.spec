[app]

# (str) Title of your application
title = Bluetooth Finder

# (str) Package name
package.name = bluetoothfinder

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source files where the let of data is (relative to directory of this file)
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.exts = py,png,jpg,kv,atlas

# (list) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
