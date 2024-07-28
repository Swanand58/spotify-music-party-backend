# spotify-music-party-backend
Music Party Web Application using Spotify Api's


- [] - Register this application with Spotify and obtain API Credentials
- [] - Implement OAuth 2.0 authentication to allow users to log in with their Spotify accounts.
- [] - Rest API for handling Rooms
- [] - Rest API for handling Users
- [] - Rest API for handling Songs
- [] - Rest API for handling Playlists
- [] - Integrate with the Spotify API for fetching playlists, songs, and controlling playback
- [] - Set up WebSocket or a similar technology for real-time communication.
- [] - Enable real-time syncing of song playback across users in a room
- [] - Write unit tests for backend APIs.
- [] - Test the entire user flow from authentication to room creation and playback.


## List of Rest API endpoints tentatively planned

- POST /auth/login: Authenticate user with Spotify and get an access token.
- PUT/ POST /auth/refresh: Refresh Spotify access token.
- GET /users/me: Get details of the logged-in user.
- POST /rooms: Create a new room.
- GET /rooms: List all available rooms.
- GET /rooms/{id}: Get details of a specific room.
- POST /rooms/{id}/join: Join a specific room.
- POST /rooms/{id}/leave: Leave a specific room.
- GET /playlists: Get user’s playlists.
- GET /playlists/{id}: Get details of a specific playlist.
- POST /rooms/{id}/playlists: Add a playlist to a room.
- GET /songs/{id}: Get details of a specific song.
- POST /rooms/{id}/songs: Add a song to a room.
- POST /rooms/{id}/play: Play a song in a room.
- POST /rooms/{id}/pause: Pause song playback in a room.
- POST /rooms/{id}/seek: Seek to a specific time in a song.

## Authors

- Swanand Sanjay Khonde
- Ayushi Lonkar
- Ritupriya Andurkar
