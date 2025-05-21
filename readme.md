Berikut adalah contoh isi `README.md` untuk sebuah project yang menggunakan **Spotify Web API** untuk **login dengan akun Spotify pengguna** dan **menarik data musik user** (seperti top tracks, top artists, dsb). Project ini bisa dikembangkan dengan Python (misalnya pakai Flask) atau JavaScript (seperti Next.js / React + Express).

---

## 🎵 Spotify User Music Dataset Extractor

A simple app to authenticate users via their Spotify account and extract personalized music data (top tracks, top artists, playlists, and more) using the [Spotify Web API](https://developer.spotify.com/).

---

### 🚀 Features

* Login with Spotify
* Get user's top tracks and artists
* Fetch playlists and saved songs
* Export data for analysis or ML modeling

---

### 🛠 Tech Stack

* Frontend: React / Next.js (or plain HTML/JS)
* Backend: Express.js (Node) or Flask (Python)
* Authentication: OAuth 2.0 (PKCE or Authorization Code Flow)
* Spotify Web API

---

### 🧾 Prerequisites

* [Spotify Developer Account](https://developer.spotify.com/dashboard/)
* Create a Spotify App to get:

  * `Client ID`
  * `Client Secret`
  * Redirect URI (e.g., `http://localhost:3000/callback`)

---

### 📦 Installation

```bash
git clone https://github.com/yourusername/spotify-user-data
cd spotify-user-data
npm install
```

Atau untuk backend Python:

```bash
pip install flask requests
```

---

### 🔐 Step 1: Set Up Spotify App

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Click "Create App"
3. Set **Redirect URI** (e.g., `http://localhost:3000/callback`)
4. Save your `Client ID` and `Client Secret`

---

### 🔁 Step 2: OAuth Flow

Spotify uses **OAuth 2.0 Authorization Code Flow** to authenticate users.

#### 1. Redirect user to login:

```text
GET https://accounts.spotify.com/authorize
```

With these query params:

```
client_id=YOUR_CLIENT_ID
response_type=code
redirect_uri=http://localhost:3000/callback
scope=user-top-read playlist-read-private
state=some-random-string
```

#### 2. After user logs in → Spotify redirects to:

```
http://localhost:3000/callback?code=AUTHORIZATION_CODE
```

#### 3. Exchange code for access token:

```bash
POST https://accounts.spotify.com/api/token
```

Body (x-www-form-urlencoded):

```
grant_type=authorization_code
code=AUTHORIZATION_CODE
redirect_uri=http://localhost:3000/callback
client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
```

---

### 🎧 Step 3: Fetch User Data

Use the access token to call the Spotify Web API:

#### Example: Get top tracks

```http
GET https://api.spotify.com/v1/me/top/tracks
Authorization: Bearer ACCESS_TOKEN
```

#### Example: Get user profile

```http
GET https://api.spotify.com/v1/me
Authorization: Bearer ACCESS_TOKEN
```

---

### 📤 Data You Can Fetch

* `GET /v1/me/top/tracks` – user’s top tracks
* `GET /v1/me/top/artists` – top artists
* `GET /v1/me/playlists` – user playlists
* `GET /v1/me/player/recently-played` – recently played tracks

---

### 📁 Export Dataset

You can convert the fetched data to JSON, CSV, or feed it into a Machine Learning model using Python (`pandas`, `scikit-learn`, etc.).

---

### 🧠 Use Cases

* Music taste profiling
* Recommendation systems
* Clustering music users
* Sentiment or genre analysis

---

### 📚 Resources

* Spotify Web API Docs: [https://developer.spotify.com/documentation/web-api](https://developer.spotify.com/documentation/web-api)
* Example scopes: [https://developer.spotify.com/documentation/web-api/concepts/scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes)

---

### ✅ Example Tools You Can Use

* **Python**: `requests`, `spotipy`
* **JavaScript**: `axios`, `node-fetch`
* **OAuth Helper Libs**: `passport-spotify`, `authlib`, etc.

---

Kalau kamu butuh versi kode langsung (misalnya Python/Flask atau Next.js), aku bisa bantu generate juga. Mau yang mana dulu?
