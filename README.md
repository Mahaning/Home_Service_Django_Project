# Home_Service_Django_Project


# Home Services Application

## Overview

The Home Services Application is a platform designed to connect users with service providers for various home-related tasks such as cleaning, repairs, and maintenance. Users can browse, book, and manage home services, while providers can list their services and manage appointments.

## Features

### For Users
- **Browse Services**: Discover various home services offered by providers.
- **Search and Filter**: Find services based on location, type, and ratings.
- **Booking**: Schedule and book appointments with service providers.
- **Provider Profiles**: View detailed profiles including ratings and reviews.
- **Appointment Management**: Track and manage your bookings.
- **Reviews**: Leave and read feedback about service providers.

### For Service Providers
- **Profile Management**: Create and manage your service provider profile.
- **Service Listings**: Add, update, or remove services you offer.
- **Booking Management**: Manage your appointments and bookings.
- **Review Management**: Respond to user reviews and feedback.

### For Admins
- **User Management**: Manage user and provider accounts, including registration and deactivation.
- **Service Approval**: Review and approve service listings.
- **Reporting**: Access reports on service usage, user activity, and provider performance.



# admin :
![AdminLogin](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/34aec800-bf05-4c9a-9a24-5ad93e4baf54)

![Screenshot 2023-12-22 153155](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/084a9cc3-5c48-4e1b-9552-65c254d77150)
![admin request pages](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/c735c2b3-2a53-443f-859d-44412b4ee3b5)
![Uploading admin service  management .png…]()
![worker Assign Page](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/06e02b29-e210-4100-a695-64d54476e65a)
![worker status page 2](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/29cdb824-ecef-4082-bb58-cc03012e8380)


# User/Client: 
![Screenshot 2023-12-22 152240](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/6b5b46a3-3ce0-495f-8fcb-a8b3c134011a)

![Screenshot 2023-12-22 152142](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/666fc216-4525-44b9-bb35-c1a1f32c1680)

![userHomepage](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/7147d9f5-d459-4085-8ea9-c5314cd19d17)

![user profile](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/6ee7794f-d2f7-42de-af2f-bb5f1c800f40)
![Screenshot 2023-12-22 152518](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/4f83fbcd-6c01-4745-9a56-4b93792902fb)
![Screenshot 2023-12-22 152547](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/5fc08a7a-1896-49ca-9606-faaafa9af4f5)

![Screenshot 2023-12-22 152825](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/9d118e88-ba4a-4c6c-9bef-ec2841d4dffb)

![user appointment history page](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/94ec9db5-34eb-448b-92f1-0bf6709f170b)

![user contact us pages](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/08f36138-9139-4adb-a206-393b56ba3a77)

![Screenshot 2023-12-22 152618](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/14caaed1-fe9d-4cb1-94f7-1a69a64ff547)

# Workers:
![Screenshot 2023-12-22 153445](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/f291f814-80b2-4e91-abf2-ea73a9c6a377)

![Screenshot 2023-12-22 153833](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/10edac50-f443-4744-b9e5-4f039c909236)

![worker tasks page](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/86f1b058-4a0e-4aa0-b69e-b0ecaca7440f)

![worker status page](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/8a9eb735-5412-41c8-8686-9f2698c6e5eb)

![worker status page 2](https://github.com/Mahaning/Home_Service_Django_Project/assets/92427624/20b865cf-fe41-413a-bfb5-5c3d6008f130)



## Installation

### Prerequisites
- [Python](https://www.python.org/) (version 3.6 or higher)
- [Django](https://www.djangoproject.com/) (version 3.2 or higher)
- [PostgreSQL](https://www.postgresql.org/) or any other supported database

### Getting Started

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Mahaning/Home_Service_Django_Project.git
    cd Home_Service_Django_Project
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser (for Admin Access)**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Application**
    ```bash
    python manage.py runserver
    ```
   The application will be available at `http://localhost:8000`.

## Usage

- **User Access**: Sign up or log in to browse services and book appointments.
- **Service Provider Access**: Register to list services and manage bookings.
- **Admin Access**: Log in to manage users, providers, and services.

## Contributing

We welcome contributions to improve the Home Services Application. To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to [your-email@example.com](mailto:your-email@example.com).

