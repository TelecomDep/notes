# Базы данных

Базы данных (далее `БД`) - это одна из основных (главных) сущностей информационных систем организаций и предприятий. `БД` представляет из себя набор совместно используемых логически связанных данных, также описание этих данных (**метаданные**).

Данные внутри `БД` могут быть структурированы по-разному - зависит от **модели данных**.
## Виды баз данных

### Реляционные базы данных

Реляционные базы данных строятся на **реляционной модели** данных. От слова **relation** - **отношение**, которое точно описывает внутреннюю структуру `БД`, но обычно такие базы данных называют **табличными**. 

**Таблицы** (`relation`) состоит из **кортежей** (строк), которые имеют однотипные *атрибуты* (столбцы). При этом один или несколько атрибутов считаются **первичным ключом**, который **ДОЛЖЕН** быть **уникальным** для всех **кортежей** (строк) в этой таблице.

@startuml
skinparam DefaultFontName Source Code Pro
skinparam DefaultFontSize 15
skinparam RankSep 50

package "eCommerce" {
  node "High Level Components" {
    component ProductCatalog
  }

  node "Abstractions" {
    component ProductFactory
  }

  node "Low Level Components" {
    component SQLProductRepository
  }

  ProductCatalog ..> ProductFactory: depends on
  ProductFactory ..> SQLProductRepository: depends on
}
@enduml

#### SQL - Structured Query Language
