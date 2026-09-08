[app]

# (str) Title of your application
title = Bluetooth Finder

# (str) Package name
package.name = bluetoothfinder

# (str) Package domain (needed for android packaging)
package.domain = org.oss

# (str) Source files where the let app live (relative to .spec file)
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,bleak

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,ACCESS_FINE_LOCATION

# (int) Automatically accept Android SDK licenses
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
