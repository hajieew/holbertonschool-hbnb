## High-Level Package Diagram

```mermaid
classDiagram

class PresentationLayer {
    +API Endpoints
    +Services
}

class Facade {
    +create_user()
    +get_places()
    +add_amenity()
    +add_review()
}

class BusinessLogicLayer {
    +User
    +Place
    +Review
    +Amenity
}

class PersistenceLayer {
    +Repositories
    +Database
}

PresentationLayer --> Facade : Uses
Facade --> BusinessLogicLayer : Logic
BusinessLogicLayer --> PersistenceLayer : Data Access