Below are the endpoints we’ll set up for Figgy's-Eats:

Authentication Endpoints:
User Signup: /api/auth/signup/ (POST)
User Login: /api/auth/login/ (POST)
Meal Management Endpoints:
List Meals: /api/meals/ (GET)
Get Meal Details: /api/meals/<int:id>/ (GET)
Add a Meal (Admin): /api/meals/ (POST)
Update a Meal (Admin): /api/meals/<int:id>/ (PUT)
Delete a Meal (Admin): /api/meals/<int:id>/ (DELETE)
Orders Management Endpoints:
Place an Order: /api/orders/ (POST)
View Orders (User): /api/orders/ (GET)
View Specific Order: /api/orders/<int:id>/ (GET)
Update Order Status (Admin): /api/orders/<int:id>/ (PUT)
Swagger Documentation Endpoint:
API Documentation: /api/docs/ (Swagger UI)

source figgyseatsvenv/bin/activate 