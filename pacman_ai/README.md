# AI-PacMan
🎮 Custom Pac-Man in Python with Pygame
Sebuah versi sederhana dari game Pac-Man yang dibuat menggunakan Python dan Pygame. Game ini menampilkan fitur dasar seperti:

Pergerakan Pac-Man

Ghost (pengejar)

Peta maze acak dengan pellet

Deteksi tabrakan dengan ghost

Skor dan nyawa

Kemenangan saat semua pellet dimakan

📂 Struktur Folder
css
Copy
Edit
pacman_game/
├── main.py
├── agent_pacman.py
├── agent_ghost.py
├── maze.py
├── README.md
▶️ Cara Menjalankan
Pastikan Python 3 dan pygame sudah terinstal:

bash
Copy
Edit
pip install pygame
Jalankan game dengan:

bash
Copy
Edit
python main.py
🕹️ Kontrol
Panah atas (↑) : Bergerak ke atas

Panah bawah (↓) : Bergerak ke bawah

Panah kiri (←) : Bergerak ke kiri

Panah kanan (→) : Bergerak ke kanan

🧠 Fitur Utama
Ukuran maze disesuaikan otomatis dengan ukuran window

Maze acak dibuat setiap game dimulai

Pac-Man bisa memakan pellet untuk mendapatkan skor

Ghost mengejar pemain dengan algoritma pathfinding (BFS)

Game berakhir saat:

Semua pellet dimakan (menang)

Nyawa habis (kalah)

📸 Tampilan Game
<!-- (Opsional, tambahkan screenshot jika ada) -->

📌 Catatan Pengembangan
Game ini dapat dikembangkan lebih lanjut dengan fitur seperti:

Beberapa jenis ghost (patrol, ambusher)

Level bertahap

Sound effect dan animasi

Leaderboard dan sistem skor tertinggi

👨‍💻 Dibuat Dengan
Python 3.x

Pygame

