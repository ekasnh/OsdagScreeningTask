# 3D Rectangular Prism Viewer Web Application

## Project Overview
The 3D Rectangular Prism Viewer Web Application is designed to enable users to view and analyze 3D models of rectangular prisms. This application provides a seamless interface for retrieving, calculating, and visualizing 3D rectangular prisms using modern web technologies and CAD tools.

### Key Features
- **Database Integration**: Retrieves prism dimensions from a MySQL/PostgreSQL database.
- **Calculation**: Calculates the surface area and volume of the prisms.
- **3D Visualization**: Displays a 3D CAD model using FreeCAD Python.
- **Technology Stack**: Backend developed with Django and Django REST Framework; frontend developed with React.

## System Architecture

### Backend

#### Database
- **Database Choice**: The application supports both MySQL and PostgreSQL databases.
- **Data Storage**: The database stores the dimensions (length, width, height) of the rectangular prisms.
- **Schema Design**: A simple table schema with columns for `id`, `length`, `width`, `height`, and `timestamp`.

#### Framework
- **Django**: Chosen for its robust ORM, scalability, and ease of integration with various databases.
- **Django REST Framework (DRF)**: Used to build the RESTful API endpoints for retrieving and posting prism data.

#### API Endpoints
- **GET /prisms/**: Retrieves a list of all rectangular prisms.
- **GET /prisms/{id}/**: Retrieves details of a specific prism by ID.
- **POST /prisms/**: Creates a new rectangular prism entry.
- **PUT /prisms/{id}/**: Updates an existing prism entry.
- **DELETE /prisms/{id}/**: Deletes a prism entry.

### Calculation
- **Surface Area Calculation**: The surface area \(A\) of a rectangular prism is calculated using the formula:
  \[
  A = 2(lw + lh + wh)
  \]
  where \(l\) is the length, \(w\) is the width, and \(h\) is the height.
- **Volume Calculation**: The volume \(V\) of a rectangular prism is calculated using the formula:
  \[
  V = l \times w \times h
  \]

### 3D Visualization
- **FreeCAD Python**: Utilized to generate and render the 3D CAD models.
- **CAD Model Generation**: Based on the dimensions retrieved from the database, the application generates a 3D model of the prism.
- **Rendering**: The generated 3D model is rendered within the web application, allowing users to interact with and inspect the model.

### Frontend

#### Framework
- **React**: Chosen for its component-based architecture, allowing for a dynamic and responsive user interface.
- **UI Components**: Developed using React to display data and interact with the backend API.

#### Features
- **Data Display**: Displays a list of all rectangular prisms with their dimensions.
- **Model Interaction**: Allows users to select a prism to view its detailed dimensions, surface area, volume, and 3D model.
- **User Input**: Provides forms for users to input new prism dimensions, which are then sent to the backend to create new entries.

## File Structure

WebRectangularPrismViewer/
├── backend/
│ ├── manage.py # Django management script
│ ├── rectangular_prism_app/ # Django application
│ └── requirements.txt # Backend dependencies
│
├── frontend/
│ ├── package.json # Frontend dependencies
│ ├── src/ # React source files
│ └── public/ # Public files
│
├── cad/
│ ├── generate_prism.py # Script for generating CAD models with FreeCAD Python
│
├── prisms.sql # SQL file to initialize the database with sample data
├── README.md # Instructions and project overview


## Workflow

1. **User Interaction**:
   - The user accesses the application through a web browser.
   - The frontend displays a list of available prisms retrieved from the backend.

2. **Data Retrieval**:
   - When a user selects a prism, the frontend sends a request to the backend API to retrieve the dimensions.
   
3. **Calculation**:
   - The backend calculates the surface area and volume based on the retrieved dimensions.
   
4. **3D Model Generation**:
   - Using FreeCAD Python, the backend generates a 3D CAD model of the selected prism.
   - The 3D model is sent to the frontend for rendering.

5. **Visualization**:
   - The frontend renders the 3D model, displaying it alongside the calculated surface area and volume.
   - Users can interact with the 3D model, inspecting it from different angles and perspectives.

## Technical Implementation

### Backend Implementation
- **Django Models**:
  ```python
  from django.db import models

  class Prism(models.Model):
      length = models.FloatField()
      width = models.FloatField()
      height = models.FloatField()
      created_at = models.DateTimeField(auto_now_add=True)
Django REST Framework Serializers:
from rest_framework import serializers
from .models import Prism

class PrismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prism
        fields = '__all__'
Django REST Framework Views:
from rest_framework import viewsets
from .models import Prism
from .serializers import PrismSerializer

class PrismViewSet(viewsets.ModelViewSet):
    queryset = Prism.objects.all()
    serializer_class = PrismSerializer
URL Routing:
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrismViewSet

router = DefaultRouter()
router.register(r'prisms', PrismViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
Frontend Implementation
React Components:

PrismList: Displays a list of all prisms.
PrismDetail: Shows detailed information and the 3D model of a selected prism.
PrismForm: Allows users to input dimensions for a new prism.
API Integration:

Using Axios or Fetch API to communicate with the Django REST API.
3D Model Rendering:

Integrating with a JavaScript library for rendering 3D models, such as Three.js, to display the FreeCAD-generated models.
Conclusion
The 3D Rectangular Prism Viewer Web Application is a comprehensive tool that combines robust backend data management, precise mathematical calculations, and advanced 3D visualization. By leveraging Django, Django REST Framework, React, and FreeCAD Python, the application provides an efficient and user-friendly platform for viewing and analyzing 3D rectangular prisms. This project demonstrates the integration of multiple technologies to create a cohesive and interactive user experience.
