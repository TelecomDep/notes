# Получение данных о местоположении смартфона (Location)
**Полный пример** [здесь](https://github.com/TelecomDep/android_notes/blob/master/Examples/android_notes/app/src/main/java/com/example/android_notes/activities/LocationActivity.kt).
## Класс LocationManager

Для получения доступа к информации о коортинатах LLA (Latitude, Longitude, Altitude) `разрешения\permissions`:

**AndroidManifest.xml**
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

Получаем доступ к `LocationManager`:

This class provides access to the system location services. These services allow applications to obtain periodic updates of the device's geographical location, or to be notified when the device enters the proximity of a given geographical location.
[оригинал](https://developer.android.com/reference/android/location/LocationManager)

```kotlin
// другие импорты
import android.location.Location
import android.location.LocationListener
import android.location.LocationManager

class LocationActivity : LocationListener, AppCompatActivity()  {

    companion object {
        private const val PERMISSION_REQUEST_ACCESS_LOCATION= 100
    }

    private lateinit var tvLat: TextView
    private lateinit var tvLon: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_location)

        locationManager = this.getSystemService(Context.LOCATION_SERVICE) as LocationManager
        tvLat = findViewById(R.id.tv_lat) as TextView
        tvLon = findViewById(R.id.tv_lon) as TextView
    }

    ...
    // Здесь какой-то код
    ...

    // Переопределенный метод интерфейса LocationListener
    override fun onLocationChanged(location: Location) {
        tvLat.setText(location.latitude.toString())
        tvLon.setText(location.longitude.toString())
    }
}
```

**Включено ли определение местоположения?**

Проверка, включена ли функция определения местоположения вашего телефона. Проверяем при помощи инициализированного ранее объекта `locationManager`:
```kotlin
private fun isLocationEnabled(): Boolean{
        return locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER) || locationManager.isProviderEnabled(LocationManager.NETWORK_PROVIDER)
}
```

**Запрос разрешений на получения доступа к определению местоположения смартфона**

```kotlin
private fun requestPermissions() {
    ActivityCompat.requestPermissions(
        this,
        arrayOf(android.Manifest.permission.ACCESS_COARSE_LOCATION,
            android.Manifest.permission.ACCESS_FINE_LOCATION),
        PERMISSION_REQUEST_ACCESS_LOCATION
    )
}
```

**Проверка, выданы ли разрешения**
```kotlin
private fun checkPermissions(): Boolean{
    if( ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED &&
        ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED )
    {
        return true
    } else {
        return false
    }
}
```

**Задаем условие обновления местопложения**
```kotlin
locationManager.requestLocationUpdates(
                LocationManager.GPS_PROVIDER,
                1000L,
                1f,
                this
            )
```