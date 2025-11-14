# Получение данных о местоположении смартфона (Location)

## Класс LocationManager

Для получения доступа к информации о коортинатах LLA (Latitude, Longitude, Altitude) `разрешения\permissions`:

**AndroidManifest.xml**
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```



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

### Включено ли определение местоположения?
Проверка, включена ли функция определения местоположения вашего телефона. Проверяем при помощи инициализированного ранее объекта `locationManager`:
```kotlin
private fun isLocationEnabled(): Boolean{
        return locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER) || locationManager.isProviderEnabled(LocationManager.NETWORK_PROVIDER)
}
```