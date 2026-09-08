[app]

title = Bluetooth Finder
package.name = bluetoothfinder
package.domain = org.oss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,bleak
orientation = portrait
android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,ACCESS_FINE_LOCATION

# إعدادات أندرويد المستقرة لتجنب مشاكل الأداة Aidl
android.api = 33
android.minapi = 24
android.ndk_version = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
