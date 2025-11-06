# 📸 Snaptide

A modern social media platform for sharing images and videos with a clean API built using FastAPI. Snaptide allows users to register, authenticate, upload media, and browse a personalized feed.

## ✨ Features

- 🔐 **User Authentication** - Secure JWT-based authentication with registration, login, and password reset
- 📤 **Media Upload** - Upload images and videos with captions
- 📱 **Social Feed** - View all posts in chronological order with user information
- 🗑️ **Content Management** - Delete your own posts
- ☁️ **Cloud Storage** - Integrated with ImageKit for reliable media hosting
- 🚀 **Async Operations** - Built with async/await for optimal performance
- 📚 **Interactive API Docs** - Auto-generated Swagger UI documentation

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- **Database**: SQLite with [SQLAlchemy](https://www.sqlalchemy.org/) (async)
- **Authentication**: [FastAPI Users](https://fastapi-users.github.io/fastapi-users/) - Complete authentication system
- **File Storage**: [ImageKit](https://imagekit.io/) - Cloud media storage and CDN
- **Server**: [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server

## 📋 Prerequisites

- Python 3.10 or higher
- ImageKit account (free tier available)
- Basic understanding of REST APIs

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Snaptide
```

### 2. Install Dependencies

Using `uv` (recommended):
```bash
uv sync
```

Or using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
# ImageKit Configuration
IMAGEKIT_PRIVATE_KEY=your_private_key_here
IMAGEKIT_PUBLIC_KEY=your_public_key_here
IMAGEKIT_URL=your_imagekit_url_endpoint
```

**Getting ImageKit credentials:**
1. Sign up at [ImageKit.io](https://imagekit.io/)
2. Go to Developer Options in your dashboard
3. Copy your Private Key, Public Key, and URL Endpoint

### 4. Run the Application

```bash
python3 main.py
```

The server will start at `http://0.0.0.0:8000`

## 📖 API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

#### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/jwt/login` | Login and get JWT token |
| POST | `/auth/jwt/logout` | Logout (invalidate token) |
| POST | `/auth/forgot-password` | Request password reset |
| POST | `/auth/reset-password` | Reset password with token |

#### Posts

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/upload` | Upload image/video with caption | ✅ |
| GET | `/feed` | Get all posts in feed | ✅ |
| DELETE | `/posts/{post_id}` | Delete your own post | ✅ |

#### Users

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/users/me` | Get current user info | ✅ |
| PATCH | `/users/me` | Update user profile | ✅ |

## 🎯 Quick Start Guide

### 1. Register a User

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

### 2. Login

```bash
curl -X POST "http://localhost:8000/auth/jwt/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=securepassword123"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Upload a Post

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "file=@/path/to/image.jpg" \
  -F "caption=My awesome photo!"
```

### 4. Get Feed

```bash
curl -X GET "http://localhost:8000/feed" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 📁 Project Structure

```
Snaptide/
├── src/
│   ├── app.py          # Main FastAPI application and routes
│   ├── db.py           # Database models and configuration
│   ├── schema.py       # Pydantic schemas for validation
│   ├── users.py        # User authentication setup
│   └── images.py       # ImageKit configuration
├── main.py             # Application entry point
├── pyproject.toml      # Project dependencies
├── .env                # Environment variables (not in git)
├── test.db             # SQLite database (auto-generated)
└── README.md           # This file
```

## 🔧 Development

### Database Reset

If you need to reset the database (this will delete all data):

```bash
rm test.db
# Restart the server - database will be recreated
python3 main.py
```

### Running in Development Mode

The server runs with auto-reload enabled by default, so any code changes will automatically restart the server.

### Adding New Features

1. Add models to `src/db.py`
2. Add validation schemas to `src/schema.py`
3. Add routes to `src/app.py`
4. Database tables are created automatically on startup

## 🐛 Common Issues

### Issue: "no such column" error
**Solution**: Delete `test.db` and restart the server to recreate the database with the latest schema.

### Issue: ImageKit upload fails
**Solution**: Check that your `.env` file has the correct ImageKit credentials and the keys are valid.

### Issue: "Not authenticated" error
**Solution**: Make sure you include the `Authorization: Bearer <token>` header in your requests.

## 🔐 Security Notes

⚠️ **Important for Production:**
- Change the `SECRET` in `src/users.py` to a strong random string
- Use a production database (PostgreSQL, MySQL) instead of SQLite
- Enable HTTPS/TLS
- Set up proper CORS policies
- Use environment variables for all secrets
- Implement rate limiting
- Add input validation and sanitization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ by Sujal

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing framework
- [FastAPI Users](https://fastapi-users.github.io/fastapi-users/) for authentication
- [ImageKit](https://imagekit.io/) for media hosting
- SQLAlchemy team for the excellent ORM

---

**Happy Coding! 🚀**

For questions or issues, please open an issue on GitHub.

