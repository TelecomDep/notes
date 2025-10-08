# Получение данных о сетях мобильной связи (2/3/4/5G)

## Класс TelephonyManager

Для получения доступа к информации о сетях мобильной связи потребуются `разрешения\permissions`:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
```

Получение разрешений:

```kotlin
override fun onResume() {
    super.onResume()
    if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.READ_PHONE_STATE) != PackageManager.PERMISSION_GRANTED ||
        ContextCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED
    ) {
        Log.d(TAG, "Нет разрешений READ_PHONE_STATE или ACCESS_COARSE_LOCATION для получения cell info")

        ActivityCompat.requestPermissions(
            this,
            arrayOf(android.Manifest.permission.READ_PHONE_STATE,
                android.Manifest.permission.ACCESS_COARSE_LOCATION),
                1
        )
    }

    // Тут будет получение информации о сетях мобильной связи
    ...
    ...
}
```

Работа с классом `TelephonyManager`:
```kotlin
// Необходимые модули
import android.content.Context
import android.telephony.TelephonyManager

...
...
override fun onResume() {
    super.onResume()
    // Здесь получали разрешения, см. код выше
    ...

    val telephonyManager = getSystemService(Context.TELEPHONY_SERVICE) as TelephonyManager
    val cellInfoList = telephonyManager.allCellInfo
    Log.d(TAG, "${cellInfoList.toString()}") // Выведем все в строку
}
```

В результате получаем в `logcat` строку:
```bash
[CellInfoLte:{mRegistered=YES mTimeStamp=225071574392525ns mCellConnectionStatus=1 
                CellIdentityLte:{ 
                    mCi=176224801 mPci=386 mTac=15401 mEarfcn=1626 mBands=[3] mBandwidth=15000 mMcc=250 mMnc=01 mAlphaLong=MTS RUS mAlphaShort=MTS RUS mAdditionalPlmns={} mCsgInfo=null
                } 
                CellSignalStrengthLte: rssi=2147483647 rsrp=-96 rsrq=-15 rssnr=10 cqiTableIndex=2147483647 cqi=2147483647 ta=1 level=2 parametersUseForLevel=0 
                android.telephony.CellConfigLte :{ isEndcAvailable = false }}]

```