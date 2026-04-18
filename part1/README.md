# Holberton School HBnB – Documentation

# TASK 0 - High-Level Package Diagram
Overview

This document presents a high-level package diagram of the HBnB application. The diagram illustrates a three-layer architecture and demonstrates how these layers communicate using the Facade design pattern.

The goal is to provide a clear and structured view of how the system is organized and how its components interact.

Architecture Overview

The HBnB application follows a layered architecture composed of three main layers:

Presentation Layer
Business Logic Layer
Persistence Layer

Each layer has a specific responsibility and communicates with the others in a controlled and structured manner.

▫️ Layer Descriptions
1. Presentation Layer

This is the layer that users directly interact with. It includes API endpoints and Services.

When a user sends a request (e.g., creating a user or viewing places), it first reaches this layer. The request is then forwarded to the system through the Facade, which acts as the main entry point.

2. Business Logic Layer

This is the “brain” of the application. It defines what should happen in the system.

It includes:

User
Place
Review
Amenity

In this layer:

Business rules are applied
Data is validated
Application behavior is controlled
3. Persistence Layer

This layer is responsible for data storage and retrieval. It communicates directly with the database and ensures data is stored and accessed correctly.

It includes:

Repository classes (e.g., UserRepository, PlaceRepository)

Its responsibilities:

Save data to the database
Retrieve data when needed
▫️ Facade Pattern

The Facade pattern simplifies communication between layers by providing a unified interface. Instead of the Presentation Layer directly interacting with the Business Logic Layer, all requests go through the Facade.

The Facade acts as a middleman that:

Receives requests
Routes them to the appropriate layer
Hides internal complexity
Benefits
Provides a single entry point
Keeps the system simple and clean
Improves readability and maintainability
Reduces tight coupling between layers
Communication Flow
The user sends a request to the Presentation Layer
The request is forwarded to the Facade
The Facade calls the Business Logic Layer
The Business Logic Layer interacts with the Persistence Layer
The result is returned back to the user through the same path